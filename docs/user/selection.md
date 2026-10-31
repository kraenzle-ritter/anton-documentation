# Auswahl und Sammelaktionen

Mehrere Verzeichnungseinheiten lassen sich in Trefferlisten ankreuzen und gemeinsam bearbeiten. Dafür gibt es zwei Aktionen: das [Verschieben](hierarchy.md), ab der Rolle `admin`, und die [Sammelbearbeitung](#sammelbearbeitung), ab der Rolle `editor`.

!!! note "Nur in einzelnen Archiven"
    Sammelaktionen müssen freigeschaltet sein. Sie sind kein Standard; die Einstellung ist im Admin-Bereich nicht änderbar, bei Anton as a Service ist dafür k & r zuständig. Wer sie nicht braucht, kann sie im eigenen [Profil](profile.md) zusätzlich abschalten.

## Zuerst die Aktion, dann die Auswahl

Die Reihenfolge ist umgekehrt zum Gewohnten und die häufigste Stolperstelle:

1. **Zuerst** die Aktion im Auswahlfeld **Aktionen** wählen: **Verschieben** oder **Bearbeiten**. Vorher lässt sich nichts ankreuzen; die Kästchen bleiben wirkungslos.
2. **Dann** die Einheiten ankreuzen. Über das Symbol mit der Klemmbrett-Liste über der Trefferliste — es zeigt die Anzahl der gewählten Einheiten — lässt sich die aktuelle Auswahl jederzeit einsehen.
3. Die Aktion ausführen. Mit **Leeren** wird die Auswahl verworfen.

!!! warning "Aktion wechseln leert die Auswahl"
    Wird das Auswahlfeld nachträglich geändert, wird die bisherige Auswahl verworfen. Die Aktion ist also vor dem Ankreuzen festzulegen.

## Was sich zusammen auswählen lässt

Zum **Verschieben** nur Einheiten, die **Geschwister sein könnten**. Sobald ein Dossier angekreuzt ist, lässt sich kein Bestand mehr dazunehmen — Anton verhindert Auswahlen, die sich nicht gemeinsam verschieben liessen. Wer eine Einheit nicht ankreuzen kann, sollte deshalb die bereits gewählten Stufen prüfen. Zum **Bearbeiten** lassen sich beliebige Einheiten zusammen wählen.

Ist bereits ein Verschiebevorgang im Gang, ist die Auswahl gesperrt, bis er abgeschlossen oder abgebrochen ist.

## Sammelbearbeitung {#sammelbearbeitung}

Mit der Aktion **Bearbeiten** führt der Knopf **Bearbeiten (Anzahl)** in der Auswahl auf die Seite **Sammelbearbeitung**. Dort gilt eine Änderung für alle gewählten Einheiten, höchstens 500 auf einmal.

| Änderung | Was sie tut |
|---|---|
| **Werteliste setzen** | Standort, Objekttyp, Status oder Detaillierungsgrad der Beschreibung auf einen Wert setzen oder leeren; wahlweise **nur wo leer** |
| **Textfeld setzen** | ein Textfeld in einer Sprache **ersetzen**, **nur wo leer** füllen oder einen Text **anhängen** (als neuen Absatz) |
| **Schlagwort** | ein bestehendes Schlagwort **hinzufügen** oder **entfernen** |
| **Suchen und ersetzen** | einen Text im Titel (alle Sprachen) oder in einem Textfeld (alle Sprachen) ersetzen; wahlweise Gross- und Kleinschreibung beachten und nur ganze Wörter |

Angeboten werden nur die Felder, die in den Bearbeitungsformularen des Archivs vorkommen. Gesucht wird wörtlich, ohne Platzhalter oder reguläre Ausdrücke. Signatur, Verzeichnungsstufe und Schutzfrist lassen sich nicht gesammelt ändern: die Signatur nicht, weil gleiche Signaturen kollidieren, Stufe und Schutzfrist nicht, weil sie über die Stellung im Baum und den Zugang auch der untergeordneten Einheiten entscheiden.

So läuft eine Sammelbearbeitung ab:

1. **Vorschau**: Anton zeigt, wie viele Einheiten sich ändern, und die ersten 20 Änderungen mit vorher und nachher. Die Vorschau schreibt nichts.
2. **Ausführen**: erst nach einer Vorschau zu genau diesen Einstellungen. Wer danach etwas ändert, braucht eine neue Vorschau.
3. Der Lauf geschieht im Hintergrund. Zuerst zieht Anton eine **Sicherung der Datenbank**; gelingt sie nicht, wird nichts geändert. Dann wird Einheit für Einheit geändert.
4. Unter **Letzte Läufe** steht der Stand: wartet, läuft, fertig oder fehlgeschlagen, die Zahl der geänderten Einheiten, Fehler und der Name der Sicherung.

Jede Änderung steht wie eine Bearbeitung in der Maske im Änderungsverlauf der Einheit und im [Bestandsprotokoll](../admin/protokolle.md), mit dem Namen der Person, die den Lauf gestartet hat. Rückgängig machen lässt sich ein Lauf über die Sicherung; dafür ist die Administration zuständig.

## Nicht dasselbe wie der Bestellkorb

Auswahl und [Bestellkorb](cart.md) sehen ähnlich aus und sind doch zwei getrennte Listen, die einander nie beeinflussen. Die Auswahl dient dem Bearbeiten, der Bestellkorb dem Bestellen. Eine Auswahl lässt sich nicht in den Bestellkorb übernehmen.
