> Dados fictícios para treinamento. Transcrição adaptada do material "Transcrições Challenger Sale" (Officer Hour SCIENT); marcações de tempo aproximadas, inseridas para a aula.

# TechScale S/A · 2026-08-10 · Diagnóstico

| Campo | Valor |
|---|---|
| Conta | TechScale S/A (deal VK-0101) |
| Etapa do funil | Diagnóstico |
| Resultado do negócio | Ganho (fechado em 2026-09-11) |
| Dono do negócio | Lucas Andrade (AE) |
| Participantes | Lucas Andrade (AE, Vektor) · Bruno Maia (Head de Engenharia, TechScale) · Rafael Torres (CTO, TechScale) |
| Duração | 95 min |
| Pauta do convite | Mapear causas raiz, quantificar o impacto de negócio, criar urgência real |
| Gravado por | Gravador de reuniões (export em texto) |

---

[01:00] **Lucas:** Obrigado pelos dois terem dedicado esse tempo. Antes de começar, quero alinhar: não sou arquiteto de software, então não vou entrar em decisões técnicas. Meu objetivo aqui é entender o impacto de negócio dos problemas que o Rafael descreveu. Bruno, você pode me dar uma visão de como os squads de vocês estão organizados hoje?

[06:04] **Bruno:** Temos oito squads. Três são core — mexem no produto principal. Dois são de plataforma — infraestrutura, dados, segurança. E três são de novos produtos que lançamos no último ano. O problema é que os squads de novos produtos dependem de mudanças nos squads core para praticamente tudo. Qualquer integração nova vai para uma fila de backlog no squad core e fica lá por semanas.

[12:04] **Lucas:** Quanto tempo, em média, uma demanda dos squads de novos produtos fica parada esperando o squad core?

[13:42] **Bruno:** Depende da complexidade. Mudança simples de API, talvez duas semanas. Funcionalidade com impacto em banco de dados pode levar dois meses.

[15:41] **Lucas:** Quantas demandas desse tipo vocês têm por mês, cruzando os três squads de novos produtos?

[17:08] **Bruno:** Umas quinze a vinte por mês. Mas muitas ficam represadas e se acumulam.

[18:25] **Lucas:** Rafael, você mencionou na última conversa que perdeu um contrato de expansão por atraso em integração. Qual era o valor daquele contrato?

[20:30] **Rafael:** Era uma expansão de R$480 mil anuais recorrentes. E tenho mais dois contratos similares em risco hoje por funcionalidades atrasadas.

[22:24] **Lucas:** Então só nesses três contratos o risco de receita recorrente é de pelo menos R$1,4 milhão por ano. Isso sem contar oportunidades que nem chegam ao pipeline porque o produto ainda não tem certas funcionalidades. Correto?

[25:46] **Rafael:** Correto. E tem o custo de retrabalho interno, que é mais difícil de quantificar.

[27:07] **Lucas:** Vamos tentar. Bruno, o que acontece quando uma feature volta para refatoração depois de já ter sido entregue em produção?

[29:02] **Bruno:** O engenheiro que desenvolveu precisa retomar o contexto — o que levou uma semana para construir agora leva mais dois ou três dias só para entender o que estava feito. Aí tem o bug fix, o QA de regressão, o deploy. E interrompe o sprint atual.

[33:17] **Lucas:** Com que frequência isso acontece por sprint?

[34:01] **Bruno:** Duas a três vezes por sprint nos squads core. Já normalizamos tanto que o pessoal nem reclama mais. É considerado parte do processo.

[36:12] **Lucas:** Isso é um sinal muito importante, Bruno. Quando o retrabalho se torna "parte do processo", ele deixa de ser visível como custo. Mas continua existindo. Se você estimasse em capacidade o que isso consome nos squads core por mês, chegaria a quanto?

[40:06] **Bruno:** Sendo conservador... uns quarenta a cinquenta pontos de story por mês só em retrabalho e bugs. Em três squads core, é o equivalente a manter um squad inteiro só corrigindo o que foi feito antes.

[43:22] **Lucas:** Um squad inteiro. Vou deixar isso no ar por um segundo. Rafael, qual é o custo mensal de manter um squad de oito pessoas na TechScale, com encargos e overhead?

[46:11] **Rafael:** Entre R$280 e R$320 mil por mês.

[46:54] **Lucas:** Então o retrabalho invisível está consumindo o equivalente a R$3 a R$3,8 milhões por ano em capacidade de engenharia — fora a receita perdida por atraso. E a solução que vocês têm considerado até agora é contratar mais.

[50:26] **Rafael:** *(pausa longa)* Quando você coloca assim... sim. A gente está adicionando capacidade num sistema que está destruindo capacidade. É um buraco sem fundo.

[52:37] **Lucas:** Exato. E aqui está o ponto que considero mais crítico: isso não é um problema técnico. É um problema de decisão gerencial acumulada. Cada vez que a pressão de entregar rápido fez a engenharia cortar caminho, um pouco de dívida técnica foi acumulado. Agora essa conta chegou — com juros. A pergunta que importa é: vocês querem continuar pagando os juros ou querem quitar o principal?

[58:42] **Rafael:** A gente quer quitar. Mas a pressão do roadmap não para para a gente resolver isso internamente. Toda vez que a gente tenta parar para refatorar, o negócio puxa pelo backlog de features.

[61:47] **Lucas:** Isso tem um nome: é o paradoxo da capacidade bloqueada. Você não consegue resolver o problema porque está ocupado demais com o problema. Trabalhamos com uma empresa de fintech de porte similar há dezoito meses. O CTO de lá descreveu exatamente essa dinâmica: "Toda sexta-feira prometo para mim mesmo que na semana seguinte a gente para para refatorar o core. Na segunda de manhã chega um incidente e a gente cancela." Isso ressoa?

[68:30] **Bruno:** É literalmente a minha vida. Tenho esse bloqueio no meu calendário há quatro semanas e já cancelei três vezes.

[70:19] **Lucas:** Então o que vocês precisam não é de mais engenheiros — é de capacidade protegida. Um time que não compete com o backlog interno de vocês pelo tempo dos sêniores. Bruno, me ajuda a mapear: se vocês tivessem um squad externo dedicado exclusivamente a destravar as integrações dos novos produtos, o que mudaria para os squads core?

[75:34] **Bruno:** Os sêniores do squad core parariam de ser bloqueados por demandas de integração. Ficaria mais fácil focar nos módulos críticos que só eles entendem. Mas alguém precisaria garantir que esse squad externo não criasse mais dívida técnica. É o que me preocupa.

[79:28] **Lucas:** Faz todo sentido essa preocupação. Voltamos a ela na proposta. Rafael, última pergunta para fechar o diagnóstico: se você descobrisse que o problema tem solução estruturada, qual é a sua régua de sucesso daqui a seis meses? O que precisaria ter mudado para você dizer que valeu o investimento?

[84:01] **Rafael:** Quero conseguir entregar o roadmap com pelo menos oitenta por cento de aderência. E quero que o time core pare de apagar incêndio e volte a construir produto de verdade.

[86:49] **Lucas:** Anotei. Vou usar isso como critério de sucesso na proposta. Até quinta-feira da semana que vem apresento a proposta com arquitetura de solução e projeção de impacto. Quero que você, o Bruno e a Fernanda — CPO de vocês — estejam no convite. Ela precisa estar alinhada com o que vamos propor.

[91:38] **Rafael:** A Fernanda já perguntou quando ia ter uma proposta. Mando o convite ainda hoje.
