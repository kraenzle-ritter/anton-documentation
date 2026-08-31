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

## Ricerca booleana del testo completo

Oltre al campo di ricerca ordinario, la ricerca avanzata offre il campo
**«Ricerca booleana del testo completo»**. Interroga gli stessi contenuti ma
comprende i connettivi — e su un punto si comporta all'**opposto** del campo
ordinario.

!!! warning "Qui le parole singole valgono O, non E"
    Nel campo ordinario devono comparire tutte le parole inserite. Nel campo
    booleano ne basta una: `Maur Gemeinde` trova i record con «Maur» **o**
    «Gemeinde». Per esigerle entrambe si scrive `Maur AND Gemeinde`.

### Gli operatori

| Immissione | Significato |
|---|---|
| `Maur Gemeinde` | ne basta una delle due |
| `Maur AND Gemeinde` | devono comparire entrambe |
| `Maur OR Gemeinde` | esplicitamente l'una o l'altra (il valore predefinito) |
| `Maur NOT Gemeinde` | «Maur», ma senza «Gemeinde» |
| `+Maur -Gemeinde` | lo stesso in forma breve |
| `"Feuerwehr Maur"` | esattamente quella sequenza di parole |
| `Gemeinde*` | tutte le parole che iniziano con «Gemeinde» |

`AND`, `OR` e `NOT` si scrivono in maiuscolo. Agiscono su entrambi i lati:
`Maur AND Gemeinde` esige anche «Maur», non solo «Gemeinde». Un segno esplicito
prevale su un `AND` che precede — `Maur AND -Gemeinde` resta un'esclusione.

### Caratteri jolly

L'asterisco vale **solo a fine parola**: `Gemeinde*` trova «Gemeindearchiv».
Anteporlo non aiuta — in `*archiv` l'asterisco viene rimosso e resta la ricerca
ordinaria di «archiv», che trova le parole che iniziano così, non quelle che così
finiscono. All'interno di una parola non ha effetto.

### Parole brevi

Le parole di meno di tre caratteri non figurano in alcun indice della banca
dati. A differenza del campo ordinario, qui **non** escono dalla ricerca: Anton
le cerca come sequenza di caratteri nel testo. Così `FC Maur` trova quello che
deve — «FC» viene allora trovato anche all'interno di una parola, poiché questa
ricerca non conosce i confini di parola.

### Che cosa il campo non può fare

- Le **parentesi** di raggruppamento vengono rimosse. `(a OR b) AND c` non è
  esprimibile.
- **Una virgoletta isolata** viene scartata anziché segnalata come errore:
  `"Feuerwehr` diventa una ricerca ordinaria di «Feuerwehr».

## Distinzione rispetto alla ricerca ponderata

La ricerca full text interroga gli **oggetti d'archivio**. La [ricerca ponderata](weighted-search.md) è un'altra funzione e riguarda le viste a elenco di **attori e attrici, luoghi e parole chiave** — lì i risultati vengono ordinati per rilevanza.
