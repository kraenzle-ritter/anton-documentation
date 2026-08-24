# Ricerca full text

La ricerca full text interroga contemporaneamente tutti i campi rilevanti delle schede archivistiche: titoli, segnature, campi di testo, attori e attrici, luoghi e parole chiave collegati — e anche il testo riconosciuto tramite OCR da PDF e immagini.

## Che cosa viene interrogato

Per ogni oggetto d'archivio vengono riuniti ai fini della ricerca:

- **Titoli** dell'oggetto e di tutte le unità superiori (fondo → serie → unità archivistica → documento)
- **Segnature** (attuali e vecchie) nonché l'ID interno
- **Denominazioni** del livello di descrizione, del tipo di oggetto, della collocazione
- **Datazioni**
- **Parole chiave collegate** in tutte le varianti linguistiche presenti
- **Luoghi collegati**
- **Attori e attrici collegati** (solo quelli visibili pubblicamente)
- **Campi di testo** visibili nel formulario esterno
- **Testo OCR** proveniente dai media (PDF, immagini)

!!! note "Vista estesa per il personale interno"
    Per le persone autenticate a partire dal ruolo `user_intern` vengono inoltre interrogati:

    - attori e attrici privati
    - tutti i campi di testo (anche quelli visibili solo internamente)
    - gli oggetti contrassegnati come privati

## Comportamento della ricerca

### Gli inizi di parola vengono riconosciuti automaticamente

I caratteri jolly (`*`) non sono necessari — la ricerca trova automaticamente tutte le parole che **iniziano** con il termine inserito.

| Ricerca | Trova |
|---|---|
| `alkohol` | «Alkohol», «Alkoholverbot», «alkoholisch» |
| `müller` | «Müller», «Müller-Weber», «Müllers» |

!!! warning "Ma non a metà parola"
    `kohol` **non** trova «Alkohol». La ricerca agisce solo all'inizio della parola.

### Più parole vengono combinate con E

| Ricerca | Trova |
|---|---|
| `alkohol verbot` | Schede in cui compaiono **entrambi** i termini — possono trovarsi a qualsiasi distanza |

### Virgolette per le espressioni esatte

| Ricerca | Trova |
|---|---|
| `"rudolf leder"` | Solo le schede in cui questa sequenza di parole compare **esattamente così** |
| `#rudolf leder#` | Identico — `#` è una notazione alternativa per `"` |

Con un'espressione **non** si cerca automaticamente per inizio di parola — l'espressione deve comparire esattamente.

!!! warning "Le parole molto brevi vengono ignorate anche nelle espressioni"
    Le parole di meno di 3 caratteri e alcune parole vuote inglesi (`the`, `for`, `and`) restano escluse dal confronto anche all'interno delle virgolette. Un'espressione come `"AG Reinach"` corrisponde quindi di fatto solo a «Reinach».

!!! note "Espressioni nel testo dei documenti"
    Se l'archivio tiene il testo integrale in forma **condensata**
    (impostazione `optimize_fulltext`), l'indice contiene solo la prima
    occorrenza di ogni parola — le espressioni sono quindi reperibili solo in
    misura limitata nel testo dei PDF. La ricerca di parole singole non ne è
    toccata. Se sia il caso lo sa l'amministrazione.

### Termini con trattino

I termini con trattino (ad es. `Arp-Hagenbach`) vengono trattati automaticamente come un'espressione: si cercano le due parti direttamente accostate.

## Che cosa non funziona

- **I termini di meno di 3 caratteri** vengono ignorati (`ag`, `zb`).
- **Le parole brevi molto frequenti** come «und», «der», «die» sono escluse dall'indice di ricerca della banca dati (le cosiddette parole vuote).
- **La ricerca a metà parola** non è possibile (vedi sopra).

## Distinzione rispetto alla ricerca ponderata

La ricerca full text interroga gli **oggetti d'archivio**. La [ricerca ponderata](weighted-search.md) è un'altra funzione e riguarda le viste a elenco di **attori e attrici, luoghi e parole chiave** — lì i risultati vengono ordinati per rilevanza.
