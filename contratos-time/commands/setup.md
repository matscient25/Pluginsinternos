---
description: Configura os templates e a pasta de destino do plugin de contratos (preenche config.json)
argument-hint: "[links do Drive dos 2 templates e da pasta, se tiver]"
allowed-tools: Bash, Read, Edit, mcp__Google_Drive__search_files, mcp__Google_Drive__get_file_metadata, mcp__Google_Drive__download_file_content
---

Ajude o usuário a configurar `${CLAUDE_PLUGIN_ROOT}/config.json`.
Contexto do usuário: `$ARGUMENTS`

## 1. Descubra os IDs
Um ID de arquivo é o trecho após `/d/` na URL; de pasta, após `/folders/`.
- Se o usuário colou links, extraia os IDs deles.
- Se não, use `mcp__Google_Drive__search_files` para localizar os dois
  templates (Full time e Freelancer) e a pasta de destino. Confirme cada
  achado com o usuário por título antes de gravar (não assuma).

## 2. Valide os templates
Para cada template, verifique com `get_file_metadata` que é um `.docx`
(`application/vnd.openxmlformats-officedocument.wordprocessingml.document`)
ou um Google Doc.
- Se for **Google Doc**, avise que ele será exportado como .docx no momento
  de gerar (o plugin lida com isso via `exportMimeType`).
- Baixe cada template e liste os placeholders reais para o usuário conferir:
  ```
  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fill_contract.py" --list --template <arquivo.docx>
  ```
  Mostre a lista e confirme que os `required_fields` do config batem com o que
  o template realmente usa. Ajuste `required_fields` se necessário.

## 3. Grave o config.json
Use `Edit` para substituir os placeholders `COLE_AQUI...` pelos IDs reais em
`${CLAUDE_PLUGIN_ROOT}/config.json`. Preencha `template_file_id` de cada tipo,
o `destination_folder_id`, e `template_name_hint` com o título do arquivo (útil
como fallback de busca).

## 4. Confirme
Mostre um resumo: qual arquivo é o template de cada tipo, a pasta de destino,
e os placeholders detectados em cada template. Diga que agora é só usar
`/contratos-time:gerar-contrato`.
