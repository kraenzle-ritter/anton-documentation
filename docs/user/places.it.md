# Luoghi

I luoghi sono schede autonome per le indicazioni geografiche — città, corsi
d'acqua, edifici, regioni. Come gli [attori e le attrici](actors.md) vengono
registrati una volta e poi utilizzati da un numero illimitato di unità di
descrizione. Si trovano in **Admin → Luoghi**.

Un luogo si collega a un'unità di descrizione in due modi: come **parola
chiave** (il luogo compare nel contenuto) oppure tramite un
[evento](antonevents.md) (lì è stato prodotto, ricevuto o rappresentato
qualcosa). La differenza è la stessa che vale per gli attori.

## Tipi

I tipi seguono le classi di entità di GeoNames: Stato/paese/regione, corsi e
specchi d'acqua, parchi e superfici, città/villaggio, strada/linea ferroviaria,
edificio/fattoria, montagna/collina, sottomarino nonché bosco/campo. Per ogni
archivio se ne possono aggiungere altri.

## Registrare

Il formulario contiene tipo, nome, altre forme del nome, varianti,
abbreviazioni, città/comune, cantone/regione, paese, indirizzo, descrizione,
fonti, commento e le coordinate.

I luoghi possono essere creati anche direttamente dal formulario dell'oggetto
tramite il **+** accanto all'elenco di selezione.

## Geocoordinate

Se un luogo possiede coordinate, la vista di dettaglio mostra una mappa.
Nell'elenco dei luoghi è inoltre possibile visualizzare una mappa d'insieme con
**mostra mappa**; è collegata all'elenco — spostando o ingrandendo la mappa si
filtra l'elenco sulla porzione visibile.

### Tramite i dati di autorità — la via più semplice

Se nella vista di modifica un luogo viene [collegato](authorities.md) a
**GeoNames** o a **ortsnamen.ch**, Anton riprende automaticamente le coordinate.

### A mano

Nel campo **coordinate (lat lng)** di un luogo **già salvato** i valori possono
essere inseriti direttamente.

!!! warning "Non ancora al momento della creazione"
    Le coordinate inserite nel formulario di un luogo **nuovo** non vengono
    salvate. Occorre prima creare il luogo e aggiungere le coordinate in seguito
    tramite **Modifica** — oppure ricavarle subito da GeoNames.

Anton riconosce automaticamente il formato e converte in WGS84:

| Formato | Esempio |
|---|---|
| WGS84 (gradi decimali) | `47.3769 8.5417` |
| Coordinate nazionali svizzere LV95 | `2683141 1247637` oppure `2'683'141 1'247'637` |
| Coordinate nazionali svizzere LV03 | `683141 247637` |

Il segno, i separatori delle migliaia (`'` o spazio), la separazione con spazio
o virgola e i decimali sono di volta in volta facoltativi.

Se sono presenti coordinate, nella vista di modifica compare inoltre un pulsante
per eliminarle.

## Eliminare

Un luogo può essere eliminato solo finché **non è utilizzato**. Anton rifiuta
l'eliminazione in entrambi i casi seguenti e segnala quale ricorre:

- il luogo partecipa a un **evento**,
- oppure è registrato come **descrittore** presso un'unità di descrizione.

Se si tratta di eliminare un doppione, l'**unione** è la via preferibile
all'eliminazione: i collegamenti migrano così sulla scheda che rimane invece di
andare perduti (vedi sotto).

!!! note "Diverso fino alla v0.82.0"
    Fino ad allora un luogo veniva eliminato senza controllo e i suoi
    collegamenti alle unità di descrizione sparivano silenziosamente con esso.

## Unire i doppioni

Due schede riferite allo stesso luogo possono essere unite. Eventi, link ai dati
di autorità e collegamenti alle unità di descrizione migrano sulla scheda di
destinazione. Vengono ripresi anche i campi di testo (descrizione, fonti,
commento) e le forme del nome del luogo soppresso; le sue coordinate migrano
soltanto se la scheda di destinazione non ne possiede ancora — quelle esistenti
non vengono mai sovrascritte. La vecchia scheda viene poi eliminata.

!!! note "Riservato ai superuser"
    L'unione è riservata ai superuser; con Anton as a Service se ne occupa k & r.
    Un luogo non può essere unito con sé stesso.
