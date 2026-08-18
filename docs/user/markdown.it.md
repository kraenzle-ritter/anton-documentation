# Markdown

In Anton i testi nei campi di testo possono essere formattati con il linguaggio di marcatura [Markdown](https://it.wikipedia.org/wiki/Markdown). Markdown è semplice e si impara rapidamente. Inoltre i dati testuali restano relativamente puliti, perché bastano pochissimi caratteri e convenzioni aggiuntive per consentire la formattazione.

[ [Informazioni dettagliate](https://www.markdownguide.org/basic-syntax/) ]


Le principali possibilità di formattazione in Anton:

### Nuove righe, nuovi paragrafi

Le nuove righe si ottengono con due spazi alla fine di una riga.

I nuovi paragrafi mediante una riga vuota.

### Titoli

I titoli si creano con `#` a inizio riga: un `#` seguito da uno spazio indica un titolo di primo livello, due `##` seguiti da uno spazio un titolo di secondo livello e così via:

```markdown
# Titolo livello 1
## Titolo livello 2
```
Risultato:
<div class="myframe">
<h1>Titolo livello 1</h1>
<h2>Titolo livello 2</h2>
</div>

### Elenchi

Gli elenchi si creano con `-` oppure `*` a inizio riga o, se numerati, con `1.`, `2.` seguiti da uno spazio. Sono possibili anche sottopunti, che vengono allora rientrati.

```markdown
- Filosofi greci
    - Aristotele
    - Platone
- Filosofi romani
    - Cicerone
```

### Link esterni

Il testo da collegare si mette tra parentesi quadre. La destinazione del link segue tra parentesi tonde.

```markdown
[Questo testo verrà collegato](https://destinazione_del_link.ch)
```

### Rimandi all'interno di Anton

I rimandi all'interno di Anton funzionano come i link. Come destinazione si indica la rispettiva URL relativa:

```markdown
[Anton](/actors/2)
```

Il rimando porta allora all'attore o attrice con ID 2. In modo del tutto
analogo si possono collegare le unità di descrizione; la destinazione è allora
`/objects/123`.

### Le segnature vengono collegate automaticamente

Di regola le segnature non devono essere collegate a mano: se in un campo di
testo viene menzionata una segnatura, Anton la riconosce nella
**vista di dettaglio** e ne fa un rimando alla ricerca. Nella vista di modifica
il testo resta intatto, così da rimanere modificabile.

!!! note "Non in ogni archivio"
    Il riconoscimento si basa su un modello di ricerca memorizzato per archivio.
    Se non ne è configurato alcuno, le segnature nel testo restano prive di
    collegamento.

### Evidenziazioni

Per le evidenziazioni si possono usare `*corsivo*` (*corsivo*) oppure `**` (**grassetto**) oppure `***` (***grassetto e corsivo***).
