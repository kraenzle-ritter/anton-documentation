# Anton as a Service

Anton funziona su un server affittato da k & r presso un fornitore di primo piano (ubicazione in Svizzera). k & r è responsabile sia della configurazione e della manutenzione del server (messa in sicurezza, monitoraggio, aggiornamenti e upgrade del sistema operativo) sia della configurazione e della manutenzione di Anton (aggiornamenti e upgrade).

Ogni giorno viene salvato un backup del server di produzione su due server situati in due luoghi diversi in Svizzera. Entrambi funzionano in RAID 1. Insieme ai dati di produzione e al backup locale cifrato sul server di produzione, i dati sono quindi presenti in sei copie, distribuite su tre ubicazioni (vedi [Infrastruttura](infrastructure.md)). Un ulteriore server controlla costantemente il funzionamento delle macchine coinvolte (monitoraggio), così che k & r sia sempre informato in caso di problemi e possa intervenire rapidamente.

## Vantaggi

- il personale dell'archivio necessita soltanto di un accesso a internet e di un browser aggiornato  
- costi costanti e prevedibili  
- perfetta armonizzazione tra infrastruttura (sistema operativo del server, software installato) e installazione di Anton  

## Svantaggi

- con volumi di dati molto elevati può risultare più costoso di una soluzione su server proprio  
- con dati sensibili: i dati non risiedono sul server dell'istituzione  
- con dati altamente sensibili: i dati vengono gestiti via internet (sconsigliato)  

## Costi

Anton intende permettere anche e soprattutto agli archivi di piccole e medie dimensioni di descrivere i propri fondi in modo professionale e sostenibile. Per questo la costosa infrastruttura viene condivisa tra più clienti di Anton. In questo modo aggiornamenti e upgrade possono essere applicati in qualsiasi momento in modo rapido ed economico. Per ogni istanza (cliente) vengono creati una directory dati propria (PDF, immagini, logo ecc.) e un database proprio. Questa struttura consente di mantenere relativamente contenuti i costi di configurazione e manutenzione di Anton. I dati della clientela restano comunque ben incapsulati e quindi facilmente gestibili nel loro insieme.
