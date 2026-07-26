---
name: notas-fiscais
description: "Convencoes para emitir a NF da certificacao GTM Engineer da SCIENT: onde estao os dados da compra (Supabase, Pagar.me), como criar cliente e venda no Conta Azul (API v2), e por que a emissao da NF e um clique manual no painel. Use ao emitir, conferir ou dar suporte a uma nota fiscal da certificacao."
---

# Nota fiscal da certificação GTM Engineer (SCIENT)

Emite a NF de serviço da certificação **GTM ENGINEER CERTIFIED**, para o time fazer sem
envolver o Matheus. Config em `${CLAUDE_PLUGIN_ROOT}/config.json`; specs da API em
`${CLAUDE_PLUGIN_ROOT}/scripts/*.md`.

## Regra de ouro
A **API da Conta Azul NÃO emite NF** (só consulta). O plugin automatiza **até criar a
venda aprovada**; o **"Emitir Nota"** é um clique manual no painel do Conta Azul. Depois,
a API confere/baixa a NFS-e.

## Onde estão os dados
- **Supabase** (projeto `gtme`, `config.json > supabase.project_id`), via conector MCP:
  - `fila_compras` — valor (`amount_brl`), `seat_count`, `customer_doc_type` (PF/PJ),
    documento, endereço (`billing_*`) e campos de NF (`nf_name`, `nf_email`,
    `nf_document`, `nf_company`). É a fonte primária.
  - `inscritos_cohort3` — complementa (nome, e-mail, empresa, valor_pago, order_id).
- **Pagar.me** (`scripts/pagarme_lookup.py`) — só redundância: confirma o valor por
  e-mail/nome/documento.

## Sequência na Conta Azul (API v2)
1. `find-pessoa --documento|--email` → se não achar, `create-pessoa`.
2. `find-servico "GTM ENGINEER CERTIFIED"` → id do serviço (tributação padrão do serviço).
3. `proximo-numero` → número da venda.
4. `create-venda` → `situacao` "APROVADO", `itens[].quantidade` = nº de seats,
   `itens[].id` = id do serviço, `condicao_pagamento.tipo_pagamento` "CARTAO_CREDITO"
   (educação = sempre cartão; **sem boleto**).
5. Handoff: pessoa clica **Emitir Nota** no painel.
6. `find-nfse --numero-venda N` → confere/baixa a NFS-e emitida.

## Preço e seats
Cada seat = **R$ 5.600** (desconto de até 15% em alguns casos). O **valor da nota** e o
**nº de seats** são SEMPRE informados pelo operador; o Supabase/Pagar.me servem para
conferir. Quantidade na venda = seats. Alerte divergências, não corrija sozinho.

## Segredos e token (tudo no Supabase, para o time)
**Nenhum segredo vai em variável de ambiente** (o campo do Environment é visível a quem
usa o ambiente). Tudo fica no Supabase, lido pelo agente via conector e injetado como env
só na hora de chamar cada script:
- `notas_fiscais_secrets`: `CONTAAZUL_CLIENT_ID`, `CONTAAZUL_CLIENT_SECRET`, `PAGARME_SECRET_KEY`.
- `conta_azul_oauth` (`id='default'`): `refresh_token` (rotaciona) + `access_token` (1h,
  reaproveitado; só renova quando expira).
Requisitos do Environment: rede liberada (`auth.contaazul.com`, `api-v2.contaazul.com`,
`api.pagar.me`) e conector Supabase ativo. Detalhes em `scripts/README.md`.

## Segurança
- Nenhum segredo no git nem no campo de env do Environment; tudo no Supabase (RLS on).
- Confirme com o operador **antes de criar cliente e antes de criar venda**.
- Conta Azul em **produção** (empresa SCIENT) — venda/nota são reais.
- Marca sempre SCIENT (maiúsculo); nunca usar travessão (—).
