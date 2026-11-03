> Dados fictícios para treinamento. Gabarito do passo 4 (Handbook) da demo.

# Handbook · Diagnóstico · Consultoria Vektor

| | |
|---|---|
| **Processo** | Diagnóstico (reunião de causa raiz e custo do problema) |
| **Etapas do funil cobertas** | Diagnóstico → Proposta (nomes exatos do CRM) |
| **Metodologia** | Challenger Sale (lente v1.0) |
| **Motion** | High touch · ticket R$ 80 mil a R$ 600 mil/mês · ciclo mediano 48 dias |
| **Dono do handbook** | Gestor comercial |
| **Versão** | 1.0 · 2026-10-22 · próxima revisão 2027-04-22 |
| **Evidências usadas** | 2 transcrições de diagnóstico (1 ganho, 1 perdido) + 6 de outras etapas · funil nov/2025–out/2026 (122 negócios) · 4 documentos · 2 entrevistas |

---

## 0. Em uma frase

> **Diagnóstico que termina com o custo do problema em reais leva 81% dos negócios para a proposta e 80% das propostas ao ganho; sem esse número, 28% avançam.** `[MEDIDO: funil.md]`

| Diagnóstico → Proposta | Com custo quantificado | Proposta → Ganho | Perdas por preço/hora |
|---|---|---|---|
| **54%** | **81%** × 28% | **80%** × 25% | **80%** |
| menor conversão do funil (outras: 79–86%) | avançam para proposta, com × sem custo em R$ | com custo quantificado × pulando o diagnóstico | vêm de negócios que pularam o diagnóstico (12 de 15) |

**O que isto significa:** o Diagnóstico é a etapa que mais perde negócio e a que mais separa o top performer dos demais. O que decide não é fazer a reunião: é sair dela com um número em reais, construído com dados do cliente e confirmado por ele.

**O que isto não significa:** não prova que o número *causa* o ganho (negócios com custo quantificado podem ser também os de dor maior). O padrão vem de 122 negócios de um ano e de transcrições de um único AE ganhador.

**Lacunas de dado:**
- `[PRECISA DE DADO]` Campo `custo_do_problema` (R$/ano) no CRM · admin do CRM · antes da validação.
- `[PRECISA DE DADO]` Transcrição de diagnóstico ganho de outro AE · gestor comercial · 2026-11-15.

---

## 1. Identificação

| Atributo | Valor |
|---|---|
| Entra de | Qualificação |
| Sai para | Proposta |
| Quem participa (Vektor) | AE dono do negócio |
| Quem participa (cliente) | Decisor principal (CTO/VP/Head de Eng) **e** quem vive o problema no dia a dia (Head de Engenharia, Tech Lead) |
| Duração típica da etapa | 11 dias de mediana até a proposta `[MEDIDO: funil.md]` |
| Reuniões típicas | 1 reunião de 90 min `[OBSERVADO: TechScale R2]` |

## 2. Por que esta etapa existe

- **Para o cliente:** enxergar que o problema não é falta de gente e quanto ele custa por ano. Sai com um número que pode levar ao CEO e ao CFO.
- **Para a Vektor:** tirar a venda da comparação por preço/hora. Sem custo do problema, a única régua que sobra para o cliente é a hora do fornecedor `[OBSERVADO: Orbita 19:40]`.
- **Princípio da metodologia:** é a etapa do **Rational Drowning** (E3) e do **Tailor** (E6): quantificar o custo do problema com os dados do cliente e falar a língua de cada papel. O Reframe (E2) se aprofunda aqui; a solução ainda **não** aparece (*lead to, not lead with*).

## 3. Hand-off de entrada

**O que a Qualificação entrega:**
- [ ] Hipótese de dor validada pelo decisor ("mais gente, menos velocidade") · nota da reunião no CRM
- [ ] Diagnóstico agendado com quem vive o problema · convite no calendário
- [ ] Pauta enviada ao cliente com o que ele deve trazer · e-mail `[OBSERVADO: TechScale R1 40:48]`
- [ ] Impacto superficial citado pelo cliente (ex.: contrato perdido) · nota da reunião

