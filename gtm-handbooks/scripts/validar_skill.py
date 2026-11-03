#!/usr/bin/env python3
"""
validar_skill.py — confere as regras de formato de uma skill (ou de uma pasta com várias).

Regras (do guia de skills da Anthropic + método do kit):
  ERRO  SKILL.md existe e começa com frontmatter YAML (--- ... ---)
  ERRO  name em kebab-case (a-z, 0-9, hífen), igual ao nome da pasta, sem "claude"/"anthropic"
  ERRO  description presente, até 1024 caracteres, sem < ou >
  AVISO description sem indicação de quando usar ("Use quando/ao/para/sempre")
  AVISO SKILL.md com mais de 500 linhas (mover detalhe para references/)
  AVISO arquivos citados em references/ ou scripts/ que não existem
  AVISO README.md dentro da pasta da skill (a documentação fica no SKILL.md)

Uso: python3 validar_skill.py <pasta-da-skill | pasta-com-skills>
Saída: lista de problemas; código 1 se houver ERRO.
"""
import os
import re
import sys

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    data, key = {}, None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            data[key] = val.strip("\"'") if val not in (">", "|", ">-", "|-") else ""
        elif key and line.startswith((" ", "\t")):
            data[key] = (data[key] + " " + line.strip()).strip()
    return data


def check(folder):
    probs = []
    name = os.path.basename(os.path.normpath(folder))
    path = os.path.join(folder, "SKILL.md")
    if not os.path.isfile(path):
        return [("ERRO", f"{name}: SKILL.md não encontrado")]
    text = open(path, encoding="utf-8").read()
    fm = parse_frontmatter(text)
    if fm is None:
        return [("ERRO", f"{name}: frontmatter YAML ausente ou malformado (precisa começar com --- e fechar com ---)")]
    n = fm.get("name", "")
    if not n:
        probs.append(("ERRO", f"{name}: campo name ausente"))
    else:
        if not KEBAB.match(n):
            probs.append(("ERRO", f"{name}: name '{n}' não está em kebab-case"))
        if n != name:
            probs.append(("ERRO", f"{name}: name '{n}' diferente do nome da pasta"))
        if "claude" in n or "anthropic" in n:
            probs.append(("ERRO", f"{name}: name não pode conter 'claude' ou 'anthropic'"))
    d = fm.get("description", "")
    if not d:
        probs.append(("ERRO", f"{name}: campo description ausente"))
    else:
        if len(d) > 1024:
            probs.append(("ERRO", f"{name}: description com {len(d)} caracteres (máximo 1024)"))
        if "<" in d or ">" in d:
            probs.append(("ERRO", f"{name}: description contém < ou >"))
        if not re.search(r"\b(use|usar|acione|leia sempre)\b", d, re.I):
            probs.append(("AVISO", f"{name}: description não diz quando usar (ex.: 'Use quando ...')"))
    lines = text.count("\n") + 1
    if lines > 500:
        probs.append(("AVISO", f"{name}: SKILL.md com {lines} linhas; mova detalhe para references/"))
    for ref in set(re.findall(r"(?<![\w{}/$])((?:references|scripts|assets)/[\w./-]+)", text)):
        ref = ref.rstrip(".,)`")
        if not os.path.exists(os.path.join(folder, ref)):
            probs.append(("AVISO", f"{name}: cita {ref}, que não existe na pasta"))
    if os.path.exists(os.path.join(folder, "README.md")):
        probs.append(("AVISO", f"{name}: README.md dentro da skill; prefira tudo no SKILL.md"))
    return probs


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = sys.argv[1]
    folders = [root] if os.path.isfile(os.path.join(root, "SKILL.md")) else [
        os.path.join(root, f) for f in sorted(os.listdir(root))
        if os.path.isfile(os.path.join(root, f, "SKILL.md"))]
    if not folders:
        sys.exit(f"Nenhuma skill encontrada em {root}")
    allp = []
    for f in folders:
        p = check(f)
        allp += p
        print(f"{'✅' if not p else ('❌' if any(x[0] == 'ERRO' for x in p) else '⚠ ')} {os.path.basename(os.path.normpath(f))}")
        for lvl, msg in p:
            print(f"   {lvl}: {msg}")
    erros = sum(1 for x in allp if x[0] == "ERRO")
    print(f"\n{len(folders)} skill(s) · {erros} erro(s) · {len(allp) - erros} aviso(s)")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
