# Roteiro da aula · Building GTM Handbooks & Skills

Certificação GTM Engineer · SCIENT · aula ao vivo de 2 horas.

- **Deck:** artifact de slides "Building GTM Handbooks & Skills" (34 telas com cara de interface, racional da aula, com notas do apresentador). Fonte em `aula/deck/` (um HTML por slide + `deck.json`; gerador em `aula/deck/_gerador/`).
- **Interface visual da jornada:** `aula/jornada.html` (apoio para tirar dúvidas sobre o fluxo).
- **Plugin:** `gtm-handbooks` instalado no Claude que vai para o telão.
- **Kit da demo:** `exemplo/vektor/` (Consultoria Vektor × TechScale, Challenger, tudo fictício).

---

## Antes da aula (checklist do professor)

- [ ] Deck aberto no modo apresentação (34 telas com cara de interface; a barra lateral mostra o passo da jornada).
- [ ] Confirmar se pode citar o nome do cliente do case da tela 27 (educação). Se não, falar só "cliente de educação".
- [ ] Card do kit publicado no skills.scient.cc e download testado com um login de aluno (citado na tela 33).
- [ ] Opcional: plugin instalado e `exemplo/vektor/saida-esperada/` aberto, para a demo extra.
- [ ] Não citar nenhum cliente com pessoa presente na turma.

---

## Versão curta (35–40 min) · a que vai para a aula

O deck principal mostra 18 telas; as outras 16 ficam ocultas (puladas na apresentação, marcadas como "extra"). A versão completa, com as 34 telas visíveis, está num deck à parte: "Building GTM Handbooks & Skills (versão completa)".

| Passo | Telas (versão curta) | Min |
|---|---|---|
| Abertura | 1 Capa | 1 |
| 1 · Por quê | 2 Por que ninguém usa o playbook · 3 Como a empresa vende de verdade (GPS) · 4 O que muda quando vira skill · 5 Os 7 passos | 9 |
| 2 · Coletar | 6 O que pedir (4 fontes) · 7 Peça também o que já está escrito | 5 |
| 3 · Metodologia | 8 A metodologia diz o que procurar | 2 |
| 4 · Analisar | 9 Manual × prática · 10 Perdas por preço | 5 |
| 5 · Documentar | 11 As 14 partes · 12 A rubrica | 5 |
| 6 · Executar | 13 Os 5 tipos de skill · 14 Cliente real, 25 skills | 4 |
| 7 · Melhoria contínua | 15 Duas reuniões, uma rubrica · 16 O que o vendedor recebe | 4 |
| Fechamento | 17 Por onde começar · 18 Regras de ouro | 2 |

Total ≈ 37 min. Para 30 min, corte 10 (perdas por preço) e 14 (case). Nunca corte 12, 15 e 16 (rubrica e coaching).

Para mudar o que aparece na versão curta: editar `CURTA` em `aula/deck/_gerador/gen_deck.py` e rodar `python3 aula/deck/_gerador/gen_deck.py`. Para a completa: `DECK_COMPLETO=1 DECK_ROOT=aula/deck-completo python3 aula/deck/_gerador/gen_deck.py`.

---

## Agenda da versão completa (120 min) · o deck é o racional, não o manual do plugin

| Tempo | Bloco | Telas | O que a turma precisa sair entendendo |
|---|---|---|---|
| 0–18 | Abertura e Por quê | 1–6 | Handbook morre na gaveta; a tese declarado × observado × medido; com IA o handbook vira execução; a jornada em 7 passos |
| 18–40 | Coletar | 7–12 | As 4 fontes, o que cada uma revela, o que pedir e quanto basta. Ênfase na fonte C (documentos), a que mais falta |
| 40–47 | Metodologia | 13–14 | Qualquer metodologia serve: ela diz o que procurar em cada reunião e quando o negócio pode mudar de etapa |
| 47–62 | Analisar | 15–18 | Cruzar as três visões; hipótese da gestão desmentida pelo funil; o que só aparece nos ganhos |
| 62–82 | Documentar | 19–24 | O que documentar, as 14 partes do handbook, começar pela conclusão, como escrever um passo, **a rubrica da etapa**, de onde vem cada informação |
| 82–92 | Executar | 25–27 | Tipos de skill; como o vendedor usa no dia a dia; case de 25 skills |
| 92–107 | Melhoria contínua | 28–32 | Como saber se está pronto; **coaching de cada reunião com a rubrica** (ganha × perdida, o que o vendedor recebe, quem usa o resultado); como manter atualizado |
| 107–110 | Fechamento | 33–34 | Por onde começar; regras de ouro |
| 110–120 | Perguntas (ou demo extra) | — | Ver abaixo |

Cortes se atrasar: telas 11 (pessoas) e 24 (tags) viram fala de 30 segundos. Nunca corte as telas 23 e 29–31 (rubrica e coaching): são o ponto central do método.

