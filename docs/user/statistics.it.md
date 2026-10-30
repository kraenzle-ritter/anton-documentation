# Statistiche

Le statistiche analizzano il patrimonio e il suo utilizzo. Sono raggiungibili
dalla pagina Admin.

!!! note "Solo per l'amministrazione"
    Le statistiche presuppongono il ruolo `admin`. Con il ruolo `editor` non
    sono accessibili.

## Le schede

**Panoramica** conta ciò che l'archivio contiene: schede, fondi, attori e
attrici, luoghi, parole chiave, media e account utente. Vi si aggiungono lo
spazio di memoria occupato e il contingente concordato — la scheda risponde
quindi anche alla domanda su quanto sia pieno l'archivio.

**Nuovi oggetti** mostra l'incremento, suddiviso per anno e per account utente.

**Prestiti e ordinazioni** riporta le [ordinazioni](cart.md) per anno, i
[prestiti](loans.md) per anno con il confronto tra prestati e restituiti, nonché
le ordinazioni per anno e per fondo — con rimando al rispettivo fondo. È l'unica
valutazione delle ordinazioni che Anton gestisce.

**Ricerca** mostra le interrogazioni: come grafico, le interrogazioni al mese negli ultimi dodici mesi e quante hanno avuto risultati; come tabella, gli ultimi 30 giorni per tipo di ricerca con il numero di interrogazioni, i risultati e il tasso di successo; e come riepilogo, tutte le interrogazioni registrate con il totale, i risultati e il tasso di successo. Un tasso di successo basso indica che chi consulta non trova ciò che cerca. Le interrogazioni vengono contate solo finché l'impostazione `log_search_queries` è attiva; non lo è di default, perché la tabella cresce senza limite di tempo.

**Fondi** elenca per ciascun fondo segnatura, titolo, numero di voci,
consistenza in metri lineari e numero di media.

**Attori e attrici**, **luoghi** e **parole chiave** hanno ciascuno una propria
scheda con la stessa struttura: il numero complessivo, quanti di essi siano
collegati a [dati di autorità](authorities.md) e la distribuzione tra i provider
— GND, Wikidata e così via. Queste tre schede mostrano quindi a che punto sia
l'allineamento con i dati di autorità.
