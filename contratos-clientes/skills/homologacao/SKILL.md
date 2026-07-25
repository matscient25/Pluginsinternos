---
name: homologacao
description: "Fornece os dados de homologação da SCIENT que clientes costumam pedir (razão social, CNPJ, endereço, faturamento, representante legal) e a lista de documentos (contrato social, cartão CNPJ, certidão negativa federal, CRF do FGTS). Use quando um cliente pedir dados ou documentos para homologação/cadastro de fornecedor."
---

# Homologação de fornecedor (SCIENT)

Quando um cliente pedir para homologar a SCIENT como fornecedor, use os dados de
`${CLAUDE_PLUGIN_ROOT}/config.json` (bloco `homologacao`). Por ora é **informativo**:
apresente os dados em texto. NÃO gere PDF nem faça upload em pasta (desativado por ora).

## Dados para homologação (informe quando pedirem)
- Razão social: Scient Consultoria de Gestão Empresarial Ltda.
- CNPJ: 48.893.099/0001-24
- Endereço: Rua Augusto dos Anjos, nº 225, Apt. 16, Melville Empresarial I e II, Barueri/SP, CEP 06485-370
- E-mail de faturamento: giovanni@scient.cc
- Financeiro: Matheus Pinheiro (matheus@scient.cc)
- Representante legal: Giovanni Barbosa Salvador, CPF 366.599.668-62

## Documentos que costumam ser solicitados
- Contrato social
- Cartão CNPJ
- Certidão negativa Federal
- Certificado de Regularidade do FGTS (CRF)

## Aviso importante sobre o CRF
O **CRF do FGTS vale 1 mês** a partir da emissão. Se o cliente solicitar, avise que
provavelmente será necessário **emitir uma nova guia** (o **Giovanni** consegue emitir).

Estilo: marca sempre SCIENT (maiúsculo); nunca use travessão (—).
