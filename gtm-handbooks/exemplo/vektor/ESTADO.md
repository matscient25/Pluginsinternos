> Dados fictícios para treinamento. Estado congelado no fim do passo 3, para a demo começar do meio (`/demo` pode pular para o passo 4). As saídas dos passos 2 e 3 estão em `saida-esperada/`.

# ESTADO · Handbooks & Skills · Consultoria Vektor

Atualizado em 2026-10-20 por analista de RevOps. Fonte da verdade do projeto: ler antes, atualizar depois.

## Escopo
| Item | Valor |
|---|---|
| Empresa | Consultoria Vektor · consultoria de desenvolvimento de software · ~300 engenheiros, 4 AEs |
| Processos (1 a 5) | 1 Qualificação · 2 Diagnóstico · 3 Proposta · 4 Negociação/Contrato · 5 Handoff CS |
| Etapas do CRM (nomes exatos) | Qualificação → Diagnóstico → Proposta → Follow-up → Contrato → Ganho / Perdido |
| CRM | Export CSV (`01-coleta/A-numeros/deals.csv`) |
| Metodologia | Challenger Sale · motivo: o cliente acha que falta gente; ganhar exige reenquadrar o problema e sair da comparação por preço/hora |
| Aprovador dos handbooks | Gestor comercial · validador: Lucas Andrade (AE sênior) |
| Prazo | 2026-11-30 |

## Jornada
| # | Passo | Status | Gate | Saída |
|---|---|---|---|---|
| 0 | Escopo | ✅ | ✅ | ESTADO.md |
| 1 | Coleta | ✅ | ✅ (Handoff CS pendente) | 01-coleta/inventario.md |
| 2 | Lente | ✅ | ✅ | saida-esperada/02-lente/lente.md |
| 3 | Análise | ✅ | ✅ | saida-esperada/03-analise/sintese.md |
| 4 | Handbook | ⬜ | ⬜ | 04-handbooks/ (gabarito: saida-esperada/04-handbooks/diagnostico.md) |
| 5 | Skills | ⬜ | ⬜ | 05-skills/ (gabarito: saida-esperada/05-skills/) |
| 6 | Validação | ⬜ | ⬜ | 06-validacao/relatorio.md |

Legenda: ⬜ não iniciado · 🟨 em andamento · ✅ concluído · ⛔ bloqueado

## Pendências
| O que falta | Quem fornece | Até quando | Bloqueia |
|---|---|---|---|
| 2 propostas reais enviadas | Gestor comercial | 2026-10-23 | Handbook de Proposta |
| Tabela de preço e alçadas de desconto | Gestor comercial | 2026-10-23 | Handbook de Negociação/Contrato |
| Entrevista de CS (Camila Reis) | RevOps | 2026-10-24 | Handbook de Handoff CS |
| Campo `custo_do_problema` no CRM | Admin do CRM | antes do passo 6 | Validação |

## Decisões
| Data | Decisão | Por quê |
|---|---|---|
| 2026-10-09 | Metodologia Challenger; BANT do manual vira checklist mínimo de qualificação | Comprador não sabe o que comprar; venda complexa e multistakeholder |
| 2026-10-16 | Diagnóstico é o primeiro handbook | Menor conversão do funil (54%) e maior diferença entre vendedores |
| 2026-10-20 | Handbook de Handoff CS só após entrevista de CS | Sem evidência do lado do CS |

## Próximo comando
`/handbook diagnostico`
