# Nebenläufigkeit: Events, Listener, Jobs

Eine Verzeichnungseinheit trägt Felder, die aus anderen Daten **folgen**: ihren
Pfad in der Tektonik, ihre Tiefe, das Freigabejahr, den Volltextindex, die über
den Teilbaum aggregierte Datierung. Diese Werte sind **materialisiert** — sie
stehen in Spalten, statt bei jeder Abfrage neu gerechnet zu werden.

Materialisierung erkauft schnelle Abfragen mit dem Zwang, die Werte konsistent
zu halten. Genau das leistet die Ereignis- und Job-Schicht. Wer sie versteht,
versteht, warum eine scheinbar einfache Änderung an einem Objekt eine Kette von
Hintergrundaufträgen auslöst.

## Das Muster

Anton koppelt Domänenoperationen und Nachpflege lose über Laravel-Events:

```
Operation am AntonObject  →  Domain-Event  →  Listener  →  Job (Queue)
```

Der Kern liegt in den Model-Hooks von `AntonObject` (`booted()`) und in
`EventServiceProvider`. Die Nachpflege läuft über die Queue, weil sie ganze
Teilbäume berühren kann — bei einer Closure Table ist das potenziell teuer.

## Warum asynchron und idempotent

Zwei Entwurfsentscheidungen erklären fast alles:

**Teilbaum-Arbeit gehört in die Queue.** Ein Verschieben schreibt Pfade und
Tiefen aller Nachkommen um; eine Titeländerung kann den Volltext des ganzen
Teilbaums betreffen. Solche Arbeit synchron im Request zu erledigen, würde ihn
sprengen — deshalb Jobs mit grosszügigen Timeouts und Retries.

**Die Jobs sind wiederholbar.** Jeder rechnet den Zielzustand aus den
Quelldaten neu, statt Deltas fortzuschreiben. Das macht sie idempotent: Ein
zweiter Lauf schadet nicht, ein verlorener Lauf lässt sich nachholen. Genau
darauf beruht die Reparaturfähigkeit — `anton:doctor` und
`RepairAllDerivedAttributes` können jederzeit den konsistenten Zustand
wiederherstellen.

## Domain-Events werden bei Massenoperationen unterdrückt

Ein wichtiges Detail: Beim Anlegen vieler Datensätze (`create_bulk`) und während
eines Verschiebens setzt der Code `$suppressDomainEvents = true` und stösst die
Nachpflege **einmal am Ende** an, statt pro Objekt. Sonst würde eine
Bulk-Operation Hunderte redundanter Jobs erzeugen. Wer eine neue Massenoperation
schreibt, muss dieses Muster kennen und selbst dafür sorgen, dass Pfade, Daten
und Volltext danach einmal aktualisiert werden.

## Die abgeleiteten Felder

| Feld | Wird neu berechnet bei | Job |
|---|---|---|
| `path`, `real_depth` | Anlegen, Verschieben | `UpdatePaths` |
| aggregierte Datierung | Datumsänderung im Teilbaum | `UpdateDates` |
| `full_text`, `full_text_intern` | Titel-/Inhaltsänderung, neuen Medien | `RefreshFulltext` |
| `release_year_calculated` | Schutzfrist-/Datumsänderung | über die Nachkommen-Pflege |
| `private`, `status_of_description_id` | Änderung auf einem Vorfahren | Vererbung an alle Nachkommen |

`RefreshFulltext` illustriert eine allgemeine Vorsichtsregel der Schicht: Bei
wenigen IDs läuft es in-process, bei vielen oder der ganzen Datenbank in einem
**eigenen PHP-Prozess** — zur Speicher-Isolation, damit ein grosser Rebuild den
Worker nicht sprengt.

## Voraussetzung: der Supervisor läuft

Die ganze Schicht setzt voraus, dass die Queue abgearbeitet wird. Steht der
Supervisor nicht, stauen sich die Jobs ohne Fehlermeldung, und die abgeleiteten
Felder veralten still. Der Reiter **Supervisor** im
[Anton Doctor](../admin/doctor.md) zeigt den Zustand — die erste Station bei
«Änderungen kommen nicht an».

## Kein Scheduler auf den Servern

Der Laravel-Scheduler (`schedule:run`) läuft auf den Produktionsservern nicht
(vgl. den Kommentar in `app/Console/Kernel.php`). Wiederkehrende Aufgaben —
Integritätsprüfungen, Disk-Messung, Normdaten-Abgleich — werden deshalb pro
Installation als Cronjob eingerichtet, nicht über den Scheduler. Wer eine
periodische Aufgabe braucht, plant sie als Cron ein.
