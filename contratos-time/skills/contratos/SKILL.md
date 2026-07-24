---
name: contratos-time
description: Como gerar contratos do time (Full time e Freelancer) a partir de templates .docx com placeholders {{CAMPO}}, preenchendo os dados da pessoa e salvando como Google Doc no Drive. Use quando o usuario pedir para criar, gerar ou preencher um contrato de contratacao.
---

# Contratos do time (Full time e Freelancer)

Este projeto gera contratos preenchidos preservando **exatamente** a formatacao
do template, sem edicao manual.

## Como funciona (por que baixar-preencher-subir)

O conector do Google Drive **nao** oferece "substituir texto" dentro de um
Google Doc existente. Para manter a formatacao do template E preencher os
campos, o fluxo e:

1. **Baixar** o template `.docx` do Drive (`download_file_content` → base64).
   Se o template for um Google Doc, exportar como `.docx`
   (`exportMimeType: application/vnd.openxmlformats-officedocument.wordprocessingml.document`).
2. **Preencher** os placeholders `{{CAMPO}}` localmente com
   `scripts/fill_contract.py` — pura stdlib, preserva fonte/negrito/tabelas e
   lida com placeholders quebrados em varios runs pelo Word.
3. **Subir** o `.docx` preenchido para a pasta de destino via `create_file`,
   deixando a conversao ligada → vira um **Google Doc editavel**.

## Convencoes

- **Placeholders (campos)**: `{{CHAVE}}` (chave em MAIUSCULAS, sem acento;
  letras, numeros, `_`, `.`, `-`). Ex.: `{{NOME}}`, `{{CPF}}`, `{{CARGO}}`,
  `{{DATA}}`, `{{VALOR}}`, `{{DATA_INICIO}}`.
- **Clausulas condicionais**: `{{#CHAVE}} ... {{/CHAVE}}` envolvendo o trecho
  que so entra em alguns contratos. Nos dados, `CHAVE: true` mantem o bloco (e
  preenche os campos internos); `CHAVE: false` (ou ausente) remove o bloco
  inteiro. Ideal por o marcador de abertura/fechamento em linha propria quando
  o bloco tem varios paragrafos (o motor limpa a linha do marcador). Ex. do
  plano de saude (clausula 12.2):
  ```
  {{#PLANO_SAUDE}}
  a) Plano de saude: {{PLANO_OPERADORA}}, em regime de coparticipacao ... ;
  b) {{PLANO_COMODIDADE}}, nas condicoes definidas pela Contratante.
  {{/PLANO_SAUDE}}
  ```
  Dados: `{"PLANO_SAUDE": true, "PLANO_OPERADORA": "Bradesco Saude", ...}`.
  Se `PLANO_SAUDE` for true, sempre confirme com o usuario a operadora e as
  condicoes antes de gerar — nunca deixe campos do plano em branco.
- **Listas repetiveis**: um paragrafo com `{{*CHAVE}}` e repetido uma vez por
  item de `data[CHAVE]` (lista), preservando o estilo (bullet/numeracao). Usado
  na clausula de Servicos: `{{*Serviços}}` vira um item por servico do cargo.
- **Cargos (roles)**: o config tem `roles` com 4 perfis (GTM Expert, Forward
  Deployment Engineer, Especialista de Hubspot, Engenheiro de dados). Cada um
  define `Objeto` (clausula do Objeto), `Área` (clausula dos Servicos) e
  `Serviços` (lista). Escolher o cargo preenche esses 3 automaticamente — os
  "2 lugares" do contrato que descrevem o que a pessoa faz.
- **Ano SEMPRE atual**: `AAAA` usa o ano corrente. `Data`/`DD`/`Mês` vem da data
  de vigencia; sem ela, a data de hoje. `Mês` por extenso pt-BR.
- **Modalidade**: pergunte full time ou part time (todos sao PJ; nao pergunte
  CLT/PJ). Guarde no registro/checklist.
- **Nunca deixe `{{...}}` cru** no contrato final. Se o template tem um
  placeholder sem valor, pergunte ao usuario antes de gerar. O script sai com
  codigo 3 e lista `unfilled` justamente para pegar isso.
- **DATA**: se nao informada, use a data de hoje em pt-BR (dd/mm/aaaa).
- **Nao invente dados** (CPF, valores, cargo). Falta obrigatorio → pergunte.
- **Dois tipos, dois templates**: `full-time` e `freelancer`, cada um com seu
  `template_file_id` em `config.json`. Sempre confirme o tipo antes de gerar.
- **Titulo do arquivo**: use `filename_pattern` do tipo (ex.:
  `Contrato Freelancer - {{NOME}} - {{DATA}}`).

## Arquivos

- `config.json` — IDs dos templates, pasta de destino, campos obrigatorios.
- `commands/setup.md` — configura os IDs e confere os placeholders.
- `commands/gerar-contrato.md` — gera um contrato preenchido.
- `scripts/fill_contract.py` — motor de preenchimento (`--list` para inspecionar,
  `--data` para preencher).

## Cuidado com dados sensiveis

Contratos contem dados pessoais (CPF, remuneracao). Trabalhe em diretorio
temporario (`mktemp -d`), nao grave dentro do plugin, e limpe ao final.
