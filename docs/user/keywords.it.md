# Parole chiave

Le parole chiave descrivono il contenuto delle unità di descrizione — per cose,
eventi, tecniche, opere. Persone e organizzazioni rientrano invece tra gli
[attori e le attrici](actors.md), le indicazioni geografiche tra i
[luoghi](places.md).

Si trovano in **Admin → Parole chiave**; il collegamento avviene nel formulario
dell'oggetto, nel campo **parole chiave (soggetti)**.

!!! note "Nessuna gerarchia"
    Le parole chiave stanno l'una accanto all'altra. Anton non gestisce un
    thesaurus: non esistono termini sovraordinati e subordinati né rimandi tra
    parole chiave. Il **tipo** si limita a raggrupparle.

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

## Dati di autorità

Come attori e luoghi, anche le parole chiave possono essere collegate a
[dati di autorità](authorities.md) — ad esempio a Wikidata o alla GND.

!!! warning "Non disponibile in ogni archivio"
    La colonna dei dati di autorità compare presso la parola chiave solo se per
    l'archivio sono configurati dei provider. Se l'impostazione manca, per la
    parola chiave non esiste alcuna possibilità di collegamento — mentre per
    attori e luoghi sì.

## Dove viene utilizzata una parola chiave

Sotto «compare in» la pagina di dettaglio mostra tutte le unità di descrizione
che recano la parola chiave.

## Eliminare

Una parola chiave può essere eliminata solo finché non è registrata presso
**alcuna unità di descrizione**. In caso contrario Anton rifiuta l'eliminazione
e ne segnala il motivo. Quali unità siano interessate lo mostra «compare in»
nella pagina di dettaglio; lì vanno dapprima rimosse le attribuzioni.
