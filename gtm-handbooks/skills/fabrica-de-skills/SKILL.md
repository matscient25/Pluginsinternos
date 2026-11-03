---
name: fabrica-de-skills
description: Converte handbooks de processo de GTM em skills do Claude que o time comercial executa no dia a dia - arquitetura (skill mestre roteadora, contexto da empresa, metodologia, uma skill por etapa do funil, CRM e avaliação de reunião), anatomia de SKILL.md (frontmatter name e description com o que faz, quando usar e gatilhos), divulgação progressiva com references, modos preparar/conduzir/registrar/revisar, casos de teste e empacotamento em .skill. Use ao criar, revisar ou empacotar skills a partir de um handbook, playbook ou processo comercial.
---

# Fábrica de skills

Handbook é para ler. Skill é para **executar**. O vendedor diz "tenho diagnóstico amanhã com a conta X" e a skill prepara a reunião, sugere as perguntas, e depois registra no CRM no padrão do handbook.

## 1. O que é uma skill
Uma pasta com:
```
<nome-da-skill>/
├── SKILL.md          obrigatório: frontmatter YAML + instruções em Markdown
├── references/       opcional: material lido só quando preciso (perguntas, exemplos, regras longas)
├── scripts/          opcional: código executável (ex.: cálculo de ROI)
└── assets/           opcional: modelos usados na saída (e-mail, proposta)
```
O Claude carrega em 3 níveis (divulgação progressiva):
1. **Frontmatter** (nome e descrição): sempre carregado. Serve para o Claude decidir **quando** usar.
2. **Corpo do SKILL.md**: carregado quando a skill é acionada. Contém o passo a passo.
3. **references/ e scripts/**: lidos só se o passo pedir.

Analogia: conectores (MCP) são a cozinha (acesso ao CRM, ao gravador, ao Drive); skills são as receitas (como fazer bem).

## 2. Arquitetura de skills de GTM de uma empresa
| Skill | Função | Origem |
|---|---|---|
| `<empresa>-como-usar` | Mestre roteadora: lista as skills, diz qual usar em cada tarefa e em que ordem | Mapa dos handbooks |
| `<empresa>-contexto` | Empresa, produto, ICP, personas, concorrência, vocabulário, provas | `declarado.md`, contexto |
| `<empresa>-metodologia` | A lente aplicada: elementos, escala 0–3, perguntas, critério por etapa | `02-lente/lente.md` |
| `<empresa>-<etapa>` | Uma por handbook: preparar, conduzir, registrar a etapa | Seções 3 a 9 do handbook |
| `<empresa>-crm` | Etapas, campos, onde registrar cada coisa, regras de passagem | Definições do CRM, seção 7 do handbook |
| `<empresa>-avaliar-reuniao` | Lê uma transcrição e devolve nota por elemento da lente e coaching | Lente + ficha de reunião |

Comece com mestre + contexto + metodologia + 1 etapa (a de maior vazamento). Acrescente as outras depois de testar.

## 3. Frontmatter (o que mais decide se a skill funciona)
```yaml
---
name: vektor-diagnostico
description: Prepara, conduz e registra a reunião de Diagnóstico da Vektor no padrão Challenger - hipóteses por papel, perguntas para quantificar o custo do problema, critério de saída e registro no CRM. Use quando o vendedor disser que tem um diagnóstico, uma segunda reunião ou uma sessão técnica com uma conta, pedir perguntas para quantificar o problema ou quiser registrar o resultado de um diagnóstico.
---
```
Regras:
- `name`: minúsculas, números e hífen (kebab-case), **igual ao nome da pasta**, sem espaços. Não usar "claude" nem "anthropic".
- `description`: **o que faz + quando usar + gatilhos** (frases que o vendedor diria). Até 1024 caracteres. Sem `<` ou `>`.
- Mencione os termos do dia a dia do time (nome da etapa no CRM, apelidos da reunião).
- Se a skill aciona demais, diga também quando **não** usar.

## 4. Corpo da skill de etapa (modelo `${CLAUDE_PLUGIN_ROOT}/templates/skill-etapa.md`)
1. **Quando usar** (1 a 3 linhas).
2. **Antes de começar:** o que ler (`<empresa>-contexto`, `<empresa>-metodologia`) e que dado buscar (CRM, transcrições anteriores da conta). Critério de entrada da etapa: se não estiver cumprido, avisar.
3. **Modos:**
   - **Preparar:** monta o plano da reunião (objetivo, hipóteses por papel, 5 a 8 perguntas do handbook, material a levar, próximo passo a propor).
   - **Conduzir:** cola de bolso (perguntas na ordem, sinais de avanço e de risco, respostas a objeções).
   - **Registrar:** a partir da transcrição ou do relato, preenche os campos do CRM, nota por elemento da lente e o próximo passo com data. **Mostra antes de gravar e pede confirmação.**
   - **Revisar:** avalia a reunião contra o critério de saída e diz se o negócio pode avançar.
4. **Critério de saída** da etapa (copiado do handbook).
5. **Red flags** que a skill deve apontar.
6. **Referências:** `<skill>/references/perguntas.md`, `<skill>/references/objecoes.md`, `<skill>/references/exemplos.md` (trechos reais).

Mantenha o SKILL.md curto (até ~300 linhas). Listas longas vão para `references/`.

## 5. Skill mestre (modelo `${CLAUDE_PLUGIN_ROOT}/templates/skill-mestre.md`)
Duas tabelas: **mapa das skills** (skill × quando usar) e **qual ler para cada tarefa** (tarefa × ordem de leitura). Diga "leia sempre primeiro" na descrição.

## 6. Testes antes de entregar
Escreva em `05-skills/<skill>/testes.md`:
- **Gatilho (3 que devem acionar, 2 que não devem):** frases reais do time. Ex.: aciona em "tenho diagnóstico amanhã com a Orbita"; não aciona em "qual o preço do squad?".
- **Execução (2 casos):** entrada (conta, transcrição) e o que a saída precisa conter.
- **Comparação:** mesma tarefa com e sem a skill; a versão com skill deve seguir o handbook (perguntas, critério, registro).
Rode `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/validar_skill.py 05-skills/` antes de empacotar.

## 7. Empacotar e distribuir
`python3 ${CLAUDE_PLUGIN_ROOT}/scripts/empacotar_skill.py 05-skills/<skill>` gera `<skill>.skill` (zip com a pasta). Instalação: Claude (Cowork / claude.ai) → Configurações → Skills (ou Plugins) → enviar o arquivo. Para o time inteiro, junte as skills num plugin da empresa.

## Problemas comuns
| Sintoma | Causa provável | Ajuste |
|---|---|---|
| Skill não aciona | Descrição sem os termos do time | Acrescentar gatilhos reais na descrição |
| Aciona em tudo | Descrição ampla demais | Especificar etapa e dizer quando não usar |
| Ignora o passo a passo | Instruções longas ou vagas | Passos numerados, críticos no topo, detalhe em references |
| Inventa perguntas | Sem `<skill>/references/perguntas.md` | Copiar perguntas literais do handbook |
| Grava errado no CRM | Sem confirmação | Sempre mostrar o que vai gravar e pedir ok |
