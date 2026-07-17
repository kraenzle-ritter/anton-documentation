# Anton Doctor

Der Anton Doctor prüft eine Installation auf Konsistenz und meldet, was nicht
stimmt. Er ist das erste Werkzeug, wenn sich Anton merkwürdig verhält —
Datensätze am falschen Ort, fehlende Vorschaubilder, ein hängender Import.

Erreichbar über die Admin-Seite; die Rolle `admin` genügt. Die Reiter sind
nicht übersetzt und erscheinen englisch.

!!! important "Der Doctor prüft Metadaten, nicht Dateien"
    Er prüft die Datenbank und ob Dateien **vorhanden** sind — er vergleicht
    **keine Prüfsummen**. Ob eine Datei unverändert ist, beantwortet
    [`media:check --levels=4`](console-commands.md#mediacheck); siehe
    [Langzeitarchivierung](preservation.md#integritat-prufen).

## Die Reiter

**Overview** fasst zusammen und ist der Einstieg.

**Supervisor** zeigt, ob die Hintergrundverarbeitung läuft und wie viele
Aufträge in der Warteschlange stehen. Fehlgeschlagene Aufträge lassen sich hier
einzeln oder gesammelt erneut anstossen. Das ist der erste Blick, wenn Uploads
nicht verarbeitet werden oder Konversionen ausbleiben: Steht der Supervisor,
staut sich alles.

**Derived Fields** betrifft die abgeleiteten Felder — Pfad, Tiefe, «hat
Kinder», Freigabejahr, Entstehungsdaten, Volltext und die Tektonik. Sie werden
aus anderen Daten errechnet und können nach Import oder Massenänderung
veralten. Der Reiter zeigt das Ergebnis des **letzten** Laufs aus dem
Zwischenspeicher; die Neuberechnung ist ausdrücklich anzustossen.

**Data Integrity** prüft beim Aufruf: Bestände innerhalb von Beständen,
Positionskollisionen unter Geschwistern, doppelte Signaturen.

**Environment** prüft Umgebungsvariablen, Einstellungen und ob die
Kundenverzeichnisse les- und schreibbar sind.

**Binaries** prüft, ob die externen Programme vorhanden sind, auf die Anton
angewiesen ist — ImageMagick, Ghostscript, ffmpeg und weitere. Fehlt eines,
schlagen die zugehörigen Konversionen still fehl. Bei fehlender
Formaterkennung lohnt hier der erste Blick.

**Disk** zeigt die Plattenbelegung.

## Auf der Kommandozeile

Dieselben Prüfungen laufen über [`anton:doctor`](console-commands.md#antondoctor),
etwa in einem wiederkehrenden Auftrag. Die Tektonik lässt sich damit auch
**reparieren** — die Prüfung meldet, der Reparaturlauf greift ein:

```bash
php artisan anton:doctor --closure --env=<slug>
php artisan anton:doctor --closure --repair --env=<slug>
```

!!! warning "Vor dem Reparieren sichern"
    Ein Reparaturlauf schreibt in die Datenbank. Vorher eine
    [Sicherung](restore.md) anlegen.

## Kein Automatismus

Anton führt die Prüfungen **nicht** von sich aus aus; einen eingebauten
Zeitplan gibt es nicht. Wo sie wiederkehrend laufen sollen, werden sie pro
Installation als Cronjob eingerichtet.
