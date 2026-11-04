#!/usr/bin/env python3
"""
funil.py — leitura determinística do funil a partir do export do CRM.

Entrada: CSV (vírgula ou ponto e vírgula), um negócio por linha, com colunas de
data de entrada por etapa. Reconhece automaticamente:
  - colunas "entrou_<etapa>"                         (padrão do kit)
  - colunas "Date entered <etapa>" / "Date entered '<etapa> (Pipeline)'" (HubSpot)
  - colunas "data de entrada <etapa>" / "entrada_<etapa>"
Colunas de apoio (detectadas por nome, ou informadas por argumento):
  status (ganho/perdido/aberto, won/lost/open), criado_em, fechado_em, motivo_perda,
  valor, dono.

Uso:
  python3 funil.py deals.csv
  python3 funil.py deals.csv --etapas "Qualificação,Diagnóstico,Proposta" \
      --segmentar custo_quantificado --saida 03-analise/funil.md [--json saida.json]

Só biblioteca padrão. Nenhum número é estimado: tudo é contagem ou mediana do arquivo.
"""
import argparse
import csv
import io
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime

DATE_FORMATS = ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ",
                "%Y-%m-%dT%H:%M:%S.%fZ", "%d/%m/%Y", "%d/%m/%Y %H:%M", "%d/%m/%Y %H:%M:%S",
                "%m/%d/%Y %H:%M", "%d-%m-%Y"]

STAGE_PATTERNS = [
    re.compile(r"^entrou[_ ](.+)$", re.I),
    re.compile(r"^entrada[_ ](.+)$", re.I),
    re.compile(r"^data de entrada (?:em |na |no )?(.+)$", re.I),
    re.compile(r"^date entered ['\"]?(.+?)['\"]?$", re.I),
]

ALIASES = {
    "status": ["status", "resultado", "deal status", "situacao", "situação", "is closed won", "estado"],
    "criado": ["criado_em", "create date", "created", "data de criacao", "data de criação", "createdate", "criado"],
    "fechado": ["fechado_em", "close date", "closed", "data de fechamento", "closedate", "fechado"],
    "motivo": ["motivo_perda", "closed lost reason", "motivo de perda", "lost reason", "motivo"],
    "valor": ["valor", "amount", "valor_mensal", "valor do negocio", "valor do negócio", "deal amount", "mrr", "arr"],
    "dono": ["dono", "owner", "deal owner", "proprietario", "proprietário", "vendedor", "responsavel", "responsável"],
}

WON = {"ganho", "won", "closed won", "ganha", "fechado ganho", "true", "sim"}
LOST = {"perdido", "lost", "closed lost", "perdida", "fechado perdido"}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def parse_date(v):
    v = (v or "").strip()
    if not v:
        return None
    for f in DATE_FORMATS:
        try:
            return datetime.strptime(v[:26], f)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(v.replace("Z", ""))
    except ValueError:
        return None


def parse_num(v):
    v = (v or "").strip().replace("R$", "").replace(" ", "")
    if not v:
        return None
    if "," in v and "." in v:
        v = v.replace(".", "").replace(",", ".") if v.rfind(",") > v.rfind(".") else v.replace(",", "")
    elif "," in v:
        v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None


