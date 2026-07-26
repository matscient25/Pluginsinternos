# Setup dos scripts (notas-fiscais)

Só Python 3 (biblioteca padrão) — não precisa instalar nada.

## Modelo pensado para o TIME

Para todo o time usar (via claude.ai web/desktop), configure **uma vez** no **Environment
compartilhado** do Claude Code:

- **Variáveis de ambiente (fixas):** `CONTAAZUL_CLIENT_ID`, `CONTAAZUL_CLIENT_SECRET`,
  `PAGARME_SECRET_KEY`.
- **Rede (allowlist):** `auth.contaazul.com`, `api-v2.contaazul.com`, `api.pagar.me`.
- **Conector Supabase** disponível no ambiente (o agente usa para o token e para os dados).

O **refresh_token da Conta Azul NÃO vai em variável de ambiente** — ele rotaciona a cada
renovação. Fica no **Supabase**, na tabela `conta_azul_oauth` (linha `id='default'`), lida
e atualizada automaticamente pelo agente. O `access_token` (1h) é reaproveitado; só renova
quando expira. Isso funciona para qualquer pessoa do time, em qualquer sessão.

Como as chaves já circularam em chat, **rotacione** quando puder (principalmente a `sk_` da
Pagar.me).

## Setup inicial (uma vez): gravar o primeiro refresh_token

O `refresh_token` inicial sai do fluxo OAuth (login no ERP). Passos:

1. **Autorizar (Etapa 1):** abra a URL de autorização da sua aplicação (portal do
   desenvolvedor da Conta Azul), faça login com o usuário/senha do ERP; você é
   redirecionado com um `code` na URL (válido ~3 min).
2. **Trocar code por token (Etapa 2):**
   ```bash
   curl -s -X POST https://auth.contaazul.com/oauth2/token \
     -H "Authorization: Basic $(printf '%s:%s' "$CONTAAZUL_CLIENT_ID" "$CONTAAZUL_CLIENT_SECRET" | base64)" \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     --data-urlencode grant_type=authorization_code \
     --data-urlencode code=SEU_CODE \
     --data-urlencode redirect_uri=https://contaazul.com
   ```
   A resposta traz `refresh_token`.
3. **Gravar no Supabase** (uma vez):
   ```sql
   update public.conta_azul_oauth
      set refresh_token = 'O_REFRESH_TOKEN', access_token = null,
          access_expires_at = null, updated_at = now(), updated_by = 'setup'
    where id = 'default';
   ```
   Pronto — a partir daí o agente renova e rotaciona sozinho.

## Como o agente usa o token (referência)

1. Lê `refresh_token, access_token, access_expires_at` de `conta_azul_oauth`.
2. Se o `access_token` ainda é válido (`access_expires_at` no futuro), reutiliza.
3. Senão: `CONTAAZUL_REFRESH_TOKEN=<rt> python3 contaazul_auth.py --json` → grava de volta
   o novo `access_token` + `refresh_token` + `access_expires_at`.
4. Chama a API com `CONTAAZUL_ACCESS_TOKEN=<token> python3 contaazul_api.py ...`.

## Testes rápidos (após o setup)

```bash
# com um access_token válido em CONTAAZUL_ACCESS_TOKEN (ou refresh_token no env):
python3 contaazul_api.py whoami                       # empresa conectada (valida auth)
python3 contaazul_api.py find-servico "GTM ENGINEER CERTIFIED"
python3 pagarme_lookup.py --email aluno@exemplo.com
```

## Uso standalone (uma máquina Mac, sem Supabase)

Dá para rodar sem Supabase: coloque `CONTAAZUL_REFRESH_TOKEN` no `.env` e o
`contaazul_auth.py` cacheia/rotaciona num arquivo local (`~/.scient/contaazul_token.json`).
Não recomendado para time (não compartilha entre pessoas/sessões).

> Os scripts seguem a documentação oficial, mas ainda **não foram testados contra a API
> real** (o ambiente de dev bloqueia os hosts). O primeiro uso na sua máquina é o teste
> de verdade — ajustes finos podem ser necessários.
