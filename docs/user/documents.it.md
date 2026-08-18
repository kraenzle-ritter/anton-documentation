# Documenti

Il modulo «Documenti» offre un accesso proprio a determinati PDF — ad esempio
rapporti di attività o pubblicazioni che un archivio intende proporre
espressamente alla lettura. È una vetrina accanto alla [ricerca](search.md), non
una via ulteriore verso la struttura archivistica.

La panoramica si trova sotto `/documents` e può essere collegata dal proprio sito
web. I documenti vi compaiono ordinati per gruppi, ciascun gruppo con un breve
testo esplicativo.

!!! note "Configurazione necessaria"
    Il modulo mostra qualcosa solo se è stato configurato — vedi
    [Configurare i documenti](../admin/documents.md). Senza configurazione la
    chiamata riporta alla pagina iniziale.

## Che cosa deve garantire la descrizione

Nel modulo **un documento corrisponde a un'unità di descrizione**. Chi intende
utilizzarlo descrive quindi i PDF singolarmente e non raccolti in un'unica unità
archivistica.

## Il visualizzatore

All'apertura di un documento compare a sinistra il contenuto del campo **forma e
contenuto**, a destra il PDF.

Un indice può essere semplicemente scritto come elenco nel campo di testo:

```markdown
Indice:
- Primo capitolo (p. 5)
- Secondo capitolo (p. 17)
```

### Quando i numeri di pagina non corrispondono

Spesso i numeri di pagina stampati differiscono dalle pagine del PDF — un
rapporto con frontespizio e prefazione può iniziare la propria pagina 5 alla
pagina 17 del PDF. Affinché il salto arrivi comunque nel punto giusto, la pagina
del PDF può essere indicata come commento dopo la voce:

```markdown
Indice:
- Primo capitolo (p. 5) <!-- 17 -->
- Secondo capitolo (p. 17) <!-- 29 -->
```

Continua a essere visualizzato il numero di pagina stampato; il salto porta alla
pagina PDF indicata nel commento. Per chi legge il commento resta invisibile.
