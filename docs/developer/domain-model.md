# Domänenmodell

Die Domäne ändert sich langsam — sie ist der haltbarste Teil des Systems. Wer
sie kennt, liest den Code mit dem richtigen mentalen Modell.

## Die Entitäten

**AntonObject** — die Verzeichnungseinheit, der zentrale Datensatz. Sie steht in
der Tektonik und trägt Titel, Signatur, Datierung, Textfelder, Medien und
Verknüpfungen. Alles andere gruppiert sich um sie.

**Actor, Place, Keyword** — die Normdaten. Eigenständige Datensätze, die einmal
erfasst und von vielen Verzeichnungseinheiten verwendet werden. Sie sind
untereinander gleichrangig; es gibt keine Hierarchie und keinen Thesaurus.

**AntonEvent** — die Verknüpfung zwischen einer Akteur:in (oder einem Ort) und einer
Verzeichnungseinheit, **mit Rolle und Datum**. Das ist die wichtigste
Unterscheidung im ganzen Modell (siehe unten).

**Note** — ein polymorphes Textfeld. Hängt an AntonObject, aber auch an Actor,
Place, Keyword und Location. Pro Sprache ein Datensatz. In der Doku heissen
diese Felder «Textfelder».

**Media** — die digitalen Objekte, über `spatie/laravel-medialibrary` mit
Konversionen (`web`, `thumb`). Der Master bleibt unverändert.

## Die Hierarchie ist eine Closure Table

Die Tektonik lebt nicht in einer `parent_id`, sondern in einer
Closure Table (`franzose/closure-table`): einer Tabelle, die für **jedes**
Vorfahren-Nachkommen-Paar eine Zeile hält, samt Tiefe.

Die Konsequenzen prägen den Rest des Systems:

- **Teilbaum-Abfragen sind billig** — «alle Nachkommen von X» ist ein Join, kein
  rekursiver Durchlauf. Darauf beruhen Vererbung von Schutzfristen, Aggregation
  von Datierungen und Sichtbarkeitsregeln.
- **Umhängen ist teuer** — es schreibt viele Zeilen um. Deshalb läuft die Pflege
  der abgeleiteten Felder nach einem Verschieben asynchron; siehe
  [Nebenläufigkeit](events-jobs.md).
- **Denormalisierte Felder begleiten die Struktur** — `path`, `real_depth`,
  `has_children`, `fonds_id`. Sie sind materialisiert und müssen konsistent
  gehalten werden; das ist die Aufgabe der Job-Schicht.

Ein Bestand innerhalb eines Bestands ist nicht zulässig — die erlaubten
Stufenübergänge stehen in `config/constants.php`.

## Die eine Unterscheidung, die man verstehen muss

Akteur:innen können auf **zwei grundverschiedene Arten** an einer
Verzeichnungseinheit hängen — und die beiden werden ständig verwechselt, in der
Bedienung wie im Code:

| Als **Deskriptor** | Als **Ereignisbeteiligter** |
|---|---|
| Verschlagwortung: Akteur:innen *kommen vor* | Akteur:innen *haben etwas getan* |
| `actors_descriptors` (belongsToMany) | `AntonEvent.actor_id` |
| keine Rolle, kein Datum | Rolle = Ereignistyp, plus Ort und Datum |
| «Schlagwörter (Akteur:innen)» im Formular | «Entstehungszeitraum», «Stecher:in» … |

Dieselbe Trennung gilt für Orte. Wer die Urheber:in erfasst, will das Ereignis; wer
festhält, dass jemand erwähnt wird, den Deskriptor.

## Invarianten

Dinge, auf die man sich verlassen kann — und die man nicht verletzen sollte:

- **Signaturen sind nicht eindeutig.** Es gibt keinen Unique-Constraint; Dubletten
  sind erlaubt und werden nur als nicht-blockierende Warnung gemeldet.
- **Ereignistyp und Notiztyp sind Antonfields.** `antonevents.event_type_id` und
  `notes.note_type_id` verweisen auf `antonfields.id`. Die Enums `Eventtype` und
  `Notetype` bilden die im Code referenzierten Typen ab — nicht zwingend alle,
  die ein Mandant konfiguriert hat.
- **Normdaten tragen eine portable UUID** (seit v0.79) — Grundlage für den
  verlustfreien Re-Import, der gleichnamige Datensätze nicht verschmilzt.
- **Löschen kaskadiert.** Der `deleting`-Hook auf AntonObject verschiebt jedes
  Kind rekursiv; es gibt keinen Papierkorb (kein `deleted_at`).

## Standards

Anton bildet vier archivische Standards ab: **ISAD(G)** die
Verzeichnungseinheiten, **ISAAR(CPF)** die Akteur:innen, **ISDIAH** die Institution,
und **RiC-O / CIDOC CRM** die Ausgabe als Linked Data. Die drei erstgenannten
sind kein Mapping im Code, sondern Referenztexte in der In-App-Hilfe unter
«Standards».
