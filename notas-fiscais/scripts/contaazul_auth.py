#!/usr/bin/env python3
"""
Autenticacao OAuth2 da Conta Azul (API v2).

O plugin usa o fluxo de *refresh_token*: com o CLIENT_ID/SECRET e um refresh_token
valido, pega um access_token novo a cada uso (o access_token expira em ~1h).

Segredos vem SEMPRE de variaveis de ambiente (nunca do repo):
  CONTAAZUL_CLIENT_ID
  CONTAAZUL_CLIENT_SECRET
  CONTAAZUL_REFRESH_TOKEN   (obtido 1x no fluxo de autorizacao; ver scripts/README.md)

Cache opcional (guarda access_token + refresh_token rotacionado) em:
  CONTAAZUL_TOKEN_CACHE  (default: ~/.scient/contaazul_token.json)

Uso:
  python3 contaazul_auth.py            # imprime um access_token valido
  python3 contaazul_auth.py --force    # ignora cache e renova
"""
import argparse
import base64
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request

AUTH_URL = os.environ.get("CONTAAZUL_AUTH_URL", "https://auth.contaazul.com/oauth2/token")


def _cache_path():
    p = os.environ.get("CONTAAZUL_TOKEN_CACHE")
    if p:
        return os.path.expanduser(p)
    return os.path.expanduser("~/.scient/contaazul_token.json")


def _load_cache():
    try:
        with open(_cache_path(), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_cache(data):
    path = _cache_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    try:
        os.chmod(path, 0o600)
    except Exception:
        pass


def _basic_header():
    cid = os.environ.get("CONTAAZUL_CLIENT_ID")
    secret = os.environ.get("CONTAAZUL_CLIENT_SECRET")
    if os.environ.get("CONTAAZUL_BASIC_AUTH"):
        return os.environ["CONTAAZUL_BASIC_AUTH"]
    if not cid or not secret:
        raise SystemExit(
            "ERRO: defina CONTAAZUL_CLIENT_ID e CONTAAZUL_CLIENT_SECRET "
            "(ou CONTAAZUL_BASIC_AUTH) nas variaveis de ambiente."
        )
    return base64.b64encode(f"{cid}:{secret}".encode()).decode()


def _refresh(refresh_token):
    body = urllib.parse.urlencode(
        {"grant_type": "refresh_token", "refresh_token": refresh_token}
    ).encode()
    req = urllib.request.Request(AUTH_URL, data=body, method="POST")
    req.add_header("Authorization", "Basic " + _basic_header())
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def refresh_tokens(refresh_token=None):
    """Renova usando o refresh_token informado (ou CONTAAZUL_REFRESH_TOKEN do env) e
    devolve o conjunto completo. Use no modelo de token COMPARTILHADO (Supabase):
    o agente le o refresh_token do Supabase, chama isto e grava o resultado de volta."""
    rt = refresh_token or os.environ.get("CONTAAZUL_REFRESH_TOKEN")
    if not rt:
        raise SystemExit("ERRO: informe --refresh-token ou CONTAAZUL_REFRESH_TOKEN.")
    tok = _refresh(rt)
    access = tok.get("access_token")
    if not access:
        raise SystemExit("ERRO: refresh nao retornou access_token: " + json.dumps(tok))
    expires_in = int(tok.get("expires_in", 3600))
    exp_dt = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=expires_in)
    return {
        "access_token": access,
        "refresh_token": tok.get("refresh_token", rt),
        "expires_in": expires_in,
        "access_expires_at": exp_dt.replace(microsecond=0).isoformat(),
    }


def get_access_token(force=False):
    cache = _load_cache()
    now = int(time.time())
    if not force and cache.get("access_token") and cache.get("expires_at", 0) > now + 60:
        return cache["access_token"]

    refresh_token = cache.get("refresh_token") or os.environ.get("CONTAAZUL_REFRESH_TOKEN")
    if not refresh_token:
        raise SystemExit(
            "ERRO: sem refresh_token. Defina CONTAAZUL_REFRESH_TOKEN (veja scripts/README.md "
            "para o passo unico de autorizacao)."
        )

    tok = _refresh(refresh_token)
    access = tok.get("access_token")
    if not access:
        raise SystemExit("ERRO: refresh nao retornou access_token: " + json.dumps(tok))
    expires_in = int(tok.get("expires_in", 3600))
    new_cache = {
        "access_token": access,
        "expires_at": now + expires_in,
        # a Conta Azul pode rotacionar o refresh_token; guardamos o mais novo
        "refresh_token": tok.get("refresh_token", refresh_token),
    }
    _save_cache(new_cache)
    return access


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Auth OAuth2 Conta Azul")
    p.add_argument("--json", action="store_true",
                   help="modelo compartilhado: renova e imprime JSON completo (p/ gravar no Supabase)")
    p.add_argument("--refresh-token", dest="refresh_token",
                   help="refresh_token a usar (senao usa CONTAAZUL_REFRESH_TOKEN)")
    p.add_argument("--force", action="store_true", help="modo arquivo-cache: ignora cache")
    a = p.parse_args()
    if a.json:
        print(json.dumps(refresh_tokens(a.refresh_token), ensure_ascii=False))
    else:
        print(get_access_token(force=a.force))
