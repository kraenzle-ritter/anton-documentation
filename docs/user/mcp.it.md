# Collegare assistenti IA (MCP)

Un assistente IA come Claude o ChatGPT può fare ricerche direttamente nel
catalogo pubblico di un archivio: avere una panoramica dei fondi, cercare,
leggere schede, spostarsi nella struttura gerarchica e citare il testo
integrale dei documenti digitalizzati. Il collegamento avviene tramite il
**Model Context Protocol (MCP)**, uno standard aperto supportato dagli
assistenti più diffusi.

L'assistente risponde così non più in base a quanto appreso durante
l'addestramento, ma in base al catalogo — con la segnatura e il link di ogni
scheda su cui si basa.

!!! note "Solo dove l'archivio l'ha attivata"
    L'interfaccia va attivata per ogni archivio ed è disponibile solo per gli
    archivi con catalogo pubblico. Se l'indirizzo risponde «Not Found», lì non
    è in funzione.

## Che cosa vede l'assistente

Esattamente ciò che è visibile nel browser senza accesso: le schede con stato
«Final» che non sono [bloccate](access.md). I documenti e il loro testo
integrale solo quando il periodo di protezione è scaduto. Attori privati, campi
di testo interni e media bloccati restano esclusi.

Non c'è un accesso, e non serve — anche con un account Anton l'interfaccia
mostra solo la vista pubblica.

!!! warning "Ciò che legge l'assistente, lo legge anche il suo fornitore"
    Tutto ciò che l'interfaccia restituisce viene trasmesso al fornitore
    dell'assistente (Anthropic, OpenAI, Microsoft …). Si tratta esclusivamente
    di dati pubblici — ma è bene saperlo.

## Indirizzo

```
https://<indirizzo dell'archivio>/api/mcp
```

Ad esempio `https://archivio.example.ch/api/mcp`.

## Configurazione

### Claude (claude.ai e Claude Desktop)

**Impostazioni → Connettori → Aggiungi connettore personalizzato**, assegnare
un nome (ad esempio quello dell'archivio) e inserire l'indirizzo. Non occorre
configurare alcuna autenticazione. La disponibilità dei connettori
personalizzati dipende dall'abbonamento.

### Claude Code

```bash
claude mcp add --transport http archivio https://archivio.example.ch/api/mcp
```

### ChatGPT, Microsoft Copilot e altri

Funziona qualsiasi assistente in grado di collegarsi a un server MCP remoto
tramite «Streamable HTTP» senza autenticazione. La posizione dell'impostazione
varia secondo il prodotto e l'abbonamento; fanno fede le istruzioni del
fornitore.

## Che cosa può farne l'assistente

| Strumento | Scopo |
|---|---|
| `holdings_overview` | Che cosa contiene l'archivio? Archivi, gruppi di fondi e fondi con segnatura, titolo e datazione |
| `search_records` | Ricerca nelle descrizioni — titoli, campi di testo, attori, luoghi, parole chiave |
| `search_media_texts` | Ricerca nel testo integrale dei documenti digitalizzati; restituisce passaggi attorno a ogni occorrenza |
| `read_record` | Una scheda con tutti i campi pubblici, i dati d'autorità collegati e i documenti; il testo integrale pagina per pagina |
| `navigate_tree` | Schede superiori e inferiori, vicine |
| `lookup_authority` | Attori, luoghi e parole chiave con rimandi agli archivi d'autorità (GND, Wikidata …) e le schede collegate |

L'assistente sceglie gli strumenti da sé. Basta chiedere:

- «Che cosa contiene l'archivio?»
- «Che cosa ha riportato la Maurmer Post sulla fondazione del FC Maur? Cita i passaggi.»
- «Quali documenti riguardano la costruzione della scuola, e dove si trovano nei fondi?»

## Limiti

- **I termini di meno di tre lettere** sono indicizzati male. Far cercare le
  abbreviazioni come frase e insieme a una parola più lunga.
- **Il riconoscimento del testo (OCR) non è privo di errori.** Se una parola
  non dà risultati, spesso aiuta un inizio di parola con `*` o un'altra grafia.
- **Solo lettura.** Ordinare, modificare o creare non è possibile tramite
  l'interfaccia.
- **Numero di richieste:** 60 al minuto per indirizzo. Una ricerca ne richiede
  di solito qualche decina.

Le risposte dell'assistente restano sue. Ciò che conta è la scheda collegata —
in caso di dubbio, controllare lì.
