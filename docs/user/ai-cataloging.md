# KI-Erschliessung

Anton kann Vorschläge für die Erschliessung von einem Sprachmodell erzeugen
lassen: Es liest die angehängten Medien und schlägt Titel, Textfelder,
Ereignisse, Schlagwörter, Akteur:innen, Orte und Sprachen vor.

!!! note "Erst freizuschalten"
    Die KI-Erschliessung ist zurzeit nicht standardmässig in Betrieb. Sie setzt
    zweierlei voraus: eine Freigabe in der Serverkonfiguration, die im
    Admin-Bereich nicht erreichbar ist — bei Anton as a Service setzt sie k & r —
    und den Schalter im Archiv selbst. Zusätzlich muss ein Kostenrahmen
    hinterlegt sein; fehlt er, brechen alle Anfragen ab.

## Vorschläge erzeugen

In der Bearbeitungsmaske steht der Block **KI-Erschliessung**; die gleichnamige
Taste oben springt dorthin. Ein Klick auf **KI-Vorschläge generieren** schickt
die Anfrage; danach erscheinen die Vorschläge als Chips neben den betroffenen
Feldern, je mit **Übernehmen**, **Anhängen** und **Ignorieren**.

Nichts wird dabei automatisch in die Datenbank geschrieben — die Vorschläge
landen im Formular, gespeichert wird erst mit der normalen Speichern-Taste. Das
Erzeugen setzt die Rolle `editor` voraus.

Je Konto gelten Grenzen: höchstens 30 Vorschläge pro Stunde und höchstens ein Viertel des Monatsbudgets pro Tag. Die Werte legt der Betrieb je Archiv fest. Tonaufnahmen und der Ton von Videos werden im Hintergrund transkribiert; solange das läuft, kommt der Vorschlag ohne sie, mit einem Hinweis. Später erneut anfragen, dann ist die Transkription dabei.

## Für alles unterhalb einer Verzeichnungseinheit

Für eine Ablieferung mit vielen Einzelstücken gibt es den **KI-Lauf**: In der Detailansicht einer Verzeichnungseinheit führt die Taste **KI-Lauf** zu einer Seite, auf der man Profil, Umfang (nur Datensätze mit Medien oder alle) und die Obergrenze an Aufrufen wählt. Darunter steht, was der Lauf voraussichtlich kostet, nach Verbrauch verrechnet, und was vom Monatsbudget und vom eigenen Tagesanteil noch übrig ist. Das Starten setzt die Rolle `editor` voraus.

Der Lauf arbeitet im Hintergrund Datensatz für Datensatz, mit denselben Regeln wie die Taste im Formular: Interne Notizen gehen nicht an den Anbieter, von gesperrten Datensätzen keine Angaben. Er hält an, wenn die Obergrenze oder das Budget erreicht ist, und lässt sich abbrechen; **Fortsetzen** macht beim nächsten Datensatz weiter.

Beim Umfang «nur Datensätze mit Medien» überspringt der Lauf Datensätze, von denen keine Datei an die KI gehen kann, etwa Word-Dateien oder Dateien, die fehlen; sie kosten nichts und stehen auf der Seite als «übersprungen». Ist der Anbieter überlastet, fragt der Lauf denselben Datensatz nach einer Pause bis zu dreimal noch einmal an.

In die Datensätze schreibt der Lauf nichts. Titel, Textfelder (etwa «Form und Inhalt»), Datierung, Sprachen, Schlagwörter, Akteur:innen und Orte landen als Vorschläge in der Prüfliste (Daten-Import › Prüfliste für Vorschläge) mit der Quelle «KI-Erschliessung»; dort lassen sie sich nach Quelle und Bestand filtern und einzeln oder gesammelt bestätigen. Ist ein Eintrag schon in Anton vorhanden, ist er vorausgewählt. Platzhalter wie «Unbekannt» oder «Nicht angegeben» schlägt der Lauf nicht vor, und eine Datierung nur, wo der Datensatz für dieses Ereignis noch keine hat. «ß» schreibt er als «ss»; das lässt sich je Archiv mit der Einstellung `ai_swiss_spelling` abschalten.

Bei Titel, Textfeld und Datierung steht neben dem Vorschlag, was der Datensatz bisher enthält. Ist das Feld leer, übernimmt Bestätigen den Vorschlag. Steht schon etwas darin, muss man in der Zeile wählen: **Bisherigen Wert ersetzen** oder, bei einem Textfeld, **An bisherigen Text anhängen**. Ohne diese Wahl bleibt der bisherige Wert stehen, auch beim gesammelten Bestätigen.

## Was Anton von sich aus übernimmt — und was nicht

Die Voreinstellungen sind bewusst ungleich:

| Vorschlag | Voreinstellung |
|---|---|
| Akteur:in, Ort, Schlagwort — **bereits vorhanden** | wird verknüpft |
| Akteur:in, Ort, Schlagwort — **neu anzulegen** | wird verworfen |
| **Titel und Textfelder** | werden verworfen |

Das heisst: **Die KI ändert den Titel nie von selbst.** Wer einen Vorschlag
will, muss ihn ausdrücklich übernehmen. Und neue Normdatensätze entstehen nicht
nebenbei — die Hürde für neue Akteur:innen und Schlagwörter bleibt bewusst hoch.

Vorgeschlagene Ereignisse legt Anton als **Entstehungszeitraum** an. Ist es ein
anderer Ereignistyp, ist er nach dem Übernehmen von Hand zu korrigieren.

## Datenschutz

Anton kennzeichnet jedes KI-Profil danach, wo es die Daten verarbeitet: 🇨🇭 für
in der Schweiz gehostete Modelle, ⚠️ für alle anderen. Bei einem
nicht-schweizerischen Profil erscheint eine rote Warnung:

> **⚠️ Achtung — Datenschutz**
> Dieses Profil verarbeitet Daten ausserhalb der Schweiz und ist NICHT
> FADP/GDPR-konform. Verwende es ausschliesslich für Daten, die du auch
> öffentlich publizieren würdest.

Voreingestellt ist ein schweizerisches Profil. Ein anderes zu wählen, ist ein
bewusster Einzelfallentscheid: Die Auswahl ist zugeklappt, gilt nur für die
laufende Anfrage und wird nicht gemerkt.

!!! danger "Vor dem Absenden prüfen"
    Mit der Anfrage verlassen die Inhalte der Verzeichnungseinheit — Medien
    eingeschlossen — das Archiv. Bei gesperrten Beständen, Personendaten und
    allem, was einer Schutzfrist unterliegt, ist das mit einem
    nicht-schweizerischen Profil nicht zulässig.

Jede Anfrage wird protokolliert; Verbrauch, Kosten und ein Audit-Trail stehen
unter **Admin → KI-Erschliessung**.
