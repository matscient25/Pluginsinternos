---
name: modelo-handbook
description: Modelo padrão de handbook operacional de processo de GTM (14 seções - manchete-conclusão com até 4 KPIs e lacunas no topo, identificação, porquê, hand-off de entrada, passo a passo com critério binário, sinais, objeções, hand-off de saída, métricas, red flags com severidade, declarado x observado x medido, rubrica da etapa para coaching, skills e aprovação) e as regras para escrevê-lo a partir da análise triangulada. Use ao escrever, revisar ou converter para HTML um handbook, playbook ou manual de processo comercial (qualificação, discovery, diagnóstico, proposta, negociação, contrato, handoff, onboarding, expansão).
---

# Modelo padrão de handbook

Modelo em branco: `${CLAUDE_PLUGIN_ROOT}/templates/handbook.md`. Versão para leitura: `${CLAUDE_PLUGIN_ROOT}/templates/handbook.html`.
Exemplo preenchido: `${CLAUDE_PLUGIN_ROOT}/exemplo/vektor/saida-esperada/04-handbooks/diagnostico.md`.

## Anatomia (e por quê)

| # | Seção | Regra | Por quê |
|---|---|---|---|
| 0 | **Em uma frase** | Manchete que é a **conclusão** (não "Handbook de Diagnóstico") + até 4 KPIs com linha de contexto + o que significa e o que não significa + lacunas | Quem abre entende em 10 segundos o que importa e o que ainda não se sabe |
| 1 | Identificação | Entra de, sai para, quem participa dos dois lados, duração | Posiciona a etapa na jornada |
| 2 | Por que existe | Ganho do cliente, ganho da empresa, elemento da metodologia | O vendedor entende o objetivo, não só a tarefa |
| 3 | Hand-off de entrada | O que recebe, onde está, critério de entrada binário | Corta negócio mal qualificado na porta |
| 4 | Passo a passo | 3 a 5 passos: foco, ações com verbo e local, perguntas literais com fonte, cuidado, DRI, SLA, critério de saída | É o coração; vira a skill de execução |
| 5 | Sinais | Frases reais de avanço e de risco | Ensina a ler o cliente |
| 6 | Objeções | Objeção literal, princípio, resposta que funcionou, fonte | Resposta testada, não teórica |
| 7 | Hand-off de saída | Entregável, onde, o que a próxima etapa confere, critério de saída | O mesmo critério que move a etapa no CRM |
| 8 | Métricas | Linha de base medida, meta, fórmula, fonte, frequência, dono | Torna o handbook gerenciável |
| 9 | Red flags | Como detectar, severidade (🔴 Crítico, 🟡 Atenção, 🟢 Acompanhar), ação, dono + escalação | Só entra red flag com ação |
| 10 | Declarado × Observado × Medido | Divergências e a decisão tomada | Mostra por que o handbook diz o que diz |
| 11 | **Rubrica da etapa** | Um critério por passo, nota 0–3 (0 = como os perdidos fazem, 3 = como os ganhos fazem), regra de avanço igual ao critério de saída, calibração | Transforma o handbook em régua de coaching de cada reunião (skill `coaching-por-rubrica`) |
| 12 | Skills | Quais skills executam o handbook | Liga documento a execução |
| 13 | Aprovação | Quem preencheu, revisou, aprovou; versão; próxima revisão | Dono e validade |

## Como escrever
1. Ler `03-analise/sintese.md`, as fichas das etapas cobertas, `funil.md`, `declarado.md` e `02-lente/lente.md`.
2. Escrever a seção 0 **por último**, depois de ter o conteúdo.
3. Passo a passo: comece pelos comportamentos que aparecem nos **ganhos** e não nos perdidos. Cada passo precisa de pelo menos uma pergunta literal com fonte; se não houver, `[PRECISA DE DADO]`.
4. Critério de saída: use o mapa elemento × etapa da lente (elementos com nota ≥ 2). Escreva como pergunta de sim ou não.
5. KPIs e linha de base: só do `funil.md`. Meta: proposta pelo gestor ou marcada `[HIPÓTESE]`.
6. Red flags: derive de padrões dos perdidos e dos motivos de perda do funil.
7. Seção 11 (rubrica): siga `${CLAUDE_PLUGIN_ROOT}/skills/coaching-por-rubrica/SKILL.md` §1. Calibre com as fichas de ganhos e perdidos da etapa.
8. Seção 10: copie da síntese as divergências que afetam esta etapa e diga qual versão o handbook adotou.
9. Gerar o `.html`: copiar `templates/handbook.html`, substituir o conteúdo do `<main>` pelas seções convertidas (tabelas como `<table>`, critérios em `.criterio`, cuidados em `.cuidado`, tags em `<span class="tag">`). Manter o `.md` como fonte.

## Regras de escrita
- Frases curtas. Verbo no início das ações ("Registrar", "Perguntar", "Enviar").
- Toda ação diz **onde** acontece ou fica registrada.
- Checklists com até 15 itens. Handbook com 3 a 5 passos. Detalhe extra vai para anexo.
- Vocabulário da empresa (nomes das etapas e campos do CRM exatamente como estão).
- Nomes de clientes nas citações: manter no handbook interno; anonimizar ("cliente de tecnologia, 3 mil funcionários") em material de treinamento externo.
- Sem jargão da metodologia sem explicação na primeira vez.

## Erros que mais aparecem
- Manchete genérica ("Visão geral do processo de diagnóstico").
- Perguntas inventadas pelo analista, sem fonte.
- Critério de saída vago ("cliente engajado").
- Documentar o processo oficial quando as conversas mostram outro.
- Mais de 4 KPIs no topo.
- Red flag sem ação ou sem dono.
