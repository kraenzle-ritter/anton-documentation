# Schlagwörter

Schlagwörter erschliessen Verzeichnungseinheiten inhaltlich — für Sachen,
Ereignisse, Techniken, Werke. Personen und Organisationen gehören dagegen zu
den [Akteur:innen](actors.md), geografische Angaben zu den [Orten](places.md).

Zu finden sind sie über **Admin → Schlagwörter**; verknüpft werden sie im
Objektformular im Feld **Schlagwörter (Sachen)**.

!!! note "Hierarchie nur auf Wunsch"
    Ohne weiteres stehen Schlagwörter nebeneinander, der **Typ** gruppiert sie lediglich. Ober- und Unterbegriffe und «siehe auch» lassen sich pro Archiv einschalten, siehe [Ober- und Unterbegriffe](#ober-und-unterbegriffe).

## Typen

Die Typen sind pro Archiv frei bestimmbar und weichen zwischen den Archiven
stark ab. Verbreitet sind Ereignis, Objekt, Masseinheit/Währung,
Sammlung/Kunstwerk, Verfahren/Prozess/Technik, Buch/Manuskript/Publikation und
anderes/diverses; Archive mit besonderen Beständen führen deutlich mehr — etwa
für Rohstoffe und Geologie, Bauwerke, Flora und Fauna oder Militärtechnik.
Massgeblich ist die Werteliste des eigenen Archivs, einsehbar unter
**Hilfe → Wertelisten**.

## Erfassen

Das Formular enthält Typ, Label, andere Namensformen, Varianten, Abkürzungen,
Beschreibung, Quellen und Kommentar.

Ob das Label **mehrsprachig** erfasst werden kann, hängt an der Einstellung
`translate_keywords`. Ist sie ausgeschaltet, gibt es nur ein Eingabefeld in der
Hauptsprache des Archivs.

Anton erkennt bestehende Schlagwörter am normalisierten Label und verwendet sie
wieder, statt Dubletten anzulegen.

Schlagwörter lassen sich auch **direkt aus dem Objektformular** anlegen: Neben
der Auswahlliste im Feld **Schlagwörter** steht ein **+**, das ein Fenster mit
demselben Anlege-Formular öffnet. Nach dem Erstellen ist das neue Schlagwort
ausgewählt — die Verzeichnungseinheit selbst muss danach noch gespeichert
werden.

## Ober- und Unterbegriffe

Ist die Einstellung `keyword_relations` unter **Admin → Einstellungen** eingeschaltet, führt jedes Schlagwort **Oberbegriffe**, **Unterbegriffe** und **Siehe auch**. Ausgeschaltet, die Vorgabe, bleibt alles wie bisher.

Im Formular des Schlagworts sucht man die Begriffe in drei Feldern wie im Objektformular aus. Ein Unterbegriff lässt sich vom Ober- wie vom Unterbegriff aus eintragen; Anton speichert die Beziehung einmal und zeigt sie auf beiden Seiten.

Ein Schlagwort darf **mehrere Oberbegriffe** haben. Einer davon ist die **Hauptstelle**: Unter ihr steht das Schlagwort im **Pfad**, der auf der Detailseite oben erscheint, etwa «Schrift › Brief». Der erste Oberbegriff wird zur Hauptstelle; hat ein Schlagwort mehrere, wählt man sie im Formular unter **Hauptstelle**.

Anton lässt keinen Kreis zu: Ein Schlagwort kann nicht unter einem seiner eigenen Unterbegriffe stehen und nicht mit sich selbst verknüpft werden. Das Formular kommt dann mit einer Meldung zurück und speichert nichts.

Der Knopf **Begriffsbaum** auf der Liste der Schlagwörter und neben dem Pfad eines Schlagworts zeigt die Ober- und Unterbegriffe als Baum. Er lädt nach, wie der Archivplan, und öffnet von einem Schlagwort aus den Weg zu ihm. Ein Schlagwort mit mehreren Oberbegriffen lässt sich nur unter seiner Hauptstelle aufklappen; unter den übrigen steht ein Verweis, etwa «Brief (siehe Schrift)».

Wird ein Schlagwort gelöscht, verschwinden seine Beziehungen mit. Werden zwei Schlagwörter zusammengeführt, übernimmt das bleibende die Beziehungen des anderen.

## Normdaten

Schlagwörter lassen sich wie Akteur:innen und Orte mit [Normdaten](authorities.md)
verknüpfen — etwa mit Wikidata oder der GND.

!!! warning "Nicht in jedem Archiv verfügbar"
    Die Normdaten-Spalte erscheint beim Schlagwort nur, wenn für das Archiv
    Provider konfiguriert sind. Fehlt die Einstellung, gibt es beim Schlagwort
    keine Verknüpfungsmöglichkeit — bei Akteur:innen und Orten dagegen schon.

## Als Thesaurus herunterladen

Sind Ober- und Unterbegriffe eingeschaltet, finden angemeldete Mitarbeitende auf der Liste der Schlagwörter den Knopf **SKOS herunterladen** und auf jedem Schlagwort **Teilbaum als SKOS**. Die Datei enthält alle Schlagwörter oder das Schlagwort mit allem darunter, als Turtle, RDF/XML oder N-Triples: Bezeichnungen in allen Sprachen, weitere Namen, Ober- und Unterbegriffe, «siehe auch» und die verknüpften Normdaten. Jedes Schlagwort steht unter seiner bleibenden Adresse. Welche Daten genau hinausgehen, zeigt die [Export-Matrix](../admin/export-matrix.md).

## Begriffsschemata und Thesaurus-Import

Unter **Admin → Begriffsschemata** führt das Archiv seine Thesauri: solche, die es einspielt (etwa einen Fachthesaurus im Format SKOS), und solche, die es selbst pflegt. Ein Schlagwort kann zu mehreren Schemata gehören und trägt in jedem die URI und die Notation des Begriffs. Auf der Detailseite steht beides unter **Begriffsschema**.

Eingespielt wird eine SKOS-Datei (Turtle, RDF/XML oder N-Triples) oder eine Tabelle (XLSX, CSV) mit den Spalten **Begriff**, **Oberbegriffe**, **Benutzt für**, **Verwende**, **Siehe auch**, **Notation** und **Definition**. Mehrere Begriffe in einer Zelle trennt man mit «;». Der Import läuft im Hintergrund; das Ergebnis steht danach auf derselben Seite.

- **Kein Doppel:** Gibt es ein Schlagwort mit derselben Bezeichnung schon, knüpft der Import daran an. Es behält seine Bezeichnung und bekommt nur die fehlenden Sprachen dazu. Tragen mehrere Schlagwörter denselben Namen, legt der Import ein neues an und meldet den Namen.
- **Ein zweiter Import** derselben Datei führt nach, statt zu verdoppeln.
- **Übernommen werden** weitere Namen, Definitionen, Ober- und Unterbegriffe, «siehe auch» und Normdaten-Links (Wikidata, GND, VIAF, Library of Congress, GeoNames). Nichts, was das Archiv geschrieben hat, wird überschrieben.
- **Nicht-Vorzugsbegriffe** einer Tabelle («Verwende …») werden zu weiteren Namen des Begriffs. Ein Kombinationsverweis («Verwende A, B») wird bei beiden eingetragen und im Ergebnis aufgeführt.
- **Kreise** lässt der Import weg und meldet sie.
- **Stillgelegte Begriffe** eines Thesaurus legt der Import nicht an. Ihre Namen kommen zum Begriff, der sie ersetzt, damit die Suche nach dem alten Namen weiterhin trifft.

Ein Schema lässt sich als SKOS herunterladen. Wird es entfernt, bleiben die Schlagwörter mit ihren Beziehungen und Verknüpfungen; nur die Zugehörigkeit zum Schema geht. Dasselbe leistet auf der Kommandozeile `anton:import-skos`.

## Wo ein Schlagwort verwendet wird

Die Detailseite zeigt unter «erscheint in» alle Verzeichnungseinheiten, die das
Schlagwort führen.

Hat das Schlagwort Unterbegriffe, nimmt der Schalter **Mit Unterbegriffen** deren Verzeichnungseinheiten in die Liste auf. Derselbe Schalter steht in der Suche neben den gewählten Filtern, sobald nach einem Schlagwort gefiltert wird.

## Löschen

Ein Schlagwort lässt sich nur löschen, solange es **bei keiner
Verzeichnungseinheit** eingetragen ist. Andernfalls verweigert Anton das Löschen
und meldet den Grund. Welche Einheiten betroffen sind, zeigt «erscheint in» auf
der Detailseite; dort sind die Zuordnungen zuerst zu entfernen.
