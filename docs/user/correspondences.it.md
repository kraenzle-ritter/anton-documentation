# Corrispondenze

La vista delle corrispondenze raggruppa le lettere in carteggi: mostra chi ha
corrisposto con chi, quante lettere si sono conservate e in quale arco di tempo.
Da lì il carteggio può essere sfogliato cronologicamente — avanti e indietro si
resta all'interno dello stesso carteggio.

La vista si trova sotto `/correspondences`. Non è collegata nella navigazione;
gli archivi che la utilizzano la inseriscono da sé nel menu.

## Un carteggio nasce da sé

Non c'è nulla da cliccare e nulla da creare. Anton ricava i carteggi
**automaticamente dagli [eventi](antonevents.md)**:

> Se un'unità di descrizione reca un evento **Periodo di creazione** con
> l'attore o l'attrice A e un evento **Ricezione** con l'attore o l'attrice B,
> essa vale come lettera da A a B.

La persona mittente viene quindi registrata come attore o attrice dell'evento di
creazione, la persona destinataria come attore o attrice dell'evento di
ricezione. Non appena esistono abbastanza coppie di questo tipo, il carteggio
compare nell'elenco. Viceversa: chi vuole usare questa vista deve impostare in
modo coerente entrambi gli eventi durante la descrizione — una lettera priva
dell'evento di ricezione non compare da nessuna parte.

Il livello di descrizione non ha alcun ruolo.

!!! note "Numero minimo di lettere"
    Una coppia di attori compare solo a partire da un numero minimo di lettere —
    cinque per impostazione predefinita. Le lettere isolate restano quindi
    escluse. La soglia è impostabile per archivio, ma non è modificabile
    nell'area Admin; con Anton as a Service se ne occupa k & r.

## Per chi ne vale la pena

La vista si rivolge agli archivi con fondi epistolari — lasciti, raccolte di
corrispondenza erudita. È presente in ogni installazione, ma resta vuota finché
la descrizione non segue questa sistematica. Per un archivio senza lettere non
ha alcuna utilità.
