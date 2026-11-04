> Dados fictícios para treinamento. Gabarito do passo 3 (análise do funil). Parte 1 = saída do `scripts/funil.py`; parte 2 = leitura do analista.

# Funil · saída do funil.py

Arquivo: `01-coleta/A-numeros/deals.csv` (comando: `funil.py deals.csv --etapas "qualificacao,diagnostico,proposta,followup,contrato" --segmentar custo_quantificado`) · 122 negócios · 36 ganhos · 83 perdidos · 3 abertos
Período de criação: 2025-11-01 a 2026-10-17
Todos os números abaixo são contagens ou medianas do arquivo. Use a tag `[MEDIDO: funil.md]`.

## Resumo

| Indicador | Valor |
|---|---|
| Win rate (ganhos ÷ fechados) | 30,3% |
| Ciclo mediano dos ganhos (dias, criação → fechamento) | 48 |
| Valor mediano dos ganhos | 170.000 |
| Negócios que pularam alguma etapa | 25 (20,5%) |

## Conversão por etapa

Entrou = tem data de entrada na etapa. Passou = dos que entraram, chegou a uma etapa posterior (ou ganhou, na última). Quem pulou a etapa não entra na conta dela (ver Etapas puladas). Conversão fechados = só negócios já ganhos ou perdidos.

| Etapa | Entrou | Passou para a seguinte | Conversão (todos) | Conversão (fechados) | Dias na etapa (mediana) |
|---|---|---|---|---|---|
| qualificacao → diagnostico | 122 | 103 | 84,4% | 84,0% | 8 |
| diagnostico → proposta | 78 | 42 | 53,8% | 53,9% | 11 |
| proposta → followup | 67 | 54 | 80,6% | 81,5% | 9 |
| followup → contrato | 54 | 42 | 77,8% | 79,2% | 12 |
| contrato → Ganho | 42 | 36 | 85,7% | 85,7% | 8 |

Conversão acumulada (ganhos ÷ negócios com alguma etapa): 29,5%

**Maior vazamento (fechados):** diagnostico (53,9% passam).
**Etapa mais lenta:** followup (12 dias de mediana).

## Perdas por etapa onde o negócio parou

| Etapa | Perdidos | Motivos (n) |
|---|---|---|
| qualificacao | 19 | sem decisor (9); timing (7); sem budget (3) |
| diagnostico | 35 | timing (12); sem decisor (12); escolheu concorrente (11) |
| proposta | 12 | preço/hora (6); sem decisor (3); timing (1); sem budget (1); escolheu concorrente (1) |
| followup | 11 | preço/hora (4); sem budget (3); escolheu concorrente (3); sem decisor (1) |
| contrato | 6 | preço/hora (5); timing (1) |

Motivo de perda preenchido em 100,0% dos perdidos.

## Etapas puladas

| Etapa pulada | Negócios | Win rate desses (fechados) |
|---|---|---|
| diagnostico | 25 | 25,0% (24 fechados) |

Win rate de quem **não** pulou etapa: 31,6% (95 fechados)

## Por dono

| Valor | Negócios | Ganhos | Perdidos | Win rate | Ciclo mediano ganho (dias) |
|---|---|---|---|---|---|
| Lucas Andrade | 31 | 17 | 13 | 56,7% | 49 |
| Diego Ramos | 31 | 7 | 23 | 23,3% | 47 |
| Patrícia Gomes | 30 | 7 | 23 | 23,3% | 52 |
| Marina Costa | 30 | 5 | 24 | 17,2% | 46 |

Conversão por etapa em cada grupo (fechados; entre parênteses: passou/chegou):

| Etapa | Diego Ramos | Lucas Andrade | Marina Costa | Patrícia Gomes |
|---|---|---|---|---|
| qualificacao → diagnostico | 86,7% (26/30) | 90,0% (27/30) | 75,9% (22/29) | 83,3% (25/30) |
| diagnostico → proposta | 28,6% (4/14) | 87,5% (21/24) | 26,7% (4/15) | 52,2% (12/23) |
| proposta → followup | 81,2% (13/16) | 87,5% (21/24) | 81,8% (9/11) | 71,4% (10/14) |
| followup → contrato | 76,9% (10/13) | 90,5% (19/21) | 66,7% (6/9) | 70,0% (7/10) |
| contrato → Ganho | 70,0% (7/10) | 89,5% (17/19) | 83,3% (5/6) | 100,0% (7/7) |

