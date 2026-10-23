## Autenticazione a due fattori (2FA)

Per una sicurezza aggiuntiva è possibile attivare l'autenticazione a due fattori.

### Configurare la 2FA

1. Accedere ad Anton
2. Aprire **Profilo** → **Sicurezza**
3. Inserire la propria password e fare clic su **Attivare** — entrambi nello
   stesso modulo
4. Scansionare il codice QR con l'app di autenticazione. Se non è possibile, la
   chiave è riportata sotto come testo e può essere inserita a mano
5. **Conservare i codici di recupero** — sono la via di ritorno se lo smartphone
   va perso
6. Inserire un codice dell'app sotto **Verificare il codice**. Anton indica se è
   corretto; non viene modificato nulla

Da quel momento Anton chiede questo codice a sei cifre dopo la password
all'accesso.

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

### Reimpostare la 2FA

Se una persona ha perso il dispositivo con il secondo fattore, l'amministrazione lo reimposta; un account superutente solo un superutente. Prima l'admin si accerta che la richiesta venga davvero da quella persona (di persona, per telefono o per e-mail dall'indirizzo dell'account).

1. Nell'area Admin andare su **Utenze**, trovare la persona e fare clic su **Reimpostare la 2FA** (nella riga della tabella o in **Modifica**).
2. In **Motivo** annotare come è stata riconosciuta la persona, p. es. «e-mail dall'indirizzo dell'account, 23.10.». Per un account superutente è obbligatorio.
3. **Rimuovere anche le passkey** è selezionato: il dispositivo perso ne porta di solito una. Deselezionare solo se manca soltanto l'app di autenticazione.
4. Confermare **Reimpostare la 2FA**.

Tutte le sessioni della persona vengono poi chiuse, anche quella sul dispositivo perso. Riceve un'e-mail all'indirizzo dell'account che dice chi ha reimpostato e quando. Al prossimo accesso configura di nuovo il secondo fattore. L'operazione figura con il motivo nel registro di sicurezza.

## Risoluzione dei problemi

| Problema | Soluzione |
|---------|--------|
| `401 Unauthorized` | Verificare il token; l'intestazione è formattata correttamente? |
| `403 Forbidden` | Verificare i diritti dell'utenza |
| `Invalid key supplied` | Token API mancante o non valido |
| Il codice 2FA non viene accettato | Sincronizzare l'orario sul dispositivo |
