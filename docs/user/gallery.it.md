# Galleria dei media

La galleria dei media mostra le immagini di un archivio come griglia di
riquadri — un accesso visivo accanto alla [ricerca](search.md). Si trova sotto
`/gallery`.

!!! note "Non collegata ovunque"
    Anton non inserisce da sé la galleria nella navigazione. Se compaia nel menu
    lo decide ogni archivio; altrimenti è raggiungibile soltanto tramite
    l'indirizzo.

## Due varianti

| Variante | Filtro |
|---|---|
| Galleria classica | Una riga di filtri sopra la griglia; quali campi contenga è configurabile per archivio |
| Galleria V2 | Una barra laterale con faccette e **numero di risultati** per fondo, parola chiave e tipo di media, oltre a un intervallo di anni |

La V2 presuppone un motore di ricerca Typesense e viene introdotta
gradualmente; quale variante usi un archivio è un'impostazione. I riquadri e la
vista ingrandita sono identici in entrambe.

## Che cosa compare nella galleria

Un'immagine compare solo se sono soddisfatte **tutte** le condizioni:

- Non è contrassegnata come «non mostrare nella galleria». Questo contrassegno
  vale per **tutti**, anche per chi è autenticato e si occupa della descrizione.
- Non è contrassegnata come media bloccato.
- Per le persone esterne inoltre: l'unità di descrizione non è bloccata, il suo
  stato non è «bozza» e il [termine di protezione](access.md) è scaduto.

L'utenza autenticata internamente vede quindi più del pubblico — il contrassegno
«non mostrare nella galleria» prevale però su qualsiasi ruolo.

È inoltre possibile limitare per archivio quali fondi la galleria mostri —
separatamente per l'uso interno e per quello pubblico.

## Togliere immagini dalla galleria

Il contrassegno si imposta nella gestione dei media in **Admin → Media**. È la
via giusta per le immagini che sono sì descritte, ma non adatte alla vetrina —
retri, esposizioni sbagliate, riprese tecniche.

Per le immagini che non possono essere mostrate per ragioni giuridiche, lo
strumento corretto è invece il [termine di protezione](access.md) o il blocco
del media: il contrassegno della galleria è una decisione di visualizzazione,
non una restrizione di accesso.
