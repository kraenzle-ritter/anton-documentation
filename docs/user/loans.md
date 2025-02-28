## Ausleihe von Objekten

### Objekte ausleihen
Um Ausleihen beim Objekt sehen und ein Objekt als geliehen markieren zu können, muss das Feld Ausleihe (id: 47) im verwendeten Formular sein. 

Nach dem Klick auf das Plus kann eine Ausleihe an einen User eingetragen werden. Bei der Ausleihe wird dieser mit dem Objekt verknüpft. Dazu lässt wird der Tag der Ausleihe eingetragen. In einem Kommentar können weitere Angaben festgehalten werden (Zweck der Ausleihe, voraussichtliches Rückgabedatum). 

### Rückgabe von Objekten
Erst bei der Rückgabe wird das Bis-Datum ausgefüllt. Damit ist die Ausleihe abgeschlossen.

### Liste Offener Ausleihen
Im Admin Bereich gibt es eine Liste der offenen Ausleihen (`/loans`), also der Ausleihen die kein Rückgabedatum besitzen. Von dort kann einerseits auf die User gesprungen werden, um etwa Ausleihen eines Users als zurückgegeben einzutragen oder auf die ausgeliehenen Objekte. 

### Anzeige bei den einzelnen Usern
Bei den einzelnen Usern (`/users/{user_id}`) werden die Ausleihen in einer Tabelle angezeigt.

### Rollen
Ausleihen können von `editor`, `admin` und `loan_admin` verwaltet werden.

<!-- 
Zurzeit noch nicht möglich: Leihfristen setzen; dafür müsste wohl das Datemodell für die Ausleihen geändert werden.
-->
