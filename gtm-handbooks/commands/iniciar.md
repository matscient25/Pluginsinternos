---
description: Cria o projeto de handbooks e skills de uma empresa - escopo, processos, etapas do CRM, metodologia e aprovador
argument-hint: "<nome da empresa>"
---

Empresa: `$ARGUMENTS`

Conduza o **Escopo (passo 0)** com o agente **maestro**. Leia `${CLAUDE_PLUGIN_ROOT}/skills/metodo-handbooks/SKILL.md`.

Pergunte de forma objetiva (pode ser numa única mensagem com as 6 perguntas):
1. O que a empresa vende e para quem (1 a 2 linhas)?
2. Quais etapas do funil existem no CRM (nomes exatos) e qual CRM?
3. Quais processos entram nos handbooks (1 a 5)? Sugira começar pela etapa com maior vazamento, se o usuário souber.
4. Qual metodologia o time usa ou treinou (Challenger, MEDDPICC, SPIN, SPICED, BANT, GPCTBA, própria, nenhuma)? Se nenhuma, recomende com a tabela de `lentes-metodologia`.
5. Quem aprova os handbooks?
6. Que conectores estão disponíveis (CRM, gravador de reuniões, Drive)?

Depois:
- Crie `handbooks/<empresa-slug>/` com as subpastas do método e `01-coleta/{A-numeros,B-conversas,C-documentos,D-pessoas}`.
- Copie `${CLAUDE_PLUGIN_ROOT}/templates/ESTADO.md` e preencha Escopo e Decisões; marque o passo 0 como ✅.
- Se houver git, commit "handbooks: escopo <empresa>".
- Próximo comando: `/coleta`.
