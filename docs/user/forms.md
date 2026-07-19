# Formulare und Felder

Anton gibt kein festes Feldschema vor. Welche Felder eine Verzeichnungseinheit
hat, in welcher Reihenfolge sie stehen und wie sie heissen, legt jedes Archiv
selbst fest. Das erklärt, warum die Masken von Archiv zu Archiv verschieden
aussehen — und warum die Beispiele in dieser Dokumentation von der eigenen
Installation abweichen können.

## Formularsätze

Ein **Formularsatz** bündelt fünf Formulare für dieselbe Sache:

| Formular | Wofür |
|---|---|
| Intern — Bearbeiten | Die Erschliessungsmaske |
| Intern — Detail | Die Detailansicht für angemeldete Benutzer:innen |
| Intern — Liste | Die Trefferliste für angemeldete Benutzer:innen |
| Extern — Detail | Die Detailansicht für die Öffentlichkeit |
| Extern — Liste | Die Trefferliste für die Öffentlichkeit |

Die Trennung intern/extern ist der Grund, weshalb Aussenstehende weniger sehen
als das Archiv selbst: Ein Feld erscheint nur, wenn es im jeweiligen Formular
steht. Ein Bearbeiten-Formular für die Öffentlichkeit gibt es nicht.

Formularsätze existieren nicht nur für Verzeichnungseinheiten, sondern auch für
[Akteur:innen](actors.md), [Orte](places.md), [Schlagwörter](keywords.md) und
Standorte.

## Welcher Formularsatz gilt?

Anton entscheidet in dieser Reihenfolge:

1. Ist im Datensatz das Feld **Formularsatz** ausgefüllt, gilt dieser.
2. Sonst gilt der Formularsatz, der gleich heisst wie die
   [Verzeichnungsstufe](hierarchy.md) — für ein Dossier also «file».
3. Sonst gilt der Standardsatz.

Das Feld **Formularsatz** steht zuoberst in der Erschliessungsmaske und bleibt
in der Regel leer. Es ist der Ausweg für Sonderfälle: Wenn ein Bestand
Fotografien enthält, die andere Felder brauchen als der Rest, lässt sich für sie
ein eigener Formularsatz anlegen und gezielt zuweisen.

## Felder

Ein Feld erscheint nur, wenn es im Formular steht **und** einen Wert hat — leere
Felder werden in der Detailansicht ausgeblendet, nicht als leere Zeile gezeigt.
In der Bearbeitungsmaske sind sie dagegen immer sichtbar.

Dasselbe Feld verhält sich je nach Ansicht anders: Was beim Bearbeiten ein
Eingabefeld oder eine Auswahlliste ist, erscheint in der Detailansicht als
reiner Text.

Grau hinterlegte **Abschnitte** gliedern die Maske. Sie sind selbst keine
Felder; ein Abschnitt ohne sichtbare Felder wird ganz weggelassen.

## Hilfetexte zu Feldern

Zu einem Feld kann ein Hilfetext hinterlegt sein — die archiveigene
Erschliessungsregel für dieses Feld. Ist er hinterlegt, erscheint er in der
Bearbeitungsmaske als kleiner Hinweis direkt unter dem Eingabefeld.

Diese Inline-Anzeige lässt sich pro Person im eigenen Profil ein- und
ausschalten; im Standard ist sie **aus**. Unabhängig davon sind alle Hilfetexte
gesammelt auf der Hilfeseite **Anton Fields** in der Anwendung einsehbar.

## Ändern

Formularsätze und Formulare werden unter **Admin → Formulare** bzw.
**Admin → Formtypen** gepflegt. Dort lassen sich Felder hinzufügen, entfernen,
umsortieren und pro Formular umbenennen — die Beschriftung eines Feldes kann
also in der Bearbeitungsmaske anders lauten als in der Detailansicht. Welche
Felder überhaupt zur Verfügung stehen, zeigt die Hilfeseite **Anton Fields** in
der Anwendung.
