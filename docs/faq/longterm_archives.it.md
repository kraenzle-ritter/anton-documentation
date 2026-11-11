# Anton come archivio digitale

Anton acquisisce i documenti digitali con verifica, ne riconosce e valida i formati e registra quanto bene possono essere conservati. Anton modifica un master solo dove l'archivio lo ha configurato o richiesto, per esempio con una regola di formato all'acquisizione o con una migrazione; entrambe vengono verificate e registrate sul media. Questo vale sia per Anton [as a Service](anton_as_service.md) sia per l'esercizio [on Premises](anton_on_premises.md).

## Offerta di base e offerta completa

Con Anton as a Service ogni abbonamento comprende l'**offerta di base «Archivio digitale»**: archiviazione e backup in quattro copie in tre sedi, tutti i controlli (checksum, virus, identificazione e validazione dei formati), i rapporti e la sostituzione dei file danneggiati a partire dal backup. Nell'offerta di base non agiamo di nostra iniziativa: non esaminiamo i protocolli, non valutiamo i rischi dei formati e migriamo i file solo su indicazione dell'archivio. La responsabilità dell'archiviazione digitale resta quindi all'archivio; Anton gli mette a disposizione i rapporti e gli strumenti necessari.

L'**offerta completa Archivio digitale** si può aggiungere a ogni abbonamento. È composta da due pacchetti:

- **Backup aggiuntivo:** un ulteriore backup indipendente, con un altro software, presso un altro fornitore, in un altro luogo, in Germania o, su richiesta, in Svizzera. Per 30 giorni nessuno può cancellare o sovrascrivere uno stato di backup, nemmeno noi.
- **Preservation Management:** esaminiamo i protocolli ogni mese e chiariamo con l'archivio le anomalie, valutiamo i rischi dei formati, curiamo l'elenco e le regole dei formati e migriamo di nostra iniziativa i formati a rischio. Consultiamo l'archivio solo se una misura richiede più spazio di quello prenotato o comporta un onere straordinario; lo stimiamo in anticipo e ne facciamo un'offerta.

I prezzi con e senza offerta completa si trovano nell'[offerta su anton.ch](https://anton.ch/#pricing); l'offerta completa viene fatturata a partire dal 2027. In Anton il pacchetto Preservation Management si chiama ancora «Technische Betreuung» (vedi il [mandato di conservazione](../admin/preservation-mandate.md), in tedesco e inglese).

!!! note "On Premises"
    Chi gestisce Anton sui propri server è responsabile in prima persona dell'archiviazione, della ridondanza e del backup. L'infrastruttura qui descritta e i due pacchetti fanno parte del nostro esercizio e non vengono forniti con il software. Siamo volentieri a disposizione per una consulenza sulla configurazione.

## Archiviazione e backup

La cosiddetta _bitstream preservation_, cioè l'archiviazione e il backup veri e propri dei dati, è garantita dall'infrastruttura di esercizio. **Con Anton as a Service** i dati digitali sono conservati in quattro copie in tre sedi in Svizzera: sul server di produzione, in un centro di calcolo, i dati di produzione e un backup locale cifrato, più un backup su ciascuno di due server di backup in due sedi a Zurigo (vedi [Infrastruttura](infrastructure.md)). Le due sedi zurighesi condividono i rischi regionali. Il backup aggiuntivo dell'offerta completa aggiunge un luogo indipendente da esse; è in esercizio di prova da novembre 2026.

All'acquisizione Anton calcola due checksum per ogni file e una volta al mese controlla rispetto a esse l'intero patrimonio di ogni archivio. Se il controllo trova un file modificato, lo sostituiamo con la versione invariata del backup e lo controlliamo di nuovo. Ogni nuovo file passa un controllo antivirus prima dell'acquisizione; i file infetti vengono messi in quarantena. Nelle installazioni con un archivio a lungo termine collegato (DIMAG), è quest'ultimo a garantire la bitstream preservation. Maggiori informazioni in [Archiviazione a lungo termine: panoramica](../admin/preservation.md).

L'accesso ai dati avviene esclusivamente tramite Anton, che consente solo accessi autorizzati. Per i dati protetti dalla legge può essere necessario chiarire criteri supplementari, come la sede del server possibile o consentita. Grazie ai metadati in Anton i dati sono in ogni momento reperibili e disponibili in modo semplice e rapido.

Sosteniamo volentieri i nostri clienti nella preparazione dell'_acquisizione_ (valutazione, ingest, pre-ingest ecc.) e del _preservation planning_.

## Preservation planning

### Identificazione dei formati

