# Scaricare un DIP

Un **DIP** (Dissemination Information Package) è un pacchetto ZIP con cui è
possibile trasmettere in un solo passaggio una scheda e tutto ciò che le è
subordinato — ad esempio per la consegna di documenti a terzi.

## Come si procede

Nella vista di dettaglio di una scheda compare — se abilitato per questo livello
di descrizione — un pulsante **«DIP»** nell'area di download. Un clic genera il
pacchetto e lo scarica immediatamente. Il nome del file è la segnatura della
scheda (ad es. `A.42.1.zip`).

Se non compare alcun pulsante, il download DIP non è previsto per questo
livello. Quali livelli siano abilitati lo stabilisce l'amministrazione.

## Che cosa contiene

Lo ZIP riproduce la scheda e tutte le unità subordinate come struttura di
cartelle:

- i **file multimediali** di tutte le unità contenute, in cartelle denominate
  secondo i titoli,
- uno **strumento di ricerca in Word** che descrive il contenuto con i metadati,
- per ogni file multimediale un piccolo **file di metadati** (Dublin Core),
- le **somme di controllo** (manifesto BagIt), con cui è possibile verificare in
  seguito la completezza del pacchetto.

!!! tip "Dimensione"
    Un DIP contiene **tutti** i media della scheda e delle sue unità
    subordinate. Con fondi cospicui il pacchetto può diventare grande e la
    creazione richiedere un momento.

!!! note
    A seconda dell'archivio il pacchetto può essere fornito anche in forma
    semplificata, senza strumento di ricerca e senza metadati — in tal caso
    contiene soltanto la struttura di cartelle con i file originali.
