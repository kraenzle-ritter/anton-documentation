# Dati di autorità nell'editor XML (VS Code, Oxygen)

Chi codifica edizioni in TEI può riprendere attori e attrici, luoghi e parole
chiave direttamente da Anton, senza uscire dall'editor: selezionare un nome,
scorciatoia da tastiera, scegliere un risultato — il plugin scrive l'ID di Anton
nell'attributo, ad esempio `<persName ref="sulger-actors-123">`. La ricerca
avviene in tempo reale in Anton; non viene mai scaricato un intero registro.

Esistono due plugin con le stesse funzioni:

| Editor | Plugin | Installazione |
|---|---|---|
| Visual Studio Code | [anton-vs](https://github.com/kraenzle-ritter/anton-vs) | il file `anton-vs-<versione>.vsix` dalle [release](https://github.com/kraenzle-ritter/anton-vs/releases/latest) |
| Oxygen XML Editor | [anton-oxy](https://github.com/kraenzle-ritter/anton-oxy) | in Oxygen tramite **Help → Install new add-ons…** con l'indirizzo `https://github.com/kraenzle-ritter/anton-oxy/releases/latest/download/updateSite.xml` |

Installazione e utilizzo sono descritti nel README di ciascun plugin su GitHub.
Questa pagina tratta ciò che va configurato dal lato di Anton.

## Archivio pubblico o non pubblico

Per un archivio **pubblico** al plugin basta l'indirizzo dell'archivio, ad
esempio `https://archivio.example.ch`.

Un archivio **non pubblico** fornisce i suoi registri solo se il plugin invia
un **token API**. Senza token il plugin segnala:

```
Anton HTTP 401 … {"error":"This archive is not public"}
```

Serve la versione 1.4.0 del plugin o una più recente.

## Creare un token API

Un token lo crea chi ha il ruolo `admin` nell'archivio. Appartiene a un account
separato con il ruolo **`user`**, non al proprio account di amministrazione: un
token ha i diritti dell'account a cui è legato. Su un account `user` può cercare
e leggere, ma non modificare nulla.

### 1. Creare un account per i plugin

Una volta per archivio; in seguito tutte le persone usano lo stesso account.

1. In **Admin → Utenti** creare un nuovo account.
2. Nome e nome utente a piacere, ad esempio «Plugin editor» e `editor-plugins`.
3. Un **indirizzo e-mail** non ancora usato da un altro account, ad esempio un
   indirizzo di progetto. Anton vi invia un invito a impostare una password;
   lo si può ignorare, perché con questo account non accede nessuno.
4. **Ruolo: `user`**.

### 2. Generare il token

1. Aprire il nuovo account in **Admin → Utenti**.
2. Nella sezione **Token API**:
    - **Nome**: chi usa il token e per cosa, ad esempio «VS Code Noëmi» o
      «Oxygen Stefan». Un token per persona — così ognuno si può revocare
      singolarmente.
    - **Scade il**: una data, ad esempio fra un anno. Vuoto significa senza
      scadenza.
3. **Crea token API**.
4. **Copiare subito il token.** Anton lo mostra solo questa volta; viene salvato
   solo un hash, nemmeno Kränzle & Ritter può leggerlo in seguito.

!!! warning "Trattare un token come una password"
    Chi possiede il token può leggere tutto ciò che l'account è autorizzato a
    leggere. Non inviarlo per e-mail né conservarlo in file condivisi.

## Inserire il token nel plugin

**VS Code**: **Impostazioni → Estensioni → Anton**, il campo del token API
(l'impostazione si chiama `anton.apiToken`). L'indirizzo dell'archivio si trova
nella stessa sezione sotto `anton.baseUrl`. Il token non viene trasferito su
altri computer dalla sincronizzazione delle impostazioni di VS Code; lì va
inserito di nuovo.

**Oxygen**: **Anton → Anton-Einstellungen…**, campo **API token**; sopra si
trova l'indirizzo dell'archivio sotto **Anton base URL**.

## Revocare e sostituire

Nella pagina dell'account la sezione **Token API** elenca ogni token con nome,
ultimo utilizzo e data di scadenza. **Revoca** lo disattiva immediatamente.

Se un token è perso, scaduto o finito in mani sbagliate: generarne uno nuovo,
inserirlo nel plugin, revocare il vecchio. Se il plugin segnala

```
Anton hat den API-Token abgelehnt (falsch, abgelaufen oder Konto gesperrt)
```

(«Anton ha rifiutato il token API (errato, scaduto o account bloccato)»), è
esattamente ciò che va fatto. Impostando l'account su `blocked` tutti i suoi
token vengono disattivati in un colpo solo.
