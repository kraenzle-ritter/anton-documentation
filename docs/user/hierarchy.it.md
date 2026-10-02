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

Anton rappresenta la struttura archivistica in due parti e, dove l'archivio l'ha
attivato, anche come [albero archivistico](#archivbaum):

- Sopra ogni scheda si trova il **percorso** — la catena delle unità superiori,
  rientrata a gradini e collegata.
- Sotto la vista di dettaglio si trova la sezione **contenuto** con l'elenco
  delle unità subordinate.

### Albero archivistico {#archivbaum}

Dove l'archivio l'ha attivato (`archive_plan_modal`, vedi
[Impostazioni](settings.md)), il pulsante **Albero archivistico** si trova
accanto a **Lista** nella pagina di dettaglio e accanto al percorso
nell'elenco del piano di classificazione. Apre la struttura come albero in una finestra propria. La
denominazione si può adattare per archivio e lingua
([Pagina iniziale e navigazione](../admin/home.md)).

- L'albero è espanso fino alla scheda corrente, evidenziata e al centro. Al
  livello superiore, il primo livello sottostante è già espanso.
- Quando la scheda esce dalla vista compare **Localizza**, che riporta lì; i
  rami aperti restano aperti.
- Ogni riga mostra segnatura, titolo e livello di descrizione tra parentesi,
  come il percorso. La freccia espande e comprime un livello; il titolo apre la
  scheda.
- I livelli con molte voci arrivano a blocchi di cento: **apri le 100 voci
  successive** e, per una scheda in fondo al livello, anche **apri le 100 voci
  precedenti**.
- Le schede che non potete vedere non compaiono né come riga né nel conteggio.

Chi non ha bisogno del pulsante lo nasconde nel proprio profilo sotto
**Impostazioni**.

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