L'identificazione dei formati basata sul MIME type o sull'estensione del file è integrata in Anton da [Siegfried](https://www.itforarchivists.com/siegfried) e/o [Fido](https://github.com/openpreserve/fido). Entrambi gli strumenti identificano i formati di file in base agli ID [PRONOM](https://www.nationalarchives.gov.uk/pronom/). Ciò consente di determinare con precisione i formati di file per l'archiviazione a lungo termine. Anton apre inoltre ogni nuovo file e verifica se può essere letto per intero; controlla l'intero patrimonio una volta all'anno.

### Valutazione dei rischi

Dall'ID PRONOM Anton ricava la valutazione dei rischi del [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation). È la base per le decisioni sulle misure di conservazione, per esempio il trasferimento in un altro formato.

Anton rivaluta ogni notte i formati del patrimonio e segnala nel rapporto mensile i nuovi formati e i rischi aumentati. Il [preservation planning](../admin/preservation-planning.md) nell'area di amministrazione mostra i formati di file presenti nell'archivio con la loro valutazione dei rischi. Senza offerta completa l'archivio valuta da sé il rapporto e commissiona le migrazioni; con l'offerta completa ce ne occupiamo noi. Il file consegnato viene conservato in ogni caso.

## Modello OAIS

Il modello di riferimento OAIS (Open Archival Information System, ISO 14721) descrive le funzioni di un archivio digitale e i pacchetti con cui i documenti entrano ed escono: il pacchetto di versamento (SIP), il pacchetto di archiviazione (AIP) e il pacchetto di distribuzione (DIP). Anton copre le funzioni come segue:

| Funzione | Che cosa fa Anton |
|---|---|
| Acquisizione (Ingest) | Importazione da Excel, secondo eCH-0160 ed E-ARK; caricamento nel browser o tramite codice QR; controllo antivirus, due checksum, identificazione dei formati secondo PRONOM, controllo di leggibilità, conversione secondo le regole di formato |
| Archiviazione (Archival Storage) | Quattro copie in tre sedi, backup ogni notte, controllo mensile con riparazione dal backup; con l'offerta completa il backup aggiuntivo |
| Gestione dei dati (Data Management) | Descrizione secondo ISAD(G), dati di autorità (GND, Geonames, Wikidata), indirizzi permanenti, eventi di conservazione secondo PREMIS |
| Pianificazione della conservazione (Preservation Planning) | Elenco e regole dei formati per archivio, valutazione dei rischi secondo NARA, migrazione; con l'offerta completa valutiamo i rischi e migriamo di nostra iniziativa |
| Accesso (Access) | Ricerca pubblica, ordinazione e prestito; OAI-PMH e REST; esportazione in EAD, Dublin Core, RiC-O, CIDOC CRM e PREMIS; pacchetti secondo E-ARK e OCFL |
| Amministrazione | Account, ruoli e autorizzazioni; protocollo di tutte le modifiche; rapporto mensile; con l'offerta completa esaminiamo il rapporto mensile |

In Anton il pacchetto di archiviazione non esiste come file separato: è costituito dal master sullo storage e dalla descrizione, dalle checksum e dagli eventi di conservazione nella banca dati. Diventa un pacchetto solo all'esportazione, secondo E-ARK o OCFL.

Panoramica in PDF: [Archivio digitale in Anton e modello OAIS](https://anton.ch/docs/anton-oais-modell.pdf) (in tedesco).

## Livelli NDSA

I «Levels of Digital Preservation» della National Digital Stewardship Alliance (NDSA, USA), versione 2.1, sono un metro diffuso per misurare quanto bene un'istituzione conserva i documenti digitali. Suddividono la conservazione in cinque ambiti (archiviazione, integrità, controllo, metadati, formati di file) e ogni ambito in quattro livelli, da «conoscere i propri documenti» a «conservare i propri documenti nel tempo». Un livello è raggiunto solo quando tutti i suoi requisiti sono soddisfatti.

Abbiamo valutato noi stessi Anton as a Service secondo questi livelli, con una prova per ogni requisito; non si tratta di una certificazione da parte di un ente esterno. L'offerta di base raggiunge il livello più alto in due ambiti su cinque (integrità e metadati). Con l'offerta completa lo raggiunge in tutti e cinque: il backup aggiuntivo riguarda l'archiviazione, il Preservation Management il controllo e i formati di file. I livelli non misurano il lavoro professionale dell'archivio, per esempio se un fondo è descritto per intero e valutato correttamente.

I requisiti nel dettaglio si trovano in due PDF (in tedesco):

- [Das Digitale Archiv in Anton und die NDSA-Stufen](https://anton.ch/docs/anton-ndsa-stufen.pdf): tutti i 38 requisiti con la nostra misura
- [Kurzfassung](https://anton.ch/docs/anton-ndsa-kurzfassung.pdf) (sintesi)

In entrambi i documenti le parti dell'offerta completa compaiono ancora separatamente, come «Paket Zusätzliche Sicherung» (backup aggiuntivo) e «Paket Preservation Management».
