# Schlagwörter

Schlagwörter erschliessen Verzeichnungseinheiten inhaltlich — für Sachen,
Ereignisse, Techniken, Werke. Personen und Organisationen gehören dagegen zu
den [Akteur:innen](actors.md), geografische Angaben zu den [Orten](places.md).

Zu finden sind sie über **Admin → Schlagwörter**; verknüpft werden sie im
Objektformular im Feld **Schlagwörter (Sachen)**.

!!! note "Keine Hierarchie"
    Schlagwörter stehen nebeneinander. Anton führt keinen Thesaurus: Es gibt
    keine Ober- und Unterbegriffe und keine Verweisungen zwischen
    Schlagwörtern. Der **Typ** gruppiert sie lediglich.

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

## Normdaten

Schlagwörter lassen sich wie Akteur:innen und Orte mit [Normdaten](authorities.md)
verknüpfen — etwa mit Wikidata oder der GND.

!!! warning "Nicht in jedem Archiv verfügbar"
    Die Normdaten-Spalte erscheint beim Schlagwort nur, wenn für das Archiv
    Provider konfiguriert sind. Fehlt die Einstellung, gibt es beim Schlagwort
    keine Verknüpfungsmöglichkeit — bei Akteur:innen und Orten dagegen schon.

## Wo ein Schlagwort verwendet wird

Die Detailseite zeigt unter «erscheint in» alle Verzeichnungseinheiten, die das
Schlagwort führen.
