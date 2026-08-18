# Anton come archivio digitale a lungo termine

L'archiviazione digitale a lungo termine è un compito molto complesso e articolato, per il quale Anton può essere impiegato [come servizio](anton_as_service.md) oppure [on premises](anton_on_premises.md).

La cosiddetta _bitstream preservation_ – ossia l'effettiva memorizzazione e messa in sicurezza dei dati – è compito dell'infrastruttura di esercizio, non dell'applicazione. **Con Anton as a Service**, cioè in esercizio sui nostri server, i dati digitali vengono conservati su un'infrastruttura adeguata che ne mantiene tre copie in tre ubicazioni – complessivamente una ridondanza sestupla.

!!! note "On premises"
    Chi gestisce Anton su server propri è responsabile in prima persona della memorizzazione, della ridondanza e del backup. L'infrastruttura descritta fa parte del nostro esercizio e non viene fornita con il software. Volentieri offriamo consulenza per la messa in opera.

Anton conserva una somma di controllo per ogni file, così da poter verificare l'integrità dei dati – ossia accertare se i dati sono stati modificati o danneggiati. Questa verifica non è un automatismo dell'applicazione, ma viene impostata per ciascuna installazione come processo ricorrente; sui nostri server è attiva per i grandi archivi. Nelle installazioni con un archivio a lungo termine collegato (DIMAG), è quest'ultimo a farsi carico della bitstream preservation. Maggiori informazioni in [Archiviazione a lungo termine: panoramica](../admin/preservation.md).

L'accesso ai dati avviene esclusivamente tramite Anton, che consente solo accessi autorizzati. Per i dati giuridicamente protetti possono rendersi necessarie ulteriori verifiche, ad esempio riguardo all'ubicazione consentita del server. Grazie ai metadati presenti in Anton, i dati restano in ogni momento facilmente reperibili e rapidamente disponibili.

Volentieri sosteniamo la nostra clientela nella preparazione della _presa in carico_ (valutazione, ingest, pre-ingest ecc.) e nel _preservation planning_.

## Preservation planning

### Riconoscimento dei formati

Il riconoscimento dei formati sulla base del tipo MIME o dell'estensione del file è completato in Anton dall'integrazione di [Siegfried](https://www.itforarchivists.com/siegfried) e/o [Fido](https://github.com/openpreserve/fido). Entrambi gli strumenti identificano i formati di file mediante gli identificativi [PRONOM](https://www.nationalarchives.gov.uk/pronom/). Ciò consente di determinare con precisione i formati ai fini della conservazione digitale a lungo termine.

### Valutazione del rischio

Con gli identificativi PRONOM possiamo cercare di riprendere in Anton la valutazione del rischio del [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation). Questa valutazione può aiutare a decidere quali misure di conservazione siano necessarie.

Nell'area di amministrazione di Anton è possibile visualizzare una panoramica dei formati di file presenti nell'archivio con la relativa valutazione del rischio.