**O que o AE confere antes de começar:**
- [ ] Pesquisa da conta: tamanho do time de engenharia, squads, produtos novos (LinkedIn, site)
- [ ] 3 a 5 hipóteses de causa para o perfil do cliente
- [ ] Perguntas separadas por papel (decisor × quem vive o problema)
- [ ] Um caso análogo de cliente parecido, contado como história

> ✅ **Critério de entrada:** reunião de diagnóstico marcada com o decisor **e** pelo menos uma pessoa que vive o problema, com pauta enviada.

## 4. Passo a passo

### 4.1 Abrir pelo impacto de negócio, não pela Vektor

**Foco:** deixar claro que a reunião é sobre o problema do cliente.
**Elemento da metodologia:** E1 Warmer

**Ações:**
- [ ] Declarar o objetivo da sessão (impacto de negócio, não arquitetura) e pedir o mapa dos times
- [ ] Retomar a hipótese validada na Qualificação
- [ ] Não abrir deck institucional nem cases

**Perguntas que funcionam:**
- "Bruno, você pode me dar uma visão de como os squads de vocês estão organizados hoje?" — `[OBSERVADO: TechScale R2 01:00]`

**Como fica uma boa execução:** "não sou arquiteto de software, então não vou entrar em decisões técnicas. Meu objetivo aqui é entender o impacto de negócio" — `[OBSERVADO: TechScale R2 01:00]`

> ⚠ **Cuidado:** abrir com "quem somos" faz o cliente pedir para parar e transforma a reunião em levantamento técnico `[OBSERVADO: Orbita 01:12–10:45]`.

| DRI | SLA | Critério de saída |
|---|---|---|
| AE | primeiros 10 min | Cliente descreveu a estrutura dos times e onde está o gargalo |

### 4.2 Medir a operação com quem vive o problema

**Foco:** transformar a dor em quantidades (tempo, volume, frequência).
**Elemento da metodologia:** E6 Tailor (linguagem do papel técnico) + E3

**Ações:**
- [ ] Fazer as perguntas de quantidade ao influenciador técnico, na língua dele (squad, sprint, fila)
- [ ] Anotar cada número com a frase do cliente
- [ ] Nomear o custo que virou rotina ("já normalizamos")

**Perguntas que funcionam:**
- "Quanto tempo, em média, uma demanda dos squads de novos produtos fica parada esperando o squad core?" — `[OBSERVADO: TechScale R2 12:04]`
- "Quantas demandas desse tipo vocês têm por mês?" — `[OBSERVADO: TechScale R2 15:41]`
- "Com que frequência isso acontece por sprint?" — `[OBSERVADO: TechScale R2 33:17]`
- "Se você estimasse em capacidade o que isso consome nos squads core por mês, chegaria a quanto?" — `[OBSERVADO: TechScale R2 36:12]`

**Como fica uma boa execução:** "Quando o retrabalho se torna 'parte do processo', ele deixa de ser visível como custo. Mas continua existindo." — `[OBSERVADO: TechScale R2 36:12]`

> ⚠ **Cuidado:** perguntas de inventário (stack, metodologia ágil, nº de engenheiros) não medem a dor `[OBSERVADO: Orbita 11:40–12:50]`.

| DRI | SLA | Critério de saída |
|---|---|---|
| AE | até 40 min de reunião | ≥ 3 números operacionais ditos pelo cliente (tempo, volume, frequência) |

### 4.3 Converter em reais com o decisor (custo do problema)

**Foco:** chegar ao custo anual do problema com os números do próprio cliente.
**Elemento da metodologia:** E3 Rational Drowning

**Ações:**
- [ ] Pedir ao decisor o custo unitário (custo mensal de um squad, valor do contrato perdido)
- [ ] Fazer a conta na frente do cliente e pedir confirmação
- [ ] Somar receita em risco + custo de capacidade desperdiçada
- [ ] Registrar o custo do problema (R$/ano) no CRM, campo `custo_do_problema` `[PRECISA DE DADO]` (hoje: nota)

