#!/usr/bin/env python3
"""
cnpj_lookup.py — Consulta um CNPJ na API cpfcnpj.com.br e imprime o JSON cru,
para o agente extrair Razão Social, endereço e o sócio administrador
(Representante legal).

Uso:
  python3 cnpj_lookup.py 48893099000124
  python3 cnpj_lookup.py 48.893.099/0001-24 --token <TOKEN> --pacote 9

- Token: por --token, senão de config.json (cnpj_api.token), ao lado do plugin.
- Requer rede liberada para api.cpfcnpj.com.br. Se estiver bloqueada (ex.: ambiente
  de dev), o script sai com erro claro e o agente deve PERGUNTAR os dados ou ler do
  cartão CNPJ enviado.
- Respeita proxy via variáveis de ambiente (HTTPS_PROXY).

Saída: JSON da API (ou {"erro": "..."} com a causa). Nunca inventa dados.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error


def load_token():
    here = os.path.dirname(os.path.abspath(__file__))
    cfg = os.path.join(here, "..", "config.json")
    try:
        with open(cfg, encoding="utf-8") as f:
            return json.load(f).get("cnpj_api", {}).get("token")
    except Exception:
        return None


def base_url():
    here = os.path.dirname(os.path.abspath(__file__))
    cfg = os.path.join(here, "..", "config.json")
    try:
        with open(cfg, encoding="utf-8") as f:
            return json.load(f).get("cnpj_api", {}).get("base_url", "https://api.cpfcnpj.com.br")
    except Exception:
        return "https://api.cpfcnpj.com.br"


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "contratos-clientes/1.0"})
    # urllib respeita proxies do ambiente por padrão (getproxies)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode("utf-8", "replace")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"_raw": raw[:2000]}


def main():
    ap = argparse.ArgumentParser(description="Consulta CNPJ na cpfcnpj.com.br")
    ap.add_argument("cnpj")
    ap.add_argument("--token")
    ap.add_argument("--pacote", help="pacote específico; senão tenta uma lista")
    args = ap.parse_args()

    token = args.token or load_token()
    if not token:
        print(json.dumps({"erro": "sem token (passe --token ou config cnpj_api.token)"},
                         ensure_ascii=False)); return 2
    cnpj = re.sub(r"\D", "", args.cnpj)
    if len(cnpj) != 14:
        print(json.dumps({"erro": f"CNPJ inválido: {args.cnpj} ({len(cnpj)} dígitos)"},
                         ensure_ascii=False)); return 2

    base = base_url().rstrip("/")
    pacotes = [args.pacote] if args.pacote else ["9", "6", "3", "2", "1"]
    last_err = None
    for pkg in pacotes:
        url = f"{base}/{token}/{pkg}/{cnpj}"
        try:
            data = fetch(url)
            # heurística: resposta útil tem razão/nome ou lista de sócios
            s = json.dumps(data, ensure_ascii=False).lower()
            if any(k in s for k in ["raz", "nome", "fantasia", "socio", "qsa", "logr"]):
                print(json.dumps({"pacote": pkg, "cnpj": cnpj, "dados": data},
                                 ensure_ascii=False, indent=2))
                return 0
            last_err = f"pacote {pkg}: resposta sem campos esperados"
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code} no pacote {pkg}"
        except urllib.error.URLError as e:
            last_err = f"rede/proxy bloqueou ({e.reason}) — api.cpfcnpj.com.br inacessível"
            break
        except Exception as e:  # noqa
            last_err = f"{type(e).__name__}: {e}"
    print(json.dumps({"erro": last_err or "falha desconhecida",
                      "dica": "peça os dados ao operador ou leia do cartão CNPJ"},
                     ensure_ascii=False))
    return 1


if __name__ == "__main__":
    sys.exit(main())
