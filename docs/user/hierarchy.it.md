# Struttura archivistica e spostamento

Tutte le unità di descrizione sono inserite in una struttura ad albero, la
struttura archivistica. Ogni unità ha esattamente un'unità superiore — fanno
eccezione gli archivi al livello più alto.

## Livelli di descrizione

I livelli seguono lo standard ISAD(G) e determinano che cosa può essere creato
sotto un'unità:

| Livello | Unità subordinate ammesse |
|---|---|
| Archivio | Gruppo di fondi, Fondo |
| Gruppo di fondi | Gruppo di fondi, Fondo |
| Fondo | Serie, Classe, Unità archivistica, Unità documentaria |
| Classe | Serie, Classe, Unità archivistica, Unità documentaria |
| Serie | Serie, Unità archivistica, Unità documentaria |
| Unità archivistica | Unità archivistica, Unità documentaria |
| Unità documentaria | Unità documentaria |

Un fondo all'interno di un fondo non è ammesso e viene rifiutato da Anton.

## Navigare nell'albero

Anton non rappresenta la struttura archivistica come un albero espandibile, ma
in due parti:

- Sopra ogni scheda si trova il **percorso** — la catena delle unità superiori,
  rientrata a gradini e collegata.
- Sotto la vista di dettaglio si trova la sezione **contenuto** con l'elenco
  delle unità subordinate.

## Spostare le schede

Lo spostamento avviene in due fasi: prima la scheda viene contrassegnata, poi si
raggiunge la destinazione.

1. Sulla scheda da spostare fare clic sul pulsante **Sposta**. Compare una
   fascia gialla con l'indicazione «Scheda da spostare», la segnatura e il
   titolo. Con la ✕ nella fascia si annulla l'operazione.
2. Navigare fino alla scheda di destinazione. La fascia resta visibile.
3. Nella fascia scegliere la posizione desiderata: **prima**, **dentro** o
   **dopo** questa scheda.

!!! tip "Nessun link visibile nella fascia?"
    I link compaiono solo se il livello di descrizione è ammesso nella posizione
    di destinazione. Un'unità archivistica non può essere spostata «dentro»
    un'unità documentaria — in quel caso la fascia non offre alcuna scelta. Uno
    sguardo alla tabella qui sopra mostra se la posizione desiderata è
    possibile.

Più schede possono essere spostate insieme; il loro ordine viene mantenuto a
destinazione. Gli archivi al livello più alto non possono essere spostati.
Nemmeno è possibile spostare una scheda all'interno del proprio sottoalbero —
Anton lo rifiuta e salta la scheda interessata.

Con lo spostamento la segnatura **non** cambia. Se necessario va adattata
manualmente in seguito.
