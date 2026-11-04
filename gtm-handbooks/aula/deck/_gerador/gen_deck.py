#!/usr/bin/env python3
"""Gera o deck 'Building GTM Handbooks & Skills' (racional da aula) com cara de interface."""
import json, os, html, datetime

ROOT = os.environ.get("DECK_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # aula/deck
COMPLETO = os.environ.get("DECK_COMPLETO") == "1"
SL = os.path.join(ROOT, "slides")

# paleta SCIENT
BG = "#EEF0F5"; WIN = "#FFFFFF"; RAIL = "#F7F8FC"; INK = "#111111"; INK2 = "#585858"
LINE = "#E1E4EC"; BLUE = "#0030E8"; BLUE_S = "#E8ECFD"; BLUE_L = "#A0B0E8"; DARK = "#282828"; DARK2 = "#303030"
GREEN = "#40E0A8"; WARN_BG = "#F1F2F5"; WARN = "#111111"; CRIT_BG = "#ECEDF1"; CRIT = "#111111"
POS_BG = "#E8ECFD"; POS = "#0030E8"
FONT = "font-family:'Sora', Arial, sans-serif"

RAIL_ITEMS = [("0", "Visão geral"), ("1", "Por quê"), ("2", "Coletar"), ("3", "Metodologia"),
              ("4", "Analisar"), ("5", "Documentar"), ("6", "Executar"), ("7", "Melhoria contínua")]

def e(t):
    return html.escape(t, quote=False)

def p(text, size=28, color=INK, weight=400, extra=""):
    return f'<p style="font-size:{size}px;color:{color};font-weight:{weight};line-height:1.4;{extra}">{text}</p>'

def chip(text, bg=BLUE_S, fg=BLUE, size=24, weight=600, grid=False):
    selfal = "justify-self:start" if grid else "align-self:flex-start"
    return (f'<p style="font-size:{size}px;font-weight:{weight};color:{fg};background:{bg};'
            f'padding:6px 14px;border-radius:4px;white-space:nowrap;{selfal}">{text}</p>')

def card(inner, bg=WIN, border=LINE, pad=28, gap=12, extra=""):
    return (f'<div style="display:flex;flex-direction:column;gap:{gap}px;background:{bg};'
            f'border:1px solid {border};border-radius:4px;padding:{pad}px;{extra}">{inner}</div>')

def row(inner, gap=24, extra=""):
    return f'<div style="display:flex;gap:{gap}px;{extra}">{inner}</div>'

def col(inner, gap=16, extra=""):
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px;{extra}">{inner}</div>'

def table(header, rows, widths, size=24, hl_col0=False):
    th = "".join(f'<th style="width:{w}%;text-align:left">{h}</th>' for h, w in zip(header, widths))
    out = [f'<table style="font-size:{size}px;color:{INK};{FONT};width:100%">',
           f'<tr style="background:{RAIL}">{th}</tr>']
    for r in rows:
        tds = "".join(f'<td style="color:{(BLUE if (hl_col0 and i == 0) else INK)}">{c}</td>' for i, c in enumerate(r))
        out.append(f"<tr>{tds}</tr>")
    out.append("</table>")
    return "".join(out)

def rail(active):
    items = []
    for n, label in RAIL_ITEMS:
        txt = label if n == "0" else f"{n}&#160;&#160;{label}"
        if n == active:
            items.append(f'<p style="font-size:24px;font-weight:600;color:#FFFFFF;background:{BLUE};padding:12px 16px;border-radius:4px;white-space:nowrap">{txt}</p>')
        else:
            items.append(f'<p style="font-size:24px;color:{INK2};padding:12px 16px;white-space:nowrap">{txt}</p>')
    return (f'<div style="width:330px;display:flex;flex-direction:column;gap:6px;background:{RAIL};'
            f'border-right:1px solid {LINE};padding:40px 24px">'
            f'<p style="font-size:24px;font-weight:600;color:{INK2};letter-spacing:2px;padding:0 20px 12px">JORNADA</p>'
            + "".join(items) + '</div>')

def topbar(crumb, idx, total):
    dots = "".join(f'<x-shape kind="ellipse" style="width:16px;height:16px;background:#D5D9E2"></x-shape>' for _ in range(3))
    return (f'<div style="display:flex;align-items:center;gap:24px;padding:20px 36px;border-bottom:1px solid {LINE};background:{WIN}">'
            f'{row(dots, 10, "align-items:center")}'
            f'<p style="font-family:\'Lexend\', Arial, sans-serif;font-size:26px;font-weight:600;letter-spacing:3px;color:{INK}">SCIENT</p>'
            f'<p style="font-size:24px;color:{INK2}">Handbooks &amp; Skills&#160;&#160;›&#160;&#160;{crumb}</p>'
            f'<div style="flex:1"></div>'
            f'<p style="font-size:24px;color:{INK2};font-variant-numeric:tabular-nums">{idx if idx == 'extra' else f'{idx} / {total}'}</p></div>')

SLIDES = []

def screen(sid, active, crumb, eyebrow, title, body, notes):
    SLIDES.append(dict(id=sid, kind="screen", active=active, crumb=crumb, eyebrow=eyebrow, title=title, body=body, notes=notes))

# Versão curta (35-40 min): telas visíveis e minutos de cada uma. As demais ficam ocultas (puladas na apresentação).
CURTA = {"r-cover": 1, "r-gaveta": 2, "r-tese": 3, "r-ia": 2, "r-jornada": 2, "r-fontes": 2, "r-documentos": 3,
         "r-lente": 2, "r-triangulacao": 3, "r-hipotese": 2, "r-anatomia": 2, "r-rubrica": 3, "r-skills": 2,
         "r-case": 2, "r-coaching": 2, "r-coaching2": 2, "r-amanha": 1, "r-regras": 1}
import re as _re
if COMPLETO:
    CURTA = None
def visivel(sid):
    return CURTA is None or sid in CURTA

def notas(sid, txt):
    if CURTA is None:
        return txt
    corpo = _re.sub(r"^[^.]*?\d+ min\.\s*", "", txt, count=1)
    if sid not in CURTA:
        return "[Tela extra, oculta na versão curta] " + corpo
    return f"{CURTA[sid]} min. " + corpo

def render_screen(s, idx, total):
    hid = "" if visivel(s["id"]) else " hidden"
    return (f'<section id="{s["id"]}" data-transition="fade"{hid} style="background:{BG};color:{INK};{FONT};padding:48px;display:flex">'
            f'<div style="flex:1;display:flex;flex-direction:column;background:{WIN};border:1px solid #D5D9E2;border-radius:4px;'
            f'box-shadow:0px 12px 40px rgba(17,17,17,0.08);overflow:hidden">'
            f'{topbar(s["crumb"], idx, total)}'
            f'<div style="flex:1;display:flex">{rail(s["active"])}'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:36px;padding:44px 56px">'
            f'<div style="display:flex;flex-direction:column;gap:10px">'
            f'<p style="font-size:24px;font-weight:600;color:{BLUE};letter-spacing:2px;text-transform:uppercase">{s["eyebrow"]}</p>'
            f'<h2 style="font-size:52px;font-weight:400;line-height:1.15;color:{INK}">{s["title"]}</h2></div>'
            f'{s["body"]}</div></div></div>'
            f'<aside>{e(notas(s["id"], s["notes"]))}</aside></section>')

# ─────────────────────────── CONTEÚDO ───────────────────────────

# 1 · capa (render próprio)
SLIDES.append(dict(id="r-cover", kind="cover"))

def render_cover(idx, total):
    steps = "".join(
        f'<p style="font-size:24px;color:{"#FFFFFF" if n != "0" else BLUE_L};border:1px solid #4A4A4A;padding:10px 18px;border-radius:4px;white-space:nowrap">{n}&#160;&#160;{l}</p>'
        for n, l in RAIL_ITEMS[1:])
    return (f'<section id="r-cover" data-transition="fade" style="background:{DARK};color:#FFFFFF;{FONT};padding:128px;display:flex;flex-direction:column;gap:40px">'
            f'<p style="font-size:24px;font-weight:600;letter-spacing:3px;color:{BLUE_L}">CERTIFICAÇÃO GTM ENGINEER · SCIENT</p>'
            f'<h1 style="font-size:112px;font-weight:300;line-height:1.05;color:#FFFFFF">Building GTM<br>Handbooks &amp; Skills</h1>'
            f'<p style="font-size:36px;font-weight:300;line-height:1.4;color:#D9D9D9;width:1300px">Como documentar o processo comercial que funciona e transformar esse documento em skills que o time usa no dia a dia.</p>'
            f'<div style="flex:1"></div>'
            f'<div style="display:flex;gap:12px;flex-wrap:wrap">{steps}</div>'
            f'<aside>{e(notas("r-cover", "Abertura, 3 min. A aula é sobre racional: o que coletar, o que documentar e por quê. A ferramenta (o kit no skills.scient.cc) aparece só no fim. Pergunta para abrir: quem aqui tem um playbook que o time abre toda semana?"))}</aside></section>')

# 2 · visão geral
screen("r-promessa", "0", "Visão geral", "Hoje", "O que vocês vão aprender hoje",
    row(
        card(chip("01") + '<h3 style="font-size:36px;font-weight:600">O que coletar</h3>'
             + p("O que pedir para a empresa, o que cada informação mostra e quanto é suficiente.", 28, INK2), extra="flex:1")
        + card(chip("02") + '<h3 style="font-size:36px;font-weight:600">O que documentar</h3>'
             + p("Quais processos documentar e como escrever um handbook que o time realmente usa.", 28, INK2), extra="flex:1")
        + card(chip("03") + '<h3 style="font-size:36px;font-weight:600">Como vira execução e coaching</h3>'
             + p("Como o handbook vira skill para o dia a dia e rubrica para avaliar cada reunião.", 28, INK2), extra="flex:1"),
        28)
    + card(p("Vamos usar um exemplo do começo ao fim: a ACME, uma empresa fictícia que vende squads de engenharia e usa Challenger.", 28, INK), bg=BLUE_S, border=BLUE_S),
    "Abertura, 2 min. Três promessas. O exemplo ACME é fictício e atravessa a aula inteira: os números que aparecem são de dados sintéticos de treinamento. A metodologia do exemplo é Challenger, mas o método vale para qualquer uma.")

# 3 · gaveta
screen("r-gaveta", "1", "Por quê", "O problema", "Por que quase ninguém usa o playbook da empresa",
    row(
        col(card(
            row(f'<x-icon name="Search" style="color:{INK2};width:28px;height:28px"></x-icon>'
                + p("Drive&#160;&#160;›&#160;&#160;Vendas&#160;&#160;›&#160;&#160;Playbooks", 24, INK2) + '<div style="flex:1"></div>'
                + chip("4 arquivos", RAIL, INK2), 14, f"align-items:center;padding:16px 22px;border-bottom:1px solid {LINE};background:{RAIL}")
            + "".join(
                row(p(ext, 22, "#FFFFFF", 600, f"background:{cor};padding:6px 0;width:84px;text-align:center;border-radius:4px")
                    + col(p(nome, 26, INK, 600) + p(meta, 24, INK2), 2, "flex:1")
                    + (chip("nunca aberto", CRIT_BG, CRIT) if alerta else ""),
                    18, f"align-items:center;padding:16px 22px;border-bottom:1px solid {LINE}")
                for ext, cor, nome, meta, alerta in [
                    ("PDF", "#585858", "Playbook Comercial v3 FINAL", "editado há 14 meses · aberto 2 vezes", False),
                    ("DOCX", "#585858", "Processo de vendas NOVO", "editado há 9 meses", True),
                    ("PPTX", "#585858", "Treinamento de metodologia", "editado há 2 anos · aberto 1 vez", False),
                    ("PPTX", "#585858", "Pitch institucional 2024", "editado há 18 meses · aberto 5 vezes", False)]),
            pad=0, gap=0, extra="overflow:hidden")
            + p("Cena comum na pasta de vendas de qualquer empresa (ilustrativo).", 24, INK2), 12, "flex:1.25")
        + col(
            card('<h3 style="font-size:30px;font-weight:600">Descreve o ideal</h3>' + p("Foi escrito a partir de um livro ou do que a gestão gostaria, e não do que acontece nas reuniões.", 26, INK2), pad=24, gap=8)
            + card('<h3 style="font-size:30px;font-weight:600">Ninguém mede</h3>' + p("Ninguém sabe se quem segue o playbook vende mais.", 26, INK2), pad=24, gap=8)
            + card('<h3 style="font-size:30px;font-weight:600">Ninguém consulta</h3>' + p("É lido no onboarding e depois esquecido.", 26, INK2), pad=24, gap=8),
            16, "flex:1"),
        36),
    "Bloco 1, 5 min. Pergunta: no último playbook que vocês escreveram, quanto veio do livro e quanto veio das reuniões? Os três motivos organizam a aula: documentar o real (coletar e analisar), medir (funil e métricas), levar para a reunião (skills).")

# 4 · tese
def tri(label, q, src, color=BLUE):
    return card(chip(label, BLUE_S, color) + f'<h3 style="font-size:32px;font-weight:600;line-height:1.25">{q}</h3>' + p(src, 26, INK2), pad=28, extra="flex:1")
screen("r-tese", "1", "Por quê", "A ideia da aula", "Um bom handbook mostra como a empresa vende de verdade",
    row(tri("DOCUMENTOS", "O que a empresa diz que faz?", "Processos escritos, PPTs de proposta e de produto, conclusões de análises.")
        + tri("GRAVAÇÕES", "O que o time faz de verdade?", "Transcrições de reuniões ganhas e perdidas, por etapa.")
        + tri("CRM", "O que dá resultado?", "Funil do CRM: conversão, tempo e motivo de perda por etapa."), 24)
    + row(f'<x-icon name="Lightbulb" style="color:{BLUE};width:48px;height:48px"></x-icon>'
          + p("Pense num GPS: o mapa mostra o caminho oficial, o trânsito mostra o que acontece de verdade e o tempo de chegada mostra o que funciona. O handbook usa os três.", 30, INK),
          24, f"align-items:center;background:{BLUE_S};padding:28px 32px;border-radius:4px"),
    "Bloco 1, 5 min. É a ideia central da aula. Nenhuma visão sozinha basta: documento sozinho é o ideal; reunião sozinha é anedota; funil sozinho diz onde quebra, mas não o porquê. A metodologia (Challenger, MEDDPICC...) diz o que procurar em cada uma delas.")

# 5 · IA
screen("r-ia", "1", "Por quê", "O que mudou", "O que muda quando o handbook vira skill",
    row(
        col(chip("ANTES", RAIL, INK2)
            + card(row(f'<x-icon name="Book" style="color:{INK2};width:56px;height:56px"></x-icon>'
                       + col(p("<b>Playbook_Comercial.pdf</b>", 28) + p("Lido no onboarding. Consultado quando alguém lembra.", 26, INK2), 4), 20, "align-items:center"), pad=28)
            + p("Só ajuda se o vendedor lembrar de abrir.", 28, INK2), 16, "flex:1")
        + col(chip("DEPOIS")
            + card(
                row('<div style="flex:1"></div>' + p("Amanhã tenho diagnóstico com a Orbita Pay. Me prepara.", 26, "#FFFFFF", 400,
                                                   f"background:{BLUE};padding:16px 22px;border-radius:4px;width:640px"), 0)
                + col(chip("skill · diagnóstico", WIN, BLUE, 24)
                      + p("<b>Objetivo:</b> sair com o custo do problema em R$", 26)
                      + p("<b>Hipóteses</b> para o CTO e para o Head de Engenharia", 26)
                      + p("<b>4 perguntas</b> para chegar ao custo em reais", 26)
                      + p("<b>Próximo passo:</b> proposta com o decisor, com data", 26),
                      8, f"background:{RAIL};padding:22px 24px;border-radius:4px;border:1px solid {LINE}"),
                pad=24, gap=16)
            + p("A skill traz o handbook na hora da reunião.", 28, INK2), 16, "flex:1.35"),
        40),
    "Bloco 1, 4 min. Skill é um pacote de instruções que o Claude carrega quando o assunto aparece. Analogia: conectores (CRM, gravador) são a cozinha; skills são as receitas. Um handbook bem escrito vira, quase direto, a receita de cada etapa. Por isso o handbook precisa ser específico: skill genérica gera resposta genérica.")

# 6 · jornada
def step(n, name, q):
    return card(chip(n) + f'<h3 style="font-size:32px;font-weight:600">{name}</h3>' + p(q, 24, INK2), pad=22, gap=10)
screen("r-jornada", "0", "Visão geral", "O caminho", "Os sete passos que vamos percorrer",
    f'<div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:20px">'
    + step("1", "Por quê", "Quais processos, qual metodologia, quem aprova?")
    + step("2", "Coletar", "Temos evidência das quatro fontes?")
    + step("3", "Metodologia", "O que procurar em cada reunião?")
    + step("4", "Analisar", "O que se diz, se faz e dá resultado?")
    + step("5", "Documentar", "Qual o processo que funciona, passo a passo?")
    + step("6", "Executar", "Como o time usa e é treinado com isso?")
    + step("7", "Melhoria contínua", "Como o processo melhora a cada reunião?")
    + card(p("Cada passo termina com uma pergunta de <b>sim ou não</b>. Só avança com sim.", 28, INK, 400), bg=BLUE_S, border=BLUE_S, pad=22)
    + '</div>',
    "Bloco 1, 3 min. Este é o mapa da aula: a barra lateral de cada tela mostra onde estamos. O gate binário de cada passo é o que impede o handbook de nascer de suposição.")

# 7 · quatro fontes
def fonte(letter, name, reveals, q):
    return card(row(f'<p style="font-size:56px;font-weight:300;color:{BLUE};line-height:1">{letter}</p>'
                    + f'<h3 style="font-size:34px;font-weight:600">{name}</h3>', 16, "align-items:center")
                + p(f"<b>Revela:</b> {reveals}", 26) + p(q, 26, INK2), pad=26, gap=12, extra="flex:1")
screen("r-fontes", "2", "Coletar", "Passo 2 · O pedido de dados", "O que pedir para a empresa antes de começar",
    f'<div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:20px">'
    + fonte("A", "Números", "em que etapa os negócios se perdem", "Export do CRM: um negócio por linha, data de entrada em cada etapa.")
    + fonte("B", "Gravações", "o que os melhores vendedores fazem", "Transcrições de reuniões ganhas e perdidas, por etapa.")
    + fonte("C", "Documentos", "o que a empresa diz que faz", "Processos escritos, análises, PPT de proposta e de produto.")
    + fonte("D", "Entrevistas", "por que as coisas são feitas assim", "Três conversas de 30 minutos.")
    + '</div>',
    "Bloco 2, 4 min. Pedir tudo junto, num único pedido, com dono por fonte e prazo (sugestão: 5 dias úteis). Pedir em partes multiplica o tempo do projeto. Pergunta: das quatro, qual vocês conseguiriam pedir amanhã? Qual é a mais difícil?")

# 8 · números
screen("r-numeros", "2", "Coletar › A. Números do CRM", "Fonte A · Números do CRM", "Onde os negócios se perdem no funil",
    card(table(["Negócio", "Parou em", "Passou pelo Diagnóstico?", "Resultado", "Motivo da perda"],
               [["Alta Saúde", "Contrato", "Sim", "Ganhou", "—"],
                ["Linha Data", "Diagnóstico", "Sim", "Perdeu", "Sem decisor"],
                ["Ponto Pay", "Follow-up", "Não, pulou", "Perdeu", "Preço"],
                ["Atlas Flow", "Proposta", "Sim", "Em aberto", "—"]],
               [19, 18, 27, 16, 20], 24), pad=16)
    + row(f'<x-icon name="Lightbulb" style="color:{BLUE};width:40px;height:40px"></x-icon>'
          + p("A Ponto Pay pulou o Diagnóstico e perdeu por preço. Quando isso se repete em muitos negócios, vira um padrão.", 26, INK),
          18, f"align-items:center;background:{BLUE_S};padding:18px 24px;border-radius:4px")
    + row(card('<h3 style="font-size:28px;font-weight:600">O que pedir</h3>' + p("A lista de negócios do CRM, com a data em que cada um entrou em cada etapa e o motivo da perda.", 24, INK2), pad=22, gap=8, extra="flex:1")
          + card('<h3 style="font-size:28px;font-weight:600">Quanto basta</h3>' + p("Pelo menos 6 meses de histórico e 30 negócios já encerrados.", 24, INK2), pad=22, gap=8, extra="flex:1"), 20),
    "Bloco 2, 3 min. Linhas do exemplo fictício. A Ponto Pay pulou o diagnóstico e perdeu por preço: um caso é anedota, mas o CRM mostra se isso acontece com muitos negócios. O campo que mais falta nos CRMs é a data de entrada em cada etapa. Sem ela, só dá para ver se o negócio foi ganho ou perdido, e não onde ele parou.")

# 9 · conversas
G = chip("Ganho", POS_BG, POS, grid=True); L = chip("Perdido", CRIT_BG, CRIT, grid=True)
screen("r-conversas", "2", "Coletar › B. Gravações", "Fonte B · Gravações", "As gravações mostram o que os melhores vendedores fazem",
    card(f'<div style="display:grid;grid-template-columns:1.1fr 0.9fr 0.6fr 1.6fr;gap:14px;align-items:center">'
         + "".join(p(h, 24, INK2, 600) for h in ["Reunião", "Etapa", "Resultado", "Por que entra na amostra"])
         + p("TechScale", 26) + p("Diagnóstico", 26) + G + p("Referência do que funciona", 26, INK2)
         + p("Orbita Pay", 26) + p("Diagnóstico", 26) + L + p("Contraste na mesma etapa", 26, INK2)
         + p("Nuvia Saúde", 26) + p("Proposta", 26) + L + p("Objeção: sem acesso ao decisor", 26, INK2)
         + p("TechScale", 26) + p("Contrato", 26) + G + p("Negociação sem desconto", 26, INK2)
         + '</div>', pad=24)
    + row(chip("2 a 4 por etapa", RAIL, INK) + chip("ganhos e perdidos", RAIL, INK) + chip("vendedores diferentes", RAIL, INK)
          + chip("transcrição inteira, não o resumo", RAIL, INK), 14, "flex-wrap:wrap"),
    "Bloco 2, 3 min. A amostra é escolhida para contraste: o mesmo momento do funil, um ganho e um perdido. Só ganhos não ensinam o que evitar. O resumo automático da ferramenta de gravação perde justamente as perguntas literais, que são o ouro do handbook.")

# 10 · documentos
screen("r-documentos", "2", "Coletar › C. Documentos", "Fonte C · Documentos", "Peça também tudo o que já está escrito",
    card(table(["Documento", "O que revela", "Vira no handbook"],
               [["Manual de vendas", "As etapas oficiais", "O que comparar com a prática"],
                ["Análises de ganhos e perdas", "O que a gestão acha", "Suspeitas para checar no CRM"],
                ["PPT de proposta", "Como o preço é apresentado", "O passo da proposta"],
                ["PPT de produto", "O que a empresa promete", "Diferenciais e provas"],
                ["Preço e descontos", "Regras de negociação", "Alertas"],
                ["Contrato e implantação", "O que se promete", "O que passar para o CS"]],
               [32, 34, 34], 24, hl_col0=True), pad=16)
    + p("Mesmo desatualizado, o documento ajuda: ele mostra o que a empresa acha que faz.", 28, INK, 600),
    "Bloco 2, 5 min. Lição de projeto: já fizemos um trabalho em que pedimos funil e transcrições e esquecemos os documentos; faltou saber o que a empresa achava que fazia, e as conclusões que ela já tinha tirado. Sem o declarado, não há divergência para resolver, e o handbook vira só uma descrição das reuniões. Peça tudo o que existir, mesmo desatualizado.")

# 11 · pessoas
def entrevista(who, qs):
    return card(chip(who) + "".join(p(f"“{q}”", 26, INK) for q in qs), pad=26, gap=14, extra="flex:1")
screen("r-pessoas", "2", "Coletar › D. Entrevistas", "Fonte D · Entrevistas", "Converse com três pessoas do time",
    row(entrevista("TOP PERFORMER", ["O que do processo oficial você não segue? Por quê?", "Em que momento você sabe que vai fechar?"])
        + entrevista("GESTOR COMERCIAL", ["Onde o funil mais vaza? Por que você acha?", "Que análise de ganhos e perdas já foi feita?"])
        + entrevista("CS / IMPLANTAÇÃO", ["Que promessa da venda mais gera problema depois?", "O que falta quando o cliente chega?"]), 24)
    + p("30 minutos com cada um, gravados. Explique no começo que não é uma avaliação: o objetivo é entender como o time vende.", 26, INK2),
    "Bloco 2, 3 min. A pergunta mais valiosa é a primeira do top performer: ela revela a divergência entre o oficial e o que funciona. A entrevista do gestor traz as hipóteses que depois testamos no funil. Se a empresa não tem nenhum documento, as entrevistas passam a ser obrigatórias.")

# 12 · quanto basta
def ingrediente(icon, nome, regra, status, ok=True):
    st = chip(status, POS_BG if ok else WARN_BG, POS if ok else WARN, 24)
    return row(f'<div style="width:64px;height:64px;background:{BLUE_S};display:flex;align-items:center;justify-content:center;border-radius:4px"><x-icon name="{icon}" style="color:{BLUE};width:36px;height:36px"></x-icon></div>'
               + col(p(f"<b>{nome}</b>", 28) + p(regra, 24, INK2), 2, "flex:1") + st,
               20, f"align-items:center;padding:14px 20px;border-bottom:1px solid {LINE}")
screen("r-basta", "2", "Coletar", "Antes de seguir", "Antes de começar, confira se você tem isto",
    p("Como numa receita: separe os ingredientes antes de ligar o fogo.", 28, INK2)
    + card(ingrediente("Chart", "Números do CRM", "Pelo menos 6 meses de negócios e 30 já encerrados.", "✓ ACME: 122 negócios")
           + ingrediente("Chat", "Gravações", "Duas reuniões de cada etapa, uma delas que deu certo.", "✓ ACME: uma ganha, uma perdida")
           + ingrediente("Book", "Documentos", "O manual de vendas ou o PPT de proposta, mesmo antigo.", "✓ ACME: manual e 2 PPTs")
           + ingrediente("Clock", "O que faltou", "Anote o que falta, quem vai trazer e até quando.", "Falta: propostas enviadas", False),
           pad=8, gap=0),
    "Bloco 2, 3 min. É o primeiro ponto de parada. O erro mais comum é começar a escrever com o que tem e completar com suposição. A ACME (exemplo) tem quase tudo; o que faltou ficou anotado, com responsável (o gestor comercial) e prazo (a próxima semana). Não é preciso ter tudo: é preciso saber o que falta e quem traz.")

# 13 · metodologia
def flow(n, t, d):
    return card(chip(n) + f'<h3 style="font-size:30px;font-weight:600">{t}</h3>' + p(d, 24, INK2), pad=22, gap=10, extra="flex:1")
arr = f'<x-shape kind="arrow-right" style="width:44px;height:24px;background:{BLUE_L}"></x-shape>'
screen("r-lente", "3", "Metodologia", "Passo 3 · Metodologia", "A metodologia diz o que procurar em cada reunião",
    row(flow("ESCOLHA", "A metodologia do time", "Challenger, MEDDPICC, SPIN, BANT ou a própria.") + arr
        + flow("OBSERVE", "O que procurar", "Perguntas e comportamentos que ela pede em cada etapa.") + arr
        + flow("DECIDA", "Quando avançar", "O que precisa ter acontecido para mudar de etapa."), 12, "align-items:center")
    + p("Exemplo: a mesma pergunta, <b>“o cliente tem um problema que vale resolver?”</b>, em quatro metodologias", 26, INK2)
    + card(table(["Metodologia", "Como ela chama", "O que procurar na reunião"],
                 [["Challenger", "Reframe + Rational Drowning", "Mostrou um custo que o cliente não via?"],
                  ["MEDDPICC", "Metrics + Implicate the Pain", "A dor tem número e consequência?"],
                  ["SPIN", "Implication + Need-payoff", "O cliente disse a consequência e o ganho?"],
                  ["BANT", "Need", "Existe necessidade real?"]],
                 [20, 36, 44], 24, hl_col0=True), pad=16),
    "Bloco 3, 4 min. Mensagem simples: o método da aula vale para qualquer metodologia. O que muda é o que procuramos nas reuniões. A metodologia vira duas coisas: a lista do que observar em cada etapa e o critério para o negócio avançar. Use a que o time já usa; trocar de metodologia é outro projeto. Se o time mistura duas, tudo bem: junte o que cada uma pede, sem repetir. Pergunta: qual metodologia o time de vocês realmente fala no dia a dia?")

# 14 · metodologia → critério
sc = "".join(chip(t, RAIL, INK) for t in ["0 não aconteceu", "1 só citado", "2 conversado", "3 confirmado pelo cliente"])
screen("r-criterio", "3", "Metodologia", "Passo 3 · Exemplo: Challenger na ACME", "Quando um negócio pode mudar de etapa",
    card(table(["Etapa", "O que precisa ter acontecido", "Pergunta para avançar"],
               [["Qualificação", "O vendedor trouxe uma ideia sobre o negócio do cliente e já marcou a próxima conversa", "Diagnóstico marcado com quem vive o problema?"],
                ["Diagnóstico", "O cliente viu o problema de outro jeito e o custo foi calculado em reais", "O cliente confirmou o custo em R$?"],
                ["Proposta", "O cliente concorda com o novo jeito de trabalhar, e cada pessoa ouviu o que importa para ela", "O decisor concorda com a mudança?"],
                ["Negociação", "O vendedor conduz o processo e tem um aliado dentro do cliente", "Cedeu em escopo, e não em preço?"]],
               [18, 48, 34], 24, hl_col0=True), pad=16)
    + row(p("Em cada reunião, cada item ganha uma nota:", 26, INK2) + sc, 14, "align-items:center;flex-wrap:wrap"),
    "Bloco 3, 4 min. Aqui a metodologia vira prática. A coluna do meio traduz o Challenger em linguagem comum: Qualificação = Warmer e Take Control; Diagnóstico = Reframe e Rational Drowning; Proposta = A New Way e Tailor; Negociação = Take Control e Mobilizer. Em cada reunião, cada item ganha uma nota de 0 a 3, e o negócio só muda de etapa no CRM quando a pergunta da direita tem resposta sim.")

# 15 · triangulação
def tri2(label, txt, src):
    return card(chip(label) + p(txt, 28, INK, 600) + p(src, 24, INK2), pad=24, gap=12, extra="flex:1")
screen("r-triangulacao", "4", "Analisar", "Exemplo · ACME", "Quando o manual e a prática não batem",
    row(tri2("O MANUAL DIZ", "“Diagnóstico é opcional, quando o cliente pedir.”", "Manual de vendas")
        + tri2("O MELHOR VENDEDOR DIZ", "“Para mim, o diagnóstico é a venda.”", "Entrevista")
        + tri2("O CRM MOSTRA", "81% avançam para proposta com custo do problema em R$. Sem ele, 28%.", "122 negócios"), 20)
    + row(f'<x-icon name="Verified" style="color:#FFFFFF;width:44px;height:44px"></x-icon>'
          + p("<b>No handbook:</b> o Diagnóstico passa a ser obrigatório, e só termina com o custo do problema em R$ confirmado pelo cliente.", 28, "#FFFFFF"),
          20, f"align-items:center;background:{BLUE};padding:26px 32px;border-radius:4px"),
    "Bloco 4, 5 min. Exemplo fictício, mas o padrão é comum: o manual tratava o diagnóstico como opcional, o melhor vendedor o considera a própria venda, e o funil confirma. Regra: observado e medido ganham do declarado. Quando observado e medido discordam, a entrevista desempata.")

# 16 · hipótese da gestão
screen("r-hipotese", "4", "Analisar", "Exemplo · ACME", "O que os dados mostraram sobre as perdas por preço",
    row(
        card(chip("O QUE A GESTÃO CONCLUIU", CRIT_BG, CRIT) + p("“Estamos perdendo principalmente por preço.”", 30, INK, 600)
             + p("Ação proposta: tabela de desconto de até 15%.", 26, INK2) + p("Fonte: análise de win/loss do semestre", 24, INK2), pad=28, gap=14, extra="flex:1")
        + card(chip("O QUE O FUNIL MOSTRA") +
               row(col(p("18%", 72, BLUE, 300, "line-height:1") + p("das perdas são por preço/hora", 24, INK2), 6, "flex:1")
                   + col(p("30%", 72, BLUE, 300, "line-height:1") + p("são por falta de decisor", 24, INK2), 6, "flex:1"), 24)
               + p("12 das 15 perdas por preço vieram de quem <b>pulou o diagnóstico</b>.", 28, INK), pad=28, gap=18, extra="flex:1.2"), 24)
    + p("<b>No handbook:</b> nada de tabela de desconto. Entram o custo do problema e o acesso ao decisor.", 30, INK),
    "Bloco 4, 4 min. Este é o momento em que o handbook paga o projeto: evitou uma política de desconto que atacaria o sintoma. Por isso pedimos as conclusões de análises na fonte C: elas viram hipóteses que o funil confirma ou desmente.")

# 17 · funil
etapas = [("Qualificação → Diagnóstico", 84), ("Diagnóstico → Proposta", 54), ("Proposta → Follow-up", 81),
          ("Follow-up → Contrato", 79), ("Contrato → Ganho", 86)]
def hbar(lbl, v):
    colr = BLUE if v == 54 else BLUE_L
    return col(p(lbl, 24, INK if v == 54 else INK2, 600 if v == 54 else 400)
               + row(f'<div style="width:{v*5}px;height:28px;background:{colr}"></div>' + p(f"{v}%", 24, INK, 600), 12, "align-items:center"), 4)
def kpi(v, lbl):
    return card(p(v, 64, BLUE, 300, "line-height:1") + p(lbl, 24, INK2), pad=22, gap=8)
screen("r-funil", "4", "Analisar", "Exemplo fictício · 122 negócios em 12 meses", "Onde o funil da ACME perde negócios",
    row(
        f'<div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:16px;width:560px">'
        + kpi("30%", "dos negócios encerrados foram ganhos") + kpi("54%", "passam do Diagnóstico para a Proposta")
        + kpi("4,4x", "mais chance de ganhar quando o vendedor calcula o custo") + kpi("57%", "de vitórias do melhor vendedor; os outros, 17% a 23%")
        + '</div>'
        + card(p("Quantos passam de uma etapa para a outra", 24, INK2, 600) + col("".join(hbar(l, v) for l, v in etapas), 14), pad=24, gap=16, extra="flex:1"),
        28),
    "Bloco 4, 4 min. Dados fictícios, calculados por script. Três leituras: quase metade dos negócios trava no Diagnóstico; quando o vendedor calcula com o cliente quanto o problema custa, a chance de ganhar é 4,4 vezes maior (65% contra 15%); e o melhor vendedor ganha bem mais que os outros com o mesmo tipo de conta. A diferença está no jeito de vender.")

# 18 · ganhos x perdidos
screen("r-padroes", "4", "Analisar", "Exemplo · ACME", "O que os vendedores fazem nas reuniões que ganham",
    card(table(["Momento", "Nos ganhos", "Nos perdidos"],
               [["Abertura", "Hipótese sobre o negócio do cliente, sem deck", "“Quem somos” e apresentação institucional"],
                ["Diagnóstico", "Perguntas que transformam operação em reais", "Levantamento técnico; impacto sem número"],
                ["Preço", "Só depois do custo do problema", "Preço por hora cedo; desconto na hora"],
                ["Próximo passo", "Vendedor define data e participantes", "“A gente olha e retorna”"]],
               [18, 41, 41], 24, hl_col0=True), pad=16)
    + p("Cada linha vira um passo do handbook: o que fazer e o que evitar, com a frase real e o minuto da gravação.", 26, INK2),
    "Bloco 4, 3 min. As fichas de cada reunião dão nota 0 a 3 por item da metodologia e guardam as perguntas literais. Comparar ganhos e perdidos na mesma etapa é o que transforma anedota em padrão.")

# 19 · o que documentar
procs = ["Prospecção", "Qualificação", "Diagnóstico", "Proposta", "Negociação", "Handoff CS", "Onboarding", "Expansão"]
pchips = "".join(chip(x, BLUE, "#FFFFFF", 26) if x == "Diagnóstico" else chip(x, RAIL, INK, 26, 400) for x in procs)
def rule(t, d):
    return card(f'<h3 style="font-size:30px;font-weight:600">{t}</h3>' + p(d, 24, INK2), pad=24, gap=8, extra="flex:1")
screen("r-oque", "5", "Documentar", "Passo 5 · Documentar", "Quais processos documentar, e em que ordem",
    card(row(pchips, 12, "flex-wrap:wrap") + p("Na ACME, o primeiro é o Diagnóstico: é onde se perde mais negócio e onde os vendedores mais diferem.", 26, INK2), pad=24, gap=18)
    + row(rule("Um por processo", "Um “handbook de vendas” fica genérico. Um “handbook de Diagnóstico” é usado.")
          + rule("3 a 5 passos", "Checklists de até 15 itens. Detalhe vai para anexo.")
          + rule("Um dono", "Nome, versão e data da próxima revisão.") , 20),
    "Bloco 5, 3 min. A recomendação de ordem sai da análise: comece onde o funil mais vaza e onde a diferença entre vendedores é maior. Um handbook pequeno que é usado vale mais que uma enciclopédia.")

# 20 · anatomia
def camada(name, desc, items):
    return card(chip(name) + p(desc, 24, INK2) + "".join(p(i, 26) for i in items), pad=26, gap=10, extra="flex:1")
screen("r-anatomia", "5", "Documentar", "O modelo de handbook", "As 14 partes de um handbook",
    row(camada("ENTENDER", "O resumo para quem abre", ["0 · A conclusão em uma frase", "1 · Onde a etapa fica no funil", "2 · Por que ela existe"])
        + camada("FAZER", "O que o vendedor faz", ["3 · O que precisa chegar pronto", "4 · Passo a passo", "5 · Sinais de que vai bem ou mal", "6 · Objeções e respostas", "7 · O que entregar para a próxima etapa"])
        + camada("ACOMPANHAR", "O que o gestor acompanha", ["8 · Números para acompanhar", "9 · Alertas", "10 · Manual × prática × CRM", "11 · Rubrica de avaliação", "12 · Skills", "13 · Quem aprovou e quando"]), 20),
    "Bloco 5, 4 min. O modelo foi inspirado em boas práticas de produtos de RevOps: manchete que é a conclusão, poucos números no topo, lacunas declaradas, severidade nos alertas. A seção 10 é a assinatura do método: mostra por que o handbook diz o que diz. A seção 11, a rubrica, é o que transforma o handbook em coaching.")

# 21 · topo
screen("r-topo", "5", "Documentar", "Parte 0 · Em uma frase", "Comece o handbook pela conclusão",
    row(card(chip("TÍTULO QUE NÃO AJUDA", CRIT_BG, CRIT) + p("Handbook de Diagnóstico: visão geral do processo", 28, INK2), pad=24, gap=12, extra="flex:1")
        + card(chip("TÍTULO QUE AJUDA", POS_BG, POS) + p("Diagnóstico que termina com o custo do problema em reais leva 81% dos negócios para a proposta. Sem esse número, 28%.", 28, INK, 600), pad=24, gap=12, extra=f"flex:2;border-left:6px solid {BLUE}"), 20)
    + f'<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:16px">'
    + "".join(col(p(v, 48, BLUE, 300, "line-height:1") + p(l, 24, INK2), 8, f"background:{RAIL};padding:20px 22px")
              for v, l in [("54%", "passam do Diagnóstico para a Proposta"), ("81% × 28%", "avançam com e sem o custo calculado"), ("12 de 15", "perdas por preço vieram de quem pulou o Diagnóstico")])
    + '</div>'
    + p('<b>Falta informação:</b> o CRM não tem um campo para o custo do problema. Quem resolve: RevOps.', 26, INK2),
    "Bloco 5, 4 min. O título que não ajuda só diz o tema. O título que ajuda já diz o que fazer e por quê. Embaixo, no máximo quatro números, todos do CRM. E o que falta aparece logo no topo, com quem vai resolver. Pergunta para a turma: qual seria a frase de abertura do processo de vocês hoje?")

# 22 · passo
screen("r-passo", "5", "Documentar", "Parte 4 · Passo a passo", "Como escrever um passo do processo",
    card(row(chip("PASSO 4.3") + f'<h3 style="font-size:32px;font-weight:600">Calcular com o cliente quanto o problema custa</h3>', 16, "align-items:center")
         + row(col(p("O QUE FAZER", 24, INK2, 600)
                   + p("☐ Pedir os números ao decisor", 26) + p("☐ Fazer a conta junto com o cliente", 26)
                   + p("☐ Anotar o valor no CRM", 26), 8, "flex:1")
               + col(p("PERGUNTA QUE FUNCIONOU", 24, INK2, 600)
                     + p("“Qual é o custo mensal de manter um squad de oito pessoas, com encargos?”", 26, INK, 600)
                     + p("Reunião ganha com a TechScale, minuto 43:22", 24, BLUE), 8, "flex:1"), 32)
         + p("<b>Cuidado:</b> aceitar “custa, né” como resposta. Sem um número, só 28% dos negócios avançam.", 26, INK, 400, f"background:{RAIL};border-left:4px solid {BLUE};padding:14px 18px")
         + row(chip("Quem faz: o vendedor", RAIL, INK) + chip("Quando: na própria reunião", RAIL, INK)
               + chip("Pronto quando: o cliente confirmou o custo em R$", BLUE, "#FFFFFF"), 12, "flex-wrap:wrap"),
         pad=28, gap=20),
    "Bloco 5, 4 min. Os ingredientes de um passo: o que fazer, em frases que começam com verbo; uma pergunta que funcionou de verdade, com a reunião e o minuto; o cuidado, que vem das reuniões perdidas; quem faz e quando; e como saber que o passo terminou, com uma pergunta de sim ou não.")

# 22b · rubrica
screen("r-rubrica", "5", "Documentar", "Parte 11 · Rubrica da etapa", "Cada handbook vira uma rubrica de avaliação",
    card(table(["Critério (passo do handbook)", "Nota 3 quando", "Nota 0 quando"],
               [["1 · Abrir pelo impacto", "Hipótese sobre o negócio do cliente, sem deck", "Abre com “quem somos”"],
                ["2 · Medir a operação", "Tempo, volume e frequência com números do cliente", "Só stack, equipe e metodologia"],
                ["3 · Custo em reais", "Custo do problema em R$ confirmado pelo cliente", "Aceita “a gente dá um jeito”"],
                ["4 · Reenquadrar", "Cliente reformula o problema com o reframe", "Aceita a premissa “falta gente”"],
                ["5 · Fechar o próximo passo", "Data, decisor e critério de sucesso do cliente", "“A gente olha e retorna”"]],
               [28, 38, 34], 24, hl_col0=True), pad=16)
    + row(chip("Só avança com nota 3 nos critérios 3 e 5", BLUE, "#FFFFFF", 26) + p("Como a ficha de um jurado: nota de 0 a 3 por critério.", 26, INK2), 20, "align-items:center"),
    "Bloco 5, 4 min. Ponto central do método: o handbook não serve só para ler; ele vira régua. Cada passo do handbook vira um critério da rubrica, com a descrição de nota 3 (como os ganhos fazem) e de nota 0 (como os perdidos fazem); as notas 1 e 2 ficam descritas no handbook. O critério de avanço da rubrica é o mesmo critério de saída da etapa no CRM. Assim, o mesmo documento ensina, avalia e governa a passagem de etapa.")

# 23 · tags
def tag(t, ex, bg=BLUE_S, fg=BLUE):
    return row(f'<div style="width:330px;display:flex">{chip(t, bg, fg)}</div>' + p(ex, 26, INK, 400, "flex:1"), 20, f"align-items:center;padding:12px 0;border-bottom:1px solid {LINE}")
screen("r-tags", "5", "Documentar", "Fontes", "Mostre de onde vem cada informação",
    p("No handbook, cada frase leva uma etiqueta dizendo de onde veio.", 28, INK2)
    + card(tag("VI NA REUNIÃO", "“Para mim, o diagnóstico é a venda.” · melhor vendedor")
           + tag("ESTÁ NO DOCUMENTO", "Diagnóstico é opcional · manual de vendas")
           + tag("VEIO DO CRM", "54% passam do Diagnóstico · 122 negócios")
           + tag("É UMA SUSPEITA", "A mesma abordagem funciona em saúde · falta confirmar", RAIL, INK2)
           + tag("FALTA INFORMAÇÃO", "Propostas enviadas · o gestor comercial vai trazer", CRIT_BG, CRIT), pad=20, gap=0),
    "Bloco 5, 3 min. As etiquetas separam o que é fato do que é opinião. Quando alguém discordar de um passo, a etiqueta mostra de onde ele veio. No plugin, as etiquetas aparecem como OBSERVADO, DECLARADO, MEDIDO, HIPÓTESE e PRECISA DE DADO.")

# componente: lista de arquivos de skill
MONO = "font-family:'IBM Plex Mono', monospace"
def arquivo(nome, desc, direita):
    return row(f'<div style="width:52px;height:52px;background:{BLUE_S};display:flex;align-items:center;justify-content:center;border-radius:4px"><x-icon name="Book" style="color:{BLUE_L};width:28px;height:28px"></x-icon></div>'
               + col(p(nome, 26, INK, 600, MONO) + p(desc, 24, INK2), 2, "flex:1") + direita,
               20, f"align-items:center;padding:14px 24px;border-bottom:1px solid {LINE}")

# 24 · tipos de skill
screen("r-skills", "6", "Executar", "Passo 6 · Executar", "Os cinco tipos de skill que saem do handbook",
    card("".join(arquivo(n, d, p(f"“{q}”", 24, BLUE, 400, "width:430px;text-align:right")) for n, d, q in [
            ("acme-como-usar.md", "Mapa: qual skill usar para cada tarefa", "Por onde eu começo?"),
            ("acme-contexto.md", "Produto, cliente ideal, personas e provas", "Como falo com um CFO de varejo?"),
            ("acme-metodologia.md", "O que procurar e quando avançar de etapa", "Esse negócio pode avançar?"),
            ("acme-diagnostico.md", "O passo a passo de uma etapa (uma skill por etapa)", "Me prepara o diagnóstico de amanhã."),
            ("acme-coaching.md", "Avalia a reunião com a rubrica da etapa", "Como foi minha reunião de hoje?")]),
         pad=8, gap=0)
    + p("Comece com quatro: como usar, contexto, metodologia e a etapa que mais perde negócios.", 26, INK2),
    "Bloco 6, 4 min. Cada skill é um arquivo de texto que o Claude lê quando o assunto aparece. A coluna da direita é o que o vendedor diria para acionar cada uma. O que é estável (contexto, metodologia) fica separado do que é de cada etapa. A descrição de cada skill precisa usar as palavras do time: é ela que decide quando o Claude usa a skill.")

# 25 · antes durante depois
def fase(n, t, items):
    return card(chip(n) + f'<h3 style="font-size:32px;font-weight:600">{t}</h3>' + "".join(p(i, 26, INK2) for i in items), pad=26, gap=12, extra="flex:1")
screen("r-uso", "6", "Executar", "Na rotina do vendedor", "Como o vendedor usa as skills no dia a dia",
    row(fase("ANTES", "Preparar", ["Plano de uma página: objetivo e critério de saída", "Hipóteses por pessoa da reunião", "5 a 8 perguntas do handbook"])
        + fase("DURANTE", "Conduzir", ["Perguntas na ordem", "Sinais de avanço e de risco", "Respostas a objeções que funcionaram"])
        + fase("DEPOIS", "Registrar e treinar", ["Nota por critério da rubrica da etapa", "CRM atualizado, com confirmação", "Coaching com o momento e a próxima pergunta"]), 20)
    + p("A skill usa o mesmo critério do handbook e do CRM.", 28, INK, 600),
    "Bloco 6, 3 min. O ganho para o gestor: o registro no CRM passa a seguir o critério do handbook, e o forecast fica mais confiável. Toda escrita em sistema é mostrada antes e só grava com confirmação do vendedor.")

# 25b · coaching: scorecard
def dots(n):
    return row("".join(f'<div style="width:28px;height:28px;background:{BLUE if i < n else "#DDE2EE"}"></div>' for i in range(3)), 6, "align-items:center")
CRIT_ROWS = [("1 · Abrir pelo impacto", 2, 0, "[01:12] “A ACME tem doze anos de mercado…”"),
             ("2 · Medir a operação", 3, 0, "[11:40] “Quantos engenheiros vocês têm hoje?”"),
             ("3 · Custo em reais", 3, 0, "[14:08] cliente: “Mas a gente vai dar um jeito.”"),
             ("4 · Reenquadrar", 3, 0, "[14:20] “Quantas pessoas vocês imaginam precisar?”"),
             ("5 · Fechar o próximo passo", 3, 1, "[22:20] “A gente olha e retorna.”")]
screen("r-coaching", "7", "Melhoria contínua", "Passo 7 · Coaching com a rubrica", "Duas reuniões avaliadas com a mesma rubrica",
    card(f'<div style="display:grid;grid-template-columns:330px 170px 170px 1fr;gap:16px;align-items:center">'
         + p("Critério", 24, INK2, 600) + p("TechScale", 24, INK2, 600) + p("Orbita Pay", 24, INK2, 600) + p("Evidência na Orbita Pay", 24, INK2, 600)
         + "".join(p(c, 26) + dots(a) + dots(b) + p(ev, 24, INK2) for c, a, b, ev in CRIT_ROWS)
         + '</div>', pad=24)
    + row(card(p("<b>TechScale · ganho</b>", 26) + p("14 de 15 · avança para a proposta", 26, POS), pad=20, gap=4, extra="flex:1")
          + card(p("<b>Orbita Pay · perdido</b>", 26) + p("1 de 15 · não avança: custo do problema ausente", 26, CRIT), pad=20, gap=4, extra="flex:1"), 20),
    "Bloco 6, 4 min. A ideia que o Gio sempre repete: cada transcrição é processada contra a rubrica da etapa em que o negócio está. Mesma etapa (Diagnóstico), duas reuniões do exemplo fictício: a que ganhou tira 14 de 15; a que perdeu tira 1. A nota sai com a evidência e o minuto, então o vendedor vê exatamente onde a reunião se perdeu. E o veredito de avanço é o mesmo critério do CRM.")

# 25c · coaching: do momento à próxima pergunta
def momento(mm, crit, aconteceu, proxima, fonte):
    return card(row(col(chip(mm, RAIL, INK) + p(crit, 26, INK, 600), 8, "width:300px")
                    + col(p("O QUE ACONTECEU", 24, INK2, 600) + p(aconteceu, 26), 6, "flex:1")
                    + col(p("NA PRÓXIMA REUNIÃO", 24, BLUE, 600) + p(proxima, 26, INK, 600) + p(fonte, 24, INK2), 6, "flex:1"), 28),
                pad=22)
screen("r-coaching2", "7", "Melhoria contínua", "Passo 7 · Coaching · Orbita Pay", "O que o vendedor recebe depois da reunião",
    momento("01:12", "1 · Abrir pelo impacto", "Dez minutos de apresentação institucional, até a cliente pedir para parar.",
            "“Meu objetivo aqui é entender o impacto de negócio.”", "Handbook 4.1 · TechScale 01:00")
    + momento("14:08", "3 · Custo em reais", "Perguntou o impacto do atraso e aceitou “a gente vai dar um jeito”.",
              "“Qual era o valor daquele contrato?”", "Handbook 4.3 · TechScale 18:25")
    + momento("22:20", "5 · Próximo passo", "Descobriu que o CFO aprova, mas saiu sem data: “a gente olha e retorna”.",
              "Propor a data da proposta e convidar o CFO.", "Handbook 4.5 · TechScale 86:49"),
    "Bloco 6, 3 min. Coaching útil não é nota: é o momento exato, o que a rubrica pedia e a frase que funcionou em outra reunião. A pergunta da coluna da direita vem do próprio handbook, que por sua vez veio de uma reunião ganha. O vendedor aprende com o melhor vendedor da casa, não com um livro.")

# 25d · ciclo da rubrica
def nivel(t, d):
    return card(chip(t) + p(d, 26, INK), pad=26, gap=14, extra="flex:1")
screen("r-ciclo", "7", "Melhoria contínua", "Passo 7 · Coaching", "Quem usa o resultado da rubrica",
    row(nivel("VENDEDOR", "Recebe a nota de cada reunião, o momento que precisa melhorar e a pergunta para usar na próxima.")
        + nivel("GESTOR", "Vê a média de cada vendedor por critério e sabe o que treinar com cada um.")
        + nivel("DONO DO HANDBOOK", "Se ninguém cumpre um critério, ou se nota alta não vira venda, é hora de revisar o handbook."), 20)
    + row(f'<x-icon name="Verified" style="color:#FFFFFF;width:44px;height:44px"></x-icon>'
          + p("<b>Teste a rubrica antes de usar:</b> avalie reuniões ganhas e perdidas. As ganhas precisam tirar notas bem maiores; se não tirarem, ajuste os critérios.", 28, "#FFFFFF"),
          20, f"align-items:center;background:{BLUE};padding:26px 32px;border-radius:4px"),
    "Bloco 6, 3 min. O mesmo processamento serve a três pessoas. Para o vendedor, é coaching. Para o gestor, é o mapa de treinamento do time, sem precisar ouvir todas as gravações. Para o dono do handbook, é o sinal de revisão: se um critério ninguém cumpre, o passo talvez esteja errado; se a nota é alta e o negócio não converte, o critério não mede o que importa. Calibração: antes de soltar a rubrica, aplique em ganhos e perdidos; ela tem que separar os dois.")

# 26 · case
screen("r-case", "6", "Executar", "Case de cliente SCIENT · educação", "Um cliente real, 25 skills",
    card("".join(arquivo(n, d, chip(c, RAIL, INK2, 24, 400)) for n, d, c in [
            ("como-usar-as-skills.md", "Qual skill ler para cada tarefa, e em que ordem", "Início"),
            ("metodologia-comercial.md", "Perguntas e critérios de cada etapa do funil", "Método"),
            ("padroes-de-ganho.md", "O que os negócios ganhos têm em comum", "Método"),
            ("hubspot-funil-e-campos.md", "Funil e campos do CRM", "CRM"),
            ("meeting-prep.md", "Briefing antes de cada reunião", "Execução")]),
         pad=8, gap=0)
    + p("E mais 20: processo de vendas, cliente ideal, produto, briefing da manhã, atualização do CRM, avaliação de qualidade… Só a estrutura, sem dados do cliente.", 24, INK2),
    "Bloco 6, 4 min. Cliente de educação da SCIENT (o LIV). Confirme antes da aula se pode citar o nome; se não, fale só 'cliente de educação'. Mostre a lógica: uma skill de início que roteia; as de método nascem dos handbooks; as de CRM ensinam onde ler e gravar; as de execução entregam o trabalho no dia a dia.")

# 27 · validar
def verdict(t, bg, fg, cond, acao):
    return card(chip(t, bg, fg, 26) + p(cond, 28, INK, 600) + p(acao, 24, INK2), pad=26, gap=12, extra="flex:1")
screen("r-validar", "7", "Melhoria contínua", "Passo 7 · Melhoria contínua", "Como saber se o handbook está pronto",
    p("Teste simples: entregue o handbook a um vendedor que não participou do projeto e peça para ele preparar uma reunião.", 28, INK)
    + row(verdict("PRONTO", BLUE, "#FFFFFF", "Prepara a reunião sem precisar perguntar nada.", "Pode publicar e treinar o time.")
          + verdict("AJUSTAR", WARN_BG, WARN, "Entende, mas diz que precisa “adaptar ao seu estilo”.", "Algum passo está genérico. Volte às gravações e traga perguntas reais.")
          + verdict("REFAZER", CRIT_BG, CRIT, "Não consegue usar sem alguém explicar.", "O handbook ficou teórico. Refaça a partir das gravações."), 20),
    "Bloco 7, 4 min. É o teste que mais revela. Antes dele, um checklist binário: manchete é conclusão? critérios são sim ou não? toda pergunta tem fonte? toda red flag tem ação e dono?")

# 28 · manutenção
def ciclo(t, d):
    return card(f'<h3 style="font-size:30px;font-weight:600">{t}</h3>' + p(d, 24, INK2), pad=22, gap=8, extra="flex:1")
arrow = f'<x-shape kind="arrow-right" style="width:44px;height:24px;background:{BLUE_L}"></x-shape>'
screen("r-manter", "7", "Melhoria contínua", "Passo 7 · Melhoria contínua", "Como manter o handbook atualizado",
    row(ciclo("Medir", "As métricas da seção 8 e as notas da rubrica.") + arrow
        + ciclo("Revisar", "A cada 6 meses ou quando ICP, produto ou processo mudar.") + arrow
        + ciclo("Regenerar", "Nova coleta, mesma metodologia, mesmo modelo.") + arrow
        + ciclo("Anotar a versão", "1.0 na primeira, 1.1 num ajuste, 2.0 quando o processo muda."), 12, "align-items:center")
    + row(f'<x-icon name="Users" style="color:{BLUE};width:44px;height:44px"></x-icon>'
          + p("Todo handbook precisa de um responsável. Como as skills são feitas a partir dele, quando o handbook muda, as skills mudam junto.", 28, INK),
          20, f"align-items:center;background:{BLUE_S};padding:26px 30px;border-radius:4px"),
    "Bloco 7, 3 min. Fechando o ciclo do slide 3: o handbook morria porque não era medido nem mantido. Aqui ele tem métrica, dono e data. E como a skill nasce do handbook, atualizar um atualiza o outro.")

# 29 · começar amanhã
def passo(n, t, d):
    return card(row(p(n, 56, BLUE, 300, "line-height:1") + col(f'<h3 style="font-size:32px;font-weight:600">{t}</h3>' + p(d, 26, INK2), 6, "flex:1"), 24, "align-items:center"), pad=24)
screen("r-amanha", "0", "Visão geral", "Para esta semana", "Por onde começar",
    passo("1", "Mandar o pedido de dados", "As quatro fontes num pedido só, com responsável e prazo de 5 dias úteis.")
    + passo("2", "Escolher um processo", "Aquele em que o funil mais perde negócios. Faça só um, até o fim.")
    + passo("3", "Treinar com o exemplo", "Kit GTM Handbooks &amp; Skills em skills.scient.cc, com um exemplo completo para praticar."),
    "Fechamento, 3 min. O kit no skills.scient.cc conduz a jornada e já traz um exemplo completo com gabarito. Mas o primeiro passo não depende de ferramenta: é mandar o data request ainda esta semana.")

# 30 · regras (render próprio)
SLIDES.append(dict(id="r-regras", kind="regras"))
REGRAS = [("Não invente nada.", "Todo número vem do CRM, toda frase vem de uma reunião, toda regra vem de um documento."),
          ("Documente o que funciona na prática.", "Se o manual diz uma coisa e os melhores vendedores fazem outra, fique com a prática e registre a diferença."),
          ("Use as palavras do cliente.", "Perguntas, sinais e objeções saem das gravações, com a fonte."),
          ("Critério de sim ou não.", "Cada etapa termina com uma pergunta que só aceita sim ou não."),
          ("Faltou informação, pare.", "Anote o que falta, quem vai trazer e até quando."),
          ("Um handbook por processo.", "De 3 a 5 passos, com um responsável."),
          ("Teste antes de entregar.", "Avalie reuniões ganhas e perdidas com a rubrica e peça para alguém de fora usar o handbook.")]
def render_regras(idx, total):
    rows = "".join(row(p(f"{i+1}", 32, BLUE_L, 300, "width:48px") + p(f"<b>{a}</b> {b}", 30, "#FFFFFF", 300, "flex:1"), 16,
                       "align-items:baseline;padding:14px 0;border-bottom:1px solid #3F3F3F") for i, (a, b) in enumerate(REGRAS))
    return (f'<section id="r-regras" data-transition="fade" style="background:{DARK};color:#FFFFFF;{FONT};padding:96px 128px;display:flex;flex-direction:column;gap:28px">'
            f'<p style="font-size:24px;font-weight:600;letter-spacing:3px;color:{BLUE_L}">PARA LEVAR</p>'
            f'<h2 style="font-size:64px;font-weight:300;color:#FFFFFF">Sete regras de ouro</h2>'
            f'<div style="display:flex;flex-direction:column">{rows}</div>'
            f'<aside>{e(notas("r-regras", "Encerramento, 3 min. Leia as sete em voz alta. Abra para perguntas. Lembre: mandar o data request esta semana."))}</aside></section>')

# ─────────────────────────── ESCRITA ───────────────────────────
ORDER = ["r-cover", "r-promessa", "r-gaveta", "r-tese", "r-ia", "r-jornada", "r-fontes", "r-numeros", "r-conversas",
         "r-documentos", "r-pessoas", "r-basta", "r-lente", "r-criterio", "r-triangulacao", "r-hipotese", "r-funil",
         "r-padroes", "r-oque", "r-anatomia", "r-topo", "r-passo", "r-rubrica", "r-tags", "r-skills", "r-uso", "r-case",
         "r-validar", "r-coaching", "r-coaching2", "r-ciclo", "r-manter", "r-amanha", "r-regras"]

def main():
    SLIDES.sort(key=lambda x: ORDER.index(x["id"]))
    os.makedirs(SL, exist_ok=True)
    total = sum(1 for x in SLIDES if visivel(x["id"]))
    vis = 0
    for s in SLIDES:
        if visivel(s["id"]):
            vis += 1
            i = vis
        else:
            i = "extra"
        if s["kind"] == "cover":
            h = render_cover(i, total)
        elif s["kind"] == "regras":
            h = render_regras(i, total)
        else:
            h = render_screen(s, i, total)
        open(os.path.join(SL, f'{s["id"]}.html'), "w", encoding="utf-8").write(h + "\n")
    order = [s["id"] for s in SLIDES]
    deck = json.load(open(os.path.join(ROOT, "deck.json"), encoding="utf-8"))
    deck["order"] = order
    deck["sections"] = {
        "s0": {"description": "Abertura: o que a turma leva e o caminho", "start": "r-cover"},
        "s1": {"description": "Por quê: handbooks morrem na gaveta; a tese declarado, observado e medido", "start": "r-gaveta"},
        "s2": {"description": "Coletar: as quatro fontes de evidência e quanto basta", "start": "r-fontes"},
        "s3": {"description": "Metodologia: o que procurar em cada reunião e quando avançar", "start": "r-lente"},
        "s4": {"description": "Analisar: cruzar as três visões revela o processo real", "start": "r-triangulacao"},
        "s5": {"description": "Documentar: o que entra no handbook e como", "start": "r-oque"},
        "s6": {"description": "Executar: o handbook vira skills que o time usa", "start": "r-skills"},
        "s7": {"description": "Melhoria contínua: testar o handbook, fazer coaching de cada reunião com a rubrica e revisar", "start": "r-validar"},
        "s8": {"description": "Fechamento: por onde começar e regras de ouro", "start": "r-amanha"},
    }
    deck["cover"] = "r-cover"
    if COMPLETO:
        deck["title"] = "Building GTM Handbooks & Skills (versão completa)"
    deck.setdefault("faces", {})["ibm-plex-mono"] = {"family": "IBM Plex Mono", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap"}
    json.dump(deck, open(os.path.join(ROOT, "deck.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(total, "slides")
    print(json.dumps(order))

if __name__ == "__main__":
    main()