def read_csv(path):
    raw = None
    for enc in ("utf-8-sig", "latin-1"):
        try:
            with open(path, encoding=enc) as fh:
                raw = fh.read()
            break
        except UnicodeDecodeError:
            continue
    if raw is None:
        sys.exit(f"Não consegui ler {path}")
    try:
        dialect = csv.Sniffer().sniff(raw[:5000], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    rows = list(csv.DictReader(io.StringIO(raw), dialect=dialect))
    if not rows:
        sys.exit("CSV vazio.")
    return rows


def find_col(headers, key, override=None):
    if override:
        if override not in headers:
            sys.exit(f"Coluna '{override}' não existe. Colunas: {', '.join(headers)}")
        return override
    nh = {norm(h): h for h in headers}
    for a in ALIASES[key]:
        if norm(a) in nh:
            return nh[norm(a)]
    return None


def stage_columns(headers, etapas_arg):
    found = []
    for h in headers:
        for p in STAGE_PATTERNS:
            m = p.match(h.strip())
            if m:
                name = re.sub(r"\s*\(.*\)$", "", m.group(1)).strip(" '\"")
                found.append((name, h))
                break
    if not found:
        sys.exit("Nenhuma coluna de entrada por etapa encontrada (ex.: entrou_proposta, 'Date entered Proposta').")
    if etapas_arg:
        ordered = []
        for e in [x.strip() for x in etapas_arg.split(",") if x.strip()]:
            match = [f for f in found if norm(f[0]) == norm(e)] or [f for f in found if norm(e) in norm(f[0])]
            if not match:
                sys.exit(f"Etapa '{e}' não encontrada. Etapas no arquivo: {', '.join(f[0] for f in found)}")
            ordered.append((e, match[0][1]))
        return ordered
    return found


def status_of(v):
    n = norm(v)
    if n in {norm(x) for x in WON}:
        return "ganho"
    if n in {norm(x) for x in LOST}:
        return "perdido"
    return "aberto"


def pct(a, b):
    return f"{100 * a / b:.1f}%".replace(".", ",") if b else "–"


def med(xs):
    return f"{statistics.median(xs):.0f}" if xs else "–"


def analyze(rows, stages, cols, seg_col):
    deals = []
    for r in rows:
        d = {
            "status": status_of(r.get(cols["status"], "")) if cols["status"] else "aberto",
            "criado": parse_date(r.get(cols["criado"], "")) if cols["criado"] else None,
            "fechado": parse_date(r.get(cols["fechado"], "")) if cols["fechado"] else None,
            "motivo": (r.get(cols["motivo"], "") or "").strip() if cols["motivo"] else "",
            "valor": parse_num(r.get(cols["valor"], "")) if cols["valor"] else None,
            "dono": (r.get(cols["dono"], "") or "").strip() if cols["dono"] else "",
            "seg": (r.get(seg_col, "") or "").strip() if seg_col else "",
            "entrou": [parse_date(r.get(c, "")) for _, c in stages],
        }
        idx = [i for i, x in enumerate(d["entrou"]) if x]
        d["ultima"] = max(idx) if idx else None
        d["pulou"] = [i for i in range(d["ultima"]) if not d["entrou"][i]] if idx else []
        deals.append(d)
    return deals


def entered_passed(ds, i, k):
    """Negócios que entraram na etapa i (com data) e, desses, os que passaram adiante."""
    entrou = [d for d in ds if d["entrou"][i]]
    if i < k - 1:
        passou = [d for d in entrou if d["ultima"] > i]
    else:
        passou = [d for d in entrou if d["status"] == "ganho"]
    return entrou, passou


def report(deals, stages, seg_col, path):
    n = len(deals)
    names = [s for s, _ in stages]
    k = len(names)
    out = []
    w = out.append
    ganhos = [d for d in deals if d["status"] == "ganho"]
    perdidos = [d for d in deals if d["status"] == "perdido"]
    fechados = ganhos + perdidos
    datas = [d["criado"] for d in deals if d["criado"]]

    w(f"# Funil · saída do funil.py\n")
    w(f"Arquivo: `{path}` · {n} negócios · {len(ganhos)} ganhos · {len(perdidos)} perdidos · "
      f"{n - len(fechados)} abertos")
    if datas:
        w(f"Período de criação: {min(datas):%Y-%m-%d} a {max(datas):%Y-%m-%d}")
    w("Todos os números abaixo são contagens ou medianas do arquivo. Use a tag `[MEDIDO: funil.md]`.\n")

    # resumo
    wr = len(ganhos) / len(fechados) if fechados else 0
    ciclo = [(d["fechado"] - d["criado"]).days for d in ganhos if d["fechado"] and d["criado"]]
    tick = [d["valor"] for d in ganhos if d["valor"] is not None]
    w("## Resumo\n")
    w("| Indicador | Valor |\n|---|---|")
    w(f"| Win rate (ganhos ÷ fechados) | {pct(len(ganhos), len(fechados))} |")
    w(f"| Ciclo mediano dos ganhos (dias, criação → fechamento) | {med(ciclo)} |")
    if tick:
        w(f"| Valor mediano dos ganhos | {statistics.median(tick):,.0f} |".replace(",", "."))
    pularam = [d for d in deals if d["pulou"]]
    w(f"| Negócios que pularam alguma etapa | {len(pularam)} ({pct(len(pularam), n)}) |\n")

    # etapas
    w("## Conversão por etapa\n")
    w("Entrou = tem data de entrada na etapa. Passou = dos que entraram, chegou a uma etapa posterior (ou ganhou, na última). "
      "Quem pulou a etapa não entra na conta dela (ver Etapas puladas). Conversão fechados = só negócios já ganhos ou perdidos.\n")
    w("| Etapa | Entrou | Passou para a seguinte | Conversão (todos) | Conversão (fechados) | Dias na etapa (mediana) |")
    w("|---|---|---|---|---|---|")
    stage_rows = []
    for i, name in enumerate(names):
        entrou, passou = entered_passed(deals, i, k)
        prox = names[i + 1] if i < k - 1 else "Ganho"
        ch_f = [d for d in entrou if d["status"] != "aberto"]
        pa_f = [d for d in passou if d["status"] != "aberto"]
        dias = []
        for d in entrou:
            a = d["entrou"][i]
            b = next((x for x in d["entrou"][i + 1:] if x), None) if i < k - 1 else (d["fechado"] if d["status"] == "ganho" else None)
            if a and b and b >= a:
                dias.append((b - a).days)
        w(f"| {name} → {prox} | {len(entrou)} | {len(passou)} | {pct(len(passou), len(entrou))} | "
          f"{pct(len(pa_f), len(ch_f))} | {med(dias)} |")
        stage_rows.append({"etapa": name, "entrou": len(entrou), "passou": len(passou),
                           "conv_todos": len(passou) / len(entrou) if entrou else None,
                           "conv_fechados": len(pa_f) / len(ch_f) if ch_f else None,
                           "dias_mediana": statistics.median(dias) if dias else None})
    total_top = sum(1 for d in deals if d["ultima"] is not None)
    w(f"\nConversão acumulada (ganhos ÷ negócios com alguma etapa): {pct(len(ganhos), total_top)}\n")

    vaz = [r for r in stage_rows if r["conv_fechados"] is not None]
    if vaz:
        pior = min(vaz, key=lambda r: r["conv_fechados"])
        w(f"**Maior vazamento (fechados):** {pior['etapa']} ({pct(pior['conv_fechados'] * 100, 100)} passam).")
    lentas = [r for r in stage_rows if r["dias_mediana"] is not None]
    if lentas:
        lenta = max(lentas, key=lambda r: r["dias_mediana"])
        w(f"**Etapa mais lenta:** {lenta['etapa']} ({lenta['dias_mediana']:.0f} dias de mediana).\n")

    # perdas
    if perdidos:
        w("## Perdas por etapa onde o negócio parou\n")
        por = defaultdict(Counter)
        for d in perdidos:
            st = names[d["ultima"]] if d["ultima"] is not None else "(sem etapa)"
            por[st][d["motivo"] or "(sem motivo)"] += 1
        w("| Etapa | Perdidos | Motivos (n) |\n|---|---|---|")
        for st in names + ["(sem etapa)"]:
            if st in por:
                c = por[st]
                w(f"| {st} | {sum(c.values())} | " + "; ".join(f"{m} ({q})" for m, q in c.most_common()) + " |")
        sem = sum(1 for d in perdidos if not d["motivo"])
        w(f"\nMotivo de perda preenchido em {pct(len(perdidos) - sem, len(perdidos))} dos perdidos.\n")

    # pulos
    if pularam:
        w("## Etapas puladas\n")
        c = Counter(names[i] for d in pularam for i in d["pulou"])
        w("| Etapa pulada | Negócios | Win rate desses (fechados) |\n|---|---|---|")
        for st, q in c.most_common():
            grupo = [d for d in pularam if names.index(st) in d["pulou"] and d["status"] != "aberto"]
            g = sum(1 for d in grupo if d["status"] == "ganho")
            w(f"| {st} | {q} | {pct(g, len(grupo))} ({len(grupo)} fechados) |")
        nao = [d for d in fechados if not d["pulou"]]
        w(f"\nWin rate de quem **não** pulou etapa: {pct(sum(1 for d in nao if d['status'] == 'ganho'), len(nao))} ({len(nao)} fechados)\n")

    def tabela(chave, titulo):
        grupos = defaultdict(list)
        for d in deals:
            grupos[d[chave] or "(vazio)"].append(d)
        w(f"## {titulo}\n")
        w("| Valor | Negócios | Ganhos | Perdidos | Win rate | Ciclo mediano ganho (dias) |\n|---|---|---|---|---|---|")
        for g, ds in sorted(grupos.items(), key=lambda x: -len(x[1])):
            gg = [d for d in ds if d["status"] == "ganho"]
            pp = [d for d in ds if d["status"] == "perdido"]
            cc = [(d["fechado"] - d["criado"]).days for d in gg if d["fechado"] and d["criado"]]
            w(f"| {g} | {len(ds)} | {len(gg)} | {len(pp)} | {pct(len(gg), len(gg) + len(pp))} | {med(cc)} |")
        w("")
        # conversão por etapa dentro de cada grupo (só negócios fechados)
        w(f"Conversão por etapa em cada grupo (fechados; entre parênteses: passou/chegou):\n")
        w("| Etapa | " + " | ".join(g for g in sorted(grupos)) + " |")
        w("|---|" + "---|" * len(grupos))
        for i, name in enumerate(names):
            prox = names[i + 1] if i < k - 1 else "Ganho"
            cel = []
            for g in sorted(grupos):
                en, pa = entered_passed([d for d in grupos[g] if d["status"] != "aberto"], i, k)
                ch = en
                cel.append(f"{pct(len(pa), len(ch))} ({len(pa)}/{len(ch)})")
            w(f"| {name} → {prox} | " + " | ".join(cel) + " |")
        w("")

    if any(d["dono"] for d in deals):
        tabela("dono", "Por dono")
    if seg_col:
        tabela("seg", f"Recorte por `{seg_col}`")

    w("## Leitura do analista\n")
    w("<!-- Escreva abaixo: maior vazamento, etapa mais lenta, diferença entre donos, o que os perdidos têm em comum. "
      "Cite só números desta página. -->")
    return "\n".join(out), {"n": n, "ganhos": len(ganhos), "perdidos": len(perdidos), "etapas": stage_rows}


def main():
    ap = argparse.ArgumentParser(description="Leitura do funil a partir do export do CRM")
    ap.add_argument("csv")
    ap.add_argument("--etapas", help="Ordem das etapas, separadas por vírgula")
    ap.add_argument("--segmentar", help="Coluna para recorte (ex.: segmento, custo_quantificado)")
    ap.add_argument("--saida", help="Arquivo .md de saída (padrão: imprime)")
    ap.add_argument("--json", help="Arquivo .json com os números")
    for k in ALIASES:
        ap.add_argument(f"--col-{k}", help=f"Nome da coluna de {k}")
    a = ap.parse_args()

    rows = read_csv(a.csv)
    headers = list(rows[0].keys())
    stages = stage_columns(headers, a.etapas)
    cols = {k: find_col(headers, k, getattr(a, f"col_{k}")) for k in ALIASES}
    if a.segmentar and a.segmentar not in headers:
        sys.exit(f"Coluna '{a.segmentar}' não existe.")
    deals = analyze(rows, stages, cols, a.segmentar)
    md, data = report(deals, stages, a.segmentar, a.csv)
    faltam = [k for k, v in cols.items() if not v]
    if faltam:
        md += f"\n\n> Colunas não encontradas: {', '.join(faltam)}. Registrar como `[PRECISA DE DADO]` ou informar com --col-<nome>."
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as fh:
            fh.write(md + "\n")
        print(f"Funil salvo em {a.saida}")
    else:
        print(md)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2, default=str)


if __name__ == "__main__":
    main()
