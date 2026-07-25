---
name: contratos-clientes
description: "Convenções para gerar contratos de cliente da SCIENT: código de proposta/contrato, produtos SCIENT, título da proposta, consulta de CNPJ e campos do template. Use ao criar, preencher ou revisar um contrato de cliente da SCIENT."
---

# Contratos de cliente (SCIENT)

Gera contratos de cliente preenchendo o template `templates/cliente.docx` com o motor
`scripts/fill_contract.py` (mesmo do contratos-time: preserva formatação).

## Código da proposta/contrato
`{FANTASIA3}SCI{AAAA}{DD}{MM}` — 3 primeiras letras do NOME FANTASIA (maiúsculas) +
`SCI` + ano + dia + mês. Ex.: Vittude em 25/07/2026 → `VITSCI20262507`. Vai no nome do
arquivo, no `{{CODIGO}}` (cabeçalho e rodapé) e dentro do `{{TITULO_PROPOSTA}}`.

## Título da proposta
`{CODIGO} PROPOSTA {NOME_FANTASIA} <> SCIENT - {PRODUTO}`. Produtos SCIENT:
ENGENHARIA DE GTM, DISCOVERY CONTINUA, IMPLEMENTAÇÃO HUBSPOT, GTM ENGINEER CERTIFIED.

## Consulta de CNPJ
`scripts/cnpj_lookup.py <CNPJ>` traz Razão Social, endereço e o sócio administrador
(Representante legal). Requer rede liberada para api.cpfcnpj.com.br; se bloquear, leia
do cartão CNPJ ou pergunte. Nunca invente dados.

## Campos do template
`{{CODIGO}}`, `{{TITULO_PROPOSTA}}`, `{{Razão Social}}`, `{{CNPJ}}`,
`{{Endereço, nº e complemento}}`, `{{Bairro}}`, `{{Estado}}`, `{{CEP}}`,
`{{Nome do Representante}}`, `{{DD}}`, `{{Mês}}`, `{{AAAA}}`.

## Intake obrigatório
CNPJ, cartão CNPJ, link da proposta, produto, nome fantasia, e **financeiro do cliente**
(nome, e-mail, telefone para NF/boletos).

## Regras
- Testemunha da SCIENT já vem fixa no template (Matheus Abraão Pinheiro Ferreira).
- Entrega: por ora só gera o .docx para download (sem upload em pasta, sem PDF).
- Nunca subir .docx pelo conector com base64.
- Anexo I (slides da proposta): por ora referencie o link; embed de slides fica para depois.
- Marca sempre SCIENT (maiúsculo). Nunca usar travessão (—).
