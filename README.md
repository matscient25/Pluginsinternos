# Pluginsinternos

Plugins internos do Claude Code do time SCIENT.

## Plugins

- **[contratos-time](./contratos-time)** — conduz a contratação do time (Full
  time e Freelancer): gera contratos preenchidos a partir de templates `.docx`,
  salva como Google Doc no Drive, e coordena o checklist de contratação
  (notebook, assinatura, e-mail, data de início, pré-onboarding).
- **[gtm-handbooks](./gtm-handbooks)** — GTM Handbooks & Skills Kit (certificação
  *Building GTM Handbooks & Skills*): transforma funil do CRM, transcrições,
  documentos de processo e PPTs de proposta e de produto em handbooks por etapa
  e em skills do time. Agnóstico de metodologia. 9 agentes, comece com `/handbooks`.

## Como instalar um plugin

Neste repositório como marketplace local de plugins:

```
/plugin marketplace add matscient25/Pluginsinternos
/plugin install contratos-time
```
