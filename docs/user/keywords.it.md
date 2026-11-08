# Parole chiave

Le parole chiave descrivono il contenuto delle unità di descrizione — per cose,
eventi, tecniche, opere. Persone e organizzazioni rientrano invece tra gli
[attori e le attrici](actors.md), le indicazioni geografiche tra i
[luoghi](places.md).

Si trovano in **Admin → Parole chiave**; il collegamento avviene nel formulario
dell'oggetto, nel campo **parole chiave (soggetti)**.

!!! note "Gerarchia su richiesta"
    Di norma le parole chiave stanno l'una accanto all'altra; il **tipo** si limita a raggrupparle. Termini più ampi e più specifici e «vedi anche» si attivano per archivio, vedi [Termini più ampi e più specifici](#termini-piu-ampi-e-piu-specifici).

## Tipi

I tipi sono liberamente definibili per archivio e variano notevolmente da un
archivio all'altro. Sono diffusi evento, oggetto, unità di misura/valuta,
raccolta/opera d'arte, procedimento/processo/tecnica,
libro/manoscritto/pubblicazione e altro/diversi; gli archivi con fondi
particolari ne gestiscono molti di più — ad esempio per materie prime e
geologia, costruzioni, flora e fauna o tecnica militare. Fa fede la lista di
valori del proprio archivio, consultabile in **Aiuto → Liste di valori**.

## Registrare

Il formulario contiene tipo, etichetta, altre forme del nome, varianti,
abbreviazioni, descrizione, fonti e commento.

Se l'etichetta possa essere registrata in forma **multilingue** dipende
dall'impostazione `translate_keywords`. Se è disattivata, esiste un solo campo
di inserimento nella lingua principale dell'archivio.

Anton riconosce le parole chiave esistenti dall'etichetta normalizzata e le
riutilizza invece di creare doppioni.

Le parole chiave possono essere create anche **direttamente dal formulario
dell'oggetto**: accanto all'elenco di selezione nel campo **parole chiave** si
trova un **+** che apre una finestra con lo stesso formulario di creazione. Dopo
la creazione la nuova parola chiave risulta selezionata — l'unità di descrizione
stessa va ancora salvata.

## Termini più ampi e più specifici

Se l'impostazione `keyword_relations` è attiva in **Admin → Impostazioni**, ogni parola chiave ha **termini più ampi**, **termini più specifici** e **vedi anche**. Disattivata, come di norma, tutto resta come prima.

Nel formulario della parola chiave i termini si scelgono in tre campi, come nel formulario dell'oggetto. Un termine più specifico si inserisce dall'una o dall'altra parte; Anton salva la relazione una volta e la mostra da entrambi i lati.

Una parola chiave può avere **più termini più ampi**. Uno di essi è il **termine principale**: sotto di esso la parola chiave compare nel **percorso** in cima alla pagina di dettaglio, per esempio «Scrittura › Lettera». Il primo termine più ampio diventa quello principale; se ce ne sono diversi, lo si sceglie nel formulario sotto **Termine principale**.

Anton non ammette cerchi: una parola chiave non può stare sotto uno dei propri termini più specifici, né essere collegata a sé stessa. Il formulario torna allora con un messaggio e non salva nulla.

Il pulsante **Albero dei termini**, sulla lista delle parole chiave e accanto al percorso di una parola chiave, mostra i termini più ampi e più specifici come albero. Si carica man mano, come il piano d'archivio, e apre il percorso fino alla parola chiave di partenza. Una parola chiave con più termini più ampi si apre solo sotto il termine principale; sotto gli altri compare come rinvio, per esempio «lettera (vedi scrittura)».

L'eliminazione di una parola chiave elimina le sue relazioni. Unendo due parole chiave, quella che resta riprende le relazioni dell'altra.

## Dati di autorità

Come attori e luoghi, anche le parole chiave possono essere collegate a
[dati di autorità](authorities.md) — ad esempio a Wikidata o alla GND.

!!! warning "Non disponibile in ogni archivio"
    La colonna dei dati di autorità compare presso la parola chiave solo se per
    l'archivio sono configurati dei provider. Se l'impostazione manca, per la
    parola chiave non esiste alcuna possibilità di collegamento — mentre per
    attori e luoghi sì.

## Scaricare come thesaurus

Con i termini più ampi e più specifici attivati, il personale connesso trova il pulsante **Scarica SKOS** sulla lista delle parole chiave e **Sottoalbero in SKOS** su ogni parola chiave. Il file contiene tutte le parole chiave, oppure la parola chiave con tutto ciò che sta sotto, in Turtle, RDF/XML o N-Triples: denominazioni in tutte le lingue, altri nomi, termini più ampi e più specifici, «vedi anche» e i dati di autorità collegati. Ogni parola chiave compare sotto il suo indirizzo permanente. La [matrice delle esportazioni](../admin/export-matrix.md) indica che cosa viene esportato.

## Schemi di concetti e importazione di thesauri

In **Admin → Schemi di concetti** l'archivio gestisce i suoi thesauri: quelli che importa (per esempio un thesaurus specialistico in SKOS) e quelli che cura in proprio. Una parola chiave può appartenere a più schemi e porta in ciascuno l'URI e la notazione del concetto. La pagina di dettaglio li mostra sotto **Schema di concetti**.

L'importazione accetta un file SKOS (Turtle, RDF/XML o N-Triples) o una tabella (XLSX, CSV) con le colonne **Term**, **Broader**, **Use for**, **Use**, **Related**, **Notation** e **Definition** (funzionano anche i nomi tedeschi). Più termini in una cella si separano con «;». L'importazione avviene in background; il risultato appare poi sulla stessa pagina.

- **Niente doppioni:** se esiste già una parola chiave con lo stesso nome, l'importazione vi si collega. Essa conserva la sua denominazione e riceve solo le lingue mancanti. Se più parole chiave portano quel nome, l'importazione ne crea una nuova e segnala il nome.
- **Una seconda importazione** dello stesso file aggiorna invece di duplicare.
- **Vengono ripresi** altri nomi, definizioni, termini più ampi e più specifici, «vedi anche» e collegamenti a dati di autorità (Wikidata, GND, VIAF, Library of Congress, GeoNames). Nulla di ciò che l'archivio ha scritto viene sovrascritto.
- **I termini non preferiti** di una tabella («usa …») diventano altri nomi del termine. Un rinvio combinato («usa A, B») viene registrato presso entrambi e figura nel risultato.
- **I cerchi** vengono omessi e segnalati.

Uno schema si può scaricare in SKOS. Rimuoverlo lascia le parole chiave con le loro relazioni e i collegamenti; si perde solo l'appartenenza allo schema. Da riga di comando fa lo stesso `anton:import-skos`.

## Dove viene utilizzata una parola chiave

Sotto «compare in» la pagina di dettaglio mostra tutte le unità di descrizione
che recano la parola chiave.

Se la parola chiave ha termini più specifici, l'interruttore **Con i termini più specifici** aggiunge le loro unità di descrizione alla lista. Lo stesso interruttore compare nella ricerca accanto ai filtri scelti non appena si filtra per una parola chiave.

## Eliminare

Una parola chiave può essere eliminata solo finché non è registrata presso
**alcuna unità di descrizione**. In caso contrario Anton rifiuta l'eliminazione
e ne segnala il motivo. Quali unità siano interessate lo mostra «compare in»
nella pagina di dettaglio; lì vanno dapprima rimosse le attribuzioni.
