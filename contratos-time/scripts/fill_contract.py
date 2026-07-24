#!/usr/bin/env python3
"""
fill_contract.py — Preenche placeholders e resolve clausulas condicionais em um
.docx, preservando a formatacao original (fonte, negrito, tabelas, cabecalho).

Sem dependencias externas: um .docx e um zip de XML, manipulado com a stdlib.

SINTAXE NO TEMPLATE
-------------------
1) Campo simples:            {{NOME}}, {{CPF}}, {{DATA}}, {{PLANO_OPERADORA}}
2) Clausula condicional:     {{#PLANO_SAUDE}} ... texto ... {{/PLANO_SAUDE}}
   - Se a chave PLANO_SAUDE for verdadeira nos dados -> o bloco fica (marcadores
     somem) e os campos internos sao preenchidos.
   - Se for falsa/ausente -> o bloco inteiro e removido do contrato.
   - Marcadores podem estar na propria linha (recomendado, para blocos de varios
     paragrafos) ou embutidos numa frase (secao "inline").
   Verdadeiro = true/sim/1/yes/on (qualquer outra coisa nao-vazia tambem conta);
   Falso = false/nao/0/no/off/vazio/ausente.

USO
---
  python3 fill_contract.py --list --template modelo.docx
  python3 fill_contract.py --template modelo.docx --out saida.docx \
      --data '{"NOME":"Maria","CPF":"111.444.777-35","DATA":"24/07/2026",
               "PLANO_SAUDE":true,"PLANO_OPERADORA":"Bradesco Saude"}'
  # --data aceita @arquivo.json

Saida (stdout): JSON com placeholders, replaced, unfilled, sections, extra_keys.
Codigo de saida: 3 se sobraram placeholders sem valor (salvo --allow-unfilled).
"""
import argparse
import copy
import json
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
T_TAG = f"{{{W_NS}}}t"
P_TAG = f"{{{W_NS}}}p"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

# Campo: qualquer conteudo entre {{ }} que NAO comece com # / ou * (marcadores).
# Aceita espacos e acentos na chave, ex.: {{Nome Completo da Pessoas}}.
FIELD_RE = re.compile(r"\{\{\s*([^{}#/*][^{}]*?)\s*\}\}")
SEC_OPEN_RE = re.compile(r"\{\{\s*#\s*([A-Za-z0-9_.\-]+)\s*\}\}")
SEC_CLOSE_RE = re.compile(r"\{\{\s*/\s*([A-Za-z0-9_.\-]+)\s*\}\}")
# Lista repetivel: {{*CHAVE}} num paragrafo -> o paragrafo e repetido uma vez por
# item da lista em data[CHAVE], preservando o estilo (bullet/numeracao) do Word.
REPEAT_RE = re.compile(r"\{\{\s*\*\s*([^{}]+?)\s*\}\}")

FALSY = {"", "false", "0", "nao", "não", "no", "n", "off", "none", "null"}


