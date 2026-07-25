# Upload automático no claude.ai web (rclone no Environment)

No terminal do Mac o rclone já sobe os contratos sozinho. No **claude.ai web** as
sessões rodam numa máquina na nuvem que não tem o seu rclone. Para o upload
automático funcionar lá também, configure o rclone **dentro do Environment**.

## Requisitos
- O Environment precisa de **rede de saída** liberada para Google APIs
  (`googleapis.com`) e para baixar o rclone (`rclone.org`). Ajuste a política de
  rede do Environment se necessário.
- Você vai guardar a config do rclone (que contém um token de acesso ao seu
  Drive) como **secret**. Trate como credencial.

## Passo 1 — no Mac: pegar a config do rclone em base64
```bash
base64 -i ~/.config/rclone/rclone.conf | tr -d '\n' | pbcopy
```
Isso copia (uma linha) o conteúdo do `rclone.conf` codificado. É esse valor que
vira o secret.

## Passo 2 — no code.claude.com: Environment
Abra o Environment usado pelas sessões web e adicione:

1. **Secret / variável de ambiente**
   - Nome: `RCLONE_CONF_B64`
   - Valor: (cole o base64 do Passo 1)

2. **Script de setup** (roda ao iniciar o container):
   ```bash
   command -v rclone >/dev/null 2>&1 || (curl -fsSL https://rclone.org/install.sh | sudo bash) || true
   if [ -n "$RCLONE_CONF_B64" ]; then
     mkdir -p "$HOME/.config/rclone"
     echo "$RCLONE_CONF_B64" | base64 -d > "$HOME/.config/rclone/rclone.conf"
   fi
   ```

## Passo 3 — testar numa sessão web
```bash
rclone lsd gdrive: --drive-root-folder-id 1Zruibh8wECstNcVhs3pIN0N16-FrN8-Y
```
Se listar (ou não der erro de token), o rclone está pronto no web e o
`/contratos-time:contratar` passa a subir automaticamente lá também.

## Observações
- O token do client_id compartilhado do rclone será aposentado ao longo de 2026;
  se parar, refaça `rclone config reconnect gdrive:` no Mac e atualize o secret.
- Alternativa mais segura (opcional): usar uma **service account** do Google com
  acesso só à pasta de contratos (compartilhe a pasta com o e-mail da SA) e
  guardar o JSON da SA como secret, em vez do token pessoal.
