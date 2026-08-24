## Sintesi
È possibile importare in Anton dati e i file corrispondenti (media). I dati di descrizione (file Excel) vengono registrati in un foglio Excel (predefinito) e caricati sul server insieme ai file. I dati vengono poi validati e, se la validazione è riuscita, può avvenire l'importazione/ingest (dati di descrizione e media). Cfr. anche la documentazione in Anton sotto `/import/documentation`.

## Hub di importazione `/import`

Tutte le vie di importazione sono raccolte a un unico indirizzo: `/import` (nel menu sotto **Import / Export → Import**). La pagina ha quattro schede:

| Scheda | Contenuto |
|---|---|
| **Casella d'entrata** (predefinita) | SIP agate in attesa, ai quali manca ancora un fondo superiore. Quando qualcosa è in attesa, nel menu Admin compare accanto un badge contatore. |
| **SIP** | Caricamento SIP diretto (pacchetti BagIt) con validazione e ingest. Vedi [SIP Ingest](../admin/sip-ingest.md) e [agate SIP](../admin/agate-sip.md). |
| **Excel** | Importazioni Excel (il tema principale di questa pagina, vedi sotto). |
| **Directory** | Importazione di una struttura di directory (ZIP/GZ). |

Le vecchie URL (`/sip/validation`, `/sip/ingest`, `/import/validation`, `/import/ingest`, `/sip/inbox`) reindirizzano in modo trasparente alla scheda corrispondente — segnalibri e link esterni restano validi.

### Vista di dettaglio nella casella d'entrata

Per ogni SIP in attesa nella casella d'entrata esiste un link **Dettagli**. Dietro si trova una pagina di ispezione che legge solo il `metadata.json` dal BagIt (senza estrarre i media) e mostra:

- la validità BagIt (manifesto, somme di controllo)
- il numero di schede nel SIP
- le categorie di tipo di oggetto NARA — con un avviso se il tenant non conosce alcun tipo adeguato per una categoria
- il titolo della scheda più alta

Così, prima dell'importazione, si può vedere se il SIP è sensato, se il vocabolario del tenant è adatto e, all'occorrenza, scartare il SIP prima che qualcosa finisca nella banca dati.

### Avanzamento in tempo reale

Tutte le importazioni vengono eseguite **in modo asincrono in background**. Dopo il clic su «Importa» si arriva su una pagina di avanzamento che aggiorna lo stato corrente ogni pochi secondi: fase (preparazione / creazione delle schede / lettura dei media), righe elaborate e, alla fine, un link all'**esecuzione nel protocollo delle importazioni**.

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

## Svolgimento (importazione Excel)
Occorre anzitutto creare un file Excel secondo le indicazioni seguenti. Questo va caricato sotto «Upload Metadata» e i file multimediali corrispondenti sotto «Upload Medien». Infine il file Excel può essere verificato sotto «Validation». La validazione segnala gli errori ed emette avvertimenti. I dati possono essere importati solo quando la validazione è priva di errori. L'importazione viene avviata sotto «Ingest» e, a seconda del volume, può richiedere alcuni minuti.

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

