# Setup dos scripts (notas-fiscais)

Só Python 3 (biblioteca padrão) — não precisa instalar nada.

## 1. Segredos por variável de ambiente

Copie `../.env.example` para um `.env` **local** (fora do git) e preencha. Antes de
rodar os scripts, carregue as variáveis (ex.: `export $(grep -v '^#' .env | xargs)`
ou use a config de ambiente do seu Claude Code).

Nunca comite valores reais. Como as chaves já circularam em chat, **rotacione** quando
puder (principalmente a `PAGARME_SECRET_KEY`).

## 2. Conta Azul — pegar o `refresh_token` (passo único)

O access_token expira em ~1h; o plugin renova sozinho com o **refresh_token**. Para
obtê-lo uma vez:

1. **Autorizar** (login no ERP): acesse a URL de autorização da sua aplicação no
   portal do desenvolvedor da Conta Azul (developers.contaazul.com) e faça login com
   o usuário/senha do ERP. Você será redirecionado para a `redirect_uri` e a URL vai
   conter um `code` (válido por ~3 min).
2. **Trocar o code por tokens**:
   ```bash
   curl -s -X POST https://auth.contaazul.com/oauth2/token \
     -H "Authorization: Basic $(printf '%s:%s' "$CONTAAZUL_CLIENT_ID" "$CONTAAZUL_CLIENT_SECRET" | base64)" \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     --data grant_type=authorization_code \
     --data code=SEU_CODE \
     --data redirect_uri=https://contaazul.com
   ```
   A resposta traz `access_token` **e** `refresh_token`. Guarde o `refresh_token` em
   `CONTAAZUL_REFRESH_TOKEN`.
3. Teste: `python3 contaazul_auth.py` deve imprimir um access_token.

> A Conta Azul pode rotacionar o refresh_token a cada renovação. O `contaazul_auth.py`
> guarda o mais novo no cache (`~/.scient/contaazul_token.json`, chmod 600).

## 3. Rede (só no claude.ai web/desktop)

No terminal do Mac funciona direto. No web/desktop, libere na política de rede do seu
Environment: `auth.contaazul.com`, `api-v2.contaazul.com`, `api.pagar.me`.

## 4. Testes rápidos

```bash
python3 contaazul_api.py whoami                       # valida auth (empresa conectada)
python3 contaazul_api.py find-servico "GTM ENGINEER CERTIFIED"
python3 pagarme_lookup.py --email aluno@exemplo.com
```

> Os scripts foram escritos a partir da documentação oficial, mas ainda **não foram
> testados contra a API real** (o ambiente de dev bloqueia esses hosts). O primeiro
> uso na sua máquina é o teste de verdade — ajustes finos podem ser necessários.
