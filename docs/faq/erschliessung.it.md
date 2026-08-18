# Descrizione archivistica

## Descrizione a più livelli secondo ISAD(G)

Anton è stato concepito come attuazione dello standard ISAD(G) e lo implementa integralmente. La descrizione gerarchica è possibile a qualsiasi profondità. Sono previsti i seguenti livelli di descrizione: Archivio, Gruppo di fondi, Fondo, Serie, Classe, Unità archivistica, Unità documentaria. Tutti i livelli tranne il fondo possono essere ripetuti al proprio interno un numero illimitato di volte.

Le singole aree informative di ISAD(G) sono realizzate mediante uno o più campi di testo, liste di valori e/o eventi Anton.

## Attribuzione automatica delle segnature
Anton attribuisce automaticamente le segnature sulla base della segnatura del fondo; esse possono però essere sovrascritte in qualsiasi momento. Per l'attribuzione delle segnature esistono diverse opzioni. È inoltre possibile programmare nuovi generatori di segnature e attivarli per singole installazioni.

## Eventi Anton
La gestione separata degli attori e delle attrici (persone, organizzazioni e altri) e il loro collegamento alle unità di descrizione tramite eventi realizzano anche idee concettuali di Records in Contexts (cfr. [https://www.ica.org/en/records-in-contexts-conceptual-model](https://www.ica.org/en/records-in-contexts-conceptual-model)). Gli «eventi Anton» contengono il tipo di evento (ad es. «creazione»), un momento o un periodo, facoltativamente un attore o un'attrice, un luogo e una descrizione più dettagliata.

In Anton esistono tipi di evento predefiniti, tra cui:

- creazione  
- versamento  
- provenienza  
- riproduzione  
- digitalizzazione  
- ricezione  
- conferenza  

## Calcolo automatico degli estremi cronologici
L'evento Anton «creazione» viene registrato solo al livello di descrizione più basso. Anton calcola quindi automaticamente gli estremi cronologici delle unità di descrizione dei livelli superiori.

## Consistenza (calcolo automatico)
In Anton i metri lineari vengono registrati per ciascun fondo. Essi vengono poi cumulati per i gruppi di fondi e per l'archivio. Per le unità archivistiche e documentarie si raccomanda di registrare la consistenza con i campi tipo di oggetto e consistenza (numero di pezzi). È disponibile anche un campo descrittivo per la consistenza.

## Descrittori
Oltre agli eventi Anton, che descrivono l'interazione di un attore o di un'attrice con l'unità di descrizione, attori, luoghi e parole chiave possono essere usati direttamente anche come descrittori per la descrizione del contenuto. Questo tipo di descrizione risulta particolarmente interessante per le raccolte audiovisive.

## Formattazione del testo e link nei campi di testo
Nei campi di testo Anton riconosce Markdown ([https://it.wikipedia.org/wiki/Markdown](https://it.wikipedia.org/wiki/Markdown)), un semplice linguaggio di marcatura. Ciò significa che, per la visualizzazione nel browser, vengono formattati ad esempio titoli ed elenchi. In questo modo è anche facile inserire link a siti esterni, a unità di descrizione correlate o ad altre pagine di Anton.

![Inserimento di testo in Markdown](images/markdown_input.png)
Inserimento di testo in Markdown. I titoli sono contrassegnati con ##; negli elenchi le righe iniziano semplicemente con - oppure *.

![Testo nella vista HTML](images/markdown_rendered.png)
Testo nella vista HTML. I titoli sono resi come tali. Anche l'elenco viene formattato.

## Linked data e dati di autorità
I descrittori attori, luoghi e parole chiave possono essere collegati facilmente a banche dati esterne o a banche dati di autorità. Per impostazione predefinita sono disponibili diverse risorse:

- Wikipedia  
- Wikidata  
- GND  
- Geonames  
- Ortsnamen  
- Metagrid  
- inserimento manuale  

Se un luogo viene collegato a Geonames, vengono salvate anche le coordinate geografiche e viene visualizzata una mappa che lo localizza.

Ulteriori risorse vengono collegate automaticamente quando una ricerca con uno degli identificativi ha dato esito positivo.

È possibile anche l'inserimento manuale di risorse (link esterni).

## Integrazione di documenti e media audiovisivi
A ogni unità di descrizione è possibile associare una o più immagini e altri media (PDF, audio, video). L'associazione avviene tramite trascinamento o importazione da Excel. Per descrivere le immagini in modo ottimale (ad es. con parole chiave) si raccomanda di registrare ogni immagine a livello di unità documentaria. Solo così la galleria di immagini può essere sfruttata al meglio (cfr. ad es. [https://archives.georgfischer.com/gallery](https://archives.georgfischer.com/gallery) oppure [https://bahnarchiv.ch](https://bahnarchiv.ch)).

La maggior parte degli archivi utilizza Anton anche come archivio digitale a lungo termine per i propri media. In tal caso è importante che i media siano stati validati in anticipo (pre-ingest) e convertiti in formati adeguati. Anton conserva e gestisce la versione di archiviazione (ad es. TIFF) e crea copie di consultazione (ad es. JPEG) in diverse risoluzioni per l'utenza esterna. Le versioni di archiviazione vengono salvate con una somma di controllo, in modo da poter verificare rapidamente in seguito l'integrità dei file.

## Diversi formulari di inserimento e visualizzazione
Per impostazione predefinita, a ogni unità di descrizione è assegnato il set di formulari del proprio livello di descrizione. Per i fondi vengono così visualizzati tipicamente i campi dell'area informativa «contesto», mentre a livello di unità documentaria si visualizzano piuttosto i campi relativi alle caratteristiche materiali. È inoltre possibile creare set di formulari specifici e assegnarli manualmente a un'unità di descrizione. I singoli formulari possono essere adattati in modo rapido e semplice.

Un set di formulari è composto da 3 formulari: inserimento (Edit), vista interna (dettaglio interno) e vista esterna (dettaglio esterno). I formulari definiscono quali campi di dati sono visibili in quale contesto. Il formulario «dettaglio interno» contiene tipicamente il campo «osservazioni interne dell'archivio». Se questo campo non è incluso nel formulario «dettaglio esterno», le «osservazioni interne dell'archivio» sono visibili soltanto all'utenza interna, agli editor e all'amministrazione.

## Accessioni
Anton non dispone di un modulo dedicato alle accessioni. In alternativa, i fondi appena acquisiti possono essere creati in Anton come bloccati/invisibili al pubblico (ad esempio in un sottoarchivio invisibile); la storia delle accessioni di un fondo può essere descritta da un lato nel campo accessioni/nuove acquisizioni (ISAD(G) 3.3.3). Dall'altro, i singoli versamenti possono essere documentati con il modulo formulario «versamento» (per ogni versamento viene creata una voce con data, ente versante e commento, visualizzata nella scheda del fondo).