Una colonna con sigla di lingua (`title_fr`) prevale su questa scelta per il proprio campo — vedi [titel](#titel-title).

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
Il file può contenere colonne aggiuntive; queste però non vengono importate. Per semplicità le colonne possono essere eliminate. Il file definitivo deve contenere almeno le colonne seguenti:

    parent
    verzeichnungsstufe

## Spiegazione e regole per le singole colonne / campi

### parent

Il campo `parent` indica dove viene agganciata la scheda da importare. Il campo non deve essere vuoto. Può contenere al massimo 100 caratteri. Deve contenere una segnatura già esistente nella banca dati.

Poiché in Anton possono esistere unità di descrizione senza segnatura (ad es. classi, gruppi di fondi), è anche possibile indicare il `parent` tramite l'`id`. Se nel `parent` si trova un numero intero (integer), l'importatore presuppone che si intenda il `parent_id`. L'`id` di un'unità di descrizione è visibile nel `permalink`.

### Verzeichnungsstufe (level_of_description)

Il campo non deve essere vuoto. Deve contenere un livello di descrizione esistente:

    Archiv
    Bestandsgruppe
    Bestand
    Klasse
    Serie
    Dossier
    Einzelstück

### signatur (identifier)

Il campo può contenere al massimo 100 caratteri. Ogni segnatura può comparire una sola volta. Se non è indicata alcuna segnatura, Anton genera una nuova segnatura univoca.

### altsignatur (identifier_old)

Il campo può contenere al massimo 100 caratteri.

### titel (title)

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

### Antonevents
Gli Antonevents collegano le unità di descrizione ad attori, attrici e luoghi. Sono composti dai campi seguenti: `actors, place, date_start, date_start_ca, date_end, date_end_ca, date_event_details`. Per importare un Antonevent, l'EventType va ora posto nella denominazione della colonna prima del nome del campo, ad esempio per la creazione (estremi cronologici):  `creation_actors, creation_place, creation_date_start, creation_date_start_ca, creation_date_end, creation_date_end_ca, creation_date_event_details`.

Esistono numerosi Antonevents: `creation`, `acquisition`, `accumulation`, `destruction`, `validation`, `migration`, `reproduction`, `publication`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. 

#### Attori e attrici (ad es. creation_actors)

Il campo può contenere al massimo 500 caratteri. L'indicazione del periodo di esistenza (date di vita) tra parentesi non è obbligatoria, ma è possibile. Le parentesi tonde non devono però essere usate per altri scopi. Più attori o attrici dovrebbero essere separati con `::`.

Esempio per due attori: 

```
Müller, Martina (1934-1977) :: Rechtsabteilung
```

Il formato non viene validato in anticipo! Attori e attrici vengono creati se non sono trovati in Anton (la ricerca avviene per nome).

Impostazione di importazione `create-actors`: attori e attrici vengono creati se non sono trovati in Anton.

Se un attore o un'attrice è già registrato in Anton, può essere richiamato anche tramite il proprio ID (integer).

Se un attore o un'attrice è stato registrato con una GND o un'altra risorsa, può essere riconosciuto anche in base a tale risorsa, aggiungendo all'indicazione un prefisso (in minuscolo e con due punti, senza spazio): «gnd:118519522» (la risorsa deve però essere univoca all'interno di Anton). Se l'attore o l'attrice non esiste ancora, viene creato in base ai dati della GND.

#### Places
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

### objekttyp (object_type)

Il campo deve contenere un tipo di oggetto già esistente:

```
Akte
Bild
Band
Film
...
```

L'elenco dei valori ammessi dipende dai tipi di oggetto definiti dal rispettivo archivio.

### umfang_zahl (object_count)

Il campo deve contenere un numero intero (integer). L'indicazione si riferisce al tipo di oggetto.

### sprache (languages)

Il campo può contenere più lingue. Le lingue devono corrispondere al [codice di lingua ISO 639-2/B](https://it.wikipedia.org/wiki/ISO_639-2) («ger» non «deu», «fre» non «fra») oppure essere scritte esattamente come nell'elenco esistente. Più lingue possono essere separate con i caratteri seguenti (virgola e punto e virgola non sono possibili):

```
    ::
```

### standort (location)

Il campo deve contenere una collocazione già in uso. Se si vuole utilizzare una nuova collocazione, va prima aggiunta in Admin - Collocazioni.

Esistono due colonne e il nome indica in ciascun caso che cosa vi appartiene: **`location_id`** accetta solo l'ID, **`location`** (anche: `standort`) accetta ID *o* denominazione. Se sono presenti entrambe, prevale `location_id`.

### formularsatz (formset)

Determina quale set di formulari viene utilizzato per la scheda — ossia quali campi compaiono e in quale ordine. Il campo è **facoltativo**: se resta vuoto, Anton risolve il set di formulari attraverso il livello di descrizione. È necessario solo se una scheda se ne discosta deliberatamente, ad esempio il set di formulari `letter` su unità documentarie.

Come per la collocazione, due colonne: **`formset`** (anche: `formularsatz`) accetta il nome *o* l'ID, **`formset_id`** solo l'ID. I nomi dei set di formulari disponibili si trovano in *Amministrazione → Set di formulari* — in un'installazione standard ad esempio `fonds`, `class`, `series`, `file`, `item`, `collection`, `recordgroup`, `default`.

La tabella di aggiornamento scaricata riporta la colonna `formset` e scrive il **nome**. Una cella vuota lascia il set di formulari invariato.

### vacat

Indica se l'unità di descrizione è un segnaposto (una lacuna nella numerazione
alla quale non corrisponde alcuna documentazione).

