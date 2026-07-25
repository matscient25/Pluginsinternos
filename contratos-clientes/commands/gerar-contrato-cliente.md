---
description: Gera o contrato de cliente da SCIENT (código, produto, dados do CNPJ) e entrega o .docx
argument-hint: "[CNPJ do cliente e/ou dados; link da proposta; produto]"
---

Gere um contrato de cliente da SCIENT a partir do template embarcado. Argumentos: `$ARGUMENTS`

Leia `${CLAUDE_PLUGIN_ROOT}/config.json` (produtos, regra do código, campos, API de CNPJ).

## 1. Intake (pergunte o que não vier em $ARGUMENTS)
1. **CNPJ do cliente**.
2. **Cartão CNPJ** do cliente (para ler os dados caso a API não responda).
3. **Link da proposta aceita** (PPT).
4. **Produto SCIENT** — um de: ENGENHARIA DE GTM, DISCOVERY CONTINUA, IMPLEMENTAÇÃO HUBSPOT, GTM ENGINEER CERTIFIED.
5. **Nome fantasia** do cliente (define as 3 letras do código; tente obter da API/cartão).
6. **Financeiro do cliente**: nome, e-mail e telefone (direcionamento de NF e boletos). Sempre pergunte; guarde para o resumo final.

## 2. Consulte o CNPJ (pré-preenche dados)
```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/cnpj_lookup.py" "<CNPJ>"
```
Do JSON, extraia e mapeie para os campos do template:
- `Razão Social`, `CNPJ`
- `Endereço, nº e complemento` (logradouro + número + complemento)
- `Bairro`, `Estado` (cidade/UF), `CEP`
- `Nome do Representante` = **sócio administrador** (no QSA, o sócio com qualificação de administrador)
Se o script retornar `erro` (rede bloqueada) OU faltar algum campo, **leia do cartão CNPJ** enviado ou **pergunte**. Nunca invente.

## 3. Monte o código e o título
- **Código** (ver `codigo_rule`): 3 primeiras letras do **nome fantasia** (MAIÚSCULAS) + `SCI` + **AAAA** + **DD** + **MM** (data de hoje). Ex.: Vittude em 25/07/2026 → `VITSCI20262507`. Descubra a data com `date +%Y` (AAAA), `date +%d` (DD), `date +%m` (MM).
- **CODIGO** vai em `{{CODIGO}}` (cabeçalho e rodapé).
- **TITULO_PROPOSTA** (ver `titulo_proposta_pattern`): `{CODIGO} PROPOSTA {NOME_FANTASIA} <> SCIENT - {PRODUTO}`. Ex.: `VITSCI20262507 PROPOSTA VITTUDE <> SCIENT - ENGENHARIA DE GTM`.
- Datas de assinatura: `DD`, `Mês` (por extenso pt-BR), `AAAA` (ano atual).

## 4. Preencha e gere o .docx
Copie o template e preencha:
```
TMP=$(mktemp -d)
cp "${CLAUDE_PLUGIN_ROOT}/templates/cliente.docx" "$TMP/modelo.docx"
# monte dados.json com: CODIGO, TITULO_PROPOSTA, Razão Social, CNPJ,
# "Endereço, nº e complemento", Bairro, Estado, CEP, Nome do Representante, DD, Mês, AAAA
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fill_contract.py" \
  --template "$TMP/modelo.docx" --out "~/Downloads/<CODIGO> Contrato <NOME_FANTASIA>.docx" --data @"$TMP/dados.json"
```
Confira `unfilled`: se não estiver vazio, resolva antes.

## 5. Entregue (sem upload por enquanto)
Entregue o `.docx` gerado ao usuário para download (config `entrega: download`). NÃO
suba pelo conector com base64. Nome do arquivo = `{CODIGO} Contrato {NOME_FANTASIA}`.

## 6. Reporte
Mostre: o **código**, o **título da proposta**, o **produto**, os dados do cliente
preenchidos, o **representante legal**, e os **dados do financeiro** (nome/e-mail/telefone)
que você coletou. Se algum dado veio do cartão CNPJ (API bloqueada), sinalize.

**Estilo:** marca sempre **SCIENT** (maiúsculo). **Nunca use travessão (—)**.
Anexo I (slides da proposta): por ora referencie o link da proposta; o embed de slides
fica para depois. Limpe `$TMP` ao final.
