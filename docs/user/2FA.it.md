## Autenticazione a due fattori (2FA)

Per una sicurezza aggiuntiva è possibile attivare l'autenticazione a due fattori.

### Configurare la 2FA

1. Accedere ad Anton
2. Aprire **Profilo** → **Sicurezza**
3. Fare clic su **Attiva l'autenticazione a due fattori**
4. Scansionare il codice QR con un'app di autenticazione
5. Inserire il codice fornito dall'app per confermare

### App di autenticazione supportate

Funziona qualsiasi app compatibile con TOTP. App open source consigliate:

| App | Piattaforma | Open source |
|-----|-----------|-------------|
| **Aegis Authenticator** | Android | ✓ |
| **2FAS** | Android, iOS | ✓ |
| **Proton Authenticator** | Android, iOS | ✓ |
| **FreeOTP+** | Android | ✓ |
| **Tofu** | iOS | ✓ |
| **KeePassXC** | Windows, macOS, Linux | ✓ |
| **Bitwarden** | Tutte le piattaforme | ✓ |

Altre app compatibili: Authy, Google Authenticator, Microsoft Authenticator, 1Password

### Disattivare la 2FA

L'amministrazione può reimpostare la 2FA:

1. Nell'area Admin andare su **Utenze**
2. Individuare la persona nell'elenco
3. Fare clic sul pulsante **Reset 2FA** (nella riga della tabella)

In alternativa anche nella pagina di modifica dell'utenza:

1. Nell'area Admin andare su **Utenze**
2. Selezionare l'utenza → **Modifica**
3. Fare clic sul pulsante **Reset 2FA**

## Risoluzione dei problemi

| Problema | Soluzione |
|---------|--------|
| `401 Unauthorized` | Verificare il token; l'intestazione è formattata correttamente? |
| `403 Forbidden` | Verificare i diritti dell'utenza |
| `Invalid key supplied` | Token API mancante o non valido |
| Il codice 2FA non viene accettato | Sincronizzare l'orario sul dispositivo |
