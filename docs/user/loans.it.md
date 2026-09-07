## Prestito di oggetti

### Prestare oggetti
Per vedere i prestiti presso l'oggetto e poter contrassegnare un oggetto come prestato, il campo prestito (id: 47) deve figurare nel formulario utilizzato.

Dopo aver fatto clic sul più è possibile registrare un prestito a un'utenza. Con il prestito questa viene collegata all'oggetto. Si registra inoltre il giorno del prestito. In un commento si possono annotare ulteriori indicazioni (scopo del prestito, data di restituzione prevista).

### Restituzione degli oggetti
Solo alla restituzione viene compilata la data finale. Il prestito è così concluso.

### Elenco dei prestiti aperti
Nell'area Admin esiste un elenco dei prestiti aperti (`/loans`), ossia dei prestiti privi di data di restituzione. Da lì si può passare sia alle utenze — per registrare ad esempio come restituiti i prestiti di una persona — sia agli oggetti prestati.

### Visualizzazione presso le singole utenze
Presso le singole utenze (`/users/{user_id}`) i prestiti sono visualizzati in una tabella.

### A quali livelli è possibile un prestito
L'impostazione `level_of_description_ids_for_loans` determina a quali livelli di
descrizione viene proposto il modulo di prestito. Ciò che si presta è un'unità
fisica, non un livello di ordinamento — senza questa restrizione era possibile
«prestare» anche un intero fondo o l'archivio stesso, il che contrassegnava come
prestate tutte le voci subordinate.

Un valore **vuoto** significa: tutti i livelli. È lo stato delle installazioni
esistenti e resta tale finché qualcuno non inserisce un valore. Le nuove
installazioni ricevono fascicolo e pezzo (`[5, 6]`). Chi presta regolarmente
interi fondi vi aggiunge il `3`.

Una scheda che porta già dei prestiti conserva il proprio modulo
indipendentemente da questa impostazione — nasconderlo non annullerebbe il
prestito, lo renderebbe soltanto irraggiungibile.

### Ruoli
I prestiti possono essere gestiti da `editor`, `admin` e `loan_admin`.

<!-- 
Attualmente non ancora possibile: impostare le scadenze di prestito; per farlo occorrerebbe probabilmente modificare il modello di dati dei prestiti.
-->
