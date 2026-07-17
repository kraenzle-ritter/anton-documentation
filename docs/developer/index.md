# Architektur — Überblick

Diese Sektion beschreibt Anton für Entwickelnde: nicht Klasse für Klasse — dafür
ist der Code die Quelle der Wahrheit —, sondern die **Form** des Systems, seine
Entscheidungen und die Invarianten, auf die man sich verlassen kann.

!!! note "Interne Konzeptpapiere"
    Vertiefte Design-Dokumente liegen im Anton-Repository unter
    `documentation/concepts/` (OCFL-Storage, RiC, Notes v2, TEI-Konfiguration,
    Typesense, SSO u.a.) und werden mit dem Code versioniert. Diese Seiten
    verweisen an den passenden Stellen dorthin; ohne Repository-Zugang sind sie
    nicht abrufbar.

## Der Stack in einem Satz

Anton ist eine **mandantenfähige Laravel-Anwendung** (Laravel 12, Livewire,
Alpine.js, Bootstrap) für die archivische Erschliessung nach **ISAD(G)**. Jedes
Archiv ist eine eigene Datenbank; derselbe Code bedient alle.

## Die tragenden Ideen

Fünf Entscheidungen prägen fast jede Stelle des Codes. Wer sie kennt, versteht,
warum Anton so gebaut ist, wie es ist.

**Ein Mandant ist eine Datenbank.** Kein Mandanten-Discriminator in den Tabellen,
sondern getrennte Datenbanken, ausgewählt über `--env={slug}` bzw. die Domain.
Das hält die einzelne Installation einfach und die Trennung hart.

**Die Hierarchie ist eine Closure Table.** Die Tektonik — Archiv, Bestand,
Serie, Dossier, Einzelstück — lebt nicht in einer `parent_id` allein, sondern in
einer materialisierten Vorfahren-Nachkommen-Tabelle. Das macht Teilbaum-Abfragen
billig und Umhängungen teuer; beides prägt das Nebenläufigkeitsmodell.

**Das Formular ist konfiguriert, nicht codiert.** Welche Felder eine
Verzeichnungseinheit hat, steht in Daten, nicht in Blade-Templates. Ein Archiv
gestaltet seine Masken selbst. Siehe [Das Formularsystem](forms.md).

**Abgeleitete Felder werden materialisiert und asynchron gepflegt.** Pfad,
Tiefe, Freigabejahr, Volltext, aggregierte Datierung — alles Werte, die aus
anderen Daten folgen, aber gespeichert und über die Queue neu berechnet werden.
Siehe [Nebenläufigkeit](events-jobs.md).

**Mandantenspezifisches dockt an, statt zu forken.** Eigene Signaturbildung,
eigene Exporter, eigene Konversionen — überall wird eine Klasse über eine
Einstellung benannt, nicht der Kern verändert. Siehe
[Erweiterungspunkte](extension-points.md).

## Die Subsysteme

| Subsystem | Wozu | Vertiefung |
|---|---|---|
| Domänenmodell | Verzeichnungseinheiten, Normdaten, Ereignisse, Medien | [Domänenmodell](domain-model.md) |
| Formular-Engine | Konfigurierbare Felder und Ansichten | [Formularsystem](forms.md) |
| Ereignis-/Job-Schicht | Konsistenz der abgeleiteten Felder | [Nebenläufigkeit](events-jobs.md) |
| Export-Schicht | EAD, RDF, TEI, DIP, OCFL, nativer Round-Trip | [Export-Matrix](../admin/export-matrix.md) |
| Medien-Pipeline | Upload, Formaterkennung, Konversionen, Cloud/DIMAG | [Langzeitarchivierung](../admin/preservation.md) |
| Suche | MySQL-Volltext und Typesense | [Schnelle Suche](../admin/typesense.md) |

## Arbeiten am Code

Setup, lokale Umgebung und Konventionen stehen im Anton-Repository selbst —
`DEVELOPMENT.md` (DDEV, Tests, Werkzeuge) und `CLAUDE.md` (Muster, Konventionen,
Verifikation). Diese öffentlichen Seiten wiederholen das bewusst nicht; sie
liefern das mentale Modell, das der Code allein nicht gibt.
