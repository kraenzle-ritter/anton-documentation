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

### Ruoli
I prestiti possono essere gestiti da `editor`, `admin` e `loan_admin`.

<!-- 
Attualmente non ancora possibile: impostare le scadenze di prestito; per farlo occorrerebbe probabilmente modificare il modello di dati dei prestiti.
-->