**Perguntas que funcionam:**
- "Qual era o valor daquele contrato?" — `[OBSERVADO: TechScale R2 18:25]`
- "Qual é o custo mensal de manter um squad de oito pessoas na TechScale, com encargos e overhead?" — `[OBSERVADO: TechScale R2 43:22]`

**Como fica uma boa execução:** "Então o retrabalho invisível está consumindo o equivalente a R$3 a R$3,8 milhões por ano em capacidade de engenharia — fora a receita perdida por atraso." — `[OBSERVADO: TechScale R2 46:54]`

> ⚠ **Cuidado:** aceitar "custa, né" ou "a gente dá um jeito" como resposta. Sem número, o negócio avança 28% das vezes `[MEDIDO: funil.md]` `[OBSERVADO: Orbita 14:08, Nuvia 11:24]`.

| DRI | SLA | Critério de saída |
|---|---|---|
| AE | na própria reunião | Custo do problema em R$/ano dito pelo AE e confirmado pelo decisor |

### 4.4 Reenquadrar e fazer o cliente se reconhecer

**Foco:** mudar a leitura do problema e criar identificação.
**Elemento da metodologia:** E2 Reframe + E4 Emotional Impact

**Ações:**
- [ ] Apresentar o reframe da Vektor: não é técnico, é decisão gerencial acumulada
- [ ] Contar um caso análogo como história (cliente parecido, mesma dinâmica)
- [ ] Descrever o novo jeito de operar sem citar oferta ("capacidade protegida")

**Perguntas que funcionam:**
- "Vocês querem continuar pagando os juros ou querem quitar o principal?" — `[OBSERVADO: TechScale R2 52:37]`
- "Isso ressoa?" (após o caso análogo) — `[OBSERVADO: TechScale R2 61:47]`

**Como fica uma boa execução:** "isso não é um problema técnico. É um problema de decisão gerencial acumulada." — `[OBSERVADO: TechScale R2 52:37]`

> ⚠ **Cuidado:** responder a dor de negócio com capacidade técnica ("a gente tem muita gente em Kotlin") `[OBSERVADO: Orbita 12:30]`.

| DRI | SLA | Critério de saída |
|---|---|---|
| AE | na própria reunião | Cliente reformula o problema com as próprias palavras |

### 4.5 Fechar com critério de sucesso e quem vai à proposta

**Foco:** sair com a régua do cliente e o próximo passo controlado.
**Elemento da metodologia:** E7 Take Control

**Ações:**
- [ ] Perguntar a régua de sucesso em 6 meses e registrá-la nas palavras do cliente
- [ ] Definir data da proposta e **quem deve estar** (decisor + influenciadores; incluir quem não esteve)
- [ ] Enviar síntese ao cliente em 24h: problema, custo, critério de sucesso, próximo passo
- [ ] Mover o negócio para Proposta no CRM só com os 3 campos preenchidos

**Perguntas que funcionam:**
- "Qual é a sua régua de sucesso daqui a seis meses? O que precisaria ter mudado para você dizer que valeu o investimento?" — `[OBSERVADO: TechScale R2 79:28]`

**Como fica uma boa execução:** "Até quinta-feira da semana que vem apresento a proposta […]. Quero que você, o Bruno e a Fernanda — CPO de vocês — estejam no convite." — `[OBSERVADO: TechScale R2 86:49]`

> ⚠ **Cuidado:** "mando a proposta e o deck por e-mail" sem data nem participantes `[OBSERVADO: Orbita 22:00]`.

| DRI | SLA | Critério de saída |
|---|---|---|
| AE | síntese em 24h | Proposta com data marcada e convite com decisor + ≥ 1 influenciador |

## 5. Sinais

