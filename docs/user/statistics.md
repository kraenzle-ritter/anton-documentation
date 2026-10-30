# Statistiken

Die Statistiken werten den Bestand und die Nutzung aus. Sie sind über die
Admin-Seite erreichbar.

!!! note "Nur für die Administration"
    Die Statistiken setzen die Rolle `admin` voraus. Mit der Rolle `editor` sind
    sie nicht zugänglich.

## Die Reiter

**Überblick** zählt, was das Archiv enthält: Datensätze, Bestände, Akteur:innen,
Orte, Schlagwörter, Medien und Benutzerkonten. Dazu kommen der belegte
Speicherplatz und das vereinbarte Kontingent — der Reiter beantwortet also auch
die Frage, wie voll das Archiv ist.

**Neue Objekte** zeigt den Zuwachs, aufgeschlüsselt pro Jahr und pro
Benutzerkonto.

**Ausleihen und Bestellungen** führt die [Bestellungen](cart.md) pro Jahr, die
[Ausleihen](loans.md) pro Jahr mit Gegenüberstellung von ausgeliehen und
zurückgegeben, sowie die Bestellungen pro Jahr und Bestand — mit Verweis auf den
jeweiligen Bestand. Das ist die einzige Auswertung der Bestellungen, die Anton
führt.

**Suche** zeigt die Suchabfragen: als Verlauf die Abfragen pro Monat über die letzten zwölf Monate und wie viele davon Treffer hatten; als Tabelle die letzten 30 Tage pro Suchart mit Zahl der Abfragen, Treffern und Erfolgsquote; und als Zusammenfassung alle gespeicherten Abfragen mit Gesamtzahl, Treffern und Erfolgsquote. Eine tiefe Erfolgsquote ist ein Hinweis darauf, dass Benutzende nicht finden, was sie suchen. Gezählt wird nur, solange die Einstellung `log_search_queries` eingeschaltet ist; sie ist es nicht von vornherein, weil die Tabelle ohne Frist wächst.

**Bestände** listet je Bestand Signatur, Titel, Anzahl Einträge, Umfang in
Laufmetern und Anzahl Medien.

**Akteur:innen**, **Orte** und **Schlagwörter** haben je einen eigenen Reiter mit
gleichem Aufbau: die Gesamtzahl, wie viele davon mit
[Normdaten](authorities.md) verknüpft sind, und die Verteilung auf die Provider
— GND, Wikidata und so fort. Diese drei Reiter zeigen also, wie weit der
Normdaten-Abgleich gediehen ist.
