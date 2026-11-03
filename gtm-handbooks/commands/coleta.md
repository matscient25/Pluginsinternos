---
description: Gera o data request (funil, transcrições, documentos e PPTs, entrevistas) ou valida o que já chegou e fecha o gate da Coleta
argument-hint: "[pedido | validar]"
---

Modo: `$ARGUMENTS` (se vazio: `pedido` quando `01-coleta/` estiver vazia, `validar` quando houver arquivos).

Delegue ao agente **coletor**, que segue `${CLAUDE_PLUGIN_ROOT}/skills/data-request/SKILL.md`.

- **pedido:** gera `01-coleta/data-request.md` e o roteiro de entrevistas; mostra o texto pronto para o usuário enviar.
- **validar:** escreve `01-coleta/inventario.md` com cobertura por etapa e o checklist do gate.

Ao final, atualize o `ESTADO.md` (passo 1, gate, lacunas com dono) e diga o próximo comando (`/lente`).