| Tipo | O que o cliente diz ou faz | Leitura | Fonte |
|---|---|---|---|
| ✅ Avanço | "(pausa longa) Quando você coloca assim... sim." | Aceitou o custo como real | `[OBSERVADO: TechScale R2 50:26]` |
| ✅ Avanço | "A gente está adicionando capacidade num sistema que está destruindo capacidade." | Adotou o reframe | `[OBSERVADO: TechScale R2 50:26]` |
| ✅ Avanço | "É literalmente a minha vida." | Influenciador se reconheceu | `[OBSERVADO: TechScale R2 68:30]` |
| ✅ Avanço | "A Fernanda já perguntou quando ia ter uma proposta." | Urgência interna, novo stakeholder | `[OBSERVADO: TechScale R2 91:38]` |
| ⚠ Risco | "Pode parar o compartilhamento? Prefiro conversar." | Abertura errada | `[OBSERVADO: Orbita 10:45]` |
| ⚠ Risco | "Preço e prazo de começar, basicamente." | Cliente comparando commodity | `[OBSERVADO: Orbita 16:38]` |
| ⚠ Risco | "Aí complica. Mas a gente vai dar um jeito." | Custo não foi quantificado | `[OBSERVADO: Orbita 14:08]` |
| ⚠ Risco | Pede preço por hora antes do custo | Vai perder por preço | `[OBSERVADO: Orbita 19:05]` + entrevista Lucas |

## 6. Objeções e respostas

| Objeção (literal) | Princípio da metodologia | Resposta que funcionou | Fonte |
|---|---|---|---|
| "Toda vez que a gente tenta parar para refatorar, o negócio puxa pelo backlog de features." | Emotional Impact | Nomear o paradoxo da capacidade bloqueada e contar o caso análogo | `[OBSERVADO: TechScale R2 58:42–61:47]` |
| "Alguém precisaria garantir que esse squad externo não criasse mais dívida técnica." | Acknowledge & Defer | "Faz todo sentido essa preocupação. Voltamos a ela na proposta." | `[OBSERVADO: TechScale R2 79:28]` |
| "O outro fornecedor passou cento e sessenta por hora." | Acknowledge & Defer → reancorar no custo do problema | Sem exemplo bom no diagnóstico. Resposta da R4: comparar o investimento com o custo anual do problema | `[OBSERVADO: TechScale R4 09:58]` `[HIPÓTESE]` para o diagnóstico |
| "Já tivemos fornecedor externo que ficou isolado." | Provar, não afirmar | Sem exemplo bom no diagnóstico. Na R4: piloto de 2 semanas | `[OBSERVADO: TechScale R4 25:08]` |

## 7. Hand-off de saída

**O que o Diagnóstico entrega:**
- [ ] Custo do problema em R$/ano, confirmado pelo cliente · CRM `custo_do_problema` (hoje: nota)
- [ ] Critério de sucesso nas palavras do cliente · CRM, nota "critério de sucesso"
- [ ] Mapa de stakeholders com papel e ganho pessoal · CRM, contatos e nota
- [ ] Proposta agendada com participantes definidos · calendário
- [ ] Síntese enviada ao cliente em 24h · e-mail

**O que a Proposta confere:**
- [ ] Custo do problema registrado · se faltar → voltar ao cliente antes de montar a proposta
- [ ] Decisor confirmado no convite · se faltar → AE pede acesso ao decisor antes de apresentar
- [ ] Critério de sucesso registrado · vira o slide de abertura da proposta

> ✅ **Critério de saída:** custo do problema (R$/ano) e critério de sucesso registrados no CRM **e** proposta agendada com decisor + ≥ 1 influenciador.

## 8. Métricas

