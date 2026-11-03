# Roteiro da aula · Building GTM Handbooks & Skills

Certificação GTM Engineer · SCIENT · aula ao vivo de 2 horas.

- **Deck:** artifact de slides "Building GTM Handbooks & Skills" (28 slides, com notas do apresentador). Fonte dos slides em `aula/deck/` (um HTML por slide + `deck.json`).
- **Interface visual da jornada:** `aula/jornada.html` (abrir em aba separada; usar nos slides 9 e 23).
- **Plugin:** `gtm-handbooks` instalado no Claude que vai para o telão.
- **Kit da demo:** `exemplo/vektor/` (Consultoria Vektor × TechScale, Challenger, tudo fictício).

---

## Antes da aula (checklist do professor)

- [ ] Plugin instalado e `/handbooks` respondendo numa conversa nova.
- [ ] Kit `exemplo/vektor/` presente e `exemplo/vektor/saida-esperada/` aberto numa aba (plano B).
- [ ] Preencher os colchetes dos slides 15 e 24 com os números de `exemplo/vektor/saida-esperada/03-analise/funil.md`.
- [ ] Confirmar se pode citar o nome do cliente do case do slide 20 (educação). Se não, falar só "um cliente de educação".
- [ ] Card do plugin publicado no skills.scient.cc e download testado com um login de aluno.
- [ ] Interface `aula/jornada.html` aberta.
- [ ] Não citar nenhum cliente com pessoa presente na turma.

---

## Agenda (120 min)

| Tempo | Bloco | Slides | Objetivo |
|---|---|---|---|
| 0–5 | Abertura | 1–3 | Promessa: plugin, primeiro handbook, primeira skill |
| 5–20 | 1 · Por que handbooks morrem | 4–7 | Handbook de gaveta × skill; conector é cozinha, skill é receita; 3 níveis |
| 20–45 | 2 · O método | 8–13 | Declarado × observado × medido; 7 passos; 4 fontes; lente; tags |
| 45–60 | 3 · O modelo de handbook | 14–16 | 13 seções; manchete é conclusão; passo com frase real e critério binário |
| 60–80 | 4 · De handbook a skills | 17–21 | Anatomia; descrição; 5 tipos; case de 25 skills; testes |
| 80–100 | 5 · Demo ao vivo | 22–24 | Plugin rodando no kit Vektor |
| 100–120 | 6 · Mão na massa | 25–28 | Exercício de 18 min, régua de qualidade, instalação, regras de ouro |

Cortes se atrasar: slide 21 (testes) e slide 7 (três níveis) viram fala de 30 segundos. Nunca corte o Bloco 6 abaixo de 15 min.

---

## Roteiro da demo (Bloco 5, 14 min)

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

- Abertura: quem tem um playbook que o time abre toda semana?
- Bloco 1: no último playbook que vocês escreveram, quanto veio do livro e quanto veio das reuniões?
- Bloco 2: das 4 fontes, qual vocês conseguiriam pedir amanhã? Qual seria a mais difícil?
- Bloco 2: qual metodologia o time de vocês realmente fala no dia a dia?
- Bloco 3: qual seria a manchete do processo comercial de vocês hoje, em uma frase?
- Bloco 4: alguém reescreve em voz alta a descrição fraca do slide 18?
- Bloco 6: quem mostra a manchete do handbook que acabou de gerar?

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
