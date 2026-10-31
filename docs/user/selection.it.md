# Selezione e azioni collettive

Più unità di descrizione possono essere spuntate negli elenchi dei risultati ed elaborate insieme. Esistono due azioni a questo scopo: lo [spostamento](hierarchy.md), dal ruolo `admin`, e la [modifica di gruppo](#sammelbearbeitung), dal ruolo `editor`.

!!! note "Solo in alcuni archivi"
    Le azioni collettive devono essere abilitate. Non sono uno standard; l'impostazione non è modificabile nell'area Admin e con Anton as a Service se ne occupa k & r. Chi non ne ha bisogno può inoltre disattivarle nel proprio [profilo](profile.md).

## Prima l'azione, poi la selezione

L'ordine è inverso rispetto all'abitudine ed è l'ostacolo più frequente:

1. **Prima** scegliere l'azione nel campo di selezione **azioni**: **sposta** o **modifica**. Prima di ciò non si può spuntare nulla; le caselle restano senza effetto.
2. **Poi** spuntare le unità. Con il simbolo dell'elenco con appunti sopra l'elenco dei risultati — che mostra il numero di unità selezionate — è possibile consultare in qualsiasi momento la selezione corrente.
3. Eseguire l'azione. Con **Svuota** la selezione viene abbandonata.

!!! warning "Cambiare azione svuota la selezione"
    Se il campo di selezione viene modificato successivamente, la selezione esistente viene abbandonata. L'azione va quindi definita prima di spuntare.

## Che cosa si può selezionare insieme

Per lo **spostamento**, soltanto unità che **potrebbero essere dello stesso livello**. Non appena è spuntata un'unità archivistica, non è più possibile aggiungere un fondo — Anton impedisce selezioni che non potrebbero essere spostate insieme. Chi non riesce a spuntare un'unità dovrebbe quindi verificare i livelli già selezionati. Per la **modifica**, si possono selezionare insieme unità qualsiasi.

Se è già in corso un'operazione di spostamento, la selezione è bloccata finché questa non è conclusa o annullata.

## Modifica di gruppo {#sammelbearbeitung}

Con l'azione **modifica**, il pulsante **Modifica (numero)** nella selezione porta alla pagina **Modifica di gruppo**. Una modifica vale lì per tutte le unità selezionate, al massimo 500 alla volta.

- **Impostare una lista di valori**: collocazione, tipo di oggetto, stato o grado di dettaglio della descrizione, oppure svuotarla; a scelta **solo dove vuoto**.
- **Impostare un campo di testo**: in una lingua, **sostituire**, riempire **solo dove vuoto** o **aggiungere in fondo** un testo (nuovo paragrafo).
- **Parola chiave**: **aggiungere** o **rimuovere** una parola chiave esistente.
- **Cerca e sostituisci**: nel titolo o in un campo di testo (tutte le lingue), a scelta rispettando maiuscole/minuscole e solo per parole intere.

Sono proposti solo i campi dei formulari di modifica dell'archivio. La ricerca è letterale, senza caratteri jolly. Segnatura, livello di descrizione e termine di protezione non si modificano in gruppo.

Lo svolgimento: prima l'**anteprima** (quante unità cambiano, le prime 20 modifiche prima e dopo; non scrive nulla), poi **Eseguire**, solo dopo un'anteprima di esattamente queste impostazioni. L'esecuzione avviene in background: Anton fa prima un **backup della banca dati**; se non riesce, nulla viene modificato. **Ultime esecuzioni** indica lo stato, il numero di unità modificate, gli errori e il nome del backup. Ogni modifica figura nella cronologia dell'unità, a nome della persona che ha avviato l'esecuzione; la si annulla tramite il backup, compito dell'amministrazione.

## Da non confondere con il carrello di ordinazione

La selezione e il [carrello di ordinazione](cart.md) si assomigliano e sono tuttavia due elenchi distinti che non si influenzano mai. La selezione serve all'elaborazione, il carrello all'ordinazione. Una selezione non può essere trasferita nel carrello di ordinazione.
