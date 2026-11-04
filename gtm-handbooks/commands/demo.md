---
description: Roda a jornada completa no kit de exemplo (ACME x TechScale, Challenger, dados fictícios) para aprender ou demonstrar ao vivo
argument-hint: "[rapido | completo] (padrão: rapido)"
---

Modo: `$ARGUMENTS`

Kit: `${CLAUDE_PLUGIN_ROOT}/exemplo/acme/` (leia `${CLAUDE_PLUGIN_ROOT}/exemplo/README.md`). Gabarito: `exemplo/acme/saida-esperada/`.

1. Copie `${CLAUDE_PLUGIN_ROOT}/exemplo/acme/` (sem `saida-esperada/` e sem `ESTADO.md`) para `handbooks/acme-demo/` na pasta de trabalho. Crie um `ESTADO.md` novo a partir do template com: metodologia Challenger; processos Qualificação, Diagnóstico, Proposta, Negociação/Contrato, Handoff CS; etapas `qualificacao, diagnostico, proposta, followup, contrato`.
2. Anuncie cada passo antes de rodar, em 1 linha ("Passo 2 · Metodologia: o metodologista vai transformar o Challenger em critério de análise").
3. **rapido** (para aula, ~10 min): Coleta (validar) → Metodologia → Análise só do funil + 2 fichas (TechScale Diagnóstico e um perdido) + síntese curta → Handbook do Diagnóstico → Skill `acme-diagnostico` → Validação do handbook.
   **completo:** todos os processos e todas as transcrições.
4. A cada passo, mostre o artefato gerado (trecho curto) e compare com o gabarito em `saida-esperada/`: o que bateu, o que ficou diferente.
5. Se algum passo falhar ou demorar, mostre o arquivo correspondente do gabarito e siga.
