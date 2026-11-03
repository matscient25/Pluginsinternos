---
name: metodo-handbooks
description: Skill mestre do GTM Handbooks & Skills Kit. Explica o método de 7 passos (Escopo, Coleta, Lente, Análise, Handbook, Skills, Validação) para transformar o processo comercial real de uma empresa em handbooks operacionais e skills, com qualquer metodologia de vendas. Define pastas, ESTADO.md, gates binários, tags de evidência e regras de ouro. Use sempre primeiro, antes de qualquer trabalho de handbook, playbook, documentação de processo comercial ou criação de skills de GTM, e quando alguém perguntar "por onde começo" ou "qual o próximo passo".
---

# Método GTM Handbooks & Skills

## Tese
O handbook é o espelho do processo que **funciona**. Ele nasce do cruzamento de três visões:

| Visão | Fonte | Pergunta |
|---|---|---|
| **Declarado** | Documentos, processos escritos, PPTs de proposta e de produto, conclusões de análises | O que a empresa diz que faz? |
| **Observado** | Transcrições de reuniões por etapa (ganhos, perdidos, abertos) | O que o time faz de verdade? |
| **Medido** | Export do funil do CRM | O que dá resultado e onde o funil quebra? |

A **metodologia** (Challenger, MEDDPICC, SPIN, SPICED, BANT, GPCTBA, própria) é a **lente** que organiza a leitura das três visões. O método não muda com a metodologia.

## Os 7 passos e os gates

| # | Passo | Agente | Saída | Gate (todos sim para avançar) |
|---|---|---|---|---|
| 0 | Escopo | `maestro` | `ESTADO.md` | Empresa, processos (1 a 5), etapas do CRM, metodologia e aprovador definidos |
| 1 | Coleta | `coletor` | `01-coleta/inventario.md` | Fonte A com ≥ 6 meses de negócios · fonte B com ≥ 2 transcrições por etapa escolhida, incluindo ≥ 1 ganho · fonte C com ≥ 1 documento de processo ou PPT · lacunas registradas com dono |
| 2 | Lente | `metodologista` | `02-lente/lente.md` | Todo elemento com definição, evidência observável, escala 0–3 e perguntas · mapa elemento × etapa preenchido · validada por alguém da empresa |
| 3 | Análise | `analista-conversas`, `analista-funil`, `analista-documentos` | `03-analise/` | 1 ficha por transcrição · `funil.md` com números calculados pelo script · `declarado.md` · `sintese.md` com divergências e padrões de ganho |
| 4 | Handbook | `redator-handbook` | `04-handbooks/<processo>.md` e `.html` | Checklist de handbook do `qualidade-handbooks` 100% sim |
| 5 | Skills | `arquiteto-skills` | `05-skills/` | `validar_skill.py` sem erro · skill mestre + contexto + metodologia + 1 por etapa · casos de teste escritos |
| 6 | Validação | `revisor` | `06-validacao/relatorio.md` | Veredito "Pronto" em todos os handbooks · teste de gatilho e de execução registrado |

Se um gate falha, o maestro **não avança**: lista o que falta, quem fornece e o comando para resolver.

## Onde fica cada coisa

Conhecimento (só leitura) vem do plugin: `${CLAUDE_PLUGIN_ROOT}/skills`, `templates`, `scripts`.
Trabalho da empresa fica na pasta do projeto, versionada se houver git:

```
handbooks/<empresa-slug>/
├── ESTADO.md                 fonte da verdade do projeto (ler antes, atualizar depois)
├── 01-coleta/
│   ├── A-numeros/            export(s) do CRM (.csv)
│   ├── B-conversas/          transcrições (.md, .txt, .vtt, .docx)
│   ├── C-documentos/         processos, PPTs, propostas, análises
│   ├── D-pessoas/            notas das entrevistas
│   ├── data-request.md       o pedido enviado
│   └── inventario.md         o que chegou e a qualidade
├── 02-lente/lente.md
├── 03-analise/
│   ├── fichas/               1 ficha por reunião
│   ├── funil.md              saída do funil.py + leitura
│   ├── declarado.md          processo declarado extraído dos documentos
│   └── sintese.md            triangulação, divergências, padrões de ganho
├── 04-handbooks/             1 por processo (.md fonte + .html para leitura)
├── 05-skills/                1 pasta por skill + .skill empacotados
└── 06-validacao/relatorio.md
```

No Cowork sem pasta local, use a pasta de trabalho que o usuário indicar (ou o Drive conectado) com a mesma estrutura.

## Tags de evidência (obrigatórias em handbook, síntese e lente)

| Tag | Quando usar |
|---|---|
| `[OBSERVADO: arquivo mm:ss]` | Visto numa transcrição |
| `[DECLARADO: documento]` | Está escrito num documento ou PPT da empresa |
| `[MEDIDO: funil.md]` | Calculado pelo script sobre o export do CRM |
| `[ENTREVISTA: papel]` | Dito numa entrevista |
| `[BENCHMARK: fonte]` | Referência externa citada |
| `[HIPÓTESE]` | Leitura do analista, sem medição |
| `[PRECISA DE DADO]` | Falta evidência; listar quem fornece |

Nunca apresentar `[HIPÓTESE]` como fato. Número sem tag não entra.

## Regras de ouro
1. **Nada inventado.** Número vem do script, frase vem da transcrição, regra vem do documento.
2. **Observado ganha do declarado.** Divergência vai para a seção 10 do handbook com a decisão tomada.
3. **Frase real do cliente.** Perguntas, sinais e objeções com fonte.
4. **Critério binário.** Entrada e saída de cada etapa respondem sim ou não.
5. **Faltou dado, para.** Lista o que falta, quem fornece e até quando.
6. **Um handbook por processo.** 3 a 5 passos, checklists de até 15 itens.
7. **Skill boa é skill usada.** Gatilho claro, passos executáveis, teste com caso real.

## Como conduzir uma sessão
1. Ler `ESTADO.md` (se não existir, rodar `/iniciar`).
2. Identificar o primeiro passo com gate vermelho.
3. Rodar o agente do passo. Ao terminar, conferir o gate.
4. Atualizar `ESTADO.md` (passo, gate, pendências, próximo comando) e salvar.
5. Dizer ao usuário em 3 linhas: o que foi feito, o que falta, o próximo comando.

## Qual skill ler para cada tarefa
| Tarefa | Leia |
|---|---|
| Montar ou validar o pedido de dados | `data-request` |
| Escolher ou montar a metodologia | `lentes-metodologia` |
| Ler transcrições, funil, documentos | `analise-triangulada` |
| Escrever handbook | `modelo-handbook` |
| Gerar skills | `fabrica-de-skills` |
| Revisar e testar | `qualidade-handbooks` |
