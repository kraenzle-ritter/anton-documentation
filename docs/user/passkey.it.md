# Passkey 

## Che cosa sono le passkey?

Le passkey sono un'alternativa moderna e sicura alla password tradizionale. Invece di dover ricordare una password si utilizzano:

- l'**impronta digitale** (Touch ID)
- il **riconoscimento facciale** (Face ID)
- il **PIN o il blocco schermo** del proprio dispositivo
- una **chiave di sicurezza hardware** (ad es. YubiKey)

Le passkey sono più sicure delle password perché non possono essere rubate, indovinate o sottratte mediante attacchi di phishing.

## Presupposti

- Il proprio archivio deve avere attivato la funzione passkey
- Un browser aggiornato (Chrome, Safari, Firefox, Edge)
- Un dispositivo con autenticazione biometrica o una chiave di sicurezza

## Configurare una passkey

1. **Accedere con la propria password** (come di consueto)
2. **Aprire il proprio profilo** dal menu utente
3. **Portarsi su «Sicurezza» o «Passkey»**
4. **Fare clic su «Aggiungi passkey»**
5. **Seguire le istruzioni del browser o del dispositivo**:
   - Confermare con impronta digitale, Face ID o PIN
   - La passkey viene salvata automaticamente sul dispositivo
6. **Assegnare un nome** alla passkey (ad es. «MacBook ufficio», «iPhone»)

> **Suggerimento:** è possibile configurare più passkey per dispositivi diversi.

## Accedere con una passkey

1. **Aprire la pagina di accesso** di Anton
2. **Fare clic su «Accedi con passkey»**
3. **Confermare con la propria impronta digitale, Face ID o PIN**
4. L'accesso è effettuato – senza password!

## Gestire le passkey

Nel proprio profilo è possibile:

- **visualizzare tutte le passkey registrate**
- **rinominare le passkey** (per una migliore visione d'insieme)
- **eliminare le passkey** (ad es. in caso di smarrimento del dispositivo)

## Domande frequenti

### Posso continuare a usare la mia password?
Sì, le passkey sono una possibilità di accesso aggiuntiva. La password continua a funzionare.

### Che cosa succede se si perde il dispositivo?
Accedere con la propria password ed eliminare nel proprio profilo la passkey del dispositivo perduto.

### La passkey funziona su altri dispositivi?
A seconda del sistema (iCloud, Google Password Manager, Windows Hello) le passkey possono essere sincronizzate tra più dispositivi. Le chiavi di sicurezza sono legate al dispositivo fisico.

### L'autenticazione a due fattori è ancora necessaria?
Le passkey sono considerate molto sicure e possono sostituire l'autenticazione a due fattori – ciò dipende dalle impostazioni del proprio archivio.

## I vantaggi in sintesi

| Password | Passkey |
|----------|---------|
| Può essere dimenticata | Sempre con sé sul proprio dispositivo |
| Può essere rubata | Protetta crittograficamente |
| Rischio di phishing | Immune al phishing |
| Regole complesse | Utilizzo semplice |


## Contesto tecnico

Le passkey si basano sullo standard WebAuthn (FIDO2). Al momento della registrazione viene creata una coppia di chiavi crittografiche:
- La **chiave privata** resta al sicuro sul proprio dispositivo
- La **chiave pubblica** viene salvata in Anton

All'accesso il dispositivo dimostra di possedere la chiave privata – senza mai trasmetterla.

*Aggiornamento: febbraio 2026*
