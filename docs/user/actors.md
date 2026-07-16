# Akteure

Akteure sind Personen, Familien und Organisationen — eigenständige Datensätze,
die einmal erfasst und dann von beliebig vielen Verzeichnungseinheiten
verwendet werden. Zu finden sind sie über **Admin → Akteurinnen/Akteure**.

## Zwei Wege zur Verzeichnungseinheit

Das ist der Punkt, an dem am häufigsten das Falsche gewählt wird. Ein Akteur
kann auf zwei Arten an einer Verzeichnungseinheit hängen:

- **Als Schlagwort** — im Feld «Schlagworte (Akteure)». Das sagt: Diese Person
  *kommt inhaltlich vor*. Ohne Rolle, ohne Datum.
- **Über ein [Ereignis](antonevents.md)** — mit Rolle, Ort, Datum und
  Kommentar. Das sagt: Diese Person *hat etwas getan* — sie hat das Dokument
  verfasst, den Stich gestochen, den Bestand abgeliefert.

Wer den Urheber erfasst, will das Ereignis. Wer festhält, dass jemand im Text
erwähnt wird, will das Schlagwort.

Auf der Detailseite eines Akteurs erscheinen beide Verwendungen getrennt: «ist
beteiligt an» listet die Ereignisse, «erscheint in» die Verzeichnungseinheiten,
in denen der Akteur Schlagwort ist.

## Typen

Sechs Typen stehen fest zur Verfügung: **Person**, **Familie**,
**Körperschaft**, **Abteilung**, **Gruppe** und **Software**. Die
Beschriftungen lassen sich pro Archiv übersetzen, die Typen selbst nicht
erweitern.

## Erfassen

Das Formular enthält im Standard Typ, Name, andere Namensformen, Varianten,
Abkürzungen, die Lebens- bzw. Wirkungsdaten, Beschreibung, Quellen und
Kommentar. Welche Felder erscheinen, hängt vom [Formularsatz](forms.md) ab.

Bei den **Daten** lässt sich je Datum «ca.» ankreuzen und Tag, Monat oder Jahr
einzeln offen lassen — unvollständige Datierungen sind also möglich.

Akteure lassen sich auch **direkt aus dem Objektformular** anlegen: Neben der
Auswahlliste steht ein **+**, das ein Fenster mit demselben Formular öffnet. Nach
dem Erstellen ist der Akteur ausgewählt — die Verzeichnungseinheit selbst muss
danach noch gespeichert werden.

Das Verknüpfen mit [Normdaten](authorities.md) wie GND oder Wikidata erfolgt in
der rechten Spalte der Bearbeitungsansicht.

## Gesperrte Akteure

Das Feld **Gesperrt** verbirgt einen Akteur vollständig vor allen, die nicht
intern angemeldet sind — in Listen, in der Detailansicht, bei den verknüpften
Verzeichnungseinheiten und in der Volltextsuche. Gedacht ist es für lebende
Personen und schützenswerte Angaben.

## Löschen

Ist ein Akteur an einem Ereignis beteiligt, verweigert Anton das Löschen und
meldet dies. Die Ereignisse sind zuerst zu bereinigen.
