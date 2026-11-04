---
name: data-request
description: Define o pedido de dados (data request) para construir handbooks de GTM a partir de 4 fontes de evidência (A números do funil do CRM, B transcrições de reuniões, C documentos como processos escritos, conclusões de análises, PPT de proposta, PPT de produto, preço, battlecards, D entrevistas) e como validar o que chegou. Use ao montar o pedido de dados para uma empresa, ao receber arquivos do cliente, ao conferir se há evidência suficiente para escrever um handbook ou quando perguntarem "o que eu preciso pedir".
---

# Data request de handbooks

O handbook só é tão bom quanto a evidência. Peça as 4 fontes no primeiro dia, junto, em um único pedido.

## As 4 fontes

### A. Números (funil do CRM)
**Pedir:** export de negócios dos últimos 6 a 12 meses, **um negócio por linha**, com:
- `deal_id`, conta, dono, segmento ou produto, valor, data de criação
- status (aberto, ganho, perdido), data de fechamento, motivo de perda
- **data de entrada em cada etapa** do pipeline (no HubSpot: propriedades "Date entered <etapa>"; no Pipedrive e Salesforce: histórico de etapa)
- campos de qualificação que já existam (ex.: champion, decisor, dor)

**Validar:** ≥ 6 meses · ≥ 30 negócios fechados (ganhos + perdidos) · nomes de etapa iguais aos do CRM · motivo de perda preenchido em ≥ 50% dos perdidos. Se não houver data de entrada por etapa, o funil sai só com status final: registrar como lacuna.

**Rodar:** `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/funil.py <arquivo.csv>` (detecta colunas `entrou_*` e "Date entered").

### B. Conversas (transcrições)
**Pedir:** 2 a 4 transcrições **por etapa** que entrará no handbook, misturando:
- negócios **ganhos** (mostram o comportamento que funciona)
- negócios **perdidos** (mostram onde quebra)
- ao menos 1 com **objeção forte**
- de vendedores diferentes, com prioridade para o top performer

Nome do arquivo: `AAAA-MM-DD_conta_etapa_resultado.md`. Metadados no topo: conta, etapa, resultado do negócio, participantes e papéis, duração.
Fontes comuns: Fathom, Fireflies, Gong, tl;dv, Meet, Zoom, gravador do CRM. Se houver conector, buscar direto.

**Validar:** ≥ 2 por etapa escolhida · ≥ 1 ganho por etapa · falantes identificáveis · transcrição completa (não só o resumo da ferramenta).

### C. Documentos (o processo declarado)
É a fonte que mais falta e a que mais muda o handbook. **Pedir tudo o que existir:**

| Documento | Para que serve no handbook |
|---|---|
| Processo comercial escrito (manual, POP, playbook antigo, wiki) | Processo declarado, etapas oficiais, critérios de passagem |
| Conclusões de análises (win/loss, post-mortem, retrospectiva, QBR de vendas) | Hipóteses da gestão para confirmar ou desmentir com o funil |
| PPT de proposta (e 1 a 2 propostas reais enviadas) | Como a empresa apresenta valor, preço e próximo passo |
| PPT de produto / pitch / apresentação institucional | Mensagem oficial, diferenciais, provas |
| Tabela de preço, política de desconto, alçadas | Regras de negociação e red flags |
| Battlecards, comparativos com concorrentes | Respostas a objeções de concorrência |
| Cases e depoimentos | Provas usadas nas etapas |
| Definição de ICP e personas | Quem é o cliente, quem decide |
| Material de onboarding e treinamento de vendas | O que se ensina hoje ao vendedor novo |
| Contrato modelo, SLA, processo de implantação, handoff para CS | Hand-off de saída da venda |
| Definições do CRM (etapas, campos obrigatórios, automações) | Onde registrar cada coisa |

**Validar:** ≥ 1 documento de processo **ou** 1 PPT de proposta. Se não existir nada escrito, registrar: o handbook será o primeiro documento da empresa e a fonte D passa a ser obrigatória.

### D. Pessoas (entrevistas de 30 min)
Roteiro em `${CLAUDE_PLUGIN_ROOT}/templates/roteiro-entrevista.md`. Mínimo: top performer e gestor comercial. Recomendado: CS ou implantação (hand-off de saída) e SDR (hand-off de entrada).

## Como montar o pedido
1. Copie `${CLAUDE_PLUGIN_ROOT}/templates/data-request.md` para `01-coleta/data-request.md`.
2. Preencha empresa, processos escolhidos, etapas exatas do CRM, prazo (sugestão: D+5 úteis) e responsável por fonte.
3. Entregue ao usuário para enviar. Não envie e-mail sem confirmação.

## Como validar o que chegou
Para cada arquivo, uma linha em `01-coleta/inventario.md`:

| Fonte | Arquivo | Etapa | Resultado | Recebido | Qualidade (ok / parcial / inútil) | Observação |
|---|---|---|---|---|---|---|

Gate da Coleta (todos sim):
- [ ] A: ≥ 6 meses e ≥ 30 negócios fechados, com etapa
- [ ] B: ≥ 2 transcrições por etapa escolhida, ≥ 1 ganho
- [ ] C: ≥ 1 documento de processo ou PPT de proposta (ou ausência registrada e D completa)
- [ ] D: ≥ 2 entrevistas (obrigatório se C estiver vazia)
- [ ] Lacunas listadas com dono e data

## Cuidados
- Dado pessoal: transcrições e CRM têm nome, e-mail e telefone de clientes. Não copiar para fora da pasta do projeto; anonimizar no handbook final quando for material de treinamento externo.
- Não aceitar "resumo da IA" no lugar da transcrição: o resumo perde as perguntas literais.
- Não aceitar só negócios ganhos: sem perdidos não há contraste.
