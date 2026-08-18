# Accesso e termini di protezione

Anton regola l'accesso su tre livelli: attraverso il ruolo della persona,
attraverso l'impostazione che stabilisce se l'archivio sia pubblico e attraverso
i termini di protezione della singola scheda.

## L'archivio è pubblico?

L'impostazione **public_access** decide se le persone esterne vedano il
catalogo. Se è disattivata, la banca dati è aperta soltanto a chi è autenticato.
Se è attivata, il catalogo è pubblico — che cosa mostrino le singole schede lo
regolano poi i termini di protezione.

Che cosa possa fare ciascun ruolo è indicato in
[Per iniziare](index.md#ruoli).

## Termini di protezione

Se un'unità di descrizione è ancora soggetta a un termine di protezione, la
scheda resta visibile, le immagini e i documenti no.

Anton calcola per ogni scheda **un** anno di liberazione. Fanno fede:

1. **Il campo «protetto fino a»** (anno di liberazione). Questo valore ha la
   precedenza e **si eredita verso il basso nell'albero** a tutte le unità
   subordinate.
2. **Altrimenti il termine di protezione del tipo scelto**, calcolato a partire
   dalla data di creazione. I termini legati al tipo valgono **solo per la
   scheda stessa** e non si ereditano.

Il campo **condizioni di accesso / termine di protezione** seleziona il tipo.
Per impostazione predefinita ne sono previsti tre:

| Tipo | Termine |
|---|---|
| pubblico | nessuno — subito liberamente accessibile |
| termine di protezione standard | 30 anni |
| termine di protezione prolungato | 70 anni |

I termini sono configurabili per archivio: i tipi possono essere rinominati,
integrati e modificati nella durata; è possibile anche «non liberare mai». La
gestione è riservata ai superuser; con Anton as a Service se ne occupa k & r.

!!! note "L'anno di liberazione visualizzato"
    Viene visualizzato il primo anno in cui l'unità è **libera** — con creazione
    nel 1990 e un termine di 30 anni, quindi 2021 e non 2020.

## Bloccare a tempo indeterminato

I **singoli media** possono essere bloccati a tempo indeterminato nella maschera
di modifica.

Le **schede intere** vengono bloccate dal campo **bloccato**. Agisce sulla
scheda, su tutte le unità subordinate e sui loro media; restano visibili
soltanto all'utenza interna, a chi descrive e all'amministrazione.

## Liberare singoli settori

A una persona con il ruolo di utente si può aprire l'accesso a determinati rami.
A tal fine, nella gestione delle utenze si inseriscono gli ID delle schede come
elenco separato da virgole. Un ID vale sempre per l'**intero ramo** sottostante.

## Stato della descrizione

Il campo è pensato per i fondi. Se un fondo è impostato su **bozza**, è
accessibile soltanto all'utenza interna, a chi descrive e all'amministrazione.
