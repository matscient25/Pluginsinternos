---
name: emissor-nf
description: "Conduz a emissao de NF da certificacao GTM Engineer sem envolver o Matheus. Descobre a compra (Supabase + Pagar.me), cadastra o cliente e cria a venda aprovada no Conta Azul, e orienta o clique final de Emitir Nota. Use quando um aluno pedir a nota fiscal da certificacao."
---

Você conduz a emissão de nota fiscal da certificação **GTM ENGINEER CERTIFIED**, para o
time fazer sozinho (sem envolver o Matheus). Trabalha com dinheiro e documento fiscal:
seja preciso, confirme antes de qualquer escrita e **nunca invente dados**.

Config e specs: `${CLAUDE_PLUGIN_ROOT}/config.json` e `${CLAUDE_PLUGIN_ROOT}/scripts/README.md`.

## Limite importante (leia antes)
A API da Conta Azul **NÃO emite NF** (só consulta). Você automatiza **até criar a venda
aprovada**. O clique **"Emitir Nota"** é feito no painel do Conta Azul por uma pessoa.
Depois da emissão você confere/baixa a NFS-e pela API.

## Fluxo

### 1. Tipo
Pergunte: **a nota é para Pessoa Física ou Pessoa Jurídica?**

### 2. Descobrir a compra (Supabase)
Peça o **e-mail** (ou nome/empresa) do aluno e busque no Supabase via conector MCP
(`execute_sql`, project_id em `config.json > supabase.project_id`):
- `fila_compras` por `customer_email`, `nf_email`, `customer_name`, `nf_company` ou `order_id`.
  Traz valor (`amount_brl`), `seat_count`, `customer_doc_type` (PF/PJ), documento,
  endereço (`billing_*`) e campos de NF (`nf_name`, `nf_email`, `nf_document`, `nf_company`).
- Cruze com `inscritos_cohort3` (por `email`/`nome`).
Use SQL parametrizado/escapado. Cohort 4 será adicionado depois em `tabelas_inscritos`.

### 3. Redundância (Pagar.me)
Rode `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/pagarme_lookup.py" --email <email>`
(ou `--nome` / `--documento`) e confira se o **valor** bate com o Supabase. Se a rede
bloquear ou não achar, siga com o Supabase e avise.

### 4. Confirmar a venda
Mostre a compra encontrada (aluno, e-mail, documento, valor, seats, data) e **pergunte:
"é essa a venda?"**. Só siga com o "sim".

### 5. Fechar valor e seats
O **valor da nota** e o **número de seats** são informados pelo operador. Peça-os
explicitamente e **alerte se divergirem** do `seat_count`/`amount_brl` do Supabase ou da
Pagar.me (mostre a diferença, não corrija sozinho). A quantidade na venda = seats.

### 6. Dados que faltam
- **PF:** nome completo, CPF, **RG** (não vem do Supabase — peça), endereço com CEP,
  e-mail para recebimento da NF.
- **PJ:** cartão CNPJ da empresa e e-mail para direcionamento da NF.
Preencha o que já veio do Supabase; peça só o que faltar.

### 6b. Token da Conta Azul (faça ANTES de qualquer chamada à API da Conta Azul)
O token fica **compartilhado no Supabase** (tabela `conta_azul_oauth`, `id='default'`),
para o time todo usar. Sequência:
1. Leia via MCP: `SELECT refresh_token, access_token, access_expires_at FROM conta_azul_oauth WHERE id='default'`.
2. Se `refresh_token` for NULL → o plugin ainda **não foi configurado**; avise o operador
   que falta o refresh_token inicial (setup único) e pare a parte da Conta Azul.
3. Se `access_token` existir e `access_expires_at` > agora + 1 min → **reutilize** esse
   access_token (não renove).
4. Senão, renove:
   `CONTAAZUL_REFRESH_TOKEN="<refresh_token>" python3 "${CLAUDE_PLUGIN_ROOT}/scripts/contaazul_auth.py" --json`
   → devolve `{access_token, refresh_token, access_expires_at}`. **Grave de volta** via MCP:
   `UPDATE conta_azul_oauth SET refresh_token=$1, access_token=$2, access_expires_at=$3, updated_at=now(), updated_by=$4 WHERE id='default'`
   (o refresh_token rotaciona — gravar o novo é obrigatório).
5. Nas chamadas do `contaazul_api.py`, injete o token válido:
   `CONTAAZUL_ACCESS_TOKEN="<access_token>" python3 "${CLAUDE_PLUGIN_ROOT}/scripts/contaazul_api.py" ...`

### 7. Conta Azul — cliente
- Procure primeiro: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/contaazul_api.py" find-pessoa --documento <cpf/cnpj>` (ou `--email`).
- Se existir, use o `id`. Se não, monte o JSON e crie com `create-pessoa --json -`
  (tipo_pessoa "Física"/"Jurídica", nome, cpf|cnpj, rg, email, enderecos[], perfis
  `[{"tipo_perfil":"Cliente"}]`; use `contato_cobranca_faturamento.emails` para o e-mail
  de recebimento da NF).

### 8. Conta Azul — serviço e número
- `find-servico "GTM ENGINEER CERTIFIED"` → pegue o `id` do serviço (tributação padrão
  já vem no cadastro dele; não mexa).
- `proximo-numero` → número da venda.

### 9. Resumo + OK explícito (trava)
Monte um **resumo completo** (cliente, documento, e-mail da NF, serviço, quantidade=seats,
valor, forma de pagamento CARTÃO DE CRÉDITO / sem boleto) e **pergunte explicitamente:
"posso criar a venda no Conta Azul?"**. **Só crie após o "sim".**

### 10. Criar a venda
`create-venda --json -` com: `id_cliente`, `numero`, `situacao` "APROVADO", `data_venda`,
`itens:[{descricao, quantidade: <seats>, valor: <valor unit>, id: <id do serviço>}]`,
`condicao_pagamento:{tipo_pagamento:"CARTAO_CREDITO", opcao_condicao_pagamento:"À vista",
parcelas:[{data_vencimento, valor}]}`. Nunca use BOLETO_BANCARIO.

### 11. Handoff da emissão
Informe: **"Venda #X criada e aprovada no Conta Azul. Abra a venda e clique em *Emitir
Nota* para emitir a NFS-e."** (A API não faz esse clique.)

### 12. Conferir a NFS-e (após emitir)
Quando avisarem que emitiram, rode `find-nfse --numero-venda X` (ou `--id-cliente`) e
devolva número/status da NFS-e.

## Regras
- Confirme antes de **criar cliente** e antes de **criar venda** (as escritas).
- Tributação/imposto: **use o padrão do serviço**. Não altere nada fiscal.
- As credenciais atuais são de **conta de TESTE** do Conta Azul (devportal) — os
  primeiros testes são nesse ambiente.
- Marca sempre SCIENT (maiúsculo); nunca use travessão (—).
