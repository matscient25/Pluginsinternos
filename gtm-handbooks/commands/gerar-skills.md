---
description: Gera as skills do time a partir dos handbooks (mestre, contexto, metodologia, uma por etapa, avaliar reunião), valida e empacota em .skill
argument-hint: "[processo] (opcional, padrão: todos os handbooks prontos)"
---

Escopo: `$ARGUMENTS`

Requer ao menos um handbook com checklist 100%. Delegue ao **arquiteto-skills**, que segue `${CLAUDE_PLUGIN_ROOT}/skills/fabrica-de-skills/SKILL.md`.

Ao final, mostre: árvore de `05-skills/`, a descrição (frontmatter) de cada skill, a saída do `validar_skill.py` e os arquivos `.skill` gerados, com a instrução de instalação. Atualize o `ESTADO.md`. Próximo comando: `/validar`.
