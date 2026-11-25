## Riepilogo
L'importazione di tabelle porta in Anton unità di descrizione e i loro file (media) da una tabella Excel, ODS o CSV. La tabella viene caricata, controllata e poi importata; i media si caricano prima nella scheda «Media». L'aiuto in Anton (Importazione di tabelle → scheda «Documentazione», `/import/excel/documentation`) mostra lo stesso elenco di colonne di questa pagina, con i valori e i separatori del proprio archivio.

## Importazione dati `/import`

Tutte le vie di importazione partono da **Admin → Import / Export → Importazione dati** (`/import`). La pagina mostra un riquadro per ogni via:

| Riquadro | Contenuto |
|---|---|
| **Importazione di tabelle** | Tabella Excel, ODS o CSV con unità e media (il tema di questa pagina). Schede: Metadati, Media, Update, Documentazione, Elenchi di valori. |
| **SIP eCH-0160** | Pacchetti di versamento secondo eCH-0160, vedi [SIP Ingest](../admin/sip-ingest.md). |
| **Importazione di cartelle** | Importazione di una struttura di cartelle (ZIP/GZ). |
| **Importazione Agate Sipline** | solo dove configurata: pacchetti da agate, vedi [agate SIP](../admin/agate-sip.md). |
| **Lista di controllo delle proposte**, **Importazioni**, **Stato DIMAG** | secondo diritti e configurazione: controllare proposte, il [registro delle importazioni](#import-protokoll), lo stato del trasferimento a DIMAG. |

Indirizzi vecchi come `/import/validation`, `/import/ingest`, `/import/documentation` o `/sip/validation` portano all'importazione di tabelle o a questa panoramica.

### Vista di dettaglio nella casella d'entrata

Per ogni SIP in attesa nella casella d'entrata esiste un link **Dettagli**. Dietro si trova una pagina di ispezione che legge solo il `metadata.json` dal pacchetto (senza estrarre i media) e mostra:

- il controllo del pacchetto: BagIt (manifesto, somme di controllo) o E-ARK (validazione E-ARK)
- il numero di schede nel SIP
- le categorie di tipo di oggetto NARA — con un avviso se il tenant non conosce alcun tipo adeguato per una categoria
- il titolo della scheda più alta

Così, prima dell'importazione, si può vedere se il SIP è sensato, se il vocabolario del tenant è adatto e, all'occorrenza, scartare il SIP prima che qualcosa finisca nella banca dati.

### Avanzamento in tempo reale

Tutte le importazioni vengono eseguite **in modo asincrono in background**. Dopo il clic su «Importa» si arriva su una pagina di avanzamento che aggiorna lo stato corrente ogni pochi secondi: fase (backup della banca dati, lettura, controllo, creazione delle schede, ripresa dei file media, fine), righe elaborate e, alla fine, un link all'**esecuzione nel protocollo delle importazioni**.

Ciò vale per tutte le vie — Excel, SIP, directory e finalizzazione della casella d'entrata.

### Una segnatura per ogni importazione

Ogni importazione (indipendentemente dalla via) riceve una segnatura `IMPORT-{aaaa}-{NNN}` e una voce nel protocollo delle importazioni. La voce registra:

- il nome del file originario
- la somma di controllo MD5
- il momento dell'importazione
- la via di importazione (Excel / SIP / directory / agate)
- le **impostazioni utilizzate** (vedi sotto)
- l'esito e, in caso di fallimento, il messaggio

<!-- v0.88.0: ricevute nell'archivio delle accessioni abolite, quelle esistenti migrate nel protocollo -->
!!! info "Nessuna ricevuta nell'archivio delle accessioni"
    Un'importazione non crea un'unità di descrizione come ricevuta. L'archivio delle accessioni resta riservato alle accessioni vere — arrivate fisicamente, non ancora descritte — e le sue segnature non vengono consumate dalle importazioni.

La segnatura viene assegnata all'avvio. Un'esecuzione fallita la mantiene quindi e resta nel protocollo con il suo errore — una consegna fallita deve restare distinguibile da una che non è mai avvenuta.

### Protocollo delle importazioni {#import-protokoll}

Sotto **`/import/audit`** si trova l'elenco di tutte le esecuzioni di importazione: segnatura, file di origine, momento, numero di schede create e lingua dei contenuti utilizzata. Si tratta di una normale tabella Anton — ordinabile, con lunghezza di pagina impostabile, e le colonne possono essere adattate in *Admin → Formulari* come per qualsiasi altro elenco.

Di norma vengono mostrate le esecuzioni riuscite; un filtro rivela quelle fallite o interrotte. Nulla viene mai cancellato.

Il link **Dettagli** porta all'esecuzione: file di origine, somma di controllo, impostazioni utilizzate con la loro provenienza, chi l'ha avviata e le schede che ha creato.

Il file importato viene conservato. Dopo un'esecuzione riuscita passa in `metadata_imported/` — così non compare più nell'elenco di scelta — e la voce indica dove si trova.

Le impostazioni vengono registrate in chiaro, una riga per impostazione con valore e provenienza. Vi restano in modo permanente — anche un anno dopo è così ricostruibile sotto quali presupposti è entrata una consegna.

## Svolgimento (importazione di tabelle)

1. **Prendere il modello.** La scheda «Documentazione» offre il modello, con un commento per colonna, elenchi di scelta e un foglio «Guida», e una tabella di esempio con righe valide del proprio archivio. Viene letto solo il primo foglio; il controllo segnala gli altri fogli come non letti.
2. **Caricare i media.** Se la tabella nomina dei file (colonna `media`), caricarli prima nella scheda «Media». Un file mancante è un errore del controllo.
3. **Caricare la tabella** nella scheda «Metadati» (`.xlsx`, `.ods` o `.csv`; Anton non legge i vecchi file `.xls`).
4. **Controllare.** L'icona a forma di occhio nell'elenco apre il controllo: colonne riconosciute e ignorate, errori, avvisi, che cosa verrebbe creato e con quali impostazioni (vedi [anteprima](#anteprima-che-cosa-creerebbe-limportazione)).
5. **Importare.** Superato il controllo, «Importa» avvia l'esecuzione in background.

Solo la scheda «Update» modifica unità esistenti (vedi [sotto](#aggiornare-schede-esistenti-aggiornamento-tramite-browser)), mai una nuova importazione: il controllo rifiuta una riga con un `id` esistente.

## Lingua dei contenuti dell'importazione

I campi traducibili — titoli, campi di testo, parole chiave, attori e attrici, luoghi e collocazioni di nuova creazione — necessitano di una lingua. Si tratta di una decisione consapevole, visibile prima dell'esecuzione.

<!-- v0.87.0: lingua dei contenuti esplicita; prima l'importazione seguiva la lingua dell'interfaccia -->
!!! note "La lingua dell'interfaccia non ha alcun ruolo"
    La lingua mostrata dall'interfaccia non ha alcuna influenza sull'importazione. Conta unicamente la lingua dei contenuti dell'esecuzione.

La lingua dei contenuti viene determinata in questo ordine — vince il primo valore impostato:

1. la scelta per questa esecuzione (`--locale` da riga di comando)
2. l'impostazione d'archivio `import_options.locale`
3. la prima lingua di `locales` — la lingua principale dell'archivio

Prima dell'avvio la pagina di ispezione indica la lingua in vigore **e da dove proviene** («scelta per questa esecuzione», «impostazione d'archivio», «valore predefinito»). Dopo l'esecuzione la stessa indicazione si trova nella voce di protocollo (vedi [Protocollo delle importazioni](#import-protokoll)).

Una colonna con sigla di lingua (`title_fr`) prevale su questa scelta per il proprio campo — vedi [colonne multilingue](#colonne-multilingue).

### Perché la lingua conta anche nella ricerca

La lingua dei contenuti determina non solo dove si scrive, ma anche **in che cosa Anton cerca attori, attrici e luoghi esistenti**. Se si scegle una lingua nella quale il fondo non è descritto, il confronto non trova nulla — e, con la creazione attivata, crea una nuova scheda per ogni nome.

Anton cerca quindi in due giri: prima nella lingua dell'esecuzione, poi nella lingua principale dell'archivio. Un riscontro proveniente dal secondo giro viene annotato nel protocollo. E l'anteprima (vedi sotto) mostra il numero di nuove creazioni prima che venga scritto qualcosa — se la lingua non corrisponde al fondo, lì quasi tutti gli attori risultano a prima vista «nuovi».

### Dove si trovano le impostazioni

Le impostazioni di importazione sono competenza dell'archivio (`import_options`) e vengono consultate dove agiscono: nella pagina di ispezione del file caricato, ciascuna con il **valore in vigore**, la sua provenienza e una spiegazione. Vengono visualizzate la lingua dei contenuti e gli interruttori che stabiliscono se attori, attrici, luoghi, parole chiave, collocazioni e tipi di oggetto sconosciuti vengano creati.

Volutamente **non** esiste un secondo deposito nel profilo utente: un valore di cui si ha bisogno solo durante l'importazione appartiene a un unico posto — e quel posto lo indica con la sua provenienza, invece di dire soltanto «predefinito».

## Anteprima: che cosa creerebbe l'importazione

Prima dell'avvio la pagina di ispezione mostra quante voci di autorità **distinte** l'esecuzione creerebbe: attori e attrici, luoghi, parole chiave, collocazioni, tipi di oggetto. Insieme ai nomi stessi.

Il numero conta voci distinte, non righe: un'attrice sconosciuta che compare in 500 righe è **una** nuova creazione.

I nomi contano più del numero. Un separatore sbagliato si manifesta nel fatto che «Muster, Hans; Beispiel, Anna» figura nell'elenco come *un solo* nome — in un semplice numero ciò resterebbe invisibile.

Se la creazione è disattivata per una categoria, le stesse voci compaiono come **non assegnabili**, con l'avviso che nell'esecuzione questi collegamenti verranno semplicemente omessi. Anche questo è un risultato che si vuole conoscere prima.

Se il numero di nuove creazioni di una categoria supera la metà delle righe, compare un **avvertimento**. Ciò indica più spesso un problema di separatore, di lingua o di colonna che un incremento reale. L'avvertimento non blocca nulla — l'esecuzione può essere avviata.

!!! note "L'anteprima non scrive nulla"
    Si limita a leggere. Non nasce alcuna scheda, nemmeno una da rimuovere in seguito.

## Colonne

Sono obbligatorie `parent` e `level_of_description` per una nuova unità, `id` o `uuid` per un aggiornamento. L'ordine delle colonne non conta, e nemmeno maiuscole e minuscole della riga d'intestazione. Una colonna che Anton non conosce non viene importata; il controllo la nomina e propone un nome simile. Un testo più lungo di quanto la banca dati contiene interrompe l'importazione con un messaggio invece di essere troncato in silenzio.

La tabella è prodotta da Anton (`anton:import-columns`), dalle stesse regole del controllo. I separatori sono quelli di una nuova installazione; ogni archivio può cambiarli, e l'aiuto in Anton mostra i propri.

<!-- BEGIN generated import columns -->

| Colonna | Contenuto | Tipo | Nuovo | Aggiornamento | Letta anche come |
|---|---|---|---|---|---|
| `id` | ID interno dell'unità. Chiave di una tabella di aggiornamento; una nuova importazione rifiuta le righe con un ID già esistente. | chiave | – | id o uuid |  |
| `uuid` | Identificatore durevole (UUID) dell'unità, chiave della tabella di aggiornamento come id. | chiave | – | id o uuid |  |
| `parent` | Unità superiore: la sua segnatura o il suo ID. Deve esistere nel patrimonio o trovarsi più in alto nella stessa tabella; un numero da solo vale come ID. | segnatura o ID | obbligatoria | – |  |
| `identifier` | Segnatura, al massimo 100 caratteri, univoca. Se vuota, Anton la ricava dall'unità superiore, tranne per gruppi di fondi e classi. | testo, univoco | sì | sì | `signatur` |
| `identifier_old` | Segnatura precedente, libera. | testo | sì | sì | `altsignatur` |
| `title` | Titolo nella lingua dell'importazione. | testo | sì | sì | `titel` |
| `title_<lang>` | Titolo in un'altra lingua dell'archivio, p. es. title_fr. | testo | sì | sì |  |
| `level_of_description` | Livello di descrizione dall'elenco di valori: etichetta, nome o ID. | elenco di valori | obbligatoria | sì | `verzeichnungsstufe` |
| `object_type` | Tipo di oggetto dall'elenco di valori. Uno sconosciuto viene creato solo se l'impostazione create-object-types è attiva. | elenco di valori | sì | sì | `objekttyp` |
| `object_count` | Numero di unità. | numero intero | sì | sì | `umfang_zahl` |
| `extent_cm` | Estensione in metri lineari, p. es. 2.5 o 2,5; Anton la salva in centimetri. Il nome inganna: la colonna accetta metri. | numero | sì | sì | `extent_lfm`, `extent_rm` |
| `creation_date_start` | Inizio della creazione: anno, mese o giorno (1900, 1900-03, 1900-03-12, anche 12.03.1900); «ca.» davanti vale 1 in creation_date_start_ca. Vuoto significa nessuna data. Formattare la cella come testo. | data | sì | – | `datum_von` |
| `creation_date_start_ca` | 1 se l'inizio è approssimativo (ca.); altrimenti 0 o vuoto. | 0 o 1 | sì | – | `datum_von_ca` |
| `creation_date_end` | Fine della creazione, data come creation_date_start; non prima dell'inizio (un anno vale come anno intero). Per un momento preciso, inizio e fine uguali. | data | sì | – | `datum_bis` |
| `creation_date_end_ca` | 1 se la fine è approssimativa (ca.); altrimenti 0 o vuoto. | 0 o 1 | sì | – | `datum_bis_ca` |
| `creation_actors` | Attori e attrici della creazione: nome, ID o identificatore d'autorità (gnd:…). Gli sconosciuti vengono creati se l'impostazione create-actors è attiva, altrimenti il controllo li segnala come errori. | attori e attrici (separati da `::` `;`) | sì | – | `provenienz_autor` |
| `creation_place` | Luoghi della creazione: nome, «nome / città», ID o geonames:…. Gli sconosciuti vengono creati se create-places è attiva. | luoghi (separati da `::` `;`) | sì | – |  |
| `creation_event_details` | Indicazioni sull'evento di creazione, libere. | testo | sì | – |  |
| `<event>_actors` | Attori e attrici di un altro evento; <event> è uno dei tipi di evento (elenco nella documentazione). | attori e attrici (separati da `::` `;`) | sì | – |  |
| `<event>_place` | Luoghi di un altro evento. | luoghi (separati da `::` `;`) | sì | – |  |
| `<event>_date_start` | Inizio di un altro evento, data come sopra; con <event>_date_start_ca. | data | sì | – |  |
| `<event>_date_end` | Fine di un altro evento, data come sopra; con <event>_date_end_ca. | data | sì | – |  |
| `<event>_event_details` | Indicazioni su un altro evento, libere. | testo | sì | – |  |
| `note.<name>` | Campo di testo del formulario secondo il suo nome, p. es. note.scopecontent o scopecontent; con un suffisso di lingua (_fr) per altre lingue. | testo | sì | sì |  |
| `languages` | Lingue del contenuto, come codici delle lingue configurate nell'archivio. | codici di lingua (separati da `::`) | sì | sì | `sprache`, `sprachen` |
| `keywords_terms` | Parole chiave per soggetto: nome o ID. Le sconosciute vengono create se create-keywords è attiva. | parole chiave (separati da `::` `,` `;`) | sì | sì | `keywords`, `sachschlagworte`, `schlagworte` |
| `keywords_actors` | Attori e attrici come parole chiave, come creation_actors. | attori e attrici (separati da `::` `;`) | sì | sì | `schlagworte_akteure`, `schlagworte_names` |
| `keywords_places` | Luoghi come parole chiave, come creation_place. | luoghi (separati da `::` `;`) | sì | sì | `schlagworte_orte`, `schlagworte_places` |
| `digitisation_actors` | Chi ha digitalizzato, attori e attrici come creation_actors. | attori e attrici (separati da `::` `;`) | sì | sì | `digitalisiert_von` |
| `location` | Collocazione: etichetta o ID. Una sconosciuta viene creata solo se create-locations è attiva. | collocazione | sì | sì | `standort` |
| `location_id` | Collocazione solo come ID. | numero intero | sì | sì |  |
| `formset` | Set di formulari: nome o ID. | set di formulari | sì | sì | `formularsatz` |
| `formset_id` | Set di formulari solo come ID. | numero intero | sì | sì |  |
| `period_of_protection` | Termine di protezione dall'elenco di valori: etichetta, nome o ID; vuoto significa nessuno. | elenco di valori | sì | sì | `schutzfrist` |
| `status_of_description` | Stato della descrizione dall'elenco di valori: etichetta, nome o ID. | elenco di valori | sì | sì | `status_beschreibung` |
| `detail_of_description` | Grado di dettaglio dall'elenco di valori: etichetta, nome o ID. | elenco di valori | sì | sì | `detail_beschreibung` |
| `vacat` | Vacat dall'elenco di valori: etichetta o ID; 0 e 1 di tabelle più vecchie sono ancora compresi. | elenco di valori | sì | sì | `fehlt` |
| `private` | 1 blocca l'unità e tutto ciò che sta sotto per il pubblico; 0 o vuoto no. | 0 o 1 | sì | sì | `privat` |
| `media` | Nomi dei file dei media, esattamente come caricati nella scheda «Media». Un file mancante è un errore del controllo. | nomi di file (separati da `::` `,` `;`) | sì | sì | `bilder` |
| `private_media` | Come media, ma i media sono visibili solo agli account autorizzati. | nomi di file (separati da `::` `,` `;`) | sì | sì | `private_bilder` |
| `loan` | Chi prende in prestito: «Cognome, Nome» o ID utente. | utente | sì | sì |  |

<!-- END generated import columns -->

### Colonne multilingue

Il campo può contenere testo libero.

Il titolo è un **campo traducibile**. In quale lingua venga scritto lo decide la [lingua dei contenuti dell'importazione](#lingua-dei-contenuti-dellimportazione) — o, più precisamente, la denominazione stessa della colonna:

| Colonna | scrive in |
|---|---|
| `titel` oppure `title` | la lingua dei contenuti dell'esecuzione |
| `title_de`, `title_fr`, `title_it`, `title_en` | esattamente la lingua indicata |

Si possono quindi importare titoli multilingue: una colonna per lingua. Entrambe le forme possono coesistere; la colonna con sigla di lingua è l'indicazione più precisa e prevale, e la pagina di ispezione lo segnala.

Lo stesso vale per i **campi di testo**: `scopecontent` scrive nella lingua dei contenuti, `scopecontent_fr` specificamente in francese, senza toccare le altre lingue dello stesso campo.

!!! note "Solo le lingue configurate"
    Una sigla di lingua viene riconosciuta solo se figura nell'impostazione `locales` dell'archivio (vedi [configurazione delle lingue](languages.md)). `title_es` in un archivio senza spagnolo non è un'indicazione di lingua, bensì una colonna sconosciuta — e l'ispezione la segnala come tale.

### Eventi

Gli eventi collegano un'unità con attori e attrici, luoghi e un periodo. Un gruppo di colonne appartiene a un tipo di evento: il tipo precede i nomi di campo `actors`, `place`, `date_start`, `date_start_ca`, `date_end`, `date_end_ca`, `event_details`, per la creazione quindi `creation_actors`, `creation_place`, `creation_date_start`, `creation_date_start_ca`, `creation_date_end`, `creation_date_end_ca`, `creation_event_details`.

Tipi di evento: `creation`, `acquisition`, `reproduction`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. L'aiuto in Anton mostra l'elenco attuale.

Le colonne di data accettano un anno, un mese o un giorno: `1900`, `1900-03`, `1900-03-12`, anche `12.03.1900`. «ca.» davanti alla data (`ca. 1900`) imposta il contrassegno ca. come un 1 nella colonna `…_ca`. Il controllo segnala una data illeggibile e una data di fine anteriore a quella d'inizio; un anno vale come anno intero, `1923` non finisce quindi prima di `1923-05-15`. Un campo vuoto significa: nessuna data.

#### Attori e attrici (ad es. creation_actors)

Un attore o un'attrice viene trovato tramite nome, ID o un identificatore d'autorità con prefisso, in minuscolo con due punti senza spazio: `gnd:118519522`. Le date di esistenza tra parentesi sono possibili ma non necessarie; le parentesi tonde non vanno usate per altro. Più attori e attrici si separano con il separatore dell'archivio (predefinito `::` o `;`):

```
Müller, Martina (1934-1977) :: Servizio giuridico
```

Se uno sconosciuto viene creato dipende dall'impostazione d'importazione `create-actors`: attiva (predefinita nel browser), viene creato, con un identificatore GND a partire dai dati della GND; disattiva, il controllo lo segnala come errore. Dalla riga di comando viene creato solo con `--create-actors`.

#### Luoghi (ad es. creation_place)

Un luogo viene trovato tramite nome, ID o un identificatore come `geonames:2954172`. Se un luogo sconosciuto viene creato dipende dall'impostazione d'importazione `create-places`.
Il campo può contenere un luogo oppure un places-id (integer). Impostazione di importazione `create-places`: i luoghi vengono creati se non sono trovati in Anton. Se un luogo è già registrato in Anton, può essere richiamato anche tramite il proprio ID (integer).

I luoghi possono contenere i seguenti elementi:  
- il nome (separato da «/»)  
- la città / il comune  
- il cantone / la regione (posto tra parentesi dopo il comune)

### Colonne con liste di valori

Diverse colonne accettano solo valori definiti nell'archivio:
`verzeichnungsstufe`, `objekttyp`, `schutzfrist`, `status_of_description`,
`detail_of_description` e `vacat`.

Le accettano tutte in **tre forme**, equivalenti:

| Forma | Esempio |
|---|---|
| Denominazione | `Bestand` |
| Nome interno | `fonds` |
| ID | `3` |

L'ID è la forma più stabile — sopravvive a una ridenominazione. Dove una
denominazione somiglia casualmente a un numero, prevale la denominazione.

!!! tip "I valori ammessi sono indicati nel messaggio d'errore"
    Se un valore non viene riconosciuto, la verifica nomina non solo il
    problema, ma anche la soluzione:

    > «Schachtel» non figura nella lista di valori. Sono ammessi: Archiv
    > (collection), Bestandsgruppe (recordgroup), Bestand (fonds), Klasse
    > (class), Dossier (file), Einzelstück (item), Serie (series)

    La denominazione viene prima, il nome interno tra parentesi. Non è quindi
    necessario consultare prima le liste.

#### Consultare tutte le liste di valori

In **Importazione tabellare → Liste di valori** (`/valuelists`) è
disponibile una panoramica di tutte le liste di valori: per
ogni voce denominazione, nome interno e ID, oltre alla colonna di importazione
a cui la lista appartiene. Un campo di ricerca filtra contemporaneamente tutte
le liste.

La pagina è di sola lettura ed è aperta a chiunque possa importare. Le liste
modificabili in *Admin → Liste di valori* richiedono invece il diritto di
**modificare** una lista — fuori dall'amministrazione di sistema lo hanno in
pochi, e solo per due delle diciassette liste. Chi voleva soltamente
consultare si trovava prima davanti a una porta chiusa.

Anche nella pagina: gli **ID delle collocazioni** per la colonna `location_id`
della tabella di aggiornamento.

Parole chiave, attori e luoghi *non* vi figurano — sono schede di autorità con
pagine proprie e ricercabili, non liste da leggere.

### vacat

Indica se l'unità di descrizione è un segnaposto (una lacuna nella numerazione
alla quale non corrisponde alcuna documentazione).

La colonna gestisce internamente ID di termini. Vengono accettati la
denominazione (`vacat`), l'ID (`56` per vacat, `57` per non vacat) e — da
tabelle più vecchie — `1` e `0`.

Viene **esportata** la denominazione: `vacat` per un segnaposto, altrimenti
una cella vuota. Le tabelle più vecchie con `56`/`57` possono continuare a
essere utilizzate senza modifiche.

### Ulteriori campi

Gli ulteriori campi sono campi di testo libero::

    Neuzugänge (note.accruals)
    Bewertung und Kassation (note.appraisal)
    Informationen des Bearbeiters (note.archivists_notes)
    Ordnung und Klassifikation (note.arrangement)
    Verwaltungsgeschichte / Biographie (note.bioghist)
    Zugangsbedingungen (note.condition_of_access)
    Reproduktionsbestimmungen (note.condition_of_reproduction)
    Bestandsgeschichte (note.custod_hist)
    Kommentar zur Datierung (note.date_comment)
    Umfang (Beschreibung) (note.extent_text)
    Findmittel (note.finding_aids)
    Allgemeine Anmerkungen (note.general_note)
    Archivinterne Bemerkungen (note.internal_note)
    Sprache/Schrift (note.language_script)
    Standort (Detail) (note.location_details)
    Physische Beschaffenheit und technische Anforderungen (note.physical_description)
    Provenienz (note.provenance)
    Publikationen (note.publications)
    Verwandte Verzeichnungseinheiten (note.related_units)
    Kopien/Reproduktionen (note.reproductions)
    Verzeichnungsgrundsätze (note.rules_note)
    Form und Inhalt (note.scopecontent)

## Aggiornare schede esistenti (aggiornamento tramite browser)

!!! warning "Funzione sperimentale"
    L'aggiornamento dei dati è contrassegnato come **sperimentale** (badge nella scheda e nella pagina di caricamento). Modifica direttamente schede esistenti. Anton crea perciò **automaticamente un backup della banca dati prima di ogni aggiornamento** (vedi sotto); verificare comunque il risultato a campione.

Oltre alla creazione di nuove schede, le unità di descrizione esistenti possono essere aggiornate anche direttamente tramite browser. A questo scopo, sotto **Importazione tabellare** esiste una scheda propria **«Update»** (dopo *Metadati* e *Media*). Lì si carica la tabella — i file di aggiornamento hanno un elenco proprio, separato dall'importazione normale — e si apre con l'icona a forma di occhio. Il file viene verificato direttamente in modalità aggiornamento e compare il pulsante **«Carica come aggiornamento»**.

Poiché la scheda *Update* verifica il file esclusivamente come aggiornamento, una tabella di solo aggiornamento (solo `id` + le colonne da modificare, senza `parent`) non richiede scorciatoie: la colonna `parent`, necessaria alla creazione, qui non è richiesta. La scheda *Metadati* regolare resta invariata per la creazione.

Un aggiornamento sovrascrive i campi delle schede esistenti «sul posto» — **non vengono create nuove schede**. Perché un aggiornamento resti sicuro e prevedibile valgono tre presupposti. Se uno di essi è violato, il file viene bloccato e il motivo è visualizzato nella pagina di ispezione:

1. **Ogni riga nomina la sua unità con `id` o `uuid`.** L'`id` di un'unità di descrizione è visibile nel `permalink`; la tabella di aggiornamento dall'elenco dei risultati li contiene entrambi.
2. **Nessuna colonna `parent` (o `parent_id`).** Un aggiornamento non deve spostare schede. Per modificare la gerarchia, riagganciare le schede in Anton nel modo consueto.
3. **Nessuna colonna di evento (Antonevents).** Colonne come `creation_actors`, `creation_date_start` ecc. non sono ammesse nell'aggiornamento, affinché non nascano eventi doppi. I collegamenti ad attori e luoghi si curano in Anton.

Che cosa scrive un aggiornamento:

- **Vengono sovrascritti solo i campi compilati.** Le celle vuote lasciano intatto il valore esistente — è quindi possibile aggiornare in modo mirato solo singole colonne (ad es. solo `titel` o solo `schutzfrist`).
- **Parole chiave, attori, luoghi, lingue e campi di testo vengono sostituiti.** Una cella compilata è la *nuova lista completa*: chi elimina una voce dalla cella scioglie con ciò anche il collegamento sulla scheda. Una cella vuota non cambia nulla. (Nell'importazione normale — ossia alla creazione — le parole chiave continuano a essere soltanto aggiunte.)
- I **media** continuano a essere aggiunti.

Lo stesso file può essere caricato più volte come aggiornamento; il blocco dei duplicati altrimenti valido (stesso file = stessa somma di controllo MD5) non si applica agli aggiornamenti, poiché un aggiornamento è ripetibile.

Dopo l'avvio la pagina di avanzamento mostra l'aggiornamento come **«aggiornamento dati»** (non come importazione) e riferisce alla fine quante schede sono state *aggiornate*.

**Backup automatico.** Prima che un aggiornamento scriva anche una sola riga, Anton crea un dump della banca dati (lo stesso backup di `anton:backup`, depositato sotto `db_backup/`). Il passaggio compare nella visualizzazione dell'avanzamento come fase *backup*; il nome del file del dump è annotato sull'esecuzione. Se il backup non può essere creato, **l'aggiornamento si interrompe** e non viene modificato nulla. Il backup viene imposto anche quando per il mandante è altrimenti impostato `no-backup` — quell'opzione è pensata per *creazioni* di massa rapide, dove il ritorno è banale.

Ogni esecuzione di aggiornamento sta — come un'importazione — nel protocollo delle importazioni, ma con una **serie di segnature propria `UPDATE-{aaaa}-{NNN}`** invece di `IMPORT-{aaaa}-{NNN}`. Un aggiornamento non è un'accessione — nell'archivio non entra nulla di nuovo — e la serie separata rende visibile a colpo d'occhio quali voci siano aggiornamenti. Il contatore scorre indipendentemente dalla serie di importazione e viene azzerato per ogni anno civile.

### Scaricare la tabella adatta

Perché un aggiornamento non debba essere composto a mano, l'**elenco dei risultati corrente può essere scaricato direttamente come tabella di aggiornamento**: nell'elenco degli oggetti, in alto a destra, il simbolo Excel accanto all'anteprima di stampa. Il download riprende esattamente i filtri attualmente visualizzati.

Il file contiene esclusivamente colonne che un aggiornamento è autorizzato a scrivere — `id`, le colonne dei campi, le lingue, la collocazione (`location_id`), parole chiave / attori / luoghi (come ID) e le colonne dei campi di testo `note.*`. Non sono deliberatamente **compresi** `parent` e le colonne di evento, che bloccherebbero l'aggiornamento. La colonna `identifier` serve solo all'orientamento: l'aggiornamento trova le schede tramite l'`id`, non scrive mai la segnatura e ignora una segnatura modificata. Per le unità senza segnatura (classi, gruppi di fondi) la cella resta vuota.

!!! tip "Archivi multilingue: una colonna di titolo per lingua"
    Se l'archivio gestisce più lingue dei contenuti, la tabella di aggiornamento contiene, al posto di `titel`, una colonna `title_de`, `title_fr` ecc. Solo così il percorso di uscita e rientro è senza perdite: con un'unica colonna di titolo, al caricamento dovrebbe essere la lingua dell'esecuzione a decidere dove torna il valore — e un titolo francese finirebbe nel campo tedesco.

    Gli archivi monolingue mantengono la consueta colonna `titel`; lì non c'è nulla da distinguere. Le tabelle più vecchie con `titel` restano in ogni caso caricabili.

!!! tip "Modificare le collocazioni"
    Per la collocazione esistono **due colonne**, e il nome indica in ciascun caso che cosa vi appartiene:

    | Colonna | Contenuto |
    |---|---|
    | `location_id` | **solo l'ID** della collocazione (si trova in *Admin → Collocazioni*) |
    | `location` | ID **oppure** denominazione |

    La tabella di aggiornamento scaricata utilizza `location_id`. Chi preferisce lavorare con le denominazioni rinomina la colonna in `location`; lì vengono accettate entrambe le forme. Una denominazione deve essere scritta esattamente come nella gestione delle collocazioni, comprese maiuscole e minuscole — l'ID è perciò la via sicura.

    Una **cella vuota lascia la collocazione invariata** — per uno spostamento occorre quindi modificare solo le righe che effettivamente cambiano posto. Una collocazione non ancora esistente va creata in precedenza in *Admin → Collocazioni*; altrimenti l'ispezione la segnala come sconosciuta e l'aggiornamento non viene eseguito.

Al clic si apre una finestra in cui si possono **selezionare le colonne**. È più di una comodità: ciò che non figura nel file, un aggiornamento non può nemmeno scriverlo. Chi vuole correggere solo un singolo titolo seleziona `id` e `titel` — così al caricamento nient'altro può subire danni. `id` è sempre incluso e non può essere deselezionato.

!!! warning "La tabella è un'istantanea"
    Tra download e aggiornamento dovrebbe passare il minor tempo possibile. Il file contiene lo stato al momento del download. Se viene caricato solo giorni più tardi, i suoi vecchi valori sovrascrivono tutto ciò che nel frattempo è stato modificato su quelle schede — comprese le modifiche che altre persone hanno apportato deliberatamente e che dovrebbero rimanere. Non conservare una tabella scaricata per riutilizzarla più tardi, ma esportarla di nuovo per ogni ciclo di correzioni. Meno colonne sono selezionate, minore è il rischio.

    **Anton lo verifica.** All'esportazione il momento viene scritto nel file (nelle proprietà del documento, non in una colonna — sopravvive anche alla ridenominazione). La pagina di ispezione lo confronta con la data di modifica delle schede interessate e segnala concretamente quali sono state modificate da allora: *«3 schede sono state modificate dopo l'esportazione della tabella (20.07.2026 08:30) — l'aggiornamento sovrascriverebbe queste modifiche: SIG-1, SIG-7, …»*. Ciò non blocca l'aggiornamento; possono esserci buone ragioni per caricarlo comunque. Se non è possibile determinare alcun momento (ad esempio con una tabella creata a mano), la pagina lo dice — l'assenza di un avviso non significa quindi mai automaticamente «tutto in ordine».

Il pulsante è riservato all'amministrazione e può essere nascosto nel proprio profilo sotto *Impostazioni*. Accanto si trova l'**esportazione Excel completa** (tutti i campi, compresi `parent` e le colonne di evento) — quella è pensata per le valutazioni e *non* può essere ricaricata come aggiornamento.

### Perché gli eventi non seguono nell'aggiornamento

Le colonne di evento (`creation_actors`, `creation_date_start`, `acquisition_place` …) sono **bloccate** nell'aggiornamento. Il motivo sta nella struttura: in Anton un evento è una tupla di *attore/attrice, luogo, periodo e tipo* — una riga per attore. Una tabella può rappresentarne, per ogni oggetto e tipo di evento, soltanto **una combinazione**: un luogo, un periodo, un testo di dettaglio, condivisi da un numero qualsiasi di attori.

Ne derivano tre cose che una tabella non può garantire:

- **Più eventi dello stesso tipo.** Se un oggetto è stato lavorato nel 1920 a Zurigo *e* nel 1925 a Berna, ciò non si può esprimere in un solo insieme di colonne. Nell'esportazione Excel completa le colonne di questo tipo vengono perciò omesse. **Una cella di evento vuota significa quindi due cose:** o non è registrato alcun evento — oppure ce ne sono più di quanti questa forma tabellare possa portare. La finestra di download lo segnala. La tabella di aggiornamento non contiene alcuna colonna di evento e non ne è interessata.
- **Eliminare eventi.** L'importazione crea gli eventi o li aggiorna soltanto; non esiste alcun modo di rimuoverne uno tramite la tabella.
- **Spostare una data.** Il confronto avviene tramite *tipo + oggetto + attore/attrice + data iniziale*. Se nella tabella la data viene modificata, nasce un **secondo** evento e quello esistente rimane.

Sono proprio gli ultimi due punti a rendere gli eventi inutilizzabili in un aggiornamento: si potrebbe solo aggiungere, mai correggere — e caricamenti ripetuti moltiplicherebbero gli eventi. Gli eventi vengono perciò curati in Anton stesso, non tramite la tabella.

Non sono inoltre rappresentati il campo di datazione a testo libero (`datierung_text`, in nessuna direzione) e l'indirizzo del luogo (`<typ>_place_address`, solo all'importazione e solo se è impostata l'opzione `import_addresses`).

!!! note "Tramite l'`id` o l'`uuid`"
    L'aggiornamento nel browser trova le schede tramite l'`id` interno o, se la tabella non ha una colonna `id`, tramite l'`uuid`, mai tramite la segnatura. Una riga con un `id` o un `uuid` sconosciuto, o con due valori che indicano schede diverse, viene respinta; un aggiornamento non crea nulla. I file che la scheda porta già non vengono allegati di nuovo, quindi la stessa tabella si può ripetere. Un aggiornamento tramite la segnatura è possibile solo da riga di comando (`--update --default-excel-column=identifier`, vedi sotto).

## Importazione da riga di comando


### Importazione semplice

Per il cliente (slug) «besenval» e il file Excel «test.xlsx» il comando di importazione è:

```bash
php artisan anton:import test.xlsx --env=besenval --import
```

Si presuppone che `test.xlsx` si trovi nella cartella `customers/besenval/metadata_to_import/`. I file da importare con esso (media) devono trovarsi nella cartella `customers/besenval/assets_to_import/`.

Senza l'opzione `--import` il file viene soltanto validato.

### Opzioni

Il comando `anton:import` offre alcune opzioni che possono essere utili in situazioni specifiche.

| Opzione|Descrizione|
|:---   | :----------|
|--no-backup | dont backup the database before import |
|--import                  |really start import|
|--locale=                 |lingua dei contenuti dell'esecuzione (ad es. `de`, `fr`). Senza indicazione vale l'impostazione d'archivio, altrimenti la lingua principale dell'archivio — vedi [lingua dei contenuti dell'importazione](#lingua-dei-contenuti-dellimportazione)|
|--update                  |aggiornare schede esistenti invece di crearne di nuove; confronto per impostazione predefinita tramite l'`id`|
|--default-excel-column=   |`id` (predefinito), `uuid` oppure `identifier` — determina, con `--update`, in base a che cosa vengono trovate le schede|
|--no-validation           |do not validate the file|
|--skip-parent-validation  |to build hierarchies with one excel file|
|--create-actors           |create new actors if they dont exist|
|--create-keywords         |create new keywords if they dont exist|
|--create-places           |create new places if they dont exist|
|--create-locations        |create new locations if they dont exist|
|--create-object-types     |create new object_type terms if they dont exist|
|--show-rules              |show rules for this file|
|--show-columns            |show the original columns of this file|
|--show-column-mapping     |show columns with mapping|
|--show-possible-columns   |show all possible column names|
|--show-mapping            |show mapping for this file|
|--show-separators         |show separators|
|--from-ead                |import file is an EAD 2002 or EAD3 file (use with --parent)|
|--parent=                  |the record the fonds goes under (id, UUID or signature)|
|--no-ead-validation        |do not check the EAD file against its schema before the import|
|--show-ead                 |show the rows the EAD file makes|
|--no-ead-import            |check and show only, import nothing|

Esempio
```bash
php artisan anton:import test_2-ead.xml --from-ead --create-actors --create-places --create-keywords --parent=1 --env=kr --import
```

Il file si trova in `metadata_to_import`, come una tabella Excel. Viene letto
ciò che scrivono gli export EAD 2002 ed EAD3 di Anton: tutte le note ISAD(G) (in
Markdown), i punti di accesso come parole chiave, attori e luoghi, le lingue, la
datazione, la consistenza, i titoli in altre lingue. Un attore già presente
nell'archivio con lo stesso numero GND viene ripreso invece di essere creato di
nuovo. Il file viene verificato rispetto al suo schema prima dell'importazione;
un file non valido non importa nulla. `anton:import-ead <file>` verifica un
file e ne mostra le righe senza importare.

## Confrontare le segnature {#signaturenabgleich}

In **Admin → Import / Export → Confronto di segnature** è possibile confrontare un elenco di segnature con il fondo: incollalo o carica una tabella (CSV, Excel, ODS, viene letta la prima colonna), al massimo 50 000 segnature. Il risultato appare nella pagina o si scarica in CSV. Ciò che non puoi vedere conta come non trovato.
