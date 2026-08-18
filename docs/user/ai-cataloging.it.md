# Descrizione assistita dall'IA

Anton può far generare a un modello linguistico proposte per la descrizione:
esso legge i media allegati e propone titoli, campi di testo, eventi, parole
chiave, attori e attrici, luoghi e lingue.

!!! note "Da abilitare prima"
    La descrizione assistita dall'IA al momento non è attiva per impostazione
    predefinita. Presuppone due cose: un'abilitazione nella configurazione del
    server, non raggiungibile dall'area Admin — con Anton as a Service la imposta
    k & r — e l'interruttore nell'archivio stesso. Inoltre deve essere impostato
    un limite di costo; se manca, tutte le richieste vengono interrotte.

## Generare proposte

Nella maschera di modifica si trova il blocco **Descrizione IA**; il pulsante
omonimo in alto vi conduce. Un clic su **genera proposte IA** invia la richiesta;
le proposte compaiono quindi come etichette accanto ai campi interessati,
ciascuna con **applica**, **aggiungi** e **ignora**.

Nulla viene scritto automaticamente nella banca dati — le proposte finiscono nel
formulario e vengono salvate solo con il normale pulsante di salvataggio. La
generazione presuppone il ruolo `editor`.

## Che cosa Anton riprende da sé — e che cosa no

Le impostazioni predefinite sono volutamente disuguali:

| Proposta | Impostazione predefinita |
|---|---|
| Attore/attrice, luogo, parola chiave — **già presenti** | vengono collegati |
| Attore/attrice, luogo, parola chiave — **da creare** | vengono scartati |
| **Titoli e campi di testo** | vengono scartati |

Ciò significa: **l'IA non modifica mai il titolo di propria iniziativa.** Chi
vuole una proposta deve applicarla espressamente. E nuove schede di autorità non
nascono per inerzia — la soglia per nuovi attori, attrici e parole chiave resta
volutamente alta.

Gli eventi proposti vengono creati da Anton come **Periodo di creazione**. Se si
tratta di un altro tipo di evento, va corretto a mano dopo l'applicazione.

## Protezione dei dati

Anton contrassegna ogni profilo IA in base al luogo in cui elabora i dati: 🇨🇭
per i modelli ospitati in Svizzera, ⚠️ per tutti gli altri. Con un profilo non
svizzero compare un avviso rosso:

> **⚠️ Attenzione — protezione dei dati**
> Questo profilo elabora dati fuori dalla Svizzera e NON è conforme a
> LPD/GDPR. Utilizzarlo esclusivamente per dati che si pubblicherebbero anche
> apertamente.

È preimpostato un profilo svizzero. Sceglierne un altro è una decisione
consapevole caso per caso: la selezione è ripiegata, vale solo per la richiesta
in corso e non viene memorizzata.

!!! danger "Verificare prima dell'invio"
    Con la richiesta i contenuti dell'unità di descrizione — media compresi —
    lasciano l'archivio. Per i fondi bloccati, i dati personali e tutto ciò che è
    soggetto a un termine di protezione questo non è ammissibile con un profilo
    non svizzero.

Ogni richiesta viene registrata; consumo, costi e una traccia di audit si trovano
in **Admin → Descrizione IA**.
