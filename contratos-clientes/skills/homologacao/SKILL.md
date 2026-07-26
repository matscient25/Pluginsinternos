---
name: homologacao
description: "Fornece os dados de homologação da SCIENT que clientes costumam pedir (razão social, CNPJ, endereço, faturamento, representante legal), o PDF pronto 'Dados para Homologação' e a lista de documentos (contrato social, cartão CNPJ, certidão negativa federal, CRF do FGTS). Use quando um cliente pedir dados ou documentos para homologação/cadastro de fornecedor."
---

# Homologação de fornecedor (SCIENT)

Quando um cliente pedir para homologar a SCIENT como fornecedor, use os dados de
`${CLAUDE_PLUGIN_ROOT}/config.json` (bloco `homologacao`).

## Como responder (padrão)
1. **Mande o PDF pronto.** Já existe um artefato "Dados para Homologação" na pasta
   de homologação do Drive. Normalmente é só enviar o link:
   `https://drive.google.com/file/d/1N14ToqiwSL1bBnfN3-JOM-I3qqk4vIvK/view`
2. Se o cliente preferir os dados em texto (ou para preencher um formulário de
   cadastro), informe os campos abaixo.

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

## Regerar o PDF (só se os dados mudarem)
O PDF é gerado 1x e reaproveitado. Se algum dado mudar, regere e suba de novo:
```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/gerar_homologacao_pdf.py" "Dados para Homologacao - SCIENT.pdf" --data DD/MM/AAAA
```
Depende de `reportlab` e `pillow` (`pip install reportlab pillow`). Lê os dados
deste bloco da config e a logo de `assets/scient_logo.png`. O arquivo sai com
~16 KB — pequeno o bastante para subir pelo conector do Drive via base64
(`create_file` com `parentId` da pasta de homologação e `disableConversionToGoogleType=true`;
funciona porque `stack@scient.cc` é editor da pasta). Após subir a nova versão,
apague as antigas e ajuste o compartilhamento do link.

Estilo: marca sempre SCIENT (maiúsculo); nunca use travessão (—).
