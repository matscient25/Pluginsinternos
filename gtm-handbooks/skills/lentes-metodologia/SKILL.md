---
name: lentes-metodologia
description: Converte qualquer metodologia de vendas (Challenger, MEDDPICC/MEDDIC, SPIN, SPICED, BANT, GPCTBA/C&I ou uma metodologia própria da empresa) numa lente de análise com elementos, evidência observável, escala 0-3, perguntas-padrão, sinais e mapa elemento por etapa do funil. Inclui lentes prontas para as metodologias mais usadas e como montar uma a partir de livro, site ou documento interno. Use ao escolher a metodologia de um projeto de handbook, ao montar a lente, ao pontuar uma reunião ou quando perguntarem "qual metodologia usar" ou "como adaptar a metodologia X".
---

# Lentes de metodologia

A lente é o que torna o método agnóstico. As fichas de reunião, a síntese e o handbook usam os elementos da lente como colunas. Troque a lente e o mesmo processo produz um handbook Challenger, MEDDPICC ou SPIN.

## Passo 1. Escolher a metodologia
Regra: **use a que a empresa já usa ou já treinou.** Trocar de metodologia é outro projeto. Se não houver nenhuma:

| Situação da empresa | Ponto de partida | Por quê |
|---|---|---|
| Cliente não sabe o que comprar, venda consultiva, risco de virar commodity | Challenger | Ensina e reenquadra o problema; sai da briga por preço |
| Enterprise, vários aprovadores, jurídico e compras pesados, forecast crítico | MEDDPICC | Qualificação e controle do processo de decisão |
| Ciclo médio, foco em descoberta de dor, vendedores juniores | SPIN | Estrutura de perguntas fácil de treinar |
| Inbound, ciclo curto, alto volume | BANT ou GPCTBA/C&I | Qualificação rápida |
| SaaS com receita recorrente e foco em impacto e evento crítico | SPICED | Só se a empresa já usa (é proprietária da Winning by Design) |
| A empresa tem metodologia própria | Própria | Monte a lente a partir do material interno (ver `references/propria.md`) |

Combinações são comuns (ex.: Challenger para conduzir + MEDDPICC para qualificar). Nesse caso, monte **uma lente só**, com os elementos das duas e sem sobreposição; registre de onde vem cada elemento.

## Passo 2. Montar a lente
1. Copie `${CLAUDE_PLUGIN_ROOT}/templates/lente.md` para `02-lente/lente.md`.
2. Parta da lente pronta em `references/<metodologia>.md`. Ela traz elementos, evidência, escala e perguntas genéricas.
3. Adapte à empresa: vocabulário, etapas exatas do CRM, onde cada elemento é registrado, o que não se aplica.
4. Preencha o mapa **elemento × etapa**: em que etapa cada elemento começa a ser trabalhado e em que etapa ele precisa estar em nota ≥ 2 para o negócio avançar. Esse mapa vira o critério de saída das etapas do handbook.
5. Valide com alguém da empresa (gestor ou top performer). Registre no topo.

## Escala 0–3 (igual para toda lente)
| Nota | Significado | Exemplo genérico |
|---|---|---|
| 0 | Ausente | Ninguém tocou no assunto |
| 1 | Mencionado ou suposto | Vendedor supôs, cliente não confirmou |
| 2 | Explorado e parcialmente confirmado | Cliente falou sobre, sem número ou nome |
| 3 | Confirmado, quantificado ou documentado | Número, nome, data ou documento do cliente |

## A mesma pergunta em cada lente
"O cliente tem um problema que vale a pena resolver?"

| Lente | Elemento | Como a pergunta aparece |
|---|---|---|
| Challenger | Reframe + Rational Drowning | O vendedor mostrou um custo que o cliente não via? |
| MEDDPICC | Metrics + Implicate the Pain | A dor tem número e consequência para o negócio? |
| SPIN | Implication + Need-payoff | O cliente verbalizou a consequência e o ganho de resolver? |
| SPICED | Pain + Impact | Há impacto racional e emocional declarado? |
| BANT | Need | Existe necessidade real? |
| GPCTBA/C&I | Challenges + Negative Consequences | Os desafios impedem metas e têm consequência? |

## Lentes prontas
| Arquivo | Metodologia |
|---|---|
| `references/challenger.md` | Challenger Sale (Dixon e Adamson) |
| `references/meddpicc.md` | MEDDIC / MEDDPICC |
| `references/spin.md` | SPIN Selling (Rackham) |
| `references/spiced.md` | SPICED (Winning by Design) |
| `references/bant.md` | BANT (IBM) |
| `references/gpctba.md` | GPCTBA/C&I (HubSpot) |
| `references/propria.md` | Como montar a lente de uma metodologia própria |

## Gate da Lente
- [ ] Todo elemento com definição, evidência observável, escala 0–3 e 2 a 4 perguntas
- [ ] Mapa elemento × etapa preenchido com as etapas exatas do CRM
- [ ] Critério de passagem proposto para cada etapa
- [ ] Validada por alguém da empresa (nome e data no topo)
