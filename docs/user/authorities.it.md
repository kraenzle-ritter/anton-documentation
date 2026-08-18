# Dati di autorità (GND, Wikidata, Metagrid …)

Attori e attrici, luoghi e parole chiave possono essere collegati a voci di
banche dati di autorità e opere di consultazione esterne – ad esempio alla
[Gemeinsame Normdatei (GND)](https://gnd.network/), a
[Wikidata](https://www.wikidata.org/) o a [Metagrid](https://metagrid.ch/).
Metagrid svolge in questo un ruolo particolare: non è una singola opera di
consultazione, bensì un **servizio di collegamento** che riunisce le voci
relative alla stessa persona attraverso numerose istituzioni svizzere di ricerca
e memoria (ad es. Dizionario storico della Svizzera, Dodis, Archivio sociale
svizzero, Archivio economico svizzero).

## Come nascono i collegamenti

Durante la modifica di un attore o un'attrice, di un luogo o di una parola
chiave è possibile cercare voci corrispondenti presso i provider e salvare il
risultato pertinente come risorsa. Anton deposita quindi un link in una tabella
`resources` dedicata – il collegamento appartiene da quel momento alla scheda.

!!! note "Copia locale"
    Anton conserva i link esterni come **copia locale** e li mostra a partire da
    essa. All'apertura di un attore o di un'attrice non vengono interrogati in
    tempo reale Metagrid, GND o Wikidata a ogni visualizzazione di pagina. Ciò
    rende la visualizzazione rapida e indipendente dalla disponibilità dei
    servizi esterni – ma significa anche che i link esterni aggiunti di recente
    compaiono solo dopo un **allineamento**.

## Allineamento (sincronizzazione)

I link esterni aggiunti di recente compaiono in Anton solo dopo un
**allineamento** con i provider. Nelle installazioni di produzione questo
allineamento viene eseguito **in modo automatico e ricorrente** come processo
pianificato; la frequenza è configurabile per ciascuna installazione. Non è
necessario un intervento manuale per ogni nuovo link – i nuovi collegamenti
compaiono da sé, al più tardi alla successiva esecuzione pianificata.

!!! info "Per l'amministrazione"
    Il comando sottostante `resources:sync` e l'esercizio pianificato sono
    descritti in [Allineamento dei dati di autorità](../admin/authorities.md).

## Due direzioni

Per l'interazione con un servizio di collegamento come Metagrid conviene tenere
distinte due direzioni. Sono indipendenti l'una dall'altra.

### Anton come fonte: far conoscere nuovi attori e attrici

Quando in Anton viene registrato un nuovo attore o una nuova attrice, spetta al
servizio di collegamento e ai partner coinvolti accogliere questa voce e –
laddove opportuno – creare un link di ritorno verso Anton. Se e con quale
frequenza un partner (ad es. il Dizionario storico della Svizzera) aggiorni i
propri collegamenti lo decide il partner o il servizio di collegamento, non
Anton.

Il contributo di Anton in questa direzione è duplice:

- il **collegamento** dell'attore o dell'attrice con la voce nel servizio di
  collegamento e
- la messa a disposizione dei dati personali tramite l'
  [API di Anton](../api/index.md), così che i partner possano prelevarli
  periodicamente (per pagine, filtrati per tipo di entità).

!!! warning "Presupposto: partenariato con Metagrid"
    Questa direzione – rendere visibili i propri attori e attrici al servizio di
    collegamento – funziona **solo** se l'istituzione si è precedentemente
    **registrata come partner presso Metagrid**. Senza questo partenariato le
    persone registrate in Anton non vengono accolte da Metagrid e non nascono
    nemmeno link di ritorno. La registrazione avviene direttamente presso
    [Metagrid](https://metagrid.ch/) ed è indipendente dall'allineamento tecnico
    in Anton.

!!! tip "Nella pratica"
    Una voce pubblicata *prima* che il relativo attore o attrice esistesse in
    Anton non contiene inizialmente alcun link di ritorno verso Anton – la
    scheda di destinazione allora non esisteva ancora. Se tali voci pregresse
    vengano aggiornate a posteriori dipende dal ritmo di aggiornamento del
    rispettivo partner. Le domande sulla frequenza di allineamento o sui link di
    ritorno vanno quindi rivolte al servizio di collegamento o al partner.

### Anton come consumatore: acquisire nuovi link

Quando al servizio di collegamento si aggiungono nuove istituzioni partner,
nascono ulteriori possibilità di collegamento per gli attori e le attrici già
esistenti. Questi nuovi link compaiono in Anton **dopo il successivo
allineamento** – ossia grazie all'esecuzione pianificata descritta sopra. Non è
richiesta alcuna procedura manuale per singolo link; l'allineamento ricorrente
recupera automaticamente i collegamenti resi disponibili.

## In sintesi

- I link esterni vengono salvati localmente e mostrati a partire da lì.
- Un allineamento pianificato e ricorrente mantiene aggiornato il patrimonio
  locale e acquisisce autonomamente i nuovi link disponibili.
- Con quale rapidità **altre** istituzioni accolgano un nuovo attore o attrice
  di Anton lo decidono quelle istituzioni o il servizio di collegamento – non
  Anton.
- Perché i propri attori e attrici compaiano in Metagrid, l'istituzione deve
  essere **registrata come partner presso Metagrid**.
