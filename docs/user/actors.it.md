# Attori e attrici

Attori e attrici sono persone, famiglie e organizzazioni — schede autonome,
registrate una volta e poi utilizzate da un numero illimitato di unità di
descrizione. Si trovano in **Admin → Attori**.

## Due vie verso l'unità di descrizione

Attori e attrici possono essere collegati a un'unità di descrizione in due modi:

- **Come parola chiave** — nel campo «parole chiave (attori)». Ciò significa:
  questa persona *compare nel contenuto*. Senza ruolo, senza data.
- **Tramite un [evento](antonevents.md)** — con ruolo, luogo, data e commento.
  Ciò significa: questa persona *ha fatto qualcosa* — ha redatto il documento,
  inciso la stampa, versato il fondo.

Chi registra l'autore o l'autrice vuole l'evento. Chi annota che qualcuno è
menzionato nel testo vuole la parola chiave.

Nella pagina di dettaglio di un attore o di un'attrice i due usi compaiono
separati: «è coinvolto in» elenca gli eventi, «compare in» le unità di
descrizione in cui la persona figura come parola chiave.

## Tipi

Sono disponibili in modo fisso sei tipi: **persona**, **famiglia**, **ente**,
**divisione**, **gruppo** e **software**. Le etichette sono traducibili per
archivio, i tipi stessi non sono estendibili.

## Registrare

Per impostazione predefinita il formulario contiene tipo, nome, altre forme del
nome, varianti, abbreviazioni, le date di vita o di attività, descrizione, fonti
e commento. Quali campi compaiano dipende dal [set di formulari](forms.md).

Per le **date** è possibile spuntare «ca.» per ciascuna data e lasciare aperti
singolarmente giorno, mese o anno — sono quindi possibili datazioni incomplete.

Attori e attrici possono essere creati anche **direttamente dal formulario
dell'oggetto**: accanto all'elenco di selezione si trova un **+** che apre una
finestra con lo stesso formulario. Dopo la creazione la nuova voce risulta
selezionata — l'unità di descrizione stessa va ancora salvata.

Il collegamento con i [dati di autorità](authorities.md) come GND o Wikidata
avviene nella colonna di destra della vista di modifica.

## Attori e attrici bloccati

Il campo **bloccato** nasconde completamente un attore o un'attrice a chiunque
non sia autenticato internamente — negli elenchi, nella vista di dettaglio,
presso le unità di descrizione collegate e nella ricerca full text. È pensato
per le persone viventi e per i dati degni di protezione.

## Eliminare

Attori e attrici possono essere eliminati solo finché **non sono utilizzati**.
Anton rifiuta l'eliminazione in entrambi i casi seguenti e segnala quale
ricorre:

- la persona partecipa a un **evento**,
- oppure è registrata come **descrittore** presso un'unità di descrizione
  (vedi [Due vie verso l'unità di descrizione](#due-vie-verso-lunita-di-descrizione)).

Per eliminare un attore o un'attrice occorre prima ripulire i collegamenti — gli
eventi presso le unità di descrizione interessate, i descrittori nel registro
«viene utilizzato come descrittore» nella pagina di dettaglio.
