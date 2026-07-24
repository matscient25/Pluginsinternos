---
description: Gera um contrato (Full time ou Freelancer) preenchido e salva como Google Doc na pasta do Drive
argument-hint: "[full-time|freelancer] dados da pessoa (nome, CPF, cargo, valor, data...)"
allowed-tools: Bash, Read, mcp__Google_Drive__download_file_content, mcp__Google_Drive__create_file, mcp__Google_Drive__get_file_metadata, mcp__Google_Drive__search_files
---

Gere um contrato preenchido a partir do template correto e salve na pasta do Drive.
Argumentos recebidos: `$ARGUMENTS`

Siga exatamente estes passos:

## 1. Carregue a configuração
Leia `${CLAUDE_PLUGIN_ROOT}/config.json`. Se `destination_folder_id` ainda
estiver com "COLE_AQUI...", peça ao usuário o link/ID da pasta de destino do
Drive (ou rode `/contratos-time:setup`).

## 2. Faça as perguntas de intake
Como todos são contratados **PJ**, NÃO pergunte CLT/PJ. Pergunte (se não vier em
`$ARGUMENTS`):
1. **Cargo** — um dos `roles` do config: GTM Expert, Forward Deployment Engineer,
   Especialista de Hubspot, Engenheiro de dados. O cargo define automaticamente
   `Objeto`, `Área` e a lista `Serviços` (que preenche os 2 lugares do contrato:
   a cláusula do Objeto e a lista de serviços).
2. **Modalidade** — full time ou part time.
3. **Salário** — valor mensal (`Salario`) e por extenso (`salario por extenso`).
4. **Data de vigência** — início do contrato (atualiza `Data`/`DD`/`Mês`).
5. **Dados da PJ e da pessoa** — `Razão social`, `CNPJ`, `Endereço Completo`,
   `Cidade`, `UF`, `Nº CEP`, `Nome Completo da Pessoas`, `Estado Civil`,
   `Nº do RG`, `Nº do CPF`.

Tipo de contrato: full-time por padrão (o template atual). Se não estiver claro
qual template usar, pergunte — nunca chute.

## 3. Monte os dados
Regras:
- **Cargo → conteúdo**: copie `Objeto`, `Área` e `Serviços` do `roles[<cargo>]`
  do config para os dados. `Serviços` é uma lista (a cláusula tem `{{*Serviços}}`,
  que vira um bullet por item).
- **Ano SEMPRE atual**: `AAAA` = `date +%Y` (ano corrente), sempre.
- **Data/DD/Mês**: da data de vigência informada; se não houver, use hoje.
  `Data`=dd/mm/aaaa, `DD`=dia, `Mês`=mês por extenso pt-BR (ex.: agosto).
- **Chaves espelhadas**: `RAZAO SOCIAL` = `Razão social` em MAIÚSCULAS.
- **CPF/CNPJ**: confira dígitos. Faltou campo obrigatório? **Pergunte** — nunca
  invente dados. Guarde a `modalidade` para o registro/checklist.

## 4. Obtenha o template
O template fica embarcado no plugin. Copie-o para um diretório temporário:
```
TMP=$(mktemp -d)
cp "${CLAUDE_PLUGIN_ROOT}/<template_path do tipo>" "$TMP/modelo.docx"
```
Se o tipo escolhido não tiver `template_path` no plugin mas tiver
`template_file_id`, baixe do Drive com `mcp__Google_Drive__download_file_content`
e decodifique o base64 para `$TMP/modelo.docx`.

## 5. Descubra os placeholders e cláusulas do template
```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fill_contract.py" --list --template "$TMP/modelo.docx"
```
O retorno tem `fields` (campos `{{CAMPO}}`) e `sections` (cláusulas
condicionais `{{#SECAO}}...{{/SECAO}}`).

- **Campos**: mapeie os dados coletados para as chaves EXATAS do template. Se
  houver campo sem valor, **pergunte ao usuário** — não deixe `{{...}}` cru.
- **Cláusulas condicionais** (ex.: `PLANO_SAUDE`): decida por cada uma se entra
  no contrato. No JSON de dados, passe a chave da seção como `true`/`false`.
  - Se a pessoa **tem** direito à cláusula, marque `true` **e** peça/preencha os
    campos internos dela (ex.: `PLANO_OPERADORA`, `PLANO_COMODIDADE`). Se o
    usuário disse "tem plano de saúde" mas não deu a operadora, **pergunte**.
  - Se **não tem**, marque `false` → o bloco é removido inteiro do contrato.

## 6. Preencha o contrato
Monte um JSON `dados.json` com o mapeamento chave→valor e rode:
```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fill_contract.py" \
  --template "$TMP/modelo.docx" --out "$TMP/contrato.docx" --data @"$TMP/dados.json"
```
Confira o relatório: se `unfilled` não estiver vazio, resolva antes de subir.

## 7. Suba para o Drive como Google Doc editável
Gere o título com o `filename_pattern` do tipo, substituindo os `{{campos}}` do
padrão pelos valores (ex.: `{{Nome Completo da Pessoas}}` e `{{Data}}`). Leia o
docx preenchido em base64 (`base64 -w0 "$TMP/contrato.docx"`)
e crie o arquivo:
- `mcp__Google_Drive__create_file` com:
  - `title`: o título gerado
  - `parentId`: `destination_folder_id`
  - `base64Content`: o base64 do contrato preenchido
  - `contentMimeType`: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
  - `disableConversionToGoogleType`: `false` (converte o .docx em Google Doc editável)

## 8. Reporte
Devolva ao usuário o **link (viewUrl)** do Google Doc criado, o tipo de
contrato, e um resumo dos campos preenchidos. Se algum placeholder ficou sem
valor, avise explicitamente.

Nunca escreva arquivos dentro da pasta do plugin; use sempre `$TMP`. Limpe o
temporário ao final (`rm -rf "$TMP"`).
