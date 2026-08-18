# Esportazione

## EAD

L'esportazione dei dati in EAD (Encoded Archival Description) è allineata ai requisiti del portale europeo degli archivi.

## TEI

I descrittori (attori e attrici, luoghi, parole chiave tematiche) possono essere esportati in TEI (Text Encoding Initiative). Anton può inoltre essere collegato tramite API REST come banca dati di indici per edizioni TEI. Dalle voci relative agli oggetti è possibile generare un header TEI. Ciò può essere realizzato con una classe specifica per cliente, in modo che l'header TEI soddisfi i requisiti richiesti.

## Dump SQL

L'amministrazione ha la possibilità di generare e scaricare in qualsiasi momento un dump completo della banca dati.

## Strumenti di ricerca in Word

Per singoli fondi è possibile generare strumenti di ricerca classici in formato Word. Sono possibili anche adattamenti più estesi.

## RDF / linked data (CIDOC CRM, RiC-O, Memobase)

Anton è l'**unica banca dati archivistica svizzera** che esporta nativamente tutti e tre i profili RDF rilevanti nel panorama archivistico:

- **CIDOC CRM 7.1.x con doppia tipizzazione RiC-O 1.1** — il modello più diffuso a livello internazionale per il linked data nell'ambito del patrimonio culturale (Wikidata, Europeana, aggregatori GND, ResearchSpace, Linked Art)
- **RiC-O 1.1 puro** (Records in Contexts Ontology del Consiglio internazionale degli archivi, ICA) — per i consumatori esclusivamente RiC-O come SPA (Swiss Archival Portal), i futuri portali dell'ICA e i sistemi archivistici conformi a RDA
- **Profilo Memobase** (RiC-O con contesto JSON-LD specifico di Memobase) — direttamente importabile in [Memobase](https://memobase.ch), il portale svizzero del patrimonio audiovisivo di Memoriav, secondo la convenzione Memoriav §9

Tutti i profili vengono generati dalla stessa base di dati e sono disponibili in **quattro serializzazioni**: RDF/Turtle, JSON-LD, RDF/XML, N-Triples. Accesso tramite interfaccia, API REST e CLI. Maggiori dettagli: [documentazione dell'esportazione RDF](../admin/download-rdf.md).

## Pubblicazione statica e round trip

Un intero fondo (o sottofondo), media compresi, può essere raccolto in *un
solo* file ZIP — senza che per la visualizzazione o il ripristino sia
necessaria un'istanza Anton in funzione:

- **A+ Static Bundle** — grafo CIDOC/RiC-O e media, filtrati secondo le
  esigenze di protezione dei dati e ospitabili offline (ad es. su GitHub
  Pages). Per la *pubblicazione*.
- **Round trip nativo** — il formato proprio di Anton e i media master,
  **senza perdita di dati e reimportabili** (`anton:export-native` /
  `anton:import-native`). Per il *backup e la migrazione* tra istanze Anton.

In questo modo i piccoli archivi possono usare Anton come editor e presentare
il proprio fondo in rete in forma statica a costi pressoché nulli. Un confronto
concreto tra i due formati (formato anton ↔ CIDOC) e la visione di un
visualizzatore statico: [Pubblicazione statica e round trip](../admin/statische-publikation.md).

## Download OCFL

Diversi archivi svizzeri di conservazione a lungo termine (UB Basilea, DLZA) richiedono OCFL (Oxford Common File Layout) per la consegna dei fondi. Anton fornisce OCFL v1.1 come pacchetto ZIP per singolo oggetto o per fondo, compresi i metadati EAD e il formato di importazione Anton per i round trip. Maggiori informazioni: [documentazione del download OCFL](../admin/download-ocfl.md).

## Download DIP

Pacchetti DIP conformi a OAIS (Dissemination Information Package) come ZIP BagIt per le consegne all'utenza finale. Maggiori informazioni: [documentazione DIP](../admin/download-dip.md).
