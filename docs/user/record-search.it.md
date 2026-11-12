# Ricerca sopra l’elenco

La ricerca sopra l’elenco sostituisce la pagina della ricerca avanzata: un clic sulla lente apre tutti i criteri di ricerca in un unico punto, sopra la tabella delle unità di descrizione. La tabella sottostante mostra i risultati e mantiene i propri filtri. L’archivio attiva la ricerca (`record_search`); senza questa impostazione resta la pagina precedente della ricerca avanzata.

## Filtri sopra ogni elenco

Sopra ogni elenco di unità di descrizione ci sono due filtri:

| Filtro | Effetto |
|---|---|
| **Filtrare la lista** | Testo che deve comparire nell’elenco |
| **Periodo** (da, a) | Unità il cui periodo di creazione tocca questo periodo; le unità senza data vengono escluse |

Entrambi i filtri restringono solo l’elenco sottostante, non il resto della pagina. Il numero di righe di un elenco non si sceglie più sopra l’elenco, ma nel [profilo](profile.md) alla voce «Elementi per pagina».

## Cercare

La lente apre la ricerca sopra la tabella. Comprende:

- **Cerca nel testo completo:** il campo di ricerca; capisce la stessa notazione della [ricerca full text](search.md) (virgolette per le frasi, segno meno per escludere)
- **Albero archivistico:** limita la ricerca a una parte dell’archivio e comprende tutto ciò che sta sotto; **Intero albero archivistico** toglie la limitazione
- **Filtri:** le faccette dell’archivio, per esempio livello di descrizione, tipo di oggetto o parole chiave, con il numero di risultati
- **Periodo:** come sopra l’elenco
- **Ricerca avanzata:** singole condizioni su campi precisi; **Aggiungi condizione** ne aggiunge un’altra, **Applica** avvia la ricerca

Tutti i criteri agiscono insieme. **Nascondi la ricerca** chiude l’area; i criteri scelti restano come chip sopra la tabella e lì si possono togliere uno per uno. **Nuova ricerca** azzera tutto.

Lo scorrimento nella vista di dettaglio, il ritorno all’elenco e le esportazioni si riferiscono ai risultati mostrati nella tabella.

## Testo completo dall’indice di ricerca

Gli archivi con [Typesense](../admin/typesense.md) possono prendere il testo completo di questa ricerca dall’indice di ricerca (`record_search_index`). L’indice tollera gli errori di battitura e trova risultati nel testo dei media, per esempio nei PDF. Albero archivistico, filtri, periodo, ordinamento e pagine provengono sempre dalla banca dati; tabella, numero di risultati ed esportazioni mostrano quindi le stesse unità.

Se l’indice trova più di 5000 risultati o non risponde, cerca la banca dati. Gli account interni (dal ruolo `user_intern`) vedono accanto al campo di ricerca chi ha risposto: «Testo completo dall’indice di ricerca» o «Testo completo dalla banca dati».

## Impostazioni

| Impostazione | Effetto | Predefinito |
|---|---|---|
| `record_search` | Ricerca sopra l’elenco al posto della pagina della ricerca avanzata | disattivato |
| `record_search_index` | Testo completo di questa ricerca dall’indice (richiede Typesense) | disattivato |
| `list_filters` | Filtri sopra gli elenchi per il personale, nell’ordine: `search` (testo), `period` (periodo); vuoto = nessuno | entrambi |
| `list_filters_extern` | lo stesso per il pubblico | entrambi |
| `search_facets_extern` | Filtri della ricerca per il pubblico, chiavi come in `search_facets` | come `search_facets` |

Gli archivi la cui ricerca è passata interamente a Typesense (`search_typesense_enabled`) prendono anch’essi il testo completo dall’indice.