## Recorte por `custo_quantificado`

| Valor | Negócios | Ganhos | Perdidos | Win rate | Ciclo mediano ganho (dias) |
|---|---|---|---|---|---|
| nao | 83 | 12 | 70 | 14,6% | 46 |
| sim | 39 | 24 | 13 | 64,9% | 48 |

Conversão por etapa em cada grupo (fechados; entre parênteses: passou/chegou):

| Etapa | nao | sim |
|---|---|---|
| qualificacao → diagnostico | 76,8% (63/82) | 100,0% (37/37) |
| diagnostico → proposta | 28,2% (11/39) | 81,1% (30/37) |
| proposta → followup | 71,4% (25/35) | 93,3% (28/30) |
| followup → contrato | 68,0% (17/25) | 89,3% (25/28) |
| contrato → Ganho | 70,6% (12/17) | 96,0% (24/25) |

## Leitura do analista

Cálculos complementares feitos sobre o mesmo `deals.csv` (contagens, sem estimativa). Tag: `[MEDIDO: funil.md]`.

### 1. O vazamento é no Diagnóstico
- Diagnóstico → Proposta é a menor conversão do funil: **54%** (42 de 78 que entraram na etapa) contra 79% a 86% nas outras etapas.
- 25 negócios pularam o Diagnóstico e não entram nessa conta (ver Etapas puladas). O Diagnóstico concentra **35 dos 83 perdidos (42%)**.

### 2. O que separa quem passa: custo do problema quantificado
| Diagnóstico | Avançaram para Proposta | Proposta → Ganho (fechados) | Win rate (fechados) | Perdas por preço/hora |
|---|---|---|---|---|
| Com custo quantificado (`sim`) | 30 de 37 (81%) | 24 de 30 (80%) | 24 de 37 (65%) | 0 |
| Sem custo quantificado | 11 de 39 (28%) | 6 de 11 (55%) | 6 de 39 (15%) | 3 |
| Pulou o Diagnóstico | n/a | 6 de 24 (25%) | 6 de 24 (25%) | 12 |

Leitura: diagnóstico **sem** número é o pior caminho (o negócio morre na própria etapa); pular o diagnóstico leva o negócio para a proposta, mas ele perde lá, por preço.

### 3. "Perdemos por preço" é sintoma, não causa
- Preço/hora explica **15 de 83 perdas (18%)**. O motivo mais comum é "sem decisor" (25) e "timing" (21).
- **12 das 15 perdas por preço/hora (80%)** vieram de negócios que pularam o Diagnóstico; as outras 3, de diagnósticos sem custo quantificado. Nenhuma veio de diagnóstico com custo quantificado.

### 4. Diferença entre vendedores
- Lucas Andrade: win rate **56,7%**; os outros três ficam entre **17,2% e 23,3%**.
- Lucas leva **88%** das propostas com diagnóstico prévio e quantifica o custo em **84%** dos diagnósticos. Diego: 24% e 14%. Marina: 36% e 38%. Patrícia: 86% e 43%.
- A distribuição de segmentos é parecida entre os quatro (rodízio): Lucas tem 8 Logística, 8 Scale-up SaaS, 6 Fintech, 5 Saúde, 4 Varejo. A hipótese "o Lucas pega as melhores contas" não se sustenta no funil.

### 5. Ciclo
- Ciclo mediano dos ganhos: **48 dias**. Com custo quantificado: 48,5 dias; ganhos que pularam o diagnóstico: 44,5 dias. O diagnóstico acrescenta ~4 dias de mediana e triplica a conversão de proposta (80% × 25%).

### 6. Segmento
- Win rate por segmento (fechados): Logística 43% (12/28) · Varejo digital 38% (9/24) · Saúde digital 23% (5/22) · Scale-up SaaS 22% (6/27) · Fintech 22% (4/18).

### Cinco números para o handbook do Diagnóstico
1. Win rate geral 30% (36/119) · ciclo mediano 48 dias.
2. Diagnóstico → Proposta: 54% (menor conversão do funil).
3. Diagnóstico com custo quantificado: 81% avançam × 28% sem custo.
4. Proposta → Ganho: 80% com custo quantificado × 25% pulando o diagnóstico.
5. 80% das perdas por preço/hora vêm de quem pulou o diagnóstico.
