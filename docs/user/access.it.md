# Accesso, schede non pubblicate e termini di consultabilità

Anton regola l'accesso su tre livelli: attraverso il ruolo della persona,
attraverso l'impostazione che stabilisce se l'archivio sia pubblico e, per la
singola scheda, attraverso due cose distinte — la **non pubblicazione** della
scheda e il **termine di consultabilità**.

## L'archivio è pubblico?

L'impostazione **public_access** decide se le persone esterne vedano il
catalogo. Se è disattivata, la banca dati è aperta soltanto a chi è autenticato.
Se è attivata, il catalogo è pubblico — che cosa mostrino le singole schede lo
regolano poi non pubblicazione e termini di consultabilità.

Che cosa possa fare ciascun ruolo è indicato in
[Per iniziare](index.md#ruoli).

## Scheda non pubblicata e termine di consultabilità

> Il **termine di consultabilità** protegge i documenti; la scheda resta
> reperibile. La **non pubblicazione** sottrae l'intera scheda, descrizione
> compresa.

| | Scheda non pubblicata | Termine di consultabilità |
|---|---|---|
| Descrizione (titolo, date, descrizione archivistica) | invisibile | visibile e reperibile |
| Immagini e documenti | invisibili | solo da «Consultabile dal» |
| Unità subordinate | sempre non pubblicate anch'esse | tipo: no; «Consultabile dal» impostato a mano: sì |
| Limitato nel tempo | no | sì |

Entrambe restano visibili all'utenza interna, a chi descrive e
all'amministrazione. Un archivio può aver rinominato i campi; da Anton 0.108 i
nomi standard sono quelli usati qui.

## Scheda non pubblicata

Il campo **Scheda non pubblicata** sottrae l'intera scheda al pubblico:
descrizione, media e tutte le unità subordinate. Non compare né nella ricerca né
attraverso le interfacce (API, OAI, sitemap). La non pubblicazione si eredita
sempre verso il basso — sotto una scheda non pubblicata non ce n'è una pubblica.

## Termine di consultabilità

Il termine di consultabilità protegge solo i documenti e le digitalizzazioni: se
un'unità di descrizione vi è ancora soggetta, la scheda resta visibile e
reperibile, le immagini e i documenti no.

Anton calcola per ogni scheda **un** anno dal quale è consultabile. Fanno fede:

1. **Il campo «Consultabile dal».** Questo valore ha la precedenza e **vale
   verso il basso nell'albero** per tutte le unità subordinate.
2. **Altrimenti il termine di consultabilità del tipo scelto**, calcolato a
   partire dalla data di creazione. I termini legati al tipo valgono **solo per
   la scheda stessa** e non si ereditano.

Il campo **Termine di consultabilità** seleziona il tipo. Per impostazione
predefinita ne sono previsti tre:

| Tipo | Termine |
|---|---|
| pubblico | nessuno — subito consultabile |
| termine standard | 30 anni |
| termine prolungato | 70 anni |

I termini sono configurabili per archivio: i tipi possono essere rinominati,
integrati e modificati nella durata; è possibile anche «mai consultabile». La
gestione è riservata ai superuser; con Anton as a Service se ne occupa k & r.

!!! note "«Consultabile dal» è il primo anno libero"
    Con creazione nel 1990 e un termine di 30 anni vi si legge 2021: dal 2021 i
    documenti sono consultabili. Fino alla 0.107 il campo si chiamava «Termine
    di protezione fino al» — il valore è sempre stato il primo anno libero.

## Singoli media: solo interno

I **singoli media** possono essere impostati su **solo interno** nella maschera
di modifica. Vale senza limite di tempo e solo per quel media; la scheda e gli
altri media restano come sono.

## Liberare singoli settori

A una persona con il ruolo di utente si può aprire l'accesso a determinati rami.
A tal fine, nella gestione delle utenze si inseriscono gli ID delle schede come
elenco separato da virgole. Un ID vale sempre per l'**intero ramo** sottostante.

## Stato della descrizione

Il campo è pensato per i fondi. Se un fondo è impostato su **bozza**, è
accessibile soltanto all'utenza interna, a chi descrive e all'amministrazione.
