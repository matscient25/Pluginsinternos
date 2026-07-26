---
description: "Emite a NF da certificacao GTM Engineer: descobre a compra (Supabase + Pagar.me), cadastra o cliente e cria a venda no Conta Azul, e orienta o clique de Emitir Nota."
---

Inicie a emissão de nota fiscal da certificação **GTM ENGINEER CERTIFIED** usando o
agente **emissor-nf** (`${CLAUDE_PLUGIN_ROOT}/agents/emissor-nf.md`).

Contexto do operador (se houver): $ARGUMENTS

Conduza o fluxo do agente:
1. Pergunte se a nota é para **Pessoa Física ou Jurídica**.
2. Descubra a compra no **Supabase** (`fila_compras` / `inscritos_cohort3`) e confirme o
   valor na **Pagar.me**.
3. Confirme com o operador que é a venda certa; peça **valor da nota** e **nº de seats**.
4. No **Conta Azul**: ache/cadastre o cliente, pegue o id do serviço e o próximo número.
5. Mostre o **resumo** e peça **OK explícito** antes de **criar a venda** (aprovada,
   cartão de crédito, sem boleto).
6. Oriente o clique final **"Emitir Nota"** no painel (a API não emite).
7. Depois, confira a **NFS-e** e devolva o número.

Lembre: nunca invente dados; confirme antes de cada escrita; tributação = padrão do serviço.
