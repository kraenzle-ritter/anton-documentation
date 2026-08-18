# Carrello

Il carrello — nell'interfaccia **carrello di ordinazione** — consente a chi
consulta di raccogliere unità e di inviarne un'ordinazione o una richiesta per
e-mail all'archivio. È un ausilio all'ordinazione, non una gestione dei
prestiti; i [prestiti](loans.md) sono gestiti separatamente.

!!! note "Non in ogni archivio"
    Il carrello di ordinazione deve essere abilitato per l'archivio.
    L'impostazione non è modificabile nell'area Admin, ma viene definita al
    momento della configurazione dell'installazione; con Anton as a Service se
    ne occupa k & r.

## Procedimento

1. Nella vista di dettaglio di un'unità di descrizione fare clic sul **simbolo
   del carrello**. Si trova a destra sopra la scheda e non reca alcuna
   etichetta.
2. La voce **carrello di ordinazione** compare nella navigazione — e soltanto
   ora: finché il carrello è vuoto, nel menu non esiste.
3. Sotto **carrello di ordinazione** si trovano le unità raccolte. Singole voci
   possono essere rimosse, l'intero carrello può essere svuotato.
4. Compilare il formulario soprastante e fare clic su **Invia**.

!!! warning "Solo unità archivistiche e documentarie"
    Il pulsante compare solo ai livelli **unità archivistica** e **unità
    documentaria**. Fondi e serie non possono essere ordinati — per essi occorre
    rivolgersi all'archivio.

## Il formulario

Per impostazione predefinita vanno indicati: **nome**, **e-mail**, la **data
della visita prevista** e un **messaggio**; l'**istituzione** è facoltativa. I
campi sono adattabili per archivio.

L'ordinazione parte come e-mail verso l'archivio. La persona che ordina vi
figura come indirizzo di risposta e ne riceve una copia.

## Che cosa ne fa l'archivio

L'ordinazione arriva nella **casella di posta** dell'archivio — è lì che viene
evasa. Anton non tiene **alcuna gestione delle ordinazioni**: non esiste un
elenco delle ordinazioni aperte, né uno stato, né una vista di dettaglio. Viene
valutato soltanto il numero, in [Statistiche](statistics.md) → «prestiti e
ordinazioni».

!!! danger "Verificare l'indirizzo del destinatario"
    Se per l'archivio non è memorizzato alcun indirizzo di destinazione,
    subentra un indirizzo predefinito fisso presso k & r — l'ordinazione non
    raggiunge allora l'archivio. Al momento della messa in esercizio del
    carrello di ordinazione occorre quindi verificare che l'indirizzo sia
    impostato e controllare, con un'ordinazione di prova, che arrivi a
    destinazione.

## Il carrello non dura per sempre

Il contenuto risiede nella sessione. Dopo la disconnessione o alla scadenza
della sessione non c'è più — i carrelli di ordinazione non possono essere
costruiti nell'arco di più giorni.
