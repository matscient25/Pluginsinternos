> Dados fictícios para treinamento.

# Testes · vektor-diagnostico

## Gatilho
| Frase do AE | Deve acionar? |
|---|---|
| "Tenho diagnóstico amanhã com a Orbita Pay, me ajuda a preparar?" | sim |
| "Segue a transcrição da segunda reunião com a TechScale, registra no CRM" | sim |
| "Esse negócio pode ir para proposta?" | sim |
| "Monta a proposta da TechScale" | não (etapa Proposta) |
| "Qual o preço do squad dedicado?" | não |

## Execução
1. **Entrada:** transcrição `01-coleta/B-conversas/2026-08-10_TechScale_diagnostico.md`, modo Registrar.
   **A saída precisa conter:** custo do problema R$ 3 a 3,8 mi/ano de retrabalho + R$ 1,4 mi de ARR em risco; critério "80% de aderência ao roadmap"; proposta com CTO, Head de Eng e CPO; pedido de confirmação antes de gravar; resposta "pode ir para Proposta: sim".
2. **Entrada:** transcrição `01-coleta/B-conversas/2026-07-07_Orbita_Pay_diagnostico.md`, modo Revisar.
   **A saída precisa conter:** "não pode ir para Proposta"; falta custo do problema e reunião com o CFO; red flag de preço por hora antes do custo; próxima ação concreta.

## Comparação com e sem a skill
Pedir "prepara meu diagnóstico com a Kora Pay" sem a skill e com a skill. Com a skill, o plano deve trazer as perguntas literais de `references/perguntas.md`, a conta do custo do problema e o próximo passo com participantes; sem deck e sem preço.
