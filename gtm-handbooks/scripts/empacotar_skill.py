#!/usr/bin/env python3
"""
empacotar_skill.py — gera <nome>.skill (zip com a pasta da skill) pronto para enviar ao Claude.

Uso: python3 empacotar_skill.py <pasta-da-skill> [--saida <pasta>]
Valida antes com validar_skill.py; não empacota se houver ERRO.
"""
import argparse
import os
import subprocess
import sys
import zipfile

IGNORAR = {".DS_Store", "__pycache__", ".git", "testes.md"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--saida", default=None)
    a = ap.parse_args()
    pasta = os.path.normpath(a.pasta)
    nome = os.path.basename(pasta)
    validar = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validar_skill.py")
    r = subprocess.run([sys.executable, validar, pasta])
    if r.returncode != 0:
        sys.exit("Corrija os erros antes de empacotar.")
    destino = os.path.join(a.saida or os.path.dirname(pasta) or ".", f"{nome}.skill")
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, dirs, arqs in os.walk(pasta):
            dirs[:] = [d for d in dirs if d not in IGNORAR]
            for f in arqs:
                if f in IGNORAR:
                    continue
                full = os.path.join(raiz, f)
                z.write(full, os.path.join(nome, os.path.relpath(full, pasta)))
    print(f"Empacotado: {destino}")


if __name__ == "__main__":
    main()
