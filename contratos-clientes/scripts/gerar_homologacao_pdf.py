#!/usr/bin/env python3
"""
Gera o PDF "Dados para Homologação" da SCIENT (artefato usado 1x, depois é só
reenviar o link). Layout fiel ao design system da SCIENT: logo, título, seções
com marcador quadrado azul + linha, tabela de dados, lista de documentos,
callout do CRF e rodapé.

Uso:
    python3 gerar_homologacao_pdf.py [saida.pdf] [--data DD/MM/AAAA]

Lê os dados de ../config.json (bloco homologacao) e a logo de ../assets/scient_logo.png.
Depende de: reportlab, pillow  (pip install reportlab pillow)
"""
import io
import json
import os
import sys

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable,
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ---- Paleta e medidas (px do HTML -> pt, fator 0.75 = 72/96) --------------
PX = 0.75
AZUL = HexColor("#0030E8")
CINZA = HexColor("#585858")
LINHA = HexColor("#E6E6E6")
PRETO = HexColor("#111111")
CALLOUT_BG = HexColor("#A0B0E8")

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "..", "config.json")
LOGO = os.path.join(HERE, "..", "assets", "scient_logo.png")


class SectionHeader(Flowable):
    """Marcador quadrado azul + título em negrito + linha fina, centralizados
    na vertical (igual ao .sec do HTML)."""

    def __init__(self, texto, largura, sq=9 * PX, altura=14 * PX,
                 gap=10 * PX, fonte="Helvetica-Bold", tam=14 * PX):
        super().__init__()
        self.texto = texto
        self.largura = largura
        self.sq = sq
        self.gap = gap
        self.fonte = fonte
        self.tam = tam
        self.height = max(altura, sq, tam)
        self.width = largura

    def draw(self):
        c = self.canv
        cy = self.height / 2.0
        # quadrado azul
        c.setFillColor(AZUL)
        c.rect(0, cy - self.sq / 2.0, self.sq, self.sq, stroke=0, fill=1)
        # texto
        x_txt = self.sq + self.gap
        c.setFillColor(PRETO)
        c.setFont(self.fonte, self.tam)
        c.drawString(x_txt, cy - self.tam * 0.34, self.texto)
        tw = c.stringWidth(self.texto, self.fonte, self.tam)
        # linha fina ate a margem direita
        x_line = x_txt + tw + self.gap
        if x_line < self.largura:
            c.setStrokeColor(LINHA)
            c.setLineWidth(1 * PX)
            c.line(x_line, cy, self.largura, cy)


def _logo_flowable(max_h=34 * PX):
    """Logo achatada em fundo branco, redimensionada por altura."""
    from PIL import Image as PILImage

    im = PILImage.open(LOGO).convert("RGBA")
    fundo = PILImage.new("RGBA", im.size, (255, 255, 255, 255))
    fundo.alpha_composite(im)
    fundo = fundo.convert("RGB")
    # downscale para manter o PDF leve (a logo aparece a ~25pt no PDF;
    # 72px de altura ja e nitido e mantem o arquivo pequeno o bastante
    # para subir pelo conector via base64)
    ratio = im.width / float(im.height)
    alvo_h = 72
    fundo = fundo.resize((int(alvo_h * ratio), alvo_h), PILImage.LANCZOS)
    buf = io.BytesIO()
    fundo.save(buf, format="PNG", optimize=True)
    buf.seek(0)
    return Image(buf, width=max_h * ratio, height=max_h)


