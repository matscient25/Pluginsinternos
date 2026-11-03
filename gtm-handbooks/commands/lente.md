---
description: Monta a lente da metodologia escolhida (elementos, escala 0-3, perguntas, mapa elemento por etapa do CRM)
argument-hint: "[metodologia] (opcional, padrão: a do ESTADO.md)"
---

Metodologia: `$ARGUMENTS`

Delegue ao agente **metodologista**, que segue `${CLAUDE_PLUGIN_ROOT}/skills/lentes-metodologia/SKILL.md` e grava `02-lente/lente.md`.

Ao final: mostre a tabela do mapa elemento × etapa e as 3 perguntas para o validador da empresa. Atualize o `ESTADO.md`. Próximo comando: `/analise`.
