> Dados fictícios para treinamento. Gabarito do passo 2 (Lente) da demo.

# Lente · Challenger Sale · aplicada à Consultoria Vektor

| | |
|---|---|
| Fonte da metodologia | *The Challenger Sale*, Matthew Dixon & Brent Adamson (CEB/Gartner, 2011) |
| Versão da lente | 1.0 · 2026-10-17 |
| Quem validou | Gestor comercial e Lucas Andrade (AE) |

## 1. A metodologia em 5 linhas
Em venda complexa, o vendedor de maior performance não é o que constrói relacionamento: é o que **ensina** o cliente algo novo sobre o próprio negócio (Teach), **adapta** a mensagem a cada pessoa do comitê (Tailor) e **conduz** o processo de compra com tensão construtiva (Take Control). O valor está no insight entregue durante a venda, não no produto. A regra de ouro: *lead to, not lead with* — a solução aparece no fim, como o melhor caminho para um problema que o cliente agora enxerga. Funciona melhor quando o comprador não sabe exatamente o que comprar — caso típico da Vektor: o cliente acha que falta gente.

## 2. Elementos da lente
Oito elementos. Os cinco primeiros seguem a coreografia do pitch de ensino; os três últimos são Tailor e Take Control.

### E1 · Warmer (hipótese antes da pergunta)
- **Definição (fonte):** mostrar que entende o mundo do cliente antes de perguntar, com dados de empresas parecidas e uma hipótese de desafio.
- **Evidência numa conversa:** vendedor abre com padrão observado em empresas similares e pede validação ("isso ressoa?"); não abre com a apresentação institucional.
- **Escala 0–3:** 0 = abre com "quem somos"/deck · 1 = pergunta aberta genérica ("qual seu desafio?") · 2 = hipótese genérica de mercado · 3 = hipótese específica do perfil do cliente, validada por ele.
- **Perguntas-padrão:** "Nos últimos meses conversei com [n] [cargos] de empresas que cresceram [x]%. O padrão é [hipótese]. Isso tem relação com o que vocês vivem?"
- **Sinais de avanço:** "Tem. Bastante." · cliente completa a hipótese com dados próprios.
- **Sinais de risco:** "Pode parar o compartilhamento? Prefiro conversar."
- **Erro comum:** abrir com logos e cases. "Cliente compra de quem conhece" (manual Vektor) é o oposto do Warmer.
- **Onde registrar no CRM:** nota da reunião, campo livre `hipotese_inicial` `[PRECISA DE DADO]` (campo não existe).

### E2 · Reframe
- **Definição (fonte):** conectar o desafio a um problema maior, que o cliente não tinha percebido. Reação desejada: "nunca tinha pensado assim", não "concordo totalmente".
- **Evidência:** cliente hesita, pausa, reformula a própria visão do problema.
- **Escala:** 0 = nenhum ponto de vista novo · 1 = vendedor repete o que o cliente disse · 2 = ponto de vista novo, cliente concorda de imediato · 3 = cliente verbaliza mudança de visão ("a gente trata como capacidade, você diz que é estrutural").
- **Perguntas-padrão:** "E se o problema não for [crença do cliente], e sim [reframe]?"
- **Reframe central da Vektor:** "o problema não é falta de gente; é como a capacidade de entrega está arquitetada."
- **Sinais de avanço:** "Hm. Não tinha enquadrado dessa forma."
- **Sinais de risco:** concordância entusiasmada imediata · cliente mantém "precisamos de mais devs".
- **Erro comum:** diluir o reframe para não gerar desconforto.

### E3 · Rational Drowning (custo do problema em reais)
- **Definição (fonte):** quantificar o custo do problema ou o tamanho da oportunidade, com dados — ROI sobre resolver o problema, não sobre comprar a solução.
- **Evidência:** número em R$ construído **com dados do cliente** durante a conversa.
- **Escala:** 0 = sem número · 1 = número genérico de mercado · 2 = número parcial do cliente (um componente) · 3 = custo total do problema em R$/ano, calculado com o cliente e confirmado por ele.
- **Perguntas-padrão:** "Quanto custa por mês manter um squad de oito pessoas aí?" · "Com que frequência isso acontece por sprint?" · "Qual era o valor daquele contrato?"
- **Sinais de avanço:** "(pausa longa) Quando você coloca assim... sim."
- **Sinais de risco:** "Custa, né. Mas não tenho um número."
- **Erro comum:** sair do diagnóstico sem número; trazer o preço antes do custo.
- **Onde registrar no CRM:** campo `custo_do_problema` (R$/ano) `[PRECISA DE DADO]` — hoje vai para as notas.

### E4 · Emotional Impact
- **Definição (fonte):** fazer o cliente se reconhecer numa história de empresa parecida; mata o "mas somos diferentes".
- **Evidência:** vendedor conta caso análogo; cliente se identifica pessoalmente.
- **Escala:** 0 = nada · 1 = case genérico de portfólio · 2 = caso análogo sem reação · 3 = cliente se reconhece ("é literalmente a minha vida").
- **Sinais de avanço:** "É como se você trabalhasse aqui."
- **Erro comum:** confundir com case de marketing (logo + resultado).

