---
description: Inicia/toca o processo de contratação de uma pessoa (checklist completo + contrato)
argument-hint: "[full-time|freelancer] nome e dados da pessoa"
allowed-tools: Bash, Read, Write, Task, mcp__Google_Drive__download_file_content, mcp__Google_Drive__create_file, mcp__Google_Drive__get_file_metadata, mcp__Google_Drive__search_files
---

Conduza o processo de contratação de uma nova pessoa. Argumentos: `$ARGUMENTS`

Delegue ao agente **coordenador-contratacao**, que segue o checklist do time:

1. **Aluguel do Notebook**
2. **Assinatura do Contrato** (gera o contrato preenchido — via `redator-contrato`)
3. **Criação do e-mail**
4. **Data de início definida**
5. **Envio do Pré-onboarding**

O coordenador deve:
- Criar/atualizar o checklist da pessoa a partir de
  `${CLAUDE_PLUGIN_ROOT}/templates/checklist_contratacao.md`.
- Identificar o que já está resolvido e perguntar objetivamente pelos pendentes.
- Gerar o contrato (tipo correto) e registrar o link no item 2.
- Preparar o pré-onboarding e confirmar a data de início.
- Ao final, mostrar o **status dos 5 itens** (feito/pendente + próxima ação e
  responsável) e os links (contrato + checklist).

Se `destination_folder_id` no `config.json` ainda não estiver preenchido, peça o
link/ID da pasta de destino do Drive antes de gerar arquivos.