La colonna gestisce internamente ID di termini. Vengono accettati la
denominazione (`vacat`), l'ID (`56` per vacat, `57` per non vacat) e — da
tabelle più vecchie — `1` e `0`.

Viene **esportata** la denominazione: `vacat` per un segnaposto, altrimenti
una cella vuota. Le tabelle più vecchie con `56`/`57` possono continuare a
essere utilizzate senza modifiche.


### bilder (media)

Il campo può contenere al massimo 500 caratteri. Più nomi di file (assets) possono essere separati con i caratteri seguenti:

```
, ; ::
```


Esempio:

```
erstes_bild.tif::zweites_bild.tif
```

### schutzfrist (period_of_protection)

Il campo deve contenere un termine di protezione esistente:

```
public
standard
prolonged
```

### private

Il campo può contenere solo 0 (no) o 1 (sì). Se private non contiene alcun valore, viene impostato 0.


### status_of_description

Il campo può contenere solo nomi della relativa lista di valori:

```
draft
final
```

### detail_of_description

Il campo può contenere solo nomi della relativa lista di valori::

```
minimal
partial
full
```

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

Oltre alla creazione di nuove schede, le unità di descrizione esistenti possono essere aggiornate anche direttamente tramite browser. A questo scopo, sotto **Importazione tabellare** esiste una scheda propria **«Update»** (dopo *Metadati* e *Media*). Lì si carica la tabella — i file di aggiornamento hanno un elenco proprio, separato dall'importazione normale — e si apre con **«Dettagli»**. Il file viene verificato direttamente in modalità aggiornamento e compare il pulsante **«Carica come aggiornamento»**.

Poiché la scheda *Update* verifica il file esclusivamente come aggiornamento, una tabella di solo aggiornamento (solo `id` + le colonne da modificare, senza `parent`) non richiede scorciatoie: la colonna `parent`, necessaria alla creazione, qui non è richiesta. La scheda *Metadati* regolare resta invariata per la creazione.

Un aggiornamento sovrascrive i campi delle schede esistenti «sul posto» — **non vengono create nuove schede**. Perché un aggiornamento resti sicuro e prevedibile valgono tre presupposti. Se uno di essi è violato, il file viene bloccato e il motivo è visualizzato nella pagina di ispezione:

1. **Ogni riga necessita di un `id` numerico.** Attraverso questo `id` viene trovata la scheda da aggiornare. L'`id` di un'unità di descrizione è visibile nel `permalink`.
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

Il file contiene esclusivamente colonne che un aggiornamento è autorizzato a scrivere — `id`, le colonne dei campi, le lingue, la collocazione (`location_id`), parole chiave / attori / luoghi (come ID) e le colonne dei campi di testo `note.*`. Non sono deliberatamente **compresi** `parent` e le colonne di evento, che bloccherebbero l'aggiornamento. La colonna `identifier` serve solo all'orientamento: l'aggiornamento trova le schede tramite l'`id`, e le modifiche alla segnatura restano senza effetto.

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

!!! note "Solo tramite l'`id` interno"
    L'aggiornamento nel browser trova le schede sempre tramite l'`id` interno, mai tramite la segnatura. Un aggiornamento tramite la segnatura è possibile solo da riga di comando (`--update --default-excel-column=identifier`, vedi sotto).

## Importazione da riga di comando


### Importazione semplice

Per il cliente (slug) «besenval» e il file Excel «test.xlsx» il comando di importazione è:

```bash
php artisan anton:import --env=besenval --file="test.xlsx" --import
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
|--default-excel-column=   |`id` (predefinito) oppure `identifier` — determina, con `--update`, in base a che cosa vengono trovate le schede|
|--dont-validate           |do not validate the file|
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
|--from-ead                |import file is a xml-ead file (also use --parent and --dont-validate)|
|--parent=                  |if import file is an ead you need a parent|

Esempio
```bash
php artisan anton:import customers/kr/ead/test_2-ead.xml --from-ead --dont-validate --create-actors --create-places --create-keywords --parent=1 --env=kr -vv --import --no-backup
```