### E5 · A New Way → Solução (lead to, not lead with)
- **Definição (fonte):** mostrar como o cliente operaria diferente (comportamento) antes da solução; só então conectar aos diferenciais.
- **Evidência:** "novo jeito de operar" aparece antes de squads, preço ou portfólio.
- **Escala:** 0 = solução e preço antes do problema · 1 = solução logo após o problema · 2 = novo jeito apresentado, mas misturado com a oferta · 3 = sequência completa problema → custo → novo jeito → solução.
- **Erro comum:** responder "a gente tem muita gente em Kotlin" para uma dor de negócio.

### E6 · Tailor (Functional Bias por papel)
- **Definição (fonte):** adaptar mensagem por setor, empresa, papel e indivíduo; entender o que cada pessoa monitora, teme e precisa provar.
- **Evidência:** perguntas e linguagem diferentes para CTO (receita, board, reputação) e Head de Engenharia (retrabalho, dependências, sprint).
- **Escala:** 0 = mesmo pitch para todos · 1 = sabe os cargos · 2 = adapta perguntas por papel · 3 = mapeia o ganho pessoal de cada um e usa isso.
- **Perguntas-padrão:** "O que você precisaria mostrar ao [chefe] para justificar essa decisão?"

### E7 · Take Control — processo de compra e próximo passo
- **Definição (fonte):** conduzir o processo de compra: orientar quem deve estar na próxima reunião, detectar "foil", sair com próximo passo específico.
- **Evidência:** vendedor diz quem deve estar ("quero que você, o Bruno e a Fernanda estejam no convite"); data e dono do próximo passo.
- **Escala:** 0 = "fico no aguardo" · 1 = próximo passo vago · 2 = próximo passo com data, sem orientar participantes · 3 = data + participantes certos + entregável combinado.
- **Sinais de risco:** "Deixa eu ver a agenda dele primeiro e te falo." · "Vou levar para o diretor."
- **Erro comum:** perguntar "quem mais precisa estar envolvido?" em vez de orientar.

### E8 · Take Control — negociação
- **Definição (fonte):** não ceder antes de entender a objeção; Acknowledge & Defer → Deepen → Explore → Concede conforme plano.
- **Evidência:** objeção de preço respondida com custo do problema; concessão em escopo/prazo, não em preço; concessão planejada.
- **Escala:** 0 = dá desconto na hora · 1 = defende preço sem argumento · 2 = reancora no valor · 3 = reancora e concede só o planejado, com troca.
- **Sinais de risco:** "O outro fornecedor passou cento e sessenta por hora." → "dá para ver alguma condição comercial".

## 3. Mapa elemento × etapa do funil (Vektor)
| Etapa do CRM | Elementos que precisam estar em ≥ 2 para avançar | Elementos que começam a ser trabalhados |
|---|---|---|
| Qualificação | E1 Warmer · E2 Reframe · E7 próximo passo | E6 Tailor |
| Diagnóstico | E3 Rational Drowning · E6 Tailor · E7 participantes da proposta | E4 Emotional Impact |
| Proposta | E5 A New Way → Solução · E3 (custo retomado) | E8 |
| Follow-up | E7 consenso e acesso ao decisor econômico · E8 | — |
| Contrato | E8 negociação | — |
| Handoff CS | critério de sucesso do cliente transferido (E3 + E6) | — |

## 4. Critério de passagem por etapa (proposta)
| Etapa | Critério de saída binário | Elemento que comprova |
|---|---|---|
| Qualificação → Diagnóstico | Diagnóstico agendado com quem vive o problema, com pauta enviada | E7 = 3 |
| Diagnóstico → Proposta | Custo do problema em R$/ano registrado e confirmado pelo cliente + critério de sucesso nas palavras dele | E3 = 3 |
| Proposta → Follow-up | Proposta apresentada ao decisor e a ≥ 1 influenciador, com data do próximo encontro | E5 ≥ 2 e E7 ≥ 2 |
| Follow-up → Contrato | Decisor econômico com reunião marcada ou aprovação dentro da alçada | E7 = 3 |
| Contrato → Ganho | Contrato assinado com concessões dentro do plano | E8 ≥ 2 |

## 5. Adaptações para a Vektor
- "Rational Drowning" é chamado internamente de **"custo do problema"**. É o termo que vai para o CRM e para as skills.
- O manual atual usa BANT simplificado na qualificação. A lente mantém BANT como checklist mínimo de qualificação, mas o critério de saída passa a ser E7.
- Negociação (E8) segue o framework de 4 passos do livro; a Vektor não cede em forma de pagamento (adiantado) — concede escopo, prazo e SLA.
- Insight "Commercial Teaching" escala por segmento: o reframe de capacidade bloqueada vale para scale-ups de tecnologia; para saúde e varejo digital é `[HIPÓTESE]` até haver transcrição.
