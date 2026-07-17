# Orte

Orte sind eigenständige Datensätze für geografische Angaben — Städte, Gewässer,
Gebäude, Regionen. Wie [Akteure](actors.md) werden sie einmal erfasst und dann
von beliebig vielen Verzeichnungseinheiten verwendet. Zu finden sind sie über
**Admin → Orte**.

Ein Ort hängt auf zwei Arten an einer Verzeichnungseinheit: als **Schlagwort**
(der Ort kommt inhaltlich vor) oder über ein [Ereignis](antonevents.md) (dort
wurde etwas hergestellt, empfangen, aufgeführt). Der Unterschied ist derselbe
wie bei den Akteuren.

## Typen

Die Typen folgen den Feature-Klassen von GeoNames: Staat/Land/Region, Gewässer,
Parks und Flächen, Stadt/Dorf, Strasse/Eisenbahnlinie, Gebäude/Hof, Berg/Hügel,
Unterwasser sowie Wald/Feld. Pro Archiv lassen sich weitere ergänzen.

## Erfassen

Das Formular enthält Typ, Name, andere Namensformen, Varianten, Abkürzungen,
Stadt/Gemeinde, Bundesland/Kanton, Land, Adresse, Beschreibung, Quellen,
Kommentar und die Koordinaten.

Orte lassen sich auch direkt aus dem Objektformular über das **+** neben der
Auswahlliste anlegen.

## Geokoordinaten

Besitzt ein Ort Koordinaten, zeigt die Detailansicht eine Karte. In der
Ortsliste lässt sich zudem über **Karte anzeigen** eine Übersichtskarte
einblenden; sie ist mit der Liste gekoppelt — wer die Karte verschiebt oder
zoomt, filtert die Liste auf den sichtbaren Ausschnitt.

### Über Normdaten — der einfachste Weg

Wird ein Ort in der Bearbeitungsansicht mit **GeoNames** oder **ortsnamen.ch**
[verknüpft](authorities.md), übernimmt Anton die Koordinaten automatisch.

### Von Hand

Im Feld **Koordinaten (lat lng)** eines **bereits gespeicherten** Ortes lassen
sich die Werte direkt eintragen.

!!! warning "Beim Anlegen noch nicht"
    Koordinaten, die im Formular für einen **neuen** Ort eingegeben werden,
    werden nicht gespeichert. Der Ort ist zuerst anzulegen und die Koordinaten
    anschliessend über **Bearbeiten** nachzutragen — oder gleich über GeoNames
    zu beziehen.

Anton erkennt das Format automatisch und rechnet in WGS84 um:

| Format | Beispiel |
|---|---|
| WGS84 (Dezimalgrad) | `47.3769 8.5417` |
| Schweizer Landeskoordinaten LV95 | `2683141 1247637` oder `2'683'141 1'247'637` |
| Schweizer Landeskoordinaten LV03 | `683141 247637` |

Vorzeichen, Tausendertrennzeichen (`'` oder Leerzeichen), Trennung durch
Leerzeichen oder Komma und Dezimalstellen sind jeweils optional.

Sind Koordinaten vorhanden, erscheint in der Bearbeitungsansicht zusätzlich eine
Taste zum Löschen.

## Dubletten zusammenführen

Zwei Datensätze für denselben Ort lassen sich zusammenführen. Dabei wandern
Ereignisse, Normdaten-Links und die Verknüpfungen zu Verzeichnungseinheiten auf
den Zieldatensatz, der alte wird gelöscht.

!!! danger "Vorbehalten und verlustbehaftet"
    Das Zusammenführen ist Superusern vorbehalten; bei Anton as a Service ist
    dafür k & r zuständig. Beschreibung, Quellen, Kommentar, Namensformen und die
    Koordinaten des aufgelösten Ortes werden **nicht** übernommen. Sie sind
    vorher zu sichern, falls sie erhalten bleiben sollen.
