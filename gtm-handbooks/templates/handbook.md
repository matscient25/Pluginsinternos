# Handbook · {{Processo}} · {{Empresa}}

| | |
|---|---|
| **Processo** | {{nome do processo, ex.: Diagnóstico}} |
| **Etapas do funil cobertas** | {{etapa de entrada}} → {{etapa de saída}} (nomes exatos do CRM) |
| **Metodologia** | {{Challenger / MEDDPICC / SPIN / ... / própria}} |
| **Motion** | {{low / mid / high touch}} · ticket {{faixa}} · ciclo típico {{dias}} |
| **Dono do handbook** | {{nome, cargo}} |
| **Versão** | 1.0 · {{data}} · próxima revisão {{data + 6 meses}} |
| **Evidências usadas** | {{n}} transcrições ({{ganhos/perdidos/abertos}}) · funil de {{período}} ({{n}} negócios) · {{n}} documentos · {{n}} entrevistas |

---

## 0. Em uma frase

> **{{Manchete que é a conclusão. Ex.: "Quem quantifica o custo do problema no diagnóstico converte 2x mais para proposta."}}** {{tag}}

| {{KPI 1}} | {{KPI 2}} | {{KPI 3}} | {{KPI 4}} |
|---|---|---|---|
| {{valor}} | {{valor}} | {{valor}} | {{valor}} |
| {{linha de contexto}} | {{linha de contexto}} | {{linha de contexto}} | {{linha de contexto}} |

No máximo 4 KPIs, todos `[MEDIDO]` ou marcados `[PRECISA DE DADO]`.

**O que isto significa:** {{2 a 3 linhas}}
**O que isto não significa:** {{1 a 2 linhas, limite da evidência}}

**Lacunas de dado** (o que falta, quem fornece, até quando):
- `[PRECISA DE DADO]` {{item}} · {{responsável}} · {{data}}

---

## 1. Identificação

| Atributo | Valor |
|---|---|
| Entra de | {{etapa/área anterior}} |
| Sai para | {{próxima etapa/área}} |
| Quem participa (empresa) | {{papéis}} |
| Quem participa (cliente) | {{papéis típicos, ex.: decisor, influenciador técnico}} |
| Duração típica da etapa | {{dias}} {{tag}} |
| Reuniões típicas | {{n}} de {{min}} min |

## 2. Por que esta etapa existe

- **Para o cliente:** {{o que ele ganha saindo desta etapa}}
- **Para a empresa:** {{o que a empresa precisa saber ou conquistar}}
- **Princípio da metodologia:** {{elemento(s) da lente que esta etapa executa, em 2 a 3 linhas}}

## 3. Hand-off de entrada

**O que a etapa anterior entrega** (com onde está registrado):
- [ ] {{item mensurável}} · {{onde: CRM campo X / pasta / e-mail}}
- [ ] {{item}} · {{onde}}

**O que esta etapa confere antes de começar:**
- [ ] {{validação}}

> ✅ **Critério de entrada:** {{condição binária}}

## 4. Passo a passo

Entre 3 e 5 passos. Cada passo segue o bloco abaixo.

### 4.{{n}} {{Nome do passo}}

**Foco:** {{objetivo do passo em 1 frase}}
**Elemento da metodologia:** {{ex.: Reframe / Metrics / Implication question}}

**Ações** (verbo + onde):
- [ ] {{Ação. Ex.: "Registrar o custo do problema no CRM, campo custo_do_problema"}}
- [ ] {{Ação}}

**Perguntas que funcionam** (literais, com fonte):
- "{{pergunta}}" — `[OBSERVADO: {{arquivo}} {{mm:ss}}]`

**Como fica uma boa execução:** "{{trecho curto real}}" — `[OBSERVADO: {{fonte}}]`

> ⚠ **Cuidado:** {{erro comum observado}} {{tag}}

| DRI | SLA | Critério de saída |
|---|---|---|
| {{papel}} | {{prazo}} | {{condição binária}} |

## 5. Sinais

| Tipo | O que o cliente diz ou faz | Leitura | Fonte |
|---|---|---|---|
| ✅ Avanço | "{{frase real}}" | {{o que indica}} | `[OBSERVADO: ...]` |
| ⚠ Risco | "{{frase real}}" | {{o que indica}} | `[OBSERVADO: ...]` |

## 6. Objeções e respostas

| Objeção (literal) | Princípio da metodologia | Resposta que funcionou | Fonte |
|---|---|---|---|
| "{{objeção}}" | {{princípio}} | {{resposta}} | `[OBSERVADO: ...]` |

## 7. Hand-off de saída

**O que esta etapa entrega:**
- [ ] {{entregável}} · {{onde}}

**O que a próxima etapa confere:**
- [ ] {{validação}} · se faltar → {{ação corretiva}}

> ✅ **Critério de saída:** {{condição binária, a mesma que move o negócio de etapa no CRM}}

## 8. Métricas

| Métrica | Linha de base | Meta | Fórmula | Fonte | Frequência | Dono |
|---|---|---|---|---|---|---|
| {{conversão da etapa}} | {{valor}} `[MEDIDO]` | {{meta}} | {{fórmula}} | {{CRM}} | {{semanal}} | {{papel}} |

## 9. Red flags

| Red flag | Como detectar | Severidade | Ação imediata | Dono |
|---|---|---|---|---|
| {{flag}} | {{sinal observável}} | 🔴 Crítico / 🟡 Atenção / 🟢 Acompanhar | {{ação}} | {{papel}} |

**Escalação:** 🔴 liderança em 24h · 🟡 gestor em 48h · 🟢 revisão semanal.

## 10. Declarado × Observado × Medido

| Tema | O que a empresa diz `[DECLARADO]` | O que o time faz `[OBSERVADO]` | O que o funil mostra `[MEDIDO]` | Decisão no handbook |
|---|---|---|---|---|
| {{tema}} | {{doc}} | {{transcrições}} | {{número}} | {{o que vale e por quê}} |

## 11. Skills que executam este handbook

| Skill | Quando usar | Comando |
|---|---|---|
| {{empresa}}-{{etapa}} | {{gatilho}} | `/{{nome}}` |

## 12. Aprovação

| Preenchido por | Revisado por | Aprovado por | Versão | Próxima revisão |
|---|---|---|---|---|
| {{nome}} | {{AE sênior}} | {{gestor}} | 1.0 | {{data}} |

Versionamento: 1.0 versão inicial · 1.x ajuste menor · 2.0 mudança de processo.