| Métrica | Linha de base | Meta | Fórmula | Fonte | Frequência | Dono |
|---|---|---|---|---|---|---|
| Conversão Diagnóstico → Proposta | 54% `[MEDIDO]` | 80% | negócios que entraram em Diagnóstico e avançaram ÷ negócios que entraram em Diagnóstico | CRM, `funil.py` | mensal | Gestor comercial |
| % de diagnósticos com custo quantificado | 50% (39 de 78) `[MEDIDO]` | 90% | diagnósticos com `custo_do_problema` preenchido ÷ diagnósticos | CRM | semanal | Gestor comercial |
| % de propostas com diagnóstico prévio | 63% (42 de 67) `[MEDIDO]` | 100% | propostas com data de diagnóstico ÷ propostas | CRM | mensal | RevOps |
| Dias no Diagnóstico | 11 (mediana) `[MEDIDO]` | ≤ 10 | mediana de dias entre entrada no Diagnóstico e na Proposta | CRM | mensal | RevOps |
| Proposta agendada na própria reunião | `[PRECISA DE DADO]` | 100% | diagnósticos com próxima reunião marcada ÷ diagnósticos | CRM, atividades | semanal | AE |

## 9. Red flags

| Red flag | Como detectar | Severidade | Ação imediata | Dono |
|---|---|---|---|---|
| Negócio em Proposta sem diagnóstico | data de Proposta preenchida e de Diagnóstico vazia | 🔴 Crítico | Voltar o negócio e marcar diagnóstico | Gestor |
| Diagnóstico sem custo do problema | campo `custo_do_problema` vazio ao mover de etapa | 🔴 Crítico | Bloquear a mudança de etapa; AE retoma com o decisor | AE |
| Só uma pessoa do cliente no diagnóstico | convite com 1 participante | 🟡 Atenção | Pedir a presença de quem vive o problema ou do decisor | AE |
| Preço por hora pedido antes do custo | nota da reunião / transcrição | 🟡 Atenção | Reancorar no custo; não enviar tabela | AE |
| Sem próximo passo com data | nenhuma atividade futura no negócio 48h após a reunião | 🟡 Atenção | Ligar e marcar a proposta com participantes | AE |
| Mais de 15 dias no Diagnóstico | dias na etapa > 15 | 🟢 Acompanhar | Revisar no pipeline semanal | Gestor |

**Escalação:** 🔴 liderança em 24h · 🟡 gestor em 48h · 🟢 revisão semanal.

## 10. Declarado × Observado × Medido

| Tema | O que a empresa diz `[DECLARADO]` | O que o time faz `[OBSERVADO]` | O que o funil mostra `[MEDIDO]` | Decisão no handbook |
|---|---|---|---|---|
| Diagnóstico | Opcional (manual §1) | Lucas: "Para mim é a venda" | 81% × 28% de avanço; 80% × 25% proposta → ganho | Obrigatório |
| Abertura | Abrir com institucional e cases (manual §3) | Ganho sem deck; perdido com deck | `[PRECISA DE DADO]` | Abrir com hipótese |
| Preço por hora | "Na ponta da língua" (manual §3) | Perdidos deram preço por hora cedo | 80% das perdas por preço/hora pularam o diagnóstico | Preço só depois do custo |
| Por que perdemos | "Por preço" (win-loss) | Perdas sem número e sem decisor | Preço/hora 18% das perdas; "sem decisor" 30% | Sem tabela de desconto; foco em custo e decisor |
| Diagnóstico e ciclo | "Alonga o ciclo" (win-loss) | — | +4 dias de mediana; conversão de proposta 3x | Manter |

## 11. Skills que executam este handbook

| Skill | Quando usar | Comando |
|---|---|---|
| `vektor-diagnostico` | Preparar, conduzir e registrar uma reunião de diagnóstico | `/vektor-diagnostico` |
| `vektor-como-usar` | Saber qual skill usar em cada momento do processo | `/vektor-como-usar` |

## 12. Aprovação

| Preenchido por | Revisado por | Aprovado por | Versão | Próxima revisão |
|---|---|---|---|---|
| Analista de RevOps | Lucas Andrade (AE sênior) | Gestor comercial | 1.0 | 2027-04-22 |

Versionamento: 1.0 versão inicial · 1.x ajuste menor · 2.0 mudança de processo.