def gerar(saida, data_str):
    with open(CONFIG, encoding="utf-8") as f:
        cfg = json.load(f)
    d = cfg["homologacao"]["dados_para_homologacao"]

    ML = MR = 20 * mm
    MT = MB = 22 * mm
    doc = SimpleDocTemplate(
        saida, pagesize=A4,
        leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
        title="Dados para Homologação - SCIENT",
        author="SCIENT",
    )
    W = A4[0] - ML - MR

    st_h1 = ParagraphStyle("h1", fontName="Helvetica", fontSize=26 * PX,
                           leading=30 * PX, textColor=PRETO, spaceAfter=6 * PX)
    st_sub = ParagraphStyle("sub", fontName="Helvetica", fontSize=12 * PX,
                            leading=15 * PX, textColor=CINZA)
    st_k = ParagraphStyle("k", fontName="Helvetica", fontSize=12.5 * PX,
                          leading=15 * PX, textColor=CINZA)
    st_v = ParagraphStyle("v", fontName="Helvetica-Bold", fontSize=12.5 * PX,
                          leading=15 * PX, textColor=PRETO)
    st_li = ParagraphStyle("li", fontName="Helvetica", fontSize=12.5 * PX,
                           leading=16 * PX, textColor=PRETO, spaceAfter=5 * PX,
                           leftIndent=16 * PX, bulletIndent=2 * PX,
                           bulletFontName="Helvetica", bulletFontSize=12.5 * PX)
    st_call = ParagraphStyle("call", fontName="Helvetica", fontSize=12 * PX,
                             leading=16 * PX, textColor=PRETO)

    el = []
    el.append(_logo_flowable())
    el.append(Spacer(1, 30 * PX))
    el.append(Paragraph("Dados para Homologação", st_h1))
    el.append(Paragraph(
        "Informações cadastrais da SCIENT para homologação como fornecedor", st_sub))

    # ---- Dados cadastrais ----
    el.append(Spacer(1, 26 * PX))
    el.append(SectionHeader("Dados cadastrais", W))
    el.append(Spacer(1, 12 * PX))

    linhas = [
        ("Razão social", d["razao_social"]),
        ("CNPJ", d["cnpj"]),
        ("Endereço", d["endereco"]),
        ("E-mail de faturamento", d["email_faturamento"]),
        ("Financeiro", "%s · %s" % (d["financeiro_nome"], d["financeiro_email"])),
        ("Representante legal", d["representante_legal_nome"]),
        ("CPF do representante", d["representante_legal_cpf"]),
    ]
    kw = W * 0.38
    tdata = [[Paragraph(k, st_k), Paragraph(v, st_v)] for k, v in linhas]
    tbl = Table(tdata, colWidths=[kw, W - kw])
    tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 9 * PX),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9 * PX),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW", (0, 0), (-1, -1), 1 * PX, LINHA),
    ]))
    el.append(tbl)

    # ---- Documentos disponíveis ----
    el.append(Spacer(1, 26 * PX))
    el.append(SectionHeader("Documentos disponíveis", W))
    el.append(Spacer(1, 8 * PX))
    docs = [
        "Contrato social",
        "Cartão CNPJ",
        "Certidão negativa Federal",
        "Certificado de Regularidade do FGTS (CRF)",
    ]
    for x in docs:
        el.append(Paragraph(x, st_li, bulletText="•"))

    # ---- Callout CRF ----
    el.append(Spacer(1, 16 * PX))
    call = Paragraph(
        "<b>Sobre o CRF (FGTS):</b> o Certificado de Regularidade do FGTS tem "
        "validade de 1 mês a partir da emissão. Caso seja solicitado, será "
        "emitida uma nova guia atualizada.", st_call)
    ct = Table([[call]], colWidths=[W])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CALLOUT_BG),
        ("TOPPADDING", (0, 0), (-1, -1), 14 * PX),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14 * PX),
        ("LEFTPADDING", (0, 0), (-1, -1), 16 * PX),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16 * PX),
    ]))
    el.append(ct)

    def rodape(canvas, _doc):
        canvas.saveState()
        y = MB - 8 * PX
        canvas.setStrokeColor(LINHA)
        canvas.setLineWidth(1 * PX)
        canvas.line(ML, y + 10 * PX, A4[0] - MR, y + 10 * PX)
        canvas.setFont("Helvetica", 9 * PX)
        canvas.setFillColor(CINZA)
        canvas.drawString(ML, y, "Scientific AI Native GTM")
        canvas.setFont("Helvetica-Bold", 9 * PX)
        canvas.setFillColor(AZUL)
        txt = "SCIENT · %s" % data_str
        canvas.drawRightString(A4[0] - MR, y, txt)
        canvas.restoreState()

    doc.build(el, onFirstPage=rodape, onLaterPages=rodape)
    return saida


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    data_str = "26/07/2026"
    if "--data" in args:
        i = args.index("--data")
        data_str = args[i + 1]
        del args[i:i + 2]
    out = args[0] if args else "Dados para Homologacao - SCIENT.pdf"
    gerar(out, data_str)
    print("PDF gerado:", out, "(%d bytes)" % os.path.getsize(out))
