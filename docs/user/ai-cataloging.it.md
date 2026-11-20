# Descrizione assistita dall'IA

Anton può far generare a un modello linguistico proposte per la descrizione:
esso legge i media allegati e propone titoli, campi di testo, eventi, parole
chiave, attori e attrici, luoghi e lingue.

!!! note "Da abilitare prima"
    La descrizione assistita dall'IA al momento non è attiva per impostazione
    predefinita. Presuppone due cose: un'abilitazione nella configurazione del
    server, non raggiungibile dall'area Admin — con Anton as a Service la imposta
    k & r — e l'interruttore nell'archivio stesso. Inoltre deve essere impostato
    un limite di costo; se manca, tutte le richieste vengono interrotte.

## Generare proposte

Nella maschera di modifica si trova il blocco **Descrizione IA**; il pulsante omonimo in alto vi conduce. Un clic su **genera proposte IA** invia la richiesta. Le proposte sono quindi già nei campi, esattamente come nella verifica dalla lista di verifica (vedi sotto): il modulo mostra solo i campi con proposte, ogni proposta ha **Applica** e **Ignorare**, e un campo che ha già un valore ha **Sostituire**, **Aggiungere in coda** o **Mantenere quello attuale**, con il valore attuale accanto.

Nulla viene scritto nella banca dati prima del normale pulsante di salvataggio: ciò che il modulo contiene allora viene ripreso, ciò che è stato ignorato viene scartato. Le proposte sono anche nella lista di verifica; ciò che al salvataggio resta aperto, per esempio perché va scelta una voce, vi attende. Una proposta già decisa per la scheda non viene rifatta. La generazione presuppone il ruolo `editor`.

Ogni account ha dei limiti: al massimo 30 proposte all'ora e al massimo un quarto del budget mensile al giorno. L'esercizio fissa i valori per ogni archivio. Le registrazioni audio e l'audio dei video vengono trascritti in background; finché ciò avviene, la proposta arriva senza di essi, con un avviso. Richiedendo più tardi, la trascrizione è inclusa.

## Per tutto ciò che sta sotto un'unità di descrizione

Per un versamento con molti pezzi c'è il **ciclo IA**: nella vista di dettaglio di un'unità di descrizione, il pulsante **Ciclo IA** porta a una pagina in cui si scelgono il profilo, l'ambito (solo schede con media, o tutte) e il limite di chiamate. Sotto si vede quanto costerà probabilmente il ciclo, fatturato in base al consumo, e quanto resta del budget mensile e della propria quota giornaliera. Per avviarlo occorre il ruolo `editor`.

Il ciclo lavora in background, scheda per scheda, con le stesse regole del pulsante nel modulo: le note interne non vanno al fornitore, né alcun dato delle schede bloccate. Si ferma quando è raggiunto il limite o il budget e può essere annullato; **Riprendi** continua con la scheda successiva.

Con l’ambito «solo schede con media», il ciclo salta le schede di cui nessun file può essere inviato all’IA, per esempio file Word o file mancanti; non costano nulla e compaiono nella pagina come «saltate». Se il fornitore è sovraccarico, il ciclo richiede la stessa scheda dopo una pausa, fino a tre volte.

Il ciclo non scrive nulla nelle schede. Titoli, campi di testo (ad esempio portata e contenuto), datazione, lingue, parole chiave, attori e luoghi finiscono come proposte nella lista di verifica, con la fonte «KI-Erschliessung»; lì si possono filtrare per fonte e fondo e confermare una per una o insieme. Se una voce esiste già in Anton, è preselezionata. Il ciclo non propone segnaposto come «Unbekannt» o «Nicht angegeben», e una datazione solo dove la scheda non ne ha ancora una per quell’evento. Scrive «ß» come «ss»; ogni archivio può disattivarlo con l’impostazione `ai_swiss_spelling`.

Per titolo, campo di testo e datazione, accanto alla proposta la lista mostra ciò che la scheda contiene finora. Se il campo è vuoto, la conferma riprende la proposta. Se contiene già un valore, occorre scegliere nella riga: **Sostituire il valore attuale** oppure, per un campo di testo, **Aggiungere al testo attuale**. Senza questa scelta il valore attuale resta, anche confermando più proposte insieme.

