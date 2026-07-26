#!/usr/bin/env python3
"""
Consulta na Pagar.me (API v5) — usada como REDUNDANCIA para confirmar a compra e o
valor a partir do e-mail ou nome do aluno/empresa. NAO cria nem altera nada.

Segredo via env (nunca no repo):
  PAGARME_SECRET_KEY   (sk_...)   -> chave de consulta

Uso:
  python3 pagarme_lookup.py --email pessoa@dominio.com
  python3 pagarme_lookup.py --nome "Fulano de Tal"
  python3 pagarme_lookup.py --documento 12345678900

Auth Pagar.me v5: Basic base64("<sk>:") (sk como usuario, senha vazia).
Valores da Pagar.me vem em centavos; devolvemos amount_brl tambem.
"""
import argparse
import base64
import json
import os
import sys
import urllib.parse
import urllib.request

API_BASE = os.environ.get("PAGARME_API_BASE", "https://api.pagar.me/core/v5")


def _auth_header():
    sk = os.environ.get("PAGARME_SECRET_KEY")
    if not sk:
        raise SystemExit("ERRO: defina PAGARME_SECRET_KEY (sk_...) no ambiente.")
    return "Basic " + base64.b64encode(f"{sk}:".encode()).decode()


def _get(path, params=None):
    url = API_BASE + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", _auth_header())
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise SystemExit(f"ERRO HTTP {e.code} em GET {path}: {detail}")


def _orders_of_customer(cid):
    out = []
    data = _get("/orders", params={"customer_id": cid, "size": 20}).get("data", [])
    for o in data:
        amount = o.get("amount")
        out.append({
            "order_id": o.get("id"),
            "code": o.get("code"),
            "status": o.get("status"),
            "amount_cents": amount,
            "amount_brl": round(amount / 100, 2) if isinstance(amount, int) else None,
            "created_at": o.get("created_at"),
            "items": [
                {"description": it.get("description"), "quantity": it.get("quantity"),
                 "amount_cents": it.get("amount")}
                for it in (o.get("items") or [])
            ],
        })
    return out


def main():
    p = argparse.ArgumentParser(description="Consulta Pagar.me (redundancia de valor)")
    p.add_argument("--email")
    p.add_argument("--nome")
    p.add_argument("--documento")
    a = p.parse_args()
    if not (a.email or a.nome or a.documento):
        raise SystemExit("Informe --email, --nome ou --documento.")

    params = {"size": 20}
    if a.email:
        params["email"] = a.email
    if a.nome:
        params["name"] = a.nome
    if a.documento:
        params["document"] = a.documento

    customers = _get("/customers", params=params).get("data", [])
    result = []
    for c in customers:
        result.append({
            "customer_id": c.get("id"),
            "name": c.get("name"),
            "email": c.get("email"),
            "document": c.get("document"),
            "orders": _orders_of_customer(c.get("id")),
        })
    print(json.dumps({"matches": result, "count": len(result)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
