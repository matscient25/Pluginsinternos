> Dados fictícios para treinamento. Transcrição adaptada do material "Transcrições Challenger Sale" (Officer Hour SCIENT); marcações de tempo aproximadas, inseridas para a aula.

# TechScale S/A · 2026-08-17 · Proposta

| Campo | Valor |
|---|---|
| Conta | TechScale S/A (deal VK-0101) |
| Etapa do funil | Proposta |
| Resultado do negócio | Ganho (fechado em 2026-09-11) |
| Dono do negócio | Lucas Andrade (AE) |
| Participantes | Lucas Andrade (AE, Vektor) · Fernanda Lima (CPO, TechScale) · Rafael Torres (CTO, TechScale) · Bruno Maia (Head de Engenharia, TechScale) |
| Duração | 75 min |
| Pauta do convite | Apresentar arquitetura de solução conectada diretamente às dores diagnosticadas |
| Gravado por | Gravador de reuniões (export em texto) |

---

[01:00] **Lucas:** Antes de começar, quero contextualizar a Fernanda, que não estava nas reuniões anteriores. Passamos duas sessões mapeando o que está acontecendo com a engenharia de vocês. O que chegamos é que o problema não é falta de gente. É que a arquitetura de entrega de vocês — como os squads estão conectados, quem depende de quem — não foi desenhada para a escala atual. Vou mostrar isso com os números que o Bruno e o Rafael me trouxeram. Fernanda, me diz: da perspectiva de produto, como você vê essa dinâmica?

[08:03] **Fernanda:** Na prática, eu tenho um roadmap que foi comprometido com clientes e com o board. E toda vez que peço previsão de entrega, recebo respostas que mudam de semana em semana. Perdi credibilidade em algumas reuniões de cliente porque prometi datas que a engenharia não conseguiu cumprir.

[11:47] **Lucas:** Então o impacto chega até você em forma de credibilidade perdida com cliente. Isso é importante porque muda o que precisamos resolver — não é só um problema interno de engenharia. É um problema que afeta a relação com o cliente. Certo. Deixa eu mostrar o que mapeamos.

[15:35] *(Lucas apresenta síntese visual do diagnóstico)*

[16:03] Com base nas duas sessões anteriores, chegamos a três diagnósticos centrais. Primeiro: capacidade bloqueada por acoplamento. Os squads de novos produtos dependem dos squads core para avançar. Isso cria uma fila de espera permanente. Em média, vinte demandas por mês, com tempo médio de espera de duas a seis semanas. Segundo: retrabalho invisível. Estimamos o equivalente a um squad inteiro — cerca de R$3,5 milhões por ano — sendo consumido em bugs, refatoração e contexto perdido. Terceiro: risco de receita imediato. R$1,4 milhão em ARR em contratos sob risco por funcionalidades atrasadas.

[23:11] **Fernanda:** Esse número de R$1,4 milhão eu precisava ter em algum lugar documentado. Isso não estava explícito para mim.

[24:39] **Lucas:** Exato. E ele vai crescer se nada mudar, porque o backlog de integrações não para de aumentar. Antes de apresentar o que proponho, quero garantir que vocês entendam o que seria diferente se esse problema fosse resolvido. Não quero falar da nossa solução ainda — quero falar do que o mundo operacional de vocês pareceria se isso estivesse funcionando. Faz sentido?

[29:28] **Rafael:** Faz sentido. Continue.

[29:47] **Lucas:** Numa empresa de tecnologia com o perfil de vocês, o que resolve o paradoxo da capacidade bloqueada é separar dois tipos de trabalho que hoje brigam pela atenção dos mesmos engenheiros: o trabalho de manutenção e evolução do núcleo do produto — que exige contexto profundo, é sensível e só os seus sêniores conseguem fazer bem — e o trabalho de expansão: novas integrações, novos módulos, novos produtos que precisam ser construídos rápido com qualidade, mas com contexto mais isolado. Quando esses dois tipos de trabalho vivem no mesmo squad, brigam. E o núcleo sempre perde, porque integração nova parece mais urgente. Quando você os separa — estruturalmente, com times diferentes — o núcleo recupera foco e a expansão ganha velocidade. O que vocês precisam não é de mais engenheiros no mesmo sistema. É de um sistema diferente.

[40:34] **Fernanda:** Isso faz sentido. Mas como você garante que o time de expansão não crie uma dívida técnica nova que vai virar o problema do quarter seguinte?

[42:39] **Lucas:** Essa é a pergunta certa — e foi exatamente a preocupação que o Bruno levantou. Respondo isso já. Mas deixa eu primeiro conectar isso ao que proponho.

[44:50] *(Lucas apresenta a proposta)*

[45:08] Propomos três squads dedicados no modelo de expansão: um squad focado nas integrações dos novos produtos com o core — o principal gargalo hoje. Um squad focado em qualidade e testes automatizados — atacando diretamente o retrabalho. E um squad de roadmap de produto junto com a Fernanda — para construir as funcionalidades que estão travando renovações e expansões. Esses squads operam integrados ao time de vocês, nas suas cerimônias, no seu stack. Não são fornecedores externos — são capacidade adicional no seu sistema.

[51:39] Sobre a preocupação do Bruno: cada squad tem um tech lead sênior com mandato explícito de não criar dívida técnica. E o acordo de trabalho inclui revisão quinzenal com o Head de Engenharia de vocês para rastrear qualidade. Se algo sair do padrão, paramos antes de virar problema.

[55:23] **Bruno:** Isso resolve minha principal preocupação. O que não me serve é contratar gente externa que cria mais problema do que resolve e vai embora depois.

[57:24] **Lucas:** Entendido. E o modelo que propomos é justamente o oposto: queremos ser avaliados pelos mesmos critérios que Rafael me deu como régua de sucesso — oitenta por cento de aderência ao roadmap e o time core fora do ciclo de apagar incêndio. Se não chegarmos nisso em noventa dias, há cláusula de revisão no contrato.

[61:45] **Fernanda:** Qual é o investimento?

[62:08] **Lucas:** Três squads, modelo dedicado, contrato inicial de seis meses: R$540 mil por mês. Com os três riscos que mapeamos — R$3,5 milhões em retrabalho e R$1,4 milhão em ARR em risco — o break-even acontece antes do segundo mês.

[65:14] **Rafael:** O número não está fora da realidade. O que eu precisaria para levar isso ao Marcelo — nosso CEO — é um documento executivo de uma página: o problema, o custo de não resolver e a proposta. Ele não vai entrar em detalhes técnicos, mas vai querer o ROI claro.

[69:11] **Lucas:** Consigo ter esse documento até amanhã ao meio-dia. E proponho que agendemos a apresentação para o Marcelo para a semana que vem — pode ser uma sessão de trinta minutos com ele. Você e a Fernanda estariam lá?

[72:13] **Rafael:** Sim. Mando disponibilidade dele até o final do dia.
