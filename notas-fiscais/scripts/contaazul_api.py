#!/usr/bin/env python3
"""
Cliente da API v2 da Conta Azul (https://api-v2.contaazul.com) para o fluxo de NF
da certificacao GTM Engineer.

IMPORTANTE: a API da Conta Azul NAO emite nota fiscal (so consulta). Este script
automatiza tudo ATE criar a venda aprovada; o clique "Emitir Nota" e feito no painel.
Depois da emissao, use `find-nfse` para conferir/baixar a NFS-e.

Auth: usa contaazul_auth.get_access_token() (refresh_token via env). Ver contaazul_auth.py.

Subcomandos (todos imprimem JSON no stdout):
  whoami
  find-servico "<texto>"
  find-pessoa [--documento CPF/CNPJ] [--email EMAIL] [--busca TEXTO] [--tipo Física|Jurídica]
  create-pessoa --json <arquivo|->        # corpo conforme POST /v1/pessoas
  proximo-numero
  create-venda --json <arquivo|->         # corpo conforme POST /v1/venda
  find-nfse --numero-venda N | --id-cliente UUID [--de YYYY-MM-DD --ate YYYY-MM-DD]

Nada aqui cria/emite sem o operador montar o payload e chamar explicitamente.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contaazul_auth import get_access_token  # noqa: E402

API_BASE = os.environ.get("CONTAAZUL_API_BASE", "https://api-v2.contaazul.com")


def _req(method, path, params=None, body=None):
    url = API_BASE + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + get_access_token())
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw.strip() else {"status": resp.status}
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise SystemExit(f"ERRO HTTP {e.code} em {method} {path}: {detail}")


def cmd_whoami(_a):
    return _req("GET", "/v1/pessoas/conta-conectada")


def cmd_find_servico(a):
    return _req("GET", "/v1/servicos", params={
        "pagina": 1, "tamanho_pagina": 20, "busca_textual": a.texto,
    })


def cmd_find_pessoa(a):
    return _req("GET", "/v1/pessoas", params={
        "pagina": 1, "tamanho_pagina": 20,
        "documentos": a.documento, "emails": a.email, "busca": a.busca,
        "tipos_pessoa": a.tipo, "tipo_perfil": "Cliente", "com_endereco": "true",
    })


def cmd_create_pessoa(a):
    return _req("POST", "/v1/pessoas", body=_read_json(a.json))


def cmd_proximo_numero(_a):
    return _req("GET", "/v1/venda/proximo-numero")


def cmd_create_venda(a):
    return _req("POST", "/v1/venda", body=_read_json(a.json))


def cmd_find_nfse(a):
    return _req("GET", "/v1/notas-fiscais-servico", params={
        "pagina": 1, "tamanho_pagina": 50,
        "data_competencia_de": a.de, "data_competencia_ate": a.ate,
        "numero_venda": a.numero_venda, "id_cliente": a.id_cliente,
    })


def _read_json(src):
    if src == "-":
        return json.load(sys.stdin)
    with open(src, encoding="utf-8") as f:
        return json.load(f)


def main():
    p = argparse.ArgumentParser(description="Conta Azul API v2 (NF GTME)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("whoami").set_defaults(func=cmd_whoami)

    s = sub.add_parser("find-servico"); s.add_argument("texto"); s.set_defaults(func=cmd_find_servico)

    s = sub.add_parser("find-pessoa")
    s.add_argument("--documento"); s.add_argument("--email")
    s.add_argument("--busca"); s.add_argument("--tipo")
    s.set_defaults(func=cmd_find_pessoa)

    s = sub.add_parser("create-pessoa"); s.add_argument("--json", required=True)
    s.set_defaults(func=cmd_create_pessoa)

    sub.add_parser("proximo-numero").set_defaults(func=cmd_proximo_numero)

    s = sub.add_parser("create-venda"); s.add_argument("--json", required=True)
    s.set_defaults(func=cmd_create_venda)

    s = sub.add_parser("find-nfse")
    s.add_argument("--numero-venda", dest="numero_venda")
    s.add_argument("--id-cliente", dest="id_cliente")
    s.add_argument("--de"); s.add_argument("--ate")
    s.set_defaults(func=cmd_find_nfse)

    args = p.parse_args()
    print(json.dumps(args.func(args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
