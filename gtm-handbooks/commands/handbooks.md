---
description: Porta de entrada do GTM Handbooks & Skills Kit - mostra o estado do projeto e roda o próximo passo da jornada
argument-hint: "[empresa] (opcional)"
---

Projeto: `$ARGUMENTS`

Delegue ao agente **maestro**.

1. Se não existir nenhuma pasta `handbooks/<empresa>/`, apresente o kit em 6 linhas (tese Declarado × Observado × Medido, os 7 passos, os 9 agentes) e ofereça duas opções: `/iniciar` (empresa real) ou `/demo` (exemplo ACME com Challenger).
2. Se existir, o maestro lê o `ESTADO.md`, mostra a tabela da jornada com status e gates, e executa o próximo passo pendente (ou lista o que falta se o passo depende do usuário).
3. Termine sempre com o próximo comando sugerido.
