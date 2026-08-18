# Per iniziare

Anton è una banca dati archivistica web. Segue lo standard ISAD(G) e rappresenta
i fondi come una struttura ad albero — dall'archivio ai fondi e alle serie fino
al singolo documento. Per ogni [unità di descrizione](objects.md) è possibile
registrare media, [attori e attrici](actors.md), [luoghi](places.md) e
[parole chiave](keywords.md).

Questa documentazione descrive il lavoro con Anton dal punto di vista della
descrizione archivistica. Per l'installazione e la configurazione si veda l'area
Admin.

## L'interfaccia

La navigazione si trova in alto. Il suo contenuto è configurabile per ogni
archivio; di regola vi si trovano:

- il **punto di accesso alla struttura archivistica**. Il nome lo decide ogni
  archivio — «catalogo», «piano d'archivio» oppure il nome dell'archivio stesso.
- **Admin** — nonostante il nome, è la pagina collettiva per tutte le persone
  autenticate. La pagina stessa è intitolata **Amministrazione** e conduce,
  tramite schede, alle **entità** (attori e attrici, luoghi, parole chiave,
  collocazioni), alle **utenze**, alle **informazioni**, all'**importazione /
  esportazione** e alle **impostazioni**. Le schede visualizzate dipendono dal
  ruolo.
- **Aiuto** — la guida integrata nell'applicazione; mostra i campi, le liste di
  valori e le regole di descrizione di **questo** archivio
- la **ricerca** in alto a destra

!!! note "Le etichette possono differire"
    Quasi ogni etichetta è configurabile per archivio — sia le voci di menu sia
    i nomi dei campi. Questa documentazione utilizza le denominazioni del
    formulario standard; nel singolo archivio possono differire. Dove le
    differenze rischiano di generare confusione, ciò è segnalato sul posto.

## Ruoli

Ciò che una persona vede e può fare dipende dal suo ruolo. Anton mantiene i nomi
dei ruoli non tradotti; nella gestione delle utenze compaiono esattamente così:

| Ruolo | Può |
|---|---|
| (non autenticato) | Consultare il catalogo pubblico — se l'archivio lo rende accessibile |
| `user` | Lo stesso, da autenticato; profilo personale, notifiche |
| `user_intern` | Inoltre vedere i contenuti bloccati e le collocazioni, prendere in prestito e scaricare i media originali |
| `loan_admin` | Inoltre gestire i prestiti |
| `editor` | Descrivere: creare, modificare, spostare ed eliminare schede (comprese le collocazioni); importazione; media |
| `admin` | Impostazioni, formulari, account utente, esportazione, statistiche |
| `blocked` | Nulla — l'accesso è bloccato |

Ogni ruolo comprende i diritti di quello precedente.

Chi descrive necessita almeno del ruolo `editor`. I pulsanti per creare,
spostare ed eliminare compaiono soltanto con questa autorizzazione — se mancano,
la ragione è il ruolo.

!!! note "Superuser"
    Oltre ad `admin` esistono i superuser per interventi quali tipi di campo,
    liste di valori e termini di protezione. Non si tratta di un ruolo nella
    gestione delle utenze, bensì di un elenco di account gestito separatamente.

## Autenticazione

L'autenticazione avviene con nome utente e password. A seconda dell'archivio
sono inoltre disponibili l'[autenticazione a due fattori](2FA.md) e le
[passkey](passkey.md).

## Dove proseguire

Il punto di partenza per il lavoro quotidiano è
[Unità di descrizione](objects.md); come è strutturato l'albero e come si
possono ricollocare le schede è descritto in
[Struttura archivistica e spostamento](hierarchy.md). Perché la propria maschera
appaia diversa dagli esempi qui riportati è spiegato in
[Formulari e campi](forms.md).
