# GTM Handbooks & Skills Kit

Plugin do Claude (Cowork e Claude Code) que transforma o processo comercial **real** de uma empresa em:

1. **Handbooks operacionais** por processo ou etapa do funil, num modelo padrão (o que fazer, quem faz, quando passa de etapa, o que medir, o que dá errado).
2. **Skills** que o time executa com o Claude no dia a dia ("vou fazer uma discovery com a conta X" → a skill guia perguntas, checklist e registro no CRM).

Funciona com **qualquer metodologia**: Challenger, MEDDPICC, SPIN, SPICED, BANT, GPCTBA/C&I ou uma metodologia própria da empresa. A metodologia entra como uma **lente**; o método é sempre o mesmo.

> Material da certificação **Building GTM Handbooks & Skills** (SCIENT). Distribuído em [skills.scient.cc](https://skills.scient.cc).

---

## A ideia em uma frase

> O handbook é o espelho do processo que **funciona**, não do processo ideal. Ele nasce do cruzamento de três visões: o que a empresa **diz** que faz (documentos), o que o time **faz** (conversas) e o que **dá resultado** (funil).

```
   DECLARADO                OBSERVADO                 MEDIDO
   documentos, PPTs,        transcrições de           funil do CRM:
   processos, propostas     reuniões por etapa        conversão, ciclo, perdas
        \                        |                        /
         \_______________  LENTE DA METODOLOGIA  _______/
                                 |
                          HANDBOOK por etapa
                                 |
                          SKILLS do time
```

---

## A jornada em 7 passos

| # | Passo | Pergunta que responde | Agente | Saída (em `handbooks/<empresa>/`) |
|---|---|---|---|---|
| 0 | **Escopo** | Quais processos, qual metodologia, quem aprova? | `maestro` | `ESTADO.md` |
| 1 | **Coleta** | Temos evidência suficiente das 4 fontes? | `coletor` | `01-coleta/inventario.md` |
| 2 | **Lente** | Como a metodologia escolhida vira critério de análise? | `metodologista` | `02-lente/lente.md` |
| 3 | **Análise** | O que o time diz, faz e o que dá resultado? | `analista-conversas`, `analista-funil`, `analista-documentos` | `03-analise/` (fichas, funil, declarado, síntese) |
| 4 | **Handbook** | Qual é o processo que funciona, etapa por etapa? | `redator-handbook` | `04-handbooks/*.md` e `.html` |
| 5 | **Skills** | Como o time executa o handbook com o Claude? | `arquiteto-skills` | `05-skills/<skill>/SKILL.md` e `.skill` |
| 6 | **Validação** | Um vendedor novo consegue usar sem coaching? | `revisor` | `06-validacao/relatorio.md` |

Cada passo tem um **gate binário** (passa ou não passa). Sem gate verde, o maestro não avança. Detalhes em `skills/metodo-handbooks/SKILL.md`.

### As 4 fontes da Coleta (o data request)

| Fonte | O que pedir | Por que |
|---|---|---|
| **A. Números** | Export do CRM: negócios com etapa, datas de entrada em cada etapa, valor, dono, status, motivo de perda | Mostra onde o funil quebra e dá a linha de base das métricas |
| **B. Conversas** | 2 a 4 transcrições por etapa, de negócios ganhos, perdidos e em aberto, com metadados | Mostra o comportamento real que gera avanço |
| **C. Documentos** | Processos já documentados, playbooks, conclusões de análises (win/loss, post-mortem), PPT de proposta, PPT de produto, tabela de preço, battlecards, materiais de onboarding, definição de ICP | Mostra o processo declarado, a mensagem oficial e as provas que o time usa |
| **D. Pessoas** | 3 entrevistas de 30 min: top performer, gestor comercial, CS/implantação | Preenche o que não está escrito e explica as divergências |

---

## Os 9 agentes

| Agente | Papel |
|---|---|
| `maestro` | Orquestra a jornada, mantém o `ESTADO.md`, aplica os gates e decide o próximo passo. Não escreve artefato. |
| `coletor` | Gera o data request, valida o que chegou e monta o inventário de evidências. |
| `metodologista` | Converte qualquer metodologia (livro, site, documento interno) numa lente de análise com escala 0–3. |
| `analista-conversas` | Lê transcrições e gera uma ficha de evidência por reunião, na lente da metodologia. Roda em lotes paralelos. |
| `analista-funil` | Roda o script de funil sobre o export do CRM e interpreta conversão, ciclo e perdas por etapa. |
| `analista-documentos` | Extrai dos documentos e PPTs o processo declarado, a mensagem oficial, as provas e as regras. |
| `redator-handbook` | Triangula declarado × observado × medido e escreve o handbook no modelo padrão. |
| `arquiteto-skills` | Converte o handbook em skills (mestre, contexto, metodologia e uma por etapa) e empacota em `.skill`. |
| `revisor` | Aplica os checklists de qualidade e os testes de gatilho e de execução das skills. |

## Comandos

| Comando | O que faz |
|---|---|
| `/handbooks` | Porta de entrada: mostra o estado do projeto e roda o próximo passo |
| `/iniciar` | Cria o projeto de uma empresa (escopo, processos, metodologia) |
| `/coleta` | Gera o data request e valida o que já chegou |
| `/lente` | Monta a lente da metodologia |
| `/analise` | Roda as três análises e a síntese |
| `/handbook` | Escreve o handbook de um processo |
| `/gerar-skills` | Gera as skills a partir dos handbooks |
| `/validar` | Roda os checklists e testes |
| `/demo` | Roda a jornada inteira com o kit de exemplo (Challenger, empresa fictícia) |

## Estrutura do plugin

```
gtm-handbooks/
├── .claude-plugin/plugin.json
├── agents/        9 agentes
├── commands/      9 comandos
├── skills/        conhecimento do método (7 skills)
│   ├── metodo-handbooks/      skill mestre: jornada, gates, regras de ouro
│   ├── data-request/          o que pedir, como validar
│   ├── lentes-metodologia/    formato da lente + lentes prontas
│   ├── analise-triangulada/   fichas, tags de evidência, síntese
│   ├── modelo-handbook/       o modelo padrão de handbook
│   ├── fabrica-de-skills/     como transformar handbook em skill
│   └── qualidade-handbooks/   checklists e testes
├── templates/     modelos em branco (ESTADO, data request, ficha, lente, handbook, skills)
├── scripts/       funil.py, validar_skill.py, empacotar_skill.py
├── exemplo/       kit de demonstração (Consultoria Vektor × TechScale, Challenger, fictício)
└── aula/          material da aula
```

## Instalação

**Claude Code (marketplace interno):**
```
/plugin install gtm-handbooks --marketplace matscient25/Pluginsinternos
```

**Claude Cowork / claude.ai:** baixe o `.zip` em [skills.scient.cc](https://skills.scient.cc), vá em *Configurações → Plugins → Adicionar* e envie o arquivo. Depois digite `/handbooks`.

Requisitos: Python 3 para os scripts (`funil.py` usa só biblioteca padrão). Conectores opcionais: CRM (HubSpot), gravador de reuniões (Fathom, Fireflies), Google Drive.

## Regras de ouro

1. **Nada inventado.** Toda afirmação do handbook carrega uma tag de evidência: `[OBSERVADO]`, `[DECLARADO]`, `[MEDIDO]`, `[BENCHMARK]`, `[HIPÓTESE]` ou `[PRECISA DE DADO]`.
2. **O observado ganha do declarado.** Se o documento diz uma coisa e as conversas mostram outra, o handbook documenta o real e registra a divergência.
3. **Frase real do cliente.** Perguntas, sinais e objeções vêm das transcrições, com fonte. Sem fonte, não entra.
4. **Critério de saída binário.** Toda etapa termina numa condição que dá para responder com sim ou não.
5. **Faltou dado, para.** O agente lista o que falta e quem fornece, em vez de completar com suposição.
6. **Um handbook por processo, não por área.** De 3 a 5 etapas, checklists de até 15 itens.
7. **Skill boa é skill usada.** Cada skill tem gatilho claro, passos executáveis e um teste com caso real.
