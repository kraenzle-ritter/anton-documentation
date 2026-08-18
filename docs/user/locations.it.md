# Collocazioni

Una collocazione è il luogo fisico di conservazione dell'originale — magazzino,
deposito, locale, scaffale. Le collocazioni sono schede a sé stanti e si
gestiscono in **Admin → Collocazioni**.

!!! note "Non per il pubblico"
    La scheda di collocazione stessa è visibile esclusivamente all'utenza
    interna, a chi descrive e all'amministrazione, mai a persone esterne — dove
    si trovi un documento non riguarda il pubblico.

    Il **campo** «collocazione» di un'unità di descrizione è cosa distinta: le
    nuove installazioni vengono consegnate con il campo rimosso dai formulari
    pubblici (esterni), così che «Collocazione: …» non compaia nel catalogo
    pubblico. Le installazioni esistenti restano invariate — lì il campo va, se
    necessario, rimosso dai formulari esterni tramite i
    [formulari](../admin/forms.md).

## Registrare

La collocazione è volutamente essenziale e prevede solo quattro campi:

| Campo | Scopo |
|---|---|
| ID | assegnato automaticamente |
| Abbreviazione | forma breve, ad es. `M2` |
| Nome | in chiaro, ad es. «Magazzino 2, scaffale C» |
| Descrizione | testo libero |

Nessun tipo, nessuna coordinata, nessun [dato di autorità](authorities.md).

!!! note "Autorizzazione"
    Creare, modificare ed eliminare collocazioni presuppone il ruolo `editor`.
    L'utenza interna (`user_intern`) può consultarle — a differenza di attori,
    luoghi e parole chiave, le collocazioni non sono affatto pubbliche.

## Assegnare

Un'unità di descrizione viene assegnata alla collocazione nel campo
**collocazione**. Si trova nella sezione «documentazione collegata» ed è un
elenco di selezione.

Un'unità di descrizione ha al massimo **una** collocazione. Se il campo compaia
nella maschera dipende dal [set di formulari](forms.md) — per impostazione
predefinita lo recano unità archivistica, serie e unità documentaria, ma non
archivio e fondo.

!!! tip "Collocazione o dettaglio della collocazione?"
    Due campi dal nome simile non vanno confusi:

    - **Collocazione** — la scelta tra le collocazioni registrate, un vero e
      proprio collegamento. Su di essa si possono fare valutazioni.
    - **Collocazione (dettaglio)** — un campo di testo per indicazioni
      complementari, senza collegamento.

## Che cosa si trova in una collocazione

La pagina di dettaglio di una collocazione elenca — come per attori e luoghi —
tutte le unità di descrizione a essa assegnate.

## Eliminare

Se a una collocazione sono ancora legate delle unità di descrizione, Anton
rifiuta l'eliminazione e lo segnala. Le assegnazioni vanno prima sciolte.

## Segnature con collocazione

In alcuni archivi l'abbreviazione della collocazione entra a far parte della
[segnatura](identifiers.md). Se ciò è configurato, nella finestra «Creare nuove
schede» compare un campo di selezione aggiuntivo **collocazione**.

!!! note "Specifico dell'archivio"
    Questa funzione presuppone una formazione delle segnature programmata
    appositamente. Lo schema standard non utilizza la collocazione — lì il campo
    di selezione resterebbe senza effetto. Con Anton as a Service, k & r sa se
    la propria installazione disponga di una simile formazione delle segnature.
