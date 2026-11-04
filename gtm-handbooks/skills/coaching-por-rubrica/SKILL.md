---
name: coaching-por-rubrica
description: Transforma cada handbook de GTM em rubrica da etapa e processa transcrições de reuniões de vendas contra a rubrica para fazer coaching - nota 0-3 por critério com evidência e minuto, veredito de avanço de etapa, os três momentos a melhorar com a pergunta do handbook para a próxima reunião, e a visão agregada por vendedor e por critério para o gestor e para revisar o handbook. Inclui a calibração (a rubrica precisa separar ganhos de perdidos). Use para criar ou calibrar a rubrica de uma etapa, avaliar uma call, dar feedback ou coaching a um vendedor, ou montar o mapa de treinamento do time.
---

# Coaching por rubrica

O handbook ensina; a rubrica mede; o coaching fecha o ciclo. Cada transcrição é avaliada contra a rubrica **da etapa em que o negócio está**.

```
HANDBOOK (seção 4: passos)  →  RUBRICA (seção 11)  →  TRANSCRIÇÃO × RUBRICA  →  COACHING
        ↑                                                                           │
        └──────────── critério que ninguém cumpre ou que não prevê ganho ───────────┘
```

## 1. Montar a rubrica (seção 11 do handbook)
1. **Um critério por passo** da seção 4 (4 a 6 critérios). O nome do critério é o nome do passo.
2. **Nota 3** = como os ganhos fazem (das fichas de reuniões ganhas). **Nota 0** = como os perdidos fazem. Notas 1 e 2 descrevem o meio do caminho. Tudo observável numa transcrição: frase ou comportamento, nunca intenção.
3. **Peso** só se um critério decide mais que os outros (padrão: todos 1).
4. **Regra de avanço** escrita sobre as notas e **idêntica** ao critério de saída da seção 7 (ex.: "custo em R$ = 3 e próximo passo ≥ 2").
5. **Calibrar** antes de usar: pontue ≥ 2 reuniões ganhas e ≥ 2 perdidas da mesma etapa. Se as médias não se separam claramente, um critério está medindo a coisa errada: reescreva e repita. Registre o resultado na seção 11.

## 2. Processar uma transcrição (coaching individual)
1. Identifique a etapa do negócio (CRM ou contexto da reunião) e carregue a rubrica dessa etapa. Reunião que mistura etapas: use a rubrica da etapa em que o negócio está.
2. Para cada critério: nota 0–3 **com citação literal ≤ 30 palavras e minuto**. Sem evidência = 0, anotado como "não apareceu na reunião".
3. Some, aplique a regra de avanço e diga **sim ou não**, com a regra que decidiu.
4. Escolha os **três momentos** de menor nota com maior impacto no avanço. Para cada um: o que aconteceu (com a frase) e o que fazer na próxima reunião, **copiado do handbook** (pergunta ou frase de uma reunião ganha, com fonte).
5. Diga o que manter (1 a 2 critérios com nota 3).
6. Escreva no modelo `${CLAUDE_PLUGIN_ROOT}/templates/coaching.md`, em `07-coaching/<arquivo-da-transcrição>.md`.

Tom: específico, sem julgamento, sempre com a próxima ação. Nunca inventar fala nem número.

## 3. Visão do gestor (agregado)
Com várias transcrições processadas, monte `07-coaching/painel.md`:

| Vendedor | Reuniões | Média por critério (1…n) | Critério mais fraco | Tendência |
|---|---|---|---|---|

- **Onde treinar:** o critério mais fraco de cada vendedor, com 1 trecho exemplar de outro vendedor (nota 3).
- **Time:** média por critério no período e comparação com o período anterior.
- Amostra pequena (menos de 5 reuniões por vendedor): diga que é amostra pequena.

## 4. Sinal para o handbook
Revise o passo ou o processo quando:
- **Ninguém cumpre um critério** (média do time < 1): o passo pode estar errado, inviável ou mal explicado.
- **Nota alta não converte** (negócios com o critério em 3 perdem tanto quanto os outros, no funil): o critério não mede o que importa.
- **Os ganhos recentes fazem algo que a rubrica não pede:** falta um critério.
Registre a decisão na seção 10 do handbook e suba a versão.

## Gate
- [ ] Toda etapa com handbook tem rubrica na seção 11, com regra de avanço igual ao critério de saída
- [ ] Rubrica calibrada (ganhos × perdidos) e resultado registrado
- [ ] Cada coaching com evidência literal por critério e sugestões vindas do handbook
