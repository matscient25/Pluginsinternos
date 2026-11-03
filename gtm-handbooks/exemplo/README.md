# Kit de demonstração · Consultoria Vektor × TechScale (Challenger)

> **Dados fictícios para treinamento.** Empresas, pessoas, conversas e números foram criados para a aula. Nenhum dado de cliente real.

Kit para aprender e demonstrar ao vivo a jornada do plugin: **Escopo → Coleta → Lente → Análise → Handbook → Skills → Validação**, com a metodologia Challenger.

## O cenário
A **Consultoria Vektor** vende squads de engenharia para empresas de tecnologia. O manual de vendas manda abrir com o portfólio e dar o preço por hora. O AE com melhor resultado (Lucas Andrade) faz o contrário: não abre deck, faz um diagnóstico de 90 minutos e só sai com o **custo do problema em reais**. O kit tem tudo para o plugin descobrir isso sozinho, cruzando documentos, conversas e funil.

## Como rodar
```
/demo            # modo rápido (~10 min): Diagnóstico de ponta a ponta
/demo completo   # todos os processos e todas as transcrições
```
O `/demo` copia `vektor/` para `handbooks/vektor-demo/` e roda os passos. Ao fim de cada passo, compara o que gerou com o gabarito em `vektor/saida-esperada/`. Se algo falhar ao vivo, abra o arquivo do gabarito e siga.

Para começar do meio (passo 4), use `vektor/ESTADO.md`: ele está congelado no fim da Análise.

## O que tem em cada pasta

| Pasta / arquivo | O que é | O que prova na aula |
|---|---|---|
| `vektor/contexto-empresa.md` | Empresa, portfólio, ICP, personas, processo de decisão do cliente | O contexto que toda skill precisa |
| `vektor/01-coleta/A-numeros/deals.csv` | Export do CRM: 122 negócios (nov/2025–out/2026), formato largo, data de entrada por etapa | O funil mostra **onde** quebra |
| `vektor/01-coleta/A-numeros/_gerar_deals.py` | Gerador determinístico do CSV (seed fixa) | Transparência: dado sintético, reproduzível |
| `vektor/01-coleta/B-conversas/` | 6 reuniões do ciclo ganho da TechScale + 2 perdidos (Orbita Pay, Nuvia Saúde) | As conversas mostram **o que** funciona e o que não funciona |
| `vektor/01-coleta/C-documentos/` | Manual de vendas (desatualizado), PPT de proposta, PPT de portfólio, win/loss do gestor | O processo **declarado** e as crenças do time |
| `vektor/01-coleta/D-pessoas/` | Entrevistas com o top performer e com o gestor | O que não está escrito |
| `vektor/01-coleta/inventario.md` | Inventário das 4 fontes com o gate da Coleta | Como validar o data request |
| `vektor/ESTADO.md` | Estado do projeto no fim do passo 3 | A fonte da verdade do maestro |
| `vektor/saida-esperada/02-lente/lente.md` | Lente Challenger com 8 elementos, escala 0–3 e mapa elemento × etapa | Metodologia vira critério |
| `vektor/saida-esperada/03-analise/fichas/` | Fichas do Diagnóstico TechScale (ganho) e Orbita Pay (perdido) | A mesma etapa, lida pela mesma régua |
| `vektor/saida-esperada/03-analise/funil.md` | Saída do `funil.py` + leitura do analista | Números reais do CSV, nada estimado |
| `vektor/saida-esperada/03-analise/sintese.md` | Declarado × observado × medido, 8 divergências | O coração do método |
| `vektor/saida-esperada/04-handbooks/diagnostico.md` | Handbook completo do Diagnóstico | O modelo padrão preenchido |
| `vektor/saida-esperada/05-skills/` | Skill `vektor-diagnostico` (com perguntas, objeções e testes) e skill mestre `vektor-como-usar` | Handbook vira execução |

## O que a análise deve encontrar (gabarito)
1. Diagnóstico → Proposta é a menor conversão do funil: **54%** (outras etapas: 79% a 86%).
2. Diagnóstico com custo quantificado: **81%** avançam para proposta × **28%** sem custo.
3. Proposta → Ganho: **80%** com custo quantificado × **25%** pulando o diagnóstico.
4. **12 das 15** perdas por preço/hora vieram de quem pulou o diagnóstico. O win/loss do gestor ("perdemos por preço") é sintoma, não causa.
5. Lucas Andrade: win rate **56,7%** × 17% a 23% dos demais, com o mesmo mix de contas (rodízio).

Os números vêm do `deals.csv` (rode `python3 ../scripts/funil.py vektor/01-coleta/A-numeros/deals.csv --segmentar custo_quantificado`).

## Créditos
Transcrições da TechScale adaptadas do material "Transcrições Challenger Sale" do Officer Hour SCIENT (ciclo fictício). Metodologia: *The Challenger Sale*, Dixon & Adamson (CEB/Gartner, 2011).