---

## Demo extra, opcional (fora do deck, 10 min)

Abra uma conversa nova no Claude com o plugin. Narre cada passo em voz alta.

| # | Comando ou ação | O que deve aparecer | O que falar |
|---|---|---|---|
| 1 | `/handbooks` | Nenhum projeto ativo; o maestro sugere `/iniciar` ou `/demo` | "O maestro sempre começa lendo o estado." |
| 2 | `/demo` | O maestro carrega `exemplo/vektor/`, cria o ESTADO.md e mostra o escopo: 5 processos, Challenger | "Empresa fictícia. Mesma jornada que vocês vão rodar." |
| 3 | (Coleta) | Inventário das 4 fontes: números, conversas (6 do ganho + 2 perdidos), documentos (4), pessoas (2). Gate verde | Mostre a fonte C: manual oficial, PPT de proposta, PPT de produto, win/loss |
| 4 | (Lente) | Lente Challenger: Teach, Tailor, Take Control, passos do pitch, escala 0–3, mapa por etapa | "Se fosse MEDDPICC, só esta lente mudava." |
| 5 | (Análise) | Três analistas em paralelo: fichas por reunião, leitura do funil (`scripts/funil.py`), processo declarado | Pare numa ficha: mostre nota 0–3 e citação com minuto |
| 6 | (Síntese) | Tabela declarado × observado × medido com divergências | Divergência-chave: o manual manda propor logo após a qualificação; quem ganha faz diagnóstico com custo quantificado |
| 7 | `/handbook diagnostico` | Handbook do Diagnóstico no modelo padrão | Leia a manchete, os KPIs, uma pergunta com tag `[OBSERVADO]` e a seção 10 |
| 8 | `/gerar-skills` | `vektor-diagnostico` e `vektor-como-usar`, validadas por `scripts/validar_skill.py` | Leia a description em voz alta: o que faz, quando, gatilhos |
| 9 | (Teste) | Escreva: "amanhã tenho o diagnóstico com a TechScale, me prepara" | A skill carrega e guia a preparação |
| 10 | `/validar` | Relatório: Pronto / Ajustar / Refazer e o que falta | "O revisor é o advogado do diabo." |

Se a demo atrasar, pule de 5 direto para 7 com o handbook do gabarito.

### Plano B

Se o plugin travar, a conexão cair ou a geração demorar mais de 3 min num passo:

1. Abra `exemplo/vektor/saida-esperada/` e siga a mesma narrativa com os arquivos prontos:
   `02-lente/lente.md` → `03-analise/fichas/` → `03-analise/funil.md` → `03-analise/sintese.md` → `04-handbooks/diagnostico.md` → `05-skills/vektor-diagnostico/SKILL.md`.
2. Use `aula/jornada.html` para mostrar o fluxo dos agentes.
3. Diga à turma: "o gabarito foi gerado pelo mesmo plugin; vocês vão rodar no exercício".

---

## Perguntas para a turma

- Abertura (tela 3): no último playbook que vocês escreveram, quanto veio do livro e quanto veio das reuniões?
- Coletar (tela 7): das 4 fontes, qual vocês conseguiriam pedir amanhã? Qual é a mais difícil?
- Coletar (tela 10): que documento da empresa de vocês contradiz o que o time faz?
- Metodologia (tela 13): qual metodologia o time realmente fala no dia a dia?
- Analisar (tela 16): qual hipótese da gestão de vocês nunca foi testada no funil?
- Documentar (tela 21): qual seria a manchete do processo comercial de vocês hoje, em uma frase?
- Coaching (tela 29): quantas gravações do time o gestor de vocês consegue ouvir por semana? E se todas fossem avaliadas pela rubrica?
- Melhoria contínua (tela 28): quem de fora do projeto poderia fazer o teste do vendedor novo?

---

## Exercício (Bloco 6, 18 min)

Regra: um processo só. Sugestão: Discovery ou Diagnóstico.

| Minuto | Comando | Entrega |
|---|---|---|
| 0–2 | `/iniciar` | ESTADO.md com 1 processo e a metodologia |
| 2–5 | `/coleta` | Data request das 4 fontes e inventário |
| 5–8 | `/lente` | Lente da metodologia |
| 8–14 | `/analise` + `/handbook` | Síntese e handbook de 1 processo |
| 14–18 | `/gerar-skills` | 1 skill de etapa validada |

- Com a própria empresa e sem dados à mão: sair com o data request pronto para enviar e a lente montada.
- Com o kit Vektor: chegar até a skill.
- Fechamento do exercício: 2 alunos mostram a manchete.

## Depois da aula

- Enviar o link do skills.scient.cc e este roteiro para a turma.
- Pedir que cada aluno mande o data request para o time na mesma semana.
