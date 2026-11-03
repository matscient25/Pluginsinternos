"""Gera deals.csv — DADOS FICTÍCIOS PARA TREINAMENTO (Consultoria Vektor).

Export sintético de CRM em formato largo: uma linha por negócio, uma coluna de data
por etapa (vazia quando o negócio não chegou na etapa). Determinístico (seed fixa).

Padrões embutidos de propósito (a análise deve descobri-los, não ler aqui):
- quem passa pelo Diagnóstico com custo do problema quantificado converte muito mais;
- o maior vazamento do funil é Diagnóstico → Proposta;
- perdas por "preço/hora" se concentram em negócios que pularam o Diagnóstico.

Uso: python3 _gerar_deals.py  (escreve deals.csv ao lado)
"""
import csv
import datetime as dt
import os
import random

SEED = 20261108
HOJE = dt.date(2026, 10, 31)
INICIO = dt.date(2025, 11, 1)
FIM_CRIACAO = dt.date(2026, 10, 20)
N = 119  # + TechScale, Orbita Pay e Nuvia Saúde fixos

rng = random.Random(SEED)

AES = {
    # dono: (prob. de fazer diagnóstico, prob. de quantificar custo no diagnóstico)
    "Lucas Andrade": (0.95, 0.80),
    "Patrícia Gomes": (0.80, 0.45),
    "Diego Ramos": (0.55, 0.15),
    "Marina Costa": (0.60, 0.25),
}
SEGMENTOS = {
    "Scale-up SaaS": (150, 450),
    "Fintech": (120, 400),
    "Saúde digital": (80, 250),
    "Varejo digital": (100, 300),
    "Logística": (80, 220),
}
PREF = ["Alta", "Nexo", "Orbe", "Kora", "Lumen", "Vega", "Tera", "Prisma", "Delta", "Atlas",
        "Zeni", "Brisa", "Faro", "Quanta", "Rumo", "Sigma", "Tropa", "Vértice", "Ponto", "Mira",
        "Hélix", "Ícaro", "Jade", "Linha"]
SUF = ["Pay", "Log", "Tech", "Saúde", "Commerce", "Bank", "Labs", "Cloud", "Data", "Go",
       "Mobi", "Hub", "Flow", "Net"]

COLS = ["deal_id", "conta", "dono", "segmento", "valor_mensal", "criado_em", "status",
        "fechado_em", "motivo_perda", "entrou_qualificacao", "entrou_diagnostico",
        "entrou_proposta", "entrou_followup", "entrou_contrato", "custo_quantificado"]


def nomes_unicos(n):
    todos = [f"{p} {s}" for p in PREF for s in SUF]
    todos = [x for x in todos if x not in ("Orbe Pay",)]
    rng.shuffle(todos)
    return todos[:n]


def d(x):
    return x.isoformat() if x else ""


def escolhe(pesos):
    r = rng.random()
    acc = 0.0
    for k, p in pesos:
        acc += p
        if r <= acc:
            return k
    return pesos[-1][0]