def truthy(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() not in FALSY


def _is_text_part(name):
    return bool(re.match(r"word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$", name))


def _t_nodes(p):
    return p.findall(f".//{T_TAG}")


def _p_text(p):
    return "".join((n.text or "") for n in _t_nodes(p))


def _redistribute(texts, a, b, repl):
    """Substitui o intervalo global [a,b) por `repl` na lista de textos dos runs,
    inserindo em [a] e removendo o miolo. Preserva a formatacao de cada run."""
    new, pos, inserted = [], 0, False
    for t in texts:
        s, e = pos, pos + len(t)
        left = t[: max(0, min(len(t), a - s))]
        right = t[max(0, min(len(t), b - s)):]
        seg = left + right
        if not inserted and s <= a <= e:
            seg = left + repl + right
            inserted = True
        new.append(seg)
        pos = e
    if not inserted and new:
        new[0] = repl + new[0]
    return new


def _write_back(nodes, new_texts):
    for n, nt in zip(nodes, new_texts):
        n.text = nt
        if nt != nt.strip() or "  " in nt:
            n.set(XML_SPACE, "preserve")


def _edit_paragraph(p, finder):
    """Aplica repetidamente `finder(full_text) -> (a, b, repl) | None` no paragrafo."""
    guard = 0
    while True:
        guard += 1
        if guard > 2000:
            break
        nodes = _t_nodes(p)
        texts = [n.text or "" for n in nodes]
        full = "".join(texts)
        hit = finder(full)
        if hit is None:
            return
        a, b, repl = hit
        _write_back(nodes, _redistribute(texts, a, b, repl))


# ── 1. Secoes condicionais que abrem e fecham no MESMO paragrafo (inline) ──────
def _resolve_inline_sections(p, mapping, stats):
    def finder(full):
        mo = SEC_OPEN_RE.search(full)
        if not mo:
            return None
        key = mo.group(1)
        mc = SEC_CLOSE_RE.search(full, mo.end())
        if not mc or mc.group(1) != key:
            return None  # abre aqui mas fecha noutro paragrafo -> secao de bloco
        keep = truthy(mapping.get(key))
        stats["sections"][key] = "mantida" if keep else "removida"
        inner = full[mo.end():mc.start()]
        return (mo.start(), mc.end(), inner if keep else "")
    _edit_paragraph(p, finder)


# ── 2. Secoes condicionais que abrangem VARIOS paragrafos (bloco) ─────────────
def _strip_marker(p, pattern, key):
    def finder(full):
        for m in pattern.finditer(full):
            if m.group(1) == key:
                return (m.start(), m.end(), "")
        return None
    _edit_paragraph(p, finder)


def _resolve_block_sections(root, mapping, stats):
    changed = True
    while changed:
        changed = False
        parent = {c: par for par in root.iter() for c in par}
        paras = list(root.iter(P_TAG))
        for i, p in enumerate(paras):
            full = _p_text(p)
            mo = SEC_OPEN_RE.search(full)
            if not mo:
                continue
            key = mo.group(1)
            mc_same = SEC_CLOSE_RE.search(full, mo.end())
            if mc_same and mc_same.group(1) == key:
                continue  # inline -> tratado noutra etapa
            # acha o paragrafo de fechamento
            j = None
            for k in range(i + 1, len(paras)):
                mc = SEC_CLOSE_RE.search(_p_text(paras[k]))
                if mc and mc.group(1) == key:
                    j = k
                    break
            if j is None:
                stats["warnings"].append(f"secao '{key}' sem fechamento {{{{/{key}}}}}")
                continue
            keep = truthy(mapping.get(key))
            stats["sections"][key] = "mantida" if keep else "removida"
            block = paras[i:j + 1]
            if keep:
                for pp in block:
                    txt = _p_text(pp)
                    only_marker = (SEC_OPEN_RE.sub("", SEC_CLOSE_RE.sub("", txt)).strip() == "")
                    if only_marker:
                        par = parent.get(pp)
                        if par is not None:
                            par.remove(pp)  # linha que so tinha o marcador
                    else:
                        _strip_marker(pp, SEC_OPEN_RE, key)
                        _strip_marker(pp, SEC_CLOSE_RE, key)
            else:
                for pp in block:
                    par = parent.get(pp)
                    if par is not None:
                        par.remove(pp)
            changed = True
            break


# ── 2b. Listas repetiveis {{*CHAVE}} (um paragrafo por item) ──────────────────
def _resolve_repeats(root, mapping, stats):
    changed = True
    while changed:
        changed = False
        parent = {c: par for par in root.iter() for c in par}
        for p in list(root.iter(P_TAG)):
            m = REPEAT_RE.search(_p_text(p))
            if not m:
                continue
            key = m.group(1).strip()
            par = parent.get(p)
            if par is None:
                continue
            items = mapping.get(key, [])
            if isinstance(items, str):
                items = [items]
            if not isinstance(items, list):
                items = [str(items)]
            idx = list(par).index(p)

            def make_finder(value):
                def finder(full):
                    mm = REPEAT_RE.search(full)
                    if mm and mm.group(1).strip() == key:
                        return (mm.start(), mm.end(), str(value))
                    return None
                return finder

            clones = []
            for value in items:
                clone = copy.deepcopy(p)
                _edit_paragraph(clone, make_finder(value))
                clones.append(clone)
            for off, el in enumerate(clones):
                par.insert(idx + off, el)
            par.remove(p)
            stats["repeats"][key] = len(items)
            changed = True
            break


# ── 3. Campos simples {{CAMPO}} ───────────────────────────────────────────────
def _resolve_fields(p, mapping, stats):
    def finder(full):
        for m in FIELD_RE.finditer(full):
            key = m.group(1)
            stats["placeholders"].add(key)
            if key in mapping:
                return (m.start(), m.end(), str(mapping[key]))
        return None
    _edit_paragraph(p, finder)
    for m in FIELD_RE.finditer(_p_text(p)):
        stats["unfilled"].add(m.group(1))


_NS_DECL_RE = re.compile(r'xmlns:([\w.\-]+)\s*=\s*"([^"]+)"')
_XML_DECL = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'


def _register_all_ns(xml_bytes):
    """Registra TODOS os prefixos de namespace declarados no XML para que a
    serializacao preserve os prefixos originais (w, w14, mc, wp, r, ...). Sem
    isso, o ElementTree renomeia prefixos e quebra `mc:Ignorable` -> o Word
    acusa 'conteudo ilegivel'."""
    head = xml_bytes.decode("utf-8", "replace")[:20000]
    for pfx, uri in set(_NS_DECL_RE.findall(head)):
        try:
            ET.register_namespace(pfx, uri)
        except (ValueError, TypeError):
            pass


def _root_tag_span(text):
    """(inicio, fim) do tag de abertura do elemento raiz, pulando <?xml?>/<!-- -->."""
    i, n = 0, len(text)
    while i < n:
        lt = text.find("<", i)
        if lt < 0:
            return None
        if text.startswith("<?", lt) or text.startswith("<!--", lt):
            gt = text.find(">", lt)
            if gt < 0:
                return None
            i = gt + 1
            continue
        gt = text.find(">", lt)
        return (lt, gt) if gt >= 0 else None
    return None


def _reinject_root_ns(orig_bytes, out_text):
    """Reinjeta no root do XML de saida as declaracoes xmlns que o ElementTree
    tenha descartado (as que so aparecem em `mc:Ignorable`), preservando a
    validade que o Word exige."""
    orig = orig_bytes.decode("utf-8", "replace")
    so, to = _root_tag_span(orig), _root_tag_span(out_text)
    if not so or not to:
        return out_text
    orig_tag = orig[so[0]:so[1] + 1]
    out_tag = out_text[to[0]:to[1] + 1]
    decls = re.findall(r'xmlns(?::[\w.\-]+)?\s*=\s*"[^"]*"', orig_tag)
    missing = [d for d in decls if d not in out_tag]
    if not missing:
        return out_text
    m = re.match(r"<[\w:.\-]+", out_tag)
    at = to[0] + m.end()
    return out_text[:at] + " " + " ".join(missing) + out_text[at:]


def _serialize(root, orig_bytes):
    out = ET.tostring(root, encoding="unicode")
    return (_XML_DECL + _reinject_root_ns(orig_bytes, out)).encode("utf-8")


def _process_xml(xml_bytes, mapping, stats):
    _register_all_ns(xml_bytes)
    root = ET.fromstring(xml_bytes)
    _resolve_block_sections(root, mapping, stats)
    _resolve_repeats(root, mapping, stats)
    for p in root.iter(P_TAG):
        _resolve_inline_sections(p, mapping, stats)
    for p in root.iter(P_TAG):
        _resolve_fields(p, mapping, stats)
    return _serialize(root, xml_bytes)


def _new_stats():
    return {"placeholders": set(), "replaced": {}, "unfilled": set(),
            "sections": {}, "repeats": {}, "warnings": []}


def run(template, out, mapping, allow_unfilled):
    stats = _new_stats()
    with zipfile.ZipFile(template, "r") as zin:
        items = zin.infolist()
        payload = {}
        for it in items:
            data = zin.read(it.filename)
            if _is_text_part(it.filename):
                data = _process_xml(data, mapping, stats)
            payload[it.filename] = data
    if out:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for it in items:
                zout.writestr(it, payload[it.filename])
    known = stats["placeholders"] | set(stats["sections"]) | set(stats["repeats"])
    report = {
        "placeholders": sorted(stats["placeholders"]),
        "sections": stats["sections"],
        "repeats": stats["repeats"],
        "unfilled": sorted(stats["unfilled"]),
        "extra_keys": sorted(set(mapping) - known),
        "warnings": stats["warnings"],
        "output": out,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if stats["unfilled"] and not allow_unfilled:
        return 3
    return 0


def list_placeholders(template):
    fields, sections, repeats = set(), set(), set()
    with zipfile.ZipFile(template, "r") as zin:
        for it in zin.infolist():
            if not _is_text_part(it.filename):
                continue
            root = ET.fromstring(zin.read(it.filename))
            for p in root.iter(P_TAG):
                full = _p_text(p)
                for m in SEC_OPEN_RE.finditer(full):
                    sections.add(m.group(1))
                for m in REPEAT_RE.finditer(full):
                    repeats.add(m.group(1).strip())
                # campos que NAO sao marcadores de secao/lista
                for m in FIELD_RE.finditer(full):
                    fields.add(m.group(1))
    print(json.dumps({"fields": sorted(fields), "sections": sorted(sections),
                      "repeats": sorted(repeats)}, ensure_ascii=False, indent=2))
    return 0


def load_data(arg):
    if arg is None:
        return {}
    if arg.startswith("@"):
        with open(arg[1:], "r", encoding="utf-8") as f:
            return json.load(f)
    return json.loads(arg)


def main():
    ap = argparse.ArgumentParser(description="Preenche {{CAMPO}} e resolve {{#SECAO}} em .docx.")
    ap.add_argument("--template", required=True)
    ap.add_argument("--out")
    ap.add_argument("--data", help='JSON ou @arquivo.json')
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--allow-unfilled", action="store_true")
    args = ap.parse_args()
    if args.list:
        return list_placeholders(args.template)
    if not args.out:
        ap.error("--out e obrigatorio quando nao se usa --list")
    return run(args.template, args.out, load_data(args.data), args.allow_unfilled)


if __name__ == "__main__":
    sys.exit(main())
