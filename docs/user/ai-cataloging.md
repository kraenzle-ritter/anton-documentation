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