def simula(conta, dono, segmento, criado):
    p_diag, p_quant = AES[dono]
    lo, hi = SEGMENTOS[segmento]
    valor = rng.randint(lo // 10, hi // 10) * 10_000
    row = {c: "" for c in COLS}
    row.update(conta=conta, dono=dono, segmento=segmento, valor_mensal=valor, criado_em=d(criado),
               custo_quantificado="nao")
    t = criado + dt.timedelta(days=rng.randint(0, 4))
    etapas = []  # (coluna, data)

    def entra(col, dias):
        nonlocal t
        t = t + dt.timedelta(days=dias)
        if t > HOJE:
            return False
        etapas.append((col, t))
        row[col] = d(t)
        return True

    def perde(motivos):
        nonlocal t
        fim = t + dt.timedelta(days=rng.randint(3, 15))
        if fim > HOJE:
            row["status"] = "aberto"
            return row
        row.update(status="perdido", fechado_em=d(fim), motivo_perda=escolhe(motivos))
        return row

    def aberto():
        row["status"] = "aberto"
        return row

    # Qualificação
    if not entra("entrou_qualificacao", 0):
        return aberto()
    if rng.random() > 0.78:
        return perde([("sem budget", 0.4), ("timing", 0.35), ("sem decisor", 0.25)])

    faz_diag = rng.random() < p_diag
    quant = False
    if faz_diag:
        if not entra("entrou_diagnostico", rng.randint(4, 12)):
            return aberto()
        quant = rng.random() < p_quant
        row["custo_quantificado"] = "sim" if quant else "nao"
        if rng.random() > (0.78 if quant else 0.28):
            return perde([("sem decisor", 0.35), ("timing", 0.35), ("escolheu concorrente", 0.30)])
        caminho = "quant" if quant else "diag"
    else:
        caminho = "pulou"

    # Proposta em diante: conversões dependem do caminho
    conv = {"quant": (0.90, 0.90, 0.92), "diag": (0.72, 0.70, 0.80), "pulou": (0.62, 0.55, 0.62)}[caminho]
    mot = {
        "quant": [("escolheu concorrente", 0.35), ("timing", 0.35), ("sem budget", 0.30)],
        "diag": [("preço/hora", 0.40), ("sem decisor", 0.30), ("escolheu concorrente", 0.30)],
        "pulou": [("preço/hora", 0.75), ("escolheu concorrente", 0.15), ("sem decisor", 0.10)],
    }[caminho]
    if not entra("entrou_proposta", rng.randint(6, 15)):
        return aberto()
    if rng.random() > conv[0]:
        return perde(mot)
    if not entra("entrou_followup", rng.randint(5, 12)):
        return aberto()
    if rng.random() > conv[1]:
        return perde(mot)
    if not entra("entrou_contrato", rng.randint(7, 20)):
        return aberto()
    if rng.random() > conv[2]:
        return perde(mot)
    fim = t + dt.timedelta(days=rng.randint(4, 12))
    if fim > HOJE:
        return aberto()
    row.update(status="ganho", fechado_em=d(fim))
    return row


def fixos():
    """Os três negócios que têm transcrição no kit."""
    ts = {c: "" for c in COLS}
    ts.update(conta="TechScale S/A", dono="Lucas Andrade", segmento="Scale-up SaaS",
              valor_mensal=380_000, criado_em="2026-08-03", status="ganho", fechado_em="2026-09-11",
              entrou_qualificacao="2026-08-04", entrou_diagnostico="2026-08-10",
              entrou_proposta="2026-08-17", entrou_followup="2026-08-24",
              entrou_contrato="2026-09-08", custo_quantificado="sim")
    orb = {c: "" for c in COLS}
    orb.update(conta="Orbita Pay", dono="Diego Ramos", segmento="Fintech", valor_mensal=260_000,
               criado_em="2026-06-29", status="perdido", fechado_em="2026-08-14",
               motivo_perda="preço/hora", entrou_qualificacao="2026-06-30",
               entrou_diagnostico="2026-07-07", entrou_proposta="2026-07-21",
               entrou_followup="2026-07-31", custo_quantificado="nao")
    nuv = {c: "" for c in COLS}
    nuv.update(conta="Nuvia Saúde", dono="Marina Costa", segmento="Saúde digital",
               valor_mensal=180_000, criado_em="2026-05-11", status="perdido",
               fechado_em="2026-06-26", motivo_perda="sem decisor",
               entrou_qualificacao="2026-05-12", entrou_proposta="2026-05-26",
               entrou_followup="2026-06-05", custo_quantificado="nao")
    return [ts, orb, nuv]


def main():
    linhas = []
    contas = nomes_unicos(N)
    donos = list(AES)
    for i in range(N):
        criado = INICIO + dt.timedelta(days=rng.randint(0, (FIM_CRIACAO - INICIO).days))
        linhas.append(simula(contas[i], donos[i % 4], rng.choice(list(SEGMENTOS)), criado))
    linhas += fixos()
    linhas.sort(key=lambda r: r["criado_em"])
    for i, r in enumerate(linhas, 1):
        r["deal_id"] = f"VK-{i:04d}"
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deals.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} negócios → {out}")


if __name__ == "__main__":
    main()
