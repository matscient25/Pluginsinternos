---
description: Revisa handbooks e skills com checklists binários e testes e emite o veredito Pronto, Ajustar ou Refazer
argument-hint: "[handbook ou skill] (opcional, padrão: tudo)"
---

Escopo: `$ARGUMENTS`

Delegue ao **revisor**, que segue `${CLAUDE_PLUGIN_ROOT}/skills/qualidade-handbooks/SKILL.md` e grava `06-validacao/relatorio.md`.

Ao final, mostre a tabela de vereditos e os 5 ajustes mais importantes. Se houver Ajustar ou Refazer, o maestro devolve ao redator ou ao arquiteto. Atualize o `ESTADO.md`.
