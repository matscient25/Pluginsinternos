---
description: Roda as três análises (conversas, funil, documentos) em paralelo e escreve a síntese declarado x observado x medido
argument-hint: "[conversas | funil | documentos | sintese] (opcional, padrão: tudo)"
---

Escopo: `$ARGUMENTS`

Requer gate da Coleta e da Metodologia ✅ no `ESTADO.md`. Siga `${CLAUDE_PLUGIN_ROOT}/skills/analise-triangulada/SKILL.md`.

Dispare **em paralelo**:
- **analista-conversas**: um agente por lote de 4 a 6 transcrições de `01-coleta/B-conversas/` → `03-analise/fichas/`
- **analista-funil**: `funil.py` sobre `01-coleta/A-numeros/` → `03-analise/funil.md`
- **analista-documentos**: `01-coleta/C-documentos/` → `03-analise/declarado.md`

Quando os três terminarem, passe ao **redator-handbook** os JSONs e padrões dos lotes para escrever `03-analise/sintese.md`.

Ao final, mostre: a manchete da síntese, a tabela de divergências e a ordem recomendada dos handbooks. Atualize o `ESTADO.md`. Próximo comando: `/handbook <processo>`.
