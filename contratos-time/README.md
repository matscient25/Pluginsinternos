# contratos-time

Plugin do Claude Code que **conduz a contratação do time** — Full time e
Freelancer. Gera o contrato preenchido a partir de templates `.docx` (salvo como
**Google Doc editável** no Drive) e coordena o **checklist de contratação**.

## Componentes

| Tipo | Nome | O que faz |
|------|------|-----------|
| Comando | `/contratos-time:contratar` | Toca o processo completo de contratação de uma pessoa (checklist + contrato). |
| Comando | `/contratos-time:gerar-contrato` | Gera só o contrato preenchido e salva como Google Doc. |
| Comando | `/contratos-time:setup` | Configura a pasta de destino e confere campos/cláusulas dos templates. |
| Agente | `redator-contrato` | Desenvolve o contrato preenchido, fiel ao template. |
| Agente | `coordenador-contratacao` | Conduz o processo pelo checklist e acompanha o status. |
| Skill | `contratos-time` | Convenções e fluxo (carrega sozinha no assunto). |
| Script | `scripts/fill_contract.py` | Motor que preenche `.docx` (`--list` / `--data`). |

## Checklist de contratação

O `coordenador-contratacao` segue estes 5 itens (template em
`templates/checklist_contratacao.md`):

1. Aluguel do Notebook
2. Assinatura do Contrato
3. Criação do e-mail
4. Data de início definida
5. Envio do Pré-onboarding

## Como funciona o contrato

O conector do Google Drive não permite substituir texto dentro de um Google Doc.
Para preservar **exatamente** a formatação do template e ainda preencher os
campos, o plugin:

1. Usa o template `.docx` **embarcado no plugin** (`templates/full_time.docx`).
2. **Preenche** os `{{campos}}` localmente com `scripts/fill_contract.py` (sem
   dependências, preserva formatação e lida com placeholders quebrados em vários
   runs pelo Word).
3. **Sobe** o resultado para a pasta do Drive, convertendo em Google Doc editável.

## Placeholders e cláusulas condicionais

**Campos**: `{{Chave}}` — a chave pode ter espaços e acentos, exatamente como no
template. Ex. do Full time: `{{Nome Completo da Pessoas}}`, `{{Nº do CPF}}`,
`{{Razão social}}`, `{{CNPJ}}`, `{{Endereço Completo}}`, `{{Cidade}}`, `{{UF}}`,
`{{Nº CEP}}`, `{{Estado Civil}}`, `{{Nº do RG}}`, `{{Salario}}`,
`{{salario por extenso}}`, e a data (`{{Data}}`, `{{DD}}`, `{{Mês}}`, `{{AAAA}}`,
preenchida automaticamente).

**Cláusulas condicionais** (entram só em alguns contratos): envolva o trecho com
`{{#CHAVE}} ... {{/CHAVE}}`. Ex. do plano de saúde (cláusula 12.2):

```
{{#PLANO_SAUDE}}
a) Plano de saúde: {{PLANO_OPERADORA}}, em regime de coparticipação ...;
b) {{PLANO_COMODIDADE}}, nas condições definidas pela Contratante.
{{/PLANO_SAUDE}}
```

`PLANO_SAUDE` verdadeiro → o bloco fica e os campos são preenchidos; falso ou
ausente → o bloco é **removido inteiro**, sem deixar rastro. Ponha cada marcador
na própria linha quando o bloco tiver vários parágrafos.

## Configuração (uma vez)

Preencha `destination_folder_id` no `config.json` (ID da pasta do Drive, parte da
URL após `/folders/`) — ou rode `/contratos-time:setup`.

O template **Full time** já vem embarcado. Para Freelancer, suba o `.docx` em
`templates/freelancer.docx` e rode o `setup` para mapear os campos.

## Uso

```
/contratos-time:contratar full-time  Maria Silva, PJ Maria Silva ME,
   CNPJ 11.222.333/0001-81, salário R$ 12.000, início 01/08/2026, com plano de saúde Bradesco
```

## Requisitos

- Conector do **Google Drive** conectado no claude.ai.
- `python3` no ambiente (usa só a stdlib).
