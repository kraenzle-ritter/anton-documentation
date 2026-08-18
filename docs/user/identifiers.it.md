# Segnature

Anton crea le segnature automaticamente. Qui viene descritto lo schema standard;
la formazione delle segnature è modificabile per archivio tramite
l'impostazione `identifier_generator`:

| Valore | Comportamento |
|---|---|
| `standard` | Lo schema descritto qui sotto |
| `recordgroup_as_base` | Come standard, ma con il gruppo di fondi al posto dell'archivio come base |
| `id_identifier` | Numero progressivo |
| `manual_identifiers` | Nessuna attribuzione automatica — la segnatura viene inserita a mano |

È inoltre possibile programmare una formazione delle segnature specifica per
archivio. L'impostazione viene scelta in fase di configurazione e non è
modificabile nell'area Admin.

## Livelli di descrizione

|Livello di descrizione|Esempio di segnatura|Descrizione|Può contenere|
|:---------------------|:-------------------|:----------|:------------|
| Archivio | KRA | Unità complessiva di un'istituzione. Non ha un'unità di descrizione superiore. | Gruppo di fondi, Fondo |
| Gruppo di fondi | irrilevante per la segnatura | Consente di ordinare logicamente i fondi. | Gruppo di fondi, Fondo |
| Fondo | KRA 3 | Unità di una provenienza o di un versamento. I fondi sono numerati progressivamente per archivio. | Serie, Classe, Unità archivistica, Unità documentaria |
| Classe | irrilevante per la segnatura | Consente di ordinare logicamente le unità archivistiche. | Serie, Classe, Unità archivistica, Unità documentaria |
| Serie | KRA 3/22 | Quanto alle segnature si comporta come un'unità archivistica | Serie, Unità archivistica, Unità documentaria |
| Unità archivistica | KRA 3/22 | Unità di descrizione standard. Fascicoli, registri e simili vengono descritti a questo livello. Le unità archivistiche sono numerate progressivamente per fondo. | Unità archivistica, Unità documentaria |
| Unità documentaria | KRA 3/22.1 | Livello di descrizione più basso, ad esempio per fotografie o singoli documenti. | Unità documentaria |

Gruppi di fondi, classi, serie, unità archivistiche e unità documentarie possono
contenere unità dello stesso tipo (ad esempio sotto-unità archivistiche). Un
fondo all'interno di un fondo non è invece ammesso.

Per **archivio, gruppo di fondi e classe** Anton non attribuisce alcuna
segnatura — questi livelli sono irrilevanti per la segnatura e vengono, se lo si
desidera, etichettati a mano.

## Schema della segnatura
La segnatura si compone della sigla dell'archivio, del numero di fondo e dei
numeri di unità archivistica e documentaria.

```
SiglaArchivio NumeroFondo/NumeroUnitàArchivistica.NumeroUnitàDocumentaria
```

Il numero di unità archivistica e quello di unità documentaria possono essere
ulteriormente annidati. Ogni livello aggiuntivo è separato da un punto.

### Esempi
> KRA, 22/1.5     (archivio KRA;  fondo 22; serie o unità archivistica 1; sotto-unità archivistica o unità documentaria 5)

> Test, 1/1       (archivio Test; fondo  1; serie, unità archivistica o unità documentaria 1)

> HDR, 25/4.7.5   (archivio HDR;  fondo 25; serie o unità archivistica 4; serie o (sotto-)unità archivistica 7; sotto-unità archivistica o unità documentaria 5)

## Modificare le segnature a mano

La segnatura attribuita automaticamente può essere sovrascritta — il campo
**segnatura** è un normale campo di inserimento.

!!! warning "Le segnature non sono univoche"
    Anton non impone segnature univoche. Se viene inserita una segnatura già
    attribuita, al salvataggio compare un avviso con il rimando alle schede
    interessate — il salvataggio avviene comunque. L'avviso non è
    deliberatamente bloccante, poiché nella pratica i doppioni esistono.

Con lo [spostamento](hierarchy.md) di una scheda la segnatura resta invariata.
Se necessario va adattata manualmente in seguito.

## Vecchia segnatura

Per le segnature e i numeri di protocollo superati è disponibile il campo
apposito **vecchia segnatura**. Viene incluso nella
[ricerca full text](search.md).
