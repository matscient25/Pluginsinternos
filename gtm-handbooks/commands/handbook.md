---
description: Escreve o handbook de um processo no modelo padrão (Markdown + HTML) a partir da análise
argument-hint: "<processo> (ex.: diagnostico) ou 'todos'"
---

Processo: `$ARGUMENTS`

Requer gate da Análise ✅. Delegue ao **redator-handbook**, que segue `${CLAUDE_PLUGIN_ROOT}/skills/modelo-handbook/SKILL.md` e o modelo `${CLAUDE_PLUGIN_ROOT}/templates/handbook.md`.

Com `todos`, dispare um redator por processo do escopo, em paralelo.

Ao final, mostre a manchete e os KPIs de cada handbook, o resultado do checklist e as lacunas. Ofereça abrir o `.html`. Atualize o `ESTADO.md`. Próximo comando: `/gerar-skills`.
