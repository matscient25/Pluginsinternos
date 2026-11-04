---
name: qualidade-handbooks
description: Checklists binários e testes para aprovar handbooks e skills de GTM antes de usar com o time - checklist do handbook (evidência, critérios binários, perguntas com fonte, red flags com ação), checklist de skill (frontmatter, gatilhos, modos, confirmação antes de gravar), testes de gatilho e de execução, teste do vendedor novo e veredito Pronto / Ajustar / Refazer. Use ao revisar, validar ou aprovar um handbook, playbook ou skill comercial, ou quando perguntarem "está pronto?".
---

# Qualidade de handbooks e skills

Veredito final por handbook: **Pronto**, **Ajustar** ou **Refazer**. Registrar em `06-validacao/relatorio.md`.

## Checklist do handbook (todos sim = Pronto)
**Evidência**
- [ ] Toda afirmação relevante tem tag de evidência
- [ ] KPIs e linhas de base vêm do `funil.md` (`[MEDIDO]`)
- [ ] Perguntas, sinais e objeções são frases reais com fonte (`[OBSERVADO]`)
- [ ] Lacunas aparecem no topo, com responsável e data
- [ ] Divergências declarado × observado × medido registradas com decisão

**Estrutura**
- [ ] Manchete é uma conclusão, não um título
- [ ] No máximo 4 KPIs no topo
- [ ] 3 a 5 passos; checklists com até 15 itens
- [ ] Critério de entrada e de saída binários (respondem sim ou não)
- [ ] O critério de saída é o mesmo que move o negócio de etapa no CRM
- [ ] Toda ação começa com verbo e diz onde acontece ou fica registrada
- [ ] Todo passo tem DRI e SLA
- [ ] Toda red flag tem como detectar, severidade, ação e dono
- [ ] Rubrica (seção 11) com um critério por passo, descrições de 0 e 3 observáveis e regra de avanço igual ao critério de saída
- [ ] Rubrica calibrada: separa reuniões ganhas de perdidas da etapa

**Uso**
- [ ] Nomes de etapas e campos iguais aos do CRM
- [ ] Vocabulário do time, jargão explicado na primeira vez
- [ ] Revisado por um vendedor sênior (nome e data)
- [ ] Tem dono, versão e data da próxima revisão

## Teste do vendedor novo
Entregue o handbook a alguém que não participou do projeto e peça para preparar uma reunião daquela etapa.

| Resultado | Veredito |
|---|---|
| Prepara e conduz sem precisar perguntar nada | **Pronto** |
| Entende, mas precisa "adaptar ao estilo" ou pergunta o que fazer em algum passo | **Ajustar**: o passo está genérico; volte às fichas e traga comportamento e perguntas reais |
| Não consegue usar sem treinamento | **Refazer**: o handbook documentou teoria; volte às transcrições |

## Checklist de skill
- [ ] `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/validar_skill.py <pasta>` sem erro
- [ ] Descrição diz o que faz, quando usar e tem gatilhos com as palavras do time
- [ ] Passos numerados; o crítico está no topo
- [ ] Modos Preparar, Conduzir, Registrar e Revisar (skills de etapa)
- [ ] Perguntas e objeções vêm de `references/` copiadas do handbook
- [ ] Mostra e pede confirmação antes de gravar em qualquer sistema
- [ ] Critério de saída idêntico ao do handbook
- [ ] `testes.md` com 3 frases que acionam, 2 que não acionam e 2 casos de execução

## Teste de gatilho
Em uma conversa nova, com a skill instalada, digite as 5 frases do `testes.md`. Registre:

| Frase | Deveria acionar? | Acionou? | Ajuste |
|---|---|---|---|

Meta: 5 de 5. Se não acionar, acrescente o termo na descrição. Se acionar indevidamente, especifique a etapa e diga quando não usar.

## Teste de execução
Rode os 2 casos do `testes.md` (de preferência com uma transcrição real que **não** foi usada para escrever o handbook). Compare a saída com o handbook: perguntas, critério de saída e campos do CRM batem?

## Relatório (`06-validacao/relatorio.md`)
| Artefato | Checklist (sim/total) | Teste vendedor novo | Gatilho | Execução | Veredito | Ajustes |
|---|---|---|---|---|---|---|
