> Dados fictícios para treinamento. Gabarito do passo 3 (síntese da análise triangulada).

# Síntese · Declarado × Observado × Medido · ACME

Base: 8 transcrições (6 TechScale ganho, Orbita Pay e Nuvia Saúde perdidos) · funil de 122 negócios (nov/2025 a out/2026) · 4 documentos · 2 entrevistas.

## Manchete
> **O processo que ganha na ACME não é o do manual: é o diagnóstico com custo do problema em reais. Quem faz isso converte 80% das propostas; quem pula, 25%.** `[MEDIDO: funil.md]` `[OBSERVADO: TechScale R2]`

## Divergências

| # | Tema | O que a empresa diz `[DECLARADO]` | O que o time faz `[OBSERVADO]` | O que o funil mostra `[MEDIDO]` | Decisão no handbook |
|---|---|---|---|---|---|
| 1 | Diagnóstico | Etapa "opcional, quando o cliente pedir" (manual §1) | Top performer: "Para mim é a venda" (entrevista Lucas). Orbita: diagnóstico virou levantamento técnico e perdeu | Diagnóstico → Proposta 81% com custo quantificado × 28% sem. Proposta → Ganho 80% × 25% pulando | **Obrigatório.** Critério de saída: custo do problema em R$/ano confirmado pelo cliente |
| 2 | Abertura da reunião | "Sempre abrir com a apresentação institucional e os cases" (manual §3) | TechScale R1 [01:00] "não vou apresentar deck". Orbita [10:45] cliente pede para parar o deck | Sem campo no CRM `[PRECISA DE DADO]` | Abrir com hipótese (Warmer). Deck institucional só se o cliente pedir |
| 3 | Preço por hora | "Levar o preço por hora na ponta da língua" (manual §3). PPT de proposta: preço no slide 10, sem custo do problema | Lucas: "eu nunca falo preço por hora" (entrevista). Orbita [19:12] e Nuvia [08:47] dão preço por hora e perdem | 12 de 15 perdas por preço/hora vieram de quem pulou o diagnóstico; 0 de quem quantificou o custo | Preço só depois do custo do problema e sempre comparado a ele. Proposta ganha slide de custo e critério de sucesso |
| 4 | Por que perdemos | "Estamos perdendo principalmente por preço" (win-loss §1); ação: tabela de desconto de até 15% | Nas duas perdas, o vendedor não tinha número do cliente nem acesso ao decisor | Preço/hora = 15 de 83 perdas (18%). "Sem decisor" = 25 (30%), maior motivo | Tabela de desconto **não** entra no handbook. Atacar custo do problema e acesso ao decisor |
| 5 | Diagnóstico e ciclo | "O diagnóstico alonga o ciclo; ir direto para proposta" (win-loss §2) | TechScale: 38 dias da qualificação ao fechamento com diagnóstico de 95 min | Ciclo mediano dos ganhos: 48,5 dias com custo quantificado × 44,5 pulando (+4 dias); conversão de proposta 3x maior | Manter o diagnóstico. Os 4 dias se pagam |
| 6 | Por que o Lucas ganha | "Pega as melhores contas" (win-loss §4; entrevista gestor) | Lucas segue a coreografia Challenger nas 6 reuniões | Contas por rodízio; mix de segmentos parecido entre os 4 AEs. Lucas 56,7% × 17–23% | A diferença é método. O método do Lucas vira o handbook |
| 7 | Decisor | BANT: "Authority: falar com alguém de engenharia ou produto" (manual §2) | Nuvia: proposta só para gerente de produto, "vou levar para o diretor". TechScale R2 [86:49]: AE define quem vai à proposta | "Sem decisor": 25 perdas, 12 delas no Diagnóstico | Critério de saída do Diagnóstico inclui proposta agendada com decisor + influenciador |
| 8 | Segmento | Logística e varejo convertem melhor (win-loss §3) | — | Logística 43%, Varejo 38%, demais 22–23% | **Confirmado.** Entra como contexto; o reframe de "capacidade bloqueada" para saúde e varejo fica `[HIPÓTESE]` |

## Padrões do que funciona (para o passo a passo)
1. Hipótese de mercado na abertura, sem deck `[OBSERVADO: TechScale R1 01:00, 05:44]`.
2. Diagnóstico com quem vive o problema (Head de Eng) **e** com quem sente o custo (CTO) `[OBSERVADO: TechScale R2]`.
3. Quatro perguntas transformam operação em reais: tempo de espera, volume por mês, valor do contrato perdido, custo mensal de um squad `[OBSERVADO: TechScale R2 12:04–43:22]`.
4. Reframe: "não é técnico, é decisão gerencial acumulada" `[OBSERVADO: R2 52:37]`.
5. Critério de sucesso nas palavras do cliente vira régua da proposta e do CS `[OBSERVADO: R2 79:28, R6]`.
6. O AE escolhe quem vai à próxima reunião `[OBSERVADO: R2 86:49, R3 69:11]`.

## Padrões do que perde
1. Abertura com "quem somos" `[OBSERVADO: Orbita 01:12, Nuvia 00:55]`.
2. Perguntas de levantamento técnico sem hipótese `[OBSERVADO: Orbita 11:40–12:50]`.
3. Impacto perguntado e não quantificado `[OBSERVADO: Orbita 14:02, Nuvia 11:15]`.
4. Preço por hora antes de qualquer número do cliente; desconto oferecido na hora `[OBSERVADO: Orbita 19:12–19:52, Nuvia 16:08]`.
5. Saída sem data: "a gente olha e retorna", "fico no aguardo" `[OBSERVADO: Orbita 22:20, Nuvia 17:50]`.

## Lacunas
- `[PRECISA DE DADO]` Campo `custo_do_problema` no CRM (hoje só nas notas) · admin do CRM.
- `[PRECISA DE DADO]` Transcrição de diagnóstico **ganho** de outro AE (hoje só Lucas) · gestor comercial.
- `[PRECISA DE DADO]` Propostas reais enviadas · gestor comercial.
- `[PRECISA DE DADO]` Entrevista de CS e dados de renovação (para o handbook de Handoff) · RevOps.

## Recomendação de ordem dos handbooks
1. **Diagnóstico** (maior vazamento e maior diferença entre vendedores) · 2. Proposta · 3. Qualificação · 4. Negociação/Contrato · 5. Handoff CS (após entrevista de CS).
