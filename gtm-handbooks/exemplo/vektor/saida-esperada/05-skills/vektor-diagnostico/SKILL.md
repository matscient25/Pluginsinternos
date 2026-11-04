---
name: vektor-diagnostico
description: Prepara, conduz e registra a reunião de Diagnóstico da Consultoria Vektor no padrão Challenger - hipóteses por papel, perguntas para chegar ao custo do problema em reais, reframe, critério de sucesso do cliente, critério de saída e registro no CRM. Use quando o AE disser que tem um diagnóstico, uma segunda reunião, uma sessão de causa raiz ou uma conversa técnica com uma conta, pedir perguntas para quantificar o problema, colar a transcrição de um diagnóstico para registrar, ou perguntar se um negócio pode ir para Proposta. Não use para montar a proposta comercial nem para negociar preço.
---

# Vektor · Diagnóstico

> Dados fictícios para treinamento. Skill-gabarito gerada a partir de `04-handbooks/diagnostico.md` (v1.0).

O Diagnóstico existe para sair com **o custo do problema em reais**, construído com os números do cliente e confirmado por ele. Sem esse número, 28% dos negócios avançam; com ele, 81%. Esta skill guia o AE antes, durante e depois da reunião.

## Antes de começar
1. Leia `vektor-contexto` (portfólio, ICP, personas) e `vektor-metodologia` (lente Challenger) se ainda não estiverem carregadas.
2. Identifique a conta e busque no CRM: notas da Qualificação, participantes confirmados, hipótese de dor.
3. Confira o **critério de entrada**: reunião marcada com o decisor **e** com quem vive o problema, com pauta enviada. Se faltar, avise o AE e sugira como resolver antes de preparar.
4. Pergunte qual modo o AE quer: **Preparar**, **Conduzir**, **Registrar** ou **Revisar**. Se ele colar uma transcrição, use Registrar.

## Modo Preparar
Entregue um plano de uma página:
1. **Objetivo da reunião** em uma frase (impacto de negócio, não arquitetura).
2. **Hipóteses de causa** (3 a 5) para o perfil da conta. Use o reframe da Vektor: "o problema não é falta de gente; é como a capacidade de entrega está arquitetada".
3. **Perguntas por papel**, em ordem, tiradas de `references/perguntas.md`:
   - quem vive o problema (Head de Eng, Tech Lead): tempo, volume, frequência;
   - decisor (CTO, VP): custo unitário, receita em risco, régua de sucesso.
4. **Conta do custo do problema** a montar na reunião: receita em risco + capacidade desperdiçada (squads equivalentes × custo mensal × 12).
5. **Caso análogo** a contar (de cliente parecido, como história).
6. **Próximo passo a propor:** data da proposta e quem deve estar (decisor + influenciadores, incluindo quem não veio).
7. **O que não levar:** deck institucional, cases de logo, tabela de preço por hora.

## Modo Conduzir
Cola de bolso, na ordem do handbook:
1. Abrir pelo impacto de negócio, sem deck. Pedir o mapa dos times.
2. Medir a operação com quem vive o problema (≥ 3 números).
3. Converter em reais com o decisor. Fazer a conta em voz alta e pedir confirmação.
4. Reenquadrar ("não é técnico, é decisão gerencial acumulada") e contar o caso análogo.
5. Fechar com a régua de sucesso em 6 meses e a proposta agendada com participantes.

Sinais de avanço: pausa antes de concordar; cliente repete o reframe com as próprias palavras; "é literalmente a minha vida". Sinais de risco: "pode parar o compartilhamento?", "preço e prazo, basicamente", "a gente dá um jeito", pedido de preço por hora. Respostas em `references/objecoes.md`.

## Modo Registrar
A partir da transcrição ou do relato do AE:
1. Extraia: números operacionais ditos pelo cliente (com a frase), custo do problema (R$/ano) e como foi calculado, critério de sucesso nas palavras do cliente, participantes e papéis, próximo passo (data, participantes).
2. Dê nota 0–3 aos elementos E1 a E7 da lente, com citação curta de cada.
3. Monte o registro no CRM:
   - `custo_do_problema` (R$/ano) — se o campo não existir, nota com o título "Custo do problema";
   - nota "Critério de sucesso";
   - contatos com papel (decisor, influenciador técnico, influenciador de produto);
   - atividade da proposta com data.
4. **Mostre o registro e peça confirmação antes de gravar.** Nunca grave número que o cliente não disse.

## Modo Revisar
Com a transcrição: aplique a rubrica de `references/rubrica.md` (seção 11 do handbook). Nota 0–3 por critério com a frase e o minuto, três momentos de coaching com a pergunta do handbook para a próxima reunião (modelo do kit: `templates/coaching.md`). Depois responda: **o negócio pode ir para Proposta?**
- Sim, só se: custo do problema (R$/ano) registrado e confirmado pelo cliente **e** critério de sucesso registrado **e** proposta agendada com decisor + ≥ 1 influenciador.
- Se não: diga exatamente o que falta e a próxima ação (ex.: "voltar ao CTO para o custo mensal do squad").

## Critério de saída
Custo do problema (R$/ano) e critério de sucesso registrados no CRM **e** proposta agendada com decisor + ≥ 1 influenciador.

## Red flags que a skill aponta
- 🔴 Negócio indo para Proposta sem diagnóstico ou sem custo do problema.
- 🟡 Só uma pessoa do cliente na reunião.
- 🟡 Preço por hora pedido antes do custo: reancorar, não enviar tabela.
- 🟡 Nenhuma atividade futura 48h depois da reunião.

## Regras
- Nunca inventar número, nome ou fala. Se faltar dado, pergunte ao AE.
- Perguntas sugeridas vêm de `references/perguntas.md`, não de improviso.
- Preço não aparece no Diagnóstico.

## Referências
- `references/perguntas.md` — perguntas literais por passo e por papel, com fonte.
- `references/objecoes.md` — objeções do diagnóstico e respostas que funcionaram.
- `references/rubrica.md` — rubrica da etapa (5 critérios, nota 0–3, regra de avanço) para o coaching.
