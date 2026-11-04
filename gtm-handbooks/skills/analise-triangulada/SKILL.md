---
name: analise-triangulada
description: Como analisar as evidências de um projeto de handbook de GTM em três frentes e cruzá-las - fichas de reunião a partir de transcrições (observado), leitura do funil do CRM com o script funil.py (medido) e extração do processo declarado de documentos, processos escritos, PPTs de proposta e de produto (declarado) - e como escrever a síntese com divergências e padrões de ganho. Use ao ler transcrições de vendas, analisar funil, ler documentos comerciais da empresa ou consolidar a análise antes de escrever um handbook.
---

# Análise triangulada

Três análises independentes, depois uma síntese. Cada análise usa a metodologia (`02-metodologia/metodologia.md`) como eixo.

## 1. Observado · fichas de reunião (agente `analista-conversas`)
- Uma ficha por transcrição, no modelo `${CLAUDE_PLUGIN_ROOT}/templates/ficha-reuniao.md`, salva em `03-analise/fichas/<mesmo-nome-do-arquivo>.md`.
- Ler o arquivo inteiro. Inferir falantes pelo contexto quando a ferramenta não identifica, sem inventar nomes.
- Nota 0–3 por item da metodologia, com citação literal curta (≤ 30 palavras) e `[mm:ss]`.
- Registrar perguntas literais do vendedor e a reação do cliente: elas viram as "perguntas que funcionam" do handbook.
- Mais de 8 transcrições: dividir em lotes de 4 a 6 e rodar agentes em paralelo. Cada agente devolve, além das fichas, um JSON por reunião: `{"arquivo","conta","etapa","resultado","notas":{"<elemento>":n},"proximo_passo_com_data":bool,"elo_mais_fraco":"...","melhor_momento":"[mm:ss] ..."}` e 5 a 8 padrões do lote.

## 2. Medido · funil (agente `analista-funil`)
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/funil.py 01-coleta/A-numeros/<arquivo>.csv \
  --etapas "Etapa 1,Etapa 2,..." --segmentar <coluna_opcional> --saida 03-analise/funil.md
```
- O script calcula: negócios por etapa, conversão etapa a etapa, conversão acumulada, tempo mediano em cada etapa, win rate, ciclo de ganho, motivos de perda por etapa onde o negócio parou, negócios que **pularam** etapas, e o recorte por uma coluna (ex.: segmento, dono ou um campo de qualificação).
- O agente lê a saída e escreve abaixo dela a **leitura**: maior vazamento, etapa mais lenta, diferença entre vendedores, o que os perdidos têm em comum. Todo número citado vem do script (`[MEDIDO: funil.md]`).
- Se o export não tem datas por etapa: rodar só com status final e registrar a lacuna.

## 3. Declarado · documentos (agente `analista-documentos`)
Para cada documento, extrair em `03-analise/declarado.md`:

| Extrair | De onde costuma vir |
|---|---|
| Etapas oficiais e critérios de passagem | Processo escrito, definições do CRM |
| Mensagem oficial: problema, tese, diferenciais | PPT de produto, pitch |
| Como a proposta é estruturada: ordem, preço, próximo passo | PPT de proposta, propostas reais |
| Regras: desconto, alçada, SLA, campos obrigatórios | Política comercial, CRM |
| Provas: cases, números, depoimentos | PPTs, cases |
| Hipóteses da gestão sobre ganhos e perdas | Win/loss, post-mortem, retrospectivas |
| O que se ensina ao vendedor novo | Onboarding |

Cada item com `[DECLARADO: arquivo, página/slide]`. Marcar o que parece desatualizado (data, produto que não existe mais).

## 4. Síntese (`03-analise/sintese.md`)
Estrutura:
1. **Manchete:** a principal conclusão em 1 frase.
2. **Processo real por etapa:** o que os ganhos fazem em cada etapa, com fontes.
3. **Padrões de ganho × perda:** notas médias da metodologia em ganhos vs. perdidos (tabela), comportamentos que só aparecem nos ganhos.
4. **Divergências declarado × observado × medido:** tabela tema · declarado · observado · medido · decisão. Regra: observado e medido ganham do declarado; quando observado e medido discordam, investigar na entrevista.
5. **Hipóteses da gestão:** confirmadas, desmentidas ou sem dado.
6. **Lacunas:** o que falta para escrever cada handbook, quem fornece.
7. **Recomendação de processos:** quais handbooks escrever, em que ordem (comece pelo maior vazamento do funil).

## Gate da Análise
- [ ] 1 ficha por transcrição do inventário
- [ ] `funil.md` gerado pelo script, com leitura
- [ ] `declarado.md` cobre todos os documentos recebidos
- [ ] `sintese.md` com tabela de divergências e padrões de ganho × perda
- [ ] Nenhum número sem tag
