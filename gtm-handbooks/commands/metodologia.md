---
description: Monta a metodologia escolhida (elementos, escala 0-3, perguntas, mapa elemento por etapa do CRM)
argument-hint: "[metodologia] (opcional, padrão: a do ESTADO.md)"
---

Metodologia: `$ARGUMENTS`

Delegue ao agente **metodologista**, que segue `${CLAUDE_PLUGIN_ROOT}/skills/metodologias/SKILL.md` e grava `02-metodologia/metodologia.md`.

Ao final: mostre a tabela do mapa elemento × etapa e as 3 perguntas para o validador da empresa. Atualize o `ESTADO.md`. Próximo comando: `/analise`.
