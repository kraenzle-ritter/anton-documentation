# Descrivere il contenuto di un film

Per i media video e audio il contenuto può essere descritto sull'asse temporale:
invece di una descrizione dell'intero film nasce un **indice** composto da voci
dotate di marcatore temporale — paragonabili a capitoli.

!!! note "Non in ogni maschera"
    L'indice è un componente del formulario e deve essere previsto nel
    [set di formulari](forms.md). Nelle unità di descrizione senza video si
    nasconde da sé.

## Registrare

Sopra la tabella si trova il lettore video. Il procedimento è pensato
espressamente per seguire la riproduzione:

1. Riprodurre il video e metterlo in pausa nel punto desiderato.
2. Il pulsante **+** crea una nuova voce **alla posizione di riproduzione
   corrente**.
3. Digitare la descrizione direttamente nella cella. Viene salvata non appena si
   abbandona il campo.

Sono inoltre disponibili: il simbolo della **puntina** imposta il marcatore
temporale di una voce esistente sulla posizione di riproduzione corrente, la
**✕** la rimuove e con la **maniglia** a sinistra le voci possono essere
riordinate con il mouse.

!!! warning "Ogni modifica ha effetto immediato"
    L'indice non ha un pulsante di salvataggio — ogni inserimento viene salvato
    immediatamente. L'eliminazione di una voce avviene senza richiesta di
    conferma e non può essere annullata.

La registrazione presuppone il ruolo `editor`.

## Nella vista di dettaglio

Lì l'indice compare come elenco con descrizione e indicazione temporale.
**Un clic su una voce fa saltare il video a quel punto** e ne avvia la
riproduzione — l'indice diventa così una navigazione all'interno del film. Lo
stesso elenco è disponibile nella [galleria dei media](gallery.md).