Poiché un passaggio fa più proposte per scheda, la lista di controllo mostra quelle con la fonte «KI-Erschliessung» **per scheda**: una riga per scheda con il numero di proposte aperte per tipo, nell'ordine dell'albero. In alto si può passare a **per proposta**. **Verificare le proposte** apre il modulo di modifica della scheda; la riga di paginazione in alto scorre allora la lista di verifica, e **Lista di verifica** riporta indietro. Il modulo mostra solo i campi con proposte e, sotto il titolo, le miniature delle copie digitali, che si aprono con un clic (**Mostrare tutti i campi** fa ricomparire gli altri campi). Un campo di parole chiave, attori o luoghi che manca nel modulo dell'archivio viene aggiunto in fondo se una tale voce è proposta, e le proposte sono già nei campi: il titolo e i campi di testo sono compilati e si possono modificare prima di salvare; se il campo ha già un valore, si sceglie **Sostituire**, **Aggiungere in coda** (campi di testo) o **Mantenere quello attuale**; il valore attuale è indicato accanto. Le lingue proposte sono spuntate; una parola chiave, un attore o un luogo esistente è nel suo campo come altrove. Ciò che viene creato o deciso solo al salvataggio compare accanto al suo campo, con l'indicazione **esistente** o **verrà creato**: nuove voci, un attore o un luogo per un evento (per esempio per la creazione, accanto alla sua datazione) e una datazione. Se esistono più voci di nome simile, si sceglie quella intesa. Come per la catalogazione con l'IA nel modulo, ogni proposta ha **Applica** e **Ignorare**; all'inizio è scelto **Applica**. **Salvare e continuare** salva la scheda come ogni modifica: ciò che la scheda contiene dopo viene ripreso, ciò che è stato ignorato viene scartato, e si apre la scheda successiva. Se resta una voce da scegliere, la scheda resta aperta e Anton dice che cosa manca. Chi modifica un testo proposto prima di salvare mantiene la propria versione; Anton conserva la proposta originale. **Scartare tutto e continuare** scarta tutte le proposte senza modificare la scheda, **Saltare** lascia la scheda aperta.

## Che cosa Anton riprende da sé — e che cosa no

Le impostazioni predefinite sono volutamente disuguali:

| Proposta | Impostazione predefinita |
|---|---|
| Attore/attrice, luogo, parola chiave — **già presenti** | vengono collegati |
| Attore/attrice, luogo, parola chiave — **da creare** | vengono scartati |
| **Titoli e campi di testo** | vengono scartati |

Ciò significa: **l'IA non modifica mai il titolo di propria iniziativa.** Chi
vuole una proposta deve applicarla espressamente. E nuove schede di autorità non
nascono per inerzia — la soglia per nuovi attori, attrici e parole chiave resta
volutamente alta.

Gli eventi proposti vengono creati da Anton come **Periodo di creazione**. Se si
tratta di un altro tipo di evento, va corretto a mano dopo l'applicazione.

## Protezione dei dati

Anton contrassegna ogni profilo IA in base al luogo in cui elabora i dati: 🇨🇭
per i modelli ospitati in Svizzera, ⚠️ per tutti gli altri. Con un profilo non
svizzero compare un avviso rosso:

> **⚠️ Attenzione — protezione dei dati**
> Questo profilo elabora dati fuori dalla Svizzera e NON è conforme a
> LPD/GDPR. Utilizzarlo esclusivamente per dati che si pubblicherebbero anche
> apertamente.

È preimpostato un profilo svizzero. Sceglierne un altro è una decisione
consapevole caso per caso: la selezione è ripiegata, vale solo per la richiesta
in corso e non viene memorizzata.

!!! danger "Verificare prima dell'invio"
    Con la richiesta i contenuti dell'unità di descrizione — media compresi —
    lasciano l'archivio. Per i fondi bloccati, i dati personali e tutto ciò che è
    soggetto a un termine di protezione questo non è ammissibile con un profilo
    non svizzero.

Ogni richiesta viene registrata; consumo, costi e una traccia di audit si trovano
in **Admin → Descrizione IA**.
