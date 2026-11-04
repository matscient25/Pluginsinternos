---
description: Processa transcrições contra a rubrica da etapa do handbook e devolve coaching (nota por critério, veredito de avanço, momentos a melhorar com a pergunta do handbook) e o painel do gestor
argument-hint: "<transcrição(ões) ou pasta> [etapa] | painel | calibrar <etapa>"
---

Entrada: `$ARGUMENTS`

Siga `${CLAUDE_PLUGIN_ROOT}/skills/coaching-por-rubrica/SKILL.md`. Requer handbook da etapa com a seção 11 (rubrica).

- **transcrição(ões):** delegue ao **analista-conversas** em modo coaching (um agente por lote de 4 a 6, em paralelo). Saída em `07-coaching/`. Se houver conector de gravação (Fathom, Fireflies), ofereça buscar as reuniões da semana.
- **painel:** consolide os coachings em `07-coaching/painel.md` (média por critério e por vendedor, onde treinar, sinais para revisar o handbook).
- **calibrar <etapa>:** pontue as reuniões ganhas e perdidas da etapa com a rubrica e diga se ela separa ganhos de perdidos; se não, proponha o ajuste do critério.

Ao final, mostre para cada reunião: nota, veredito de avanço e o primeiro momento de coaching.
