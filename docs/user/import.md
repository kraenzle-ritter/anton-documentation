## Zusammenfassung
Es ist möglich, Daten und dazugehörige Dateien (media) in Anton zu importieren. Die Erschliessungsdaten (Excel-File) werden in einem (vorgegeben) Excelsheet erfasst und mit den Dateien auf den Server geladen. Danach werden die Daten validiert und falls die Validierung erfolgreich war, kann der Import/Ingest erfolgen (Erschliessungsdaten und media). Vgl. auch die Dokumentation in Anton `/import/documentation`.

## Import-Hub `/import`

Seit **v0.62.0** sind alle Import-Pfade unter einer Adresse zusammengefasst: `/import` (im Menü unter **Import / Export → Import**). Die Seite hat vier Tabs:

| Tab | Inhalt |
|---|---|
| **Eingangskorb** (Standard) | Wartende agate-SIPs, die noch einen Parent-Bestand brauchen. Wenn etwas wartet, erscheint im Admin-Menü eine Zähler-Badge daneben. |
| **SIP** | Direkter SIP-Upload (BagIt-Pakete) mit Validation + Ingest. Siehe [SIP Ingest](../admin/sip-ingest.md) und [agate SIP](../admin/agate-sip.md). |
| **Excel** | Excel-Importe (das Hauptthema dieser Seite, siehe unten). |
| **Verzeichnis** | Import einer Verzeichnis-Struktur (ZIP/GZ) als Akzessionsarchiv-Eingang. |

Die alten URLs (`/sip/validation`, `/sip/ingest`, `/import/validation`, `/import/ingest`, `/sip/inbox`) leiten transparent auf den passenden Tab um — Lesezeichen und externe Links bleiben gültig.

### Detail-Ansicht im Eingangskorb

Pro wartendem SIP im Eingangskorb gibt es einen **Details**-Link. Dahinter steht eine Inspektions-Seite, die nur die `metadata.json` aus dem BagIt liest (kein Auspacken der Medien) und zeigt:

- BagIt-Validität (Manifest, Checksummen)
- Anzahl Datensätze im SIP
- NARA-Objekttyp-Kategorien — mit Hinweis, falls der Tenant für eine Kategorie keinen passenden Typ kennt
- Titel des obersten Datensatzes

So lässt sich vor dem Import sehen, ob das SIP sinnvoll ist, ob das Tenant-Vokabular passt, und das SIP gegebenenfalls verwerfen, bevor etwas in der Datenbank landet.

### Live-Fortschritt

Alle Imports laufen seit v0.62.0 **asynchron im Hintergrund**. Nach dem Klick auf "Importieren" landet man auf einer Fortschritts-Seite, die alle paar Sekunden den aktuellen Stand aktualisiert: Phase (Vorbereitung / Datensätze anlegen / Medien einlesen), erledigte Zeilen, am Ende ein Link zur entstandenen **Akzessions-Signatur** im Archiv.

Das gilt für alle Pfade — Excel, SIP, Verzeichnis und Eingangskorb-Finalisieren.

### Akzessions-Signatur für jeden Import

Jeder Import (egal über welchen Pfad) erzeugt einen Sidecar-Datensatz im Akzessionsarchiv (AKZ) mit der Nummer `AKZ {Jahr}/{N}`. Der Eintrag hält fest:

- Ursprünglicher Dateiname
- MD5-Prüfsumme
- Import-Zeitpunkt
- Import-Pfad (Excel / SIP / Verzeichnis / agate)
- die **verwendeten Einstellungen**, seit v0.87.0 (siehe unten)

Fehlgeschlagene Importe hinterlassen **keine Lücke** in der AKZ-Nummerierung — die Nummer wird erst beim erfolgreichen Abschluss vergeben.

### Import-Protokoll

Unter **`/import/audit`** steht die Liste aller Importläufe: Signatur, Quelldatei, Zeitpunkt, Zahl der erzeugten Datensätze und die verwendete Inhaltssprache. Seit **v0.87.0** ist das eine gewöhnliche Anton-Tabelle — sortierbar, mit einstellbarer Seitenlänge, und die Spalten lassen sich wie bei jeder anderen Liste unter *Admin → Formulare* anpassen.

Der **Details**-Link führt zum Akzessions-Datensatz. Dessen Ansicht zeigt seit v0.87.0 nur noch, was einen Import beschreibt — Quelldatei, Prüfsumme, verwendete Einstellungen samt Herkunft, die hochgeladene Datei als Medium, und wer den Lauf ausgelöst hat. Felder, die auf eine Import-Quittung nicht anwendbar sind (*Ausleihe*, *Verschoben*), erscheinen dort nicht mehr.

Die Einstellungen werden im Klartext festgehalten, eine Zeile je Einstellung mit Wert und Herkunft. Sie stehen dort dauerhaft — auch ein Jahr später ist damit nachvollziehbar, unter welchen Annahmen eine Lieferung hereingekommen ist.

## Ablauf (Excel-Import)
Zunächst ist ein Excel-File nach den folgenden Massgaben zu erstellen. Dieses ist unter "Upload Metadata" hochzuladen und dazugehörige Mediendateien sind unter "Upload Medien" hochzuladen. Abschliessend kann das Excel-File unter "Validation" überprüft werden. Die Validierung zeigt Fehler an und gibt Warnungen aus. Importieren kann man die Daten erst, wenn die Validierung fehlerfrei ist. Der Import wird unter "Ingest" ausgelöst und kann je nach Umfang einige Minuten dauern.

## Inhaltssprache des Imports

Übersetzbare Felder — Titel, Textfelder, neu angelegte Schlagworte, Akteur:innen, Orte und Standorte — brauchen eine Sprache. Seit **v0.87.0** ist das eine bewusste Entscheidung, die vor dem Lauf sichtbar ist.

!!! warning "Verhaltensänderung"
    Bis v0.86.x richtete sich Anton nach der **Sprache der Oberfläche**. Wer die Bedienoberfläche auf Englisch stehen hatte und eine Tabelle einspielte, legte für jeden Datensatz eine *englische* Titel-Übersetzung an — mit dem unveränderten deutschen Text darin. Der Datensatz sah auf Englisch richtig aus und hatte auf Deutsch keinen Titel mehr. Ab v0.87.0 spielt die Oberflächensprache keine Rolle mehr.

Die Inhaltssprache wird in dieser Reihenfolge bestimmt — der erste gesetzte Wert gewinnt:

1. die Wahl für diesen Lauf (`--locale` auf der Kommandozeile)
2. die Archiv-Einstellung `import_options.locale`
3. die erste Sprache aus `locales` — die Hauptsprache des Archivs

Die Inspektionsseite nennt vor dem Start die geltende Sprache **und woher sie stammt** («für diesen Lauf gewählt», «Archiv-Einstellung», «Vorgabe»). Nach dem Lauf steht dieselbe Angabe im Akzessions-Datensatz (siehe [Import-Protokoll](#import-protokoll)).

Eine Spalte mit Sprachkürzel (`title_fr`) sticht diese Wahl für ihr Feld aus — siehe [titel](#titel-title).

### Warum die Sprache auch beim Suchen zählt

Die Inhaltssprache bestimmt nicht nur, wohin geschrieben wird, sondern auch, **worin Anton nach bestehenden Akteur:innen und Orten sucht**. Wird eine Sprache gewählt, in der der Bestand nicht erfasst ist, findet der Abgleich nichts — und legt bei eingeschaltetem Anlegen für jeden Namen einen neuen Datensatz an.

Anton sucht deshalb in zwei Runden: zuerst in der Sprache des Laufs, dann in der Hauptsprache des Archivs. Ein Treffer aus der zweiten Runde wird im Protokoll vermerkt. Und die Vorschau (siehe unten) zeigt die Zahl der Neuanlagen, bevor etwas geschrieben wird — passt die Sprache nicht zum Bestand, sind dort auf einen Blick fast alle Akteur:innen «neu».

### Wo die Einstellungen stehen

Die Import-Einstellungen sind Sache des Archivs (`import_options`) und werden dort eingesehen, wo sie wirken: auf der Inspektionsseite der hochgeladenen Datei, jeweils mit dem **geltenden Wert**, dessen Herkunft und einer Erklärung. Angezeigt werden die Inhaltssprache und die Schalter, ob unbekannte Akteur:innen, Orte, Schlagworte, Standorte und Objekttypen neu angelegt werden.

Es gibt bewusst **keine** zweite Ablage im Benutzerprofil: ein Wert, den man nur beim Importieren braucht, gehört an eine Stelle — und diese Stelle nennt ihn samt Herkunft, statt bloss «Standard» zu sagen.

## Vorschau: was der Import neu anlegen würde

Die Inspektionsseite zeigt vor dem Start, wie viele **verschiedene** Normdaten-Einträge der Lauf neu anlegen würde: Akteur:innen, Orte, Schlagworte, Standorte, Objekttypen. Dazu die Namen selbst.

Die Zahl zählt verschiedene Einträge, nicht Zeilen: Eine unbekannte Akteurin, die in 500 Zeilen vorkommt, ist **eine** Neuanlage.

Die Namen sind wichtiger als die Zahl. Ein falsches Trennzeichen zeigt sich daran, dass «Muster, Hans; Beispiel, Anna» als *ein* Name in der Liste steht — in einer blossen Zahl wäre das unsichtbar.

Ist das Anlegen für eine Art ausgeschaltet, erscheinen dieselben Einträge als **nicht zuzuordnen**, mit dem Hinweis, dass diese Verknüpfungen im Lauf ersatzlos entfallen. Auch das ist ein Ergebnis, das man vorher kennen will.

Übersteigt die Zahl der Neuanlagen einer Art die Hälfte der Zeilen, erscheint eine **Warnung**. Das deutet häufiger auf ein Trennzeichen-, Sprach- oder Spaltenproblem hin als auf echten Zuwachs. Die Warnung blockiert nichts — der Lauf lässt sich starten.

!!! note "Die Vorschau schreibt nichts"
    Sie liest nur. Es entsteht kein Datensatz, auch keiner, der hinterher wieder entfernt werden müsste.

## Spalten
Das File darf zusätzliche Spalten enthalten; diese werden jedoch nicht importiert. Zur Vereinfachung dürfen Spalten gelöscht werden. Das endgültige File muss mindestens folgende Spalten enthalten:

    parent
    verzeichnungsstufe

## Erläuterung und Regeln für die einzelnen Spalten/Felder

### parent

Das Feld `parent` gibt an, wo der zu importierende Datensatz angehängt wird. Das Feld darf nicht leer sein. Es darf höchstens 100 Zeichen enthalten. Es muss eine Signatur enthalten, die es bereits in der Datenbank gibt.

Da es in Anton Verzeichnungseinheiten ohne Signatur geben kann (z.B. Klassen, Bestandsgruppen), ist es auch möglich den `parent` über die `id` anzugeben. Wenn im `parent` eine ganze Zahl (integer) steht, geht der Importer davon aus, dass die `parent_id` gemein ist. Die `id` einer Verzeichnungseinheit ist aus dem `permalink` ersichtlich.

### Verzeichnungsstufe (level_of_description)

Das Feld darf nicht leer sein. Es muss eine existierende Verzeichnungsstufe enthalten:

    Archiv
    Bestandsgruppe
    Bestand
    Klasse
    Serie
    Dossier
    Einzelstück

### signatur (identifier)

Das Feld darf höchstens 100 Zeichen enthalten. Jede Signatur darf nur einmal vorkommen. Ist keine Signatur angegeben, wird eine neue, eindeutige Signatur von Anton erzeugt.

### altsignatur (identifier_old)

Das Feld darf höchstens 100 Zeichen enthalten.

### titel (title)

Das Feld kann freien Text enthalten.

Der Titel ist ein **übersetzbares Feld**. In welche Sprache er geschrieben wird, entscheidet die [Inhaltssprache des Imports](#inhaltssprache-des-imports) — oder, genauer, die Spaltenbezeichnung selbst:

| Spalte | schreibt nach |
|---|---|
| `titel` bzw. `title` | die Inhaltssprache des Laufs |
| `title_de`, `title_fr`, `title_it`, `title_en` | genau die genannte Sprache |

Seit **v0.87.0** lassen sich also mehrsprachige Titel importieren: eine Spalte je Sprache. Beide Formen dürfen nebeneinander stehen; die Spalte mit Sprachkürzel ist die genauere Angabe und gewinnt, und die Inspektionsseite weist darauf hin.

Dasselbe gilt für die **Textfelder**: `scopecontent` schreibt in die Inhaltssprache, `scopecontent_fr` gezielt ins Französische, ohne die anderen Sprachen desselben Textfelds anzutasten.

!!! note "Nur konfigurierte Sprachen"
    Ein Sprachkürzel wird nur erkannt, wenn es in der Einstellung `locales` des Archivs steht (siehe [Sprachkonfiguration](languages.md)). `title_es` in einem Archiv ohne Spanisch ist keine Sprachangabe, sondern eine unbekannte Spalte — und die Inspektion meldet sie als solche.

### Antonevents
Antonevents verknüpfen die Verzeichnungseinheiten mit den Akteur:innen und den Orten. Sie bestehen aus folgenden Feldern: `actors, place, date_start, date_start_ca, date_end, date_end_ca, date_event_details`. Um ein Antonevent zu importieren muss nun der EventType in der Spaltenbezeichnung vor den Feldnamen gesetzt werden, z.B. für die Erstellung (Laufzeit):  `creation_actors, creation_place, creation_date_start, creation_date_start_ca, creation_date_end, creation_date_end_ca, creation_date_event_details`.

Es gibt zahlreiche Antonevents: `creation`, `acquisition`, `accumulation`, `destruction`, `validation`, `migration`, `reproduction`, `publication`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. 

#### Akteur:innen (z.B. creation_actors)

Das Feld darf höchstens 500 Zeichen enthalten. Die Angabe des Existenzzeitraums (Lebensdaten) in Klammern ist nicht obligatorisch, aber möglich. Runde Klammer dürfen aber nicht zu anderen Zwecken verwendet werden. Mehrere Akteur:innen sollten mit `::` getrennt werden.

Beispiel für zwei Akteur:innen: 

```
Müller, Martina (1934-1977) :: Rechtsabteilung
```

Das Format wird nicht vorab validiert! Akteur:innen werden neu angelegt, wenn sie in Anton nicht gefunden werden (gesucht wird nach dem Namen).

Import-Einstellung `create-actors`: Akteur:innen werden neu angelegt, wenn sie in Anton nicht gefunden werden.

Wenn eine Akteur:in bereits in Anton erfasst ist, kann sie auch über ihre ID (integer) referenziert werden.

Wurde eine Akteur:in mit einer GND oder einer anderen Ressource erfasst, kann sie auch anhand dieser Ressource erkannt werden, in dem die Angabe mit einem Prefix versehen wird (kleingeschrieben und mit Doppelpunkt ohne Leerzeichen): "gnd:118519522" (die Ressource muss innerhalb von Anton allerdings eindeutig sein). Gibt es die Akteur:in noch nicht, wird sie anhand der Angaben der GND neu angelegt.

#### Places
Das Feld kann einen Ort oder eine places-id (integer) enthalten. Import-Einstellung `create-places`: Orte werden neu angelegt, wenn sie in Anton nicht gefunden werden. Wenn ein Ort bereits in Anton erfasst ist, kann er auch über seine ID (integer) referenziert werden.

Orte können folgende Elemente enthalten:  
- Namen (wird durch "/" abgetrennt)  
- Stadt/Gemeinde  
- Kanton/Bundesland (wird in Klammern hinter der Gemeinde gesetzt)

### Spalten mit Wertelisten

Mehrere Spalten nehmen nur Werte an, die im Archiv definiert sind:
`verzeichnungsstufe`, `objekttyp`, `schutzfrist`, `status_of_description`,
`detail_of_description` und `vacat`.

Seit **v0.87.0** nehmen sie alle **drei Formen** an, gleichwertig (`vacat`
bereits seit v0.86.4):

| Form | Beispiel |
|---|---|
| Bezeichnung | `Bestand` |
| interner Name | `fonds` |
| ID | `3` |

Die ID ist die stabilste Form — sie übersteht ein Umbenennen. Wo eine
Bezeichnung zufällig wie eine Zahl aussieht, gewinnt die Bezeichnung.

!!! tip "Die erlaubten Werte stehen in der Fehlermeldung"
    Wird ein Wert nicht erkannt, nennt die Prüfung nicht nur das Problem,
    sondern auch die Lösung:

    > «Schachtel» steht nicht in der Werteliste. Erlaubt sind: Archiv
    > (collection), Bestandsgruppe (recordgroup), Bestand (fonds), Klasse
    > (class), Dossier (file), Einzelstück (item), Serie (series)

    Die Bezeichnung steht voran, der interne Name in Klammern. Man muss die
    Listen also nicht vorher nachschlagen.

#### Alle Wertelisten nachschlagen

Seit **v0.87.0** gibt es unter **Tabellen-Import → Wertelisten**
(`/valuelists`) eine Übersicht aller Wertelisten: pro Eintrag Bezeichnung,
interner Name und ID, dazu die Import-Spalte, zu der die Liste gehört. Ein
Suchfeld filtert über alle Listen gleichzeitig.

Die Seite ist rein lesend und steht allen offen, die importieren dürfen. Die
bearbeitbaren Listen unter *Admin → Wertelisten* verlangen dagegen das Recht,
eine Liste zu **ändern** — das haben ausserhalb der Systemverwaltung nur
wenige, und nur für zwei der siebzehn Listen. Wer bloss nachschlagen wollte,
stand vorher vor einer verschlossenen Tür.

Ebenfalls auf der Seite: die **Standort-IDs** für die Spalte `location_id`
der Update-Tabelle.

Schlagworte, Akteur:innen und Orte stehen dort *nicht* — das sind
Normdatensätze mit eigenen, durchsuchbaren Seiten, keine Listen zum
Durchlesen.

### objekttyp (object_type)

Das Feld muss einen bereits existierenden Objekttyp enthalten:

```
Akte
Bild
Band
Film
...
```

Die Liste der erlaubten Werte ist abhängig von den Objekttypen, die das jeweilige Archiv definiert hat.

### umfang_zahl (object_count)

Das Feld muss eine ganze Zahl (integer) enthalten. Die Angabe bezieht sich auf den Objekttyp.

### sprache (languages)

Das Feld kann mehrere Sprachen enthalten. Die Sprachen müssen entweder dem [ISO-639-2/B Sprachcode](https://de.wikipedia.org/wiki/Liste_der_ISO-639-Sprachcodes) entsprechen ("ger" nicht "deu", "fre" nicht "fra") oder exakt wie in der vorhandenen Liste geschrieben sein. Mehrere Sprachen werden können mit folgenden Zeichen getrennt (Komma und Strichpunkt sind nicht möglich):

```
    ::
```

### standort (location)

Das Feld muss einen bereits verwendeten Standort enthalten. Wenn ein neuer Standort verwendet werden soll, erst in Admin-Standorte hinzufügen.

Es gibt zwei Spalten, und der Name sagt jeweils, was hineingehört: **`location_id`** nimmt nur die ID, **`location`** (auch: `standort`) nimmt ID *oder* Bezeichnung. Sind beide vorhanden, gewinnt `location_id`.

### formularsatz (formset)

Bestimmt, welcher Formularsatz für den Datensatz verwendet wird — also welche Felder in welcher Reihenfolge erscheinen. Das Feld ist **optional**: bleibt es leer, löst Anton den Formularsatz über die Verzeichnungsstufe auf. Nötig ist es nur, wenn ein Datensatz bewusst davon abweicht, etwa der Formularsatz `letter` auf Einzelstücken.

Wie beim Standort zwei Spalten: **`formset`** (auch: `formularsatz`) nimmt den Namen *oder* die ID, **`formset_id`** nur die ID. Die Namen der verfügbaren Formularsätze stehen unter *Administration → Formularsätze* — in einer Standardinstallation etwa `fonds`, `class`, `series`, `file`, `item`, `collection`, `recordgroup`, `default`.

Die heruntergeladene Update-Tabelle führt die Spalte `formset` und schreibt den **Namen**. Eine leere Zelle lässt den Formularsatz unverändert.

!!! note "Vor v0.86 wurde die Spalte still verworfen"
    Frühere Versionen kannten `formset` nicht: die Spalte wurde als unbekannt gemeldet und danach folgenlos übergangen, der Lauf meldete Erfolg. Wer den Formularsatz per Tabelle gesetzt hat und sich wundert, warum nichts passiert ist — das war der Grund.

### vacat

Gibt an, ob die Verzeichnungseinheit ein Platzhalter ist (eine Lücke in der
Zählung, zu der es keine Unterlagen gibt).

Die Spalte führt intern Term-IDs. Angenommen werden die Bezeichnung
(`vacat`), die ID (`56` für vacat, `57` für nicht vacat) und — aus älteren
Tabellen — `1` und `0`.

**Exportiert** wird seit **v0.87.0** die Bezeichnung: `vacat` für einen
Platzhalter, sonst eine leere Zelle. Vorher stand dort die interne Nummer,
die in einer Spalte ohne `_id` im Namen nichts sagte und wie ein
versehentlich geänderter Wert aussah. Ältere Tabellen mit `56`/`57` lassen
sich unverändert weiterverwenden.

!!! warning "Vor v0.86.4"
    Bis dahin exportierte die Update-Tabelle die interne Nummer, die Prüfung
    liess aber nur `0` und `1` zu. Eine unveränderte Update-Tabelle war damit
    nicht einspielbar, und die Meldung nannte einen Wert, den niemand
    eingegeben hatte. Wer auf eine ältere Version stösst: die Spalte `vacat`
    im Download-Dialog abwählen.


### bilder (media)

Das Feld darf höchstens 500 Zeichen enthalten. Mehrere Dateinamen (assets) können mit folgenden Zeichen getrennt werden:

```
, ; ::
```


Beispiel:

```
erstes_bild.tif::zweites_bild.tif
```

### schutzfrist (period_of_protection)

Das Feld muss eine existierende Schutzfrist enthalten:

```
public
standard
prolonged
```

### private

Das Feld darf nur 0 (nein) oder 1 (ja) enthalten. Enthält private keinen Wert, wird 0 gesetzt.


### status_of_description

Das Feld darf nur Namen der entsprechenden Werteliste enthalten:

```
draft
final
```

### detail_of_description

Das Feld darf nur Namen der entsprechenden Werteliste enthalten::

```
minimal
partial
full
```

### Weitere Felder

Die weiteren Felder sind freie Textfelder::

    Neuzugänge (note.accruals)
    Bewertung und Kassation (note.appraisal)
    Informationen des Bearbeiters (note.archivists_notes)
    Ordnung und Klassifikation (note.arrangement)
    Verwaltungsgeschichte / Biographie (note.bioghist)
    Zugangsbedingungen (note.condition_of_access)
    Reproduktionsbestimmungen (note.condition_of_reproduction)
    Bestandsgeschichte (note.custod_hist)
    Kommentar zur Datierung (note.date_comment)
    Umfang (Beschreibung) (note.extent_text)
    Findmittel (note.finding_aids)
    Allgemeine Anmerkungen (note.general_note)
    Archivinterne Bemerkungen (note.internal_note)
    Sprache/Schrift (note.language_script)
    Standort (Detail) (note.location_details)
    Physische Beschaffenheit und technische Anforderungen (note.physical_description)
    Provenienz (note.provenance)
    Publikationen (note.publications)
    Verwandte Verzeichnungseinheiten (note.related_units)
    Kopien/Reproduktionen (note.reproductions)
    Verzeichnungsgrundsätze (note.rules_note)
    Form und Inhalt (note.scopecontent)

## Bestehende Datensätze aktualisieren (Update über den Browser)

!!! warning "Experimentelles Feature"
    Das Datenupdate ist als **experimentell** gekennzeichnet (Badge im Reiter und auf der Upload-Seite). Es verändert bestehende Datensätze direkt. Anton legt deshalb **vor jedem Update automatisch eine Sicherung der Datenbank** an (siehe unten); das Ergebnis trotzdem stichprobenweise prüfen.

Neben dem Neuanlegen können bestehende Verzeichnungseinheiten auch direkt über den Browser aktualisiert werden. Dafür gibt es unter **Tabellen-Import** seit **v0.81.2** einen eigenen Reiter **«Update»** (nach *Metadaten* und *Medien*). Dort die Tabelle hochladen — Update-Dateien haben eine eigene Liste, getrennt vom normalen Import — und mit **«Details»** öffnen. Die Datei wird direkt im Update-Modus geprüft, und es erscheint der Button **«Als Update einspielen»**.

Weil der *Update*-Reiter die Datei ausschliesslich als Update prüft, braucht eine reine Update-Tabelle (nur `id` + zu ändernde Spalten, ohne `parent`) keine Umwege: die beim Neuanlegen nötige `parent`-Spalte wird hier nicht verlangt. Der reguläre *Metadaten*-Reiter bleibt unverändert fürs Neuanlegen.

Ein Update überschreibt die Felder der bestehenden Datensätze «an Ort und Stelle» — es werden dabei **keine neuen Datensätze angelegt**. Damit ein Update sicher und vorhersehbar bleibt, gelten drei Voraussetzungen. Ist eine davon verletzt, wird die Datei blockiert und der Grund auf der Inspektionsseite angezeigt:

1. **Jede Zeile braucht eine numerische `id`.** Über diese `id` wird der zu aktualisierende Datensatz gefunden. Die `id` einer Verzeichnungseinheit ist aus dem `permalink` ersichtlich.
2. **Keine `parent`- (oder `parent_id`-) Spalte.** Ein Update darf Datensätze nicht verschieben. Um die Hierarchie zu ändern, die Datensätze regulär in Anton umhängen.
3. **Keine Ereignis-Spalten (Antonevents).** Spalten wie `creation_actors`, `creation_date_start` usw. sind im Update nicht erlaubt, damit keine doppelten Ereignisse entstehen. Akteur:innen-/Orts-Verknüpfungen in Anton pflegen.

Was ein Update schreibt:

- **Nur befüllte Felder werden überschrieben.** Leere Zellen lassen den bestehenden Wert unangetastet — es ist also möglich, gezielt nur einzelne Spalten (z.B. nur `titel` oder nur `schutzfrist`) zu aktualisieren.
- **Schlagworte, Akteur:innen, Orte, Sprachen und Textfelder werden ersetzt.** Eine befüllte Zelle ist die *vollständige neue Liste*: Wer einen Eintrag aus der Zelle löscht, löst damit auch die Verknüpfung am Datensatz. Eine leere Zelle ändert nichts. (Beim normalen Import — also beim Neuanlegen — werden Schlagworte weiterhin nur ergänzt.)
- **Medien** werden weiterhin ergänzt.

Dieselbe Datei darf mehrfach als Update eingespielt werden; die sonst geltende Duplikat-Sperre (gleiche Datei = gleiche MD5-Prüfsumme) greift für Updates nicht, da ein Update wiederholbar ist.

Nach dem Start zeigt die Fortschritts-Seite das Update als **«Datenupdate»** an (nicht als Import) und meldet am Schluss, wie viele Datensätze *aktualisiert* wurden.

**Automatische Sicherung.** Bevor ein Update auch nur eine Zeile schreibt, legt Anton einen Dump der Datenbank an (dieselbe Sicherung wie `anton:backup`, abgelegt unter `db_backup/`). Der Schritt erscheint in der Fortschritts-Anzeige als Phase *backup* und wird als eigener Eintrag protokolliert, der den Dateinamen des Dumps nennt. Lässt sich die Sicherung nicht anlegen, **bricht das Update ab** und es wird nichts geändert. Die Sicherung wird auch dann erzwungen, wenn für den Mandanten sonst `no-backup` gesetzt ist — diese Option ist für schnelle Massen-*Neuanlagen* gedacht, wo ein Rückweg trivial ist.

Jeder Update-Lauf wird — wie ein Import — im Akzessionsarchiv protokolliert, aber mit einer **eigenen Signatur-Serie `UPDATE-{jjjj}-{NNN}`** statt `IMPORT-{jjjj}-{NNN}` bzw. `AKZ {jjjj}/{N}`. Ein Update ist keine Akzession — es kommt nichts Neues ins Archiv —, und die eigene Serie macht in der Akzessionsliste auf einen Blick sichtbar, welche Einträge Updates sind. Der Zähler läuft unabhängig von der Import-Serie und wird pro Kalenderjahr zurückgesetzt.

### Passende Tabelle herunterladen

Damit ein Update nicht von Hand zusammengestellt werden muss, lässt sich die aktuelle **Trefferliste direkt als Update-Tabelle herunterladen**: in der Objektliste rechts oben das Excel-Symbol neben der Druckansicht. Der Download übernimmt genau die Filter, die gerade angezeigt werden.

Die Datei enthält ausschliesslich Spalten, die ein Update auch schreiben darf — `id`, die Feld-Spalten, Sprachen, den Standort (`location_id`), Schlagworte/Akteur:innen/Orte (als IDs) und die Textfeld-Spalten `note.*`. Bewusst **nicht** enthalten sind `parent` und die Ereignis-Spalten, die würden das Update blockieren. Die Spalte `identifier` dient nur der Orientierung: das Update findet die Datensätze über die `id`, Änderungen an der Signatur bleiben wirkungslos.

!!! tip "Mehrsprachige Archive: eine Titel-Spalte je Sprache"
    Führt das Archiv mehrere Inhaltssprachen, enthält die Update-Tabelle seit **v0.87.0** statt `titel` je eine Spalte `title_de`, `title_fr` usw. Nur so ist der Weg hinaus und wieder hinein verlustfrei: Mit einer einzigen Titel-Spalte müsste beim Einspielen die Sprache des Laufs entscheiden, wohin der Wert zurückgeht — und ein französischer Titel landete im deutschen Feld.

    Einsprachige Archive behalten die gewohnte Spalte `titel`; dort gibt es nichts zu unterscheiden. Ältere Tabellen mit `titel` bleiben in jedem Fall einspielbar.

!!! tip "Standorte ändern"
    Für den Standort gibt es **zwei Spalten**, und der Name sagt jeweils, was hineingehört:

    | Spalte | Inhalt |
    |---|---|
    | `location_id` | **nur die ID** des Standorts (steht unter *Admin → Standorte*) |
    | `location` | ID **oder** Bezeichnung |

    Die heruntergeladene Update-Tabelle nutzt `location_id`. Wer lieber mit Bezeichnungen arbeitet, benennt die Spalte in `location` um; dort werden beide Formen akzeptiert. Eine Bezeichnung muss exakt so geschrieben sein wie in der Standort-Verwaltung, inklusive Gross- und Kleinschreibung — die ID ist deshalb der sichere Weg.

    Eine **leere Zelle lässt den Standort unverändert** — zum Umräumen also nur die Zeilen ändern, die wirklich umziehen. Ein Standort, den es noch nicht gibt, muss vorher unter *Admin → Standorte* angelegt werden; sonst meldet die Inspektion ihn als unbekannt und das Update läuft nicht.

!!! warning "Vor v0.87.0 lud der Knopf nichts herunter"
    Der Herunterladen-Knopf im Spaltendialog schloss den Dialog, brach aber im
    selben Zug die Übertragung ab — ohne Fehlermeldung. Es sah aus, als sei
    etwas passiert; im Download-Ordner kam nichts an. v0.86.4 behob einen Teil
    davon, der Knopf blieb aber wirkungslos; erst seit v0.87.0 ist es ein
    echter Download.

Beim Klick öffnet sich ein Dialog, in dem sich die **Spalten auswählen** lassen. Das ist mehr als Bequemlichkeit: Was nicht in der Datei steht, kann ein Update auch nicht schreiben. Wer nur einen einzelnen Titel korrigieren will, wählt `id` und `titel` — dann kann beim Einspielen nichts anderes zu Schaden kommen. `id` ist immer enthalten und nicht abwählbar.

!!! warning "Die Tabelle ist eine Momentaufnahme"
    Zwischen Download und Update sollte möglichst wenig Zeit liegen. Die Datei enthält den Stand vom Zeitpunkt des Downloads. Wird sie erst Tage später eingespielt, überschreiben ihre alten Werte alles, was in der Zwischenzeit an diesen Datensätzen geändert wurde — auch Änderungen, die andere Personen bewusst vorgenommen haben und die erhalten bleiben sollen. Eine heruntergeladene Tabelle nicht aufbewahren und später wiederverwenden, sondern für jede Korrekturrunde neu exportieren. Je weniger Spalten gewählt sind, desto kleiner ist das Risiko.

    **Anton prüft das mit.** Beim Export wird der Zeitpunkt in die Datei geschrieben (in die Dokument-Eigenschaften, nicht in eine Spalte — er übersteht auch das Umbenennen). Die Inspektionsseite vergleicht ihn mit dem Änderungsdatum der betroffenen Datensätze und meldet konkret, welche seither bearbeitet wurden: *«3 Datensätze wurden seit dem Export der Tabelle (20.07.2026 08:30) bearbeitet — das Update würde diese Änderungen überschreiben: SIG-1, SIG-7, …»*. Das blockiert das Update nicht; es kann gute Gründe geben, trotzdem einzuspielen. Lässt sich kein Zeitpunkt ermitteln (etwa bei einer von Hand erstellten Tabelle), sagt die Seite auch das — ein fehlender Hinweis bedeutet also nie automatisch «alles in Ordnung».

Der Knopf ist Administrator:innen vorbehalten und lässt sich im eigenen Profil unter *Einstellungen* ausblenden. Daneben steht der **vollständige Excel-Export** (alle Felder inklusive `parent` und Ereignis-Spalten) — der ist für Auswertungen gedacht und lässt sich *nicht* als Update wieder einspielen.

### Warum Ereignisse im Update nicht mitgehen

Ereignis-Spalten (`creation_actors`, `creation_date_start`, `acquisition_place` …) sind im Update **gesperrt**. Der Grund liegt in der Struktur: In Anton ist ein Ereignis ein Tupel aus *Akteur:in, Ort, Zeitraum und Typ* — eine Zeile pro Akteur:in. Eine Tabelle kann davon pro Objekt und Ereignistyp nur **eine Kombination** abbilden: einen Ort, einen Zeitraum, einen Detailtext, geteilt von beliebig vielen Akteur:innen.

Daraus folgen drei Dinge, die eine Tabelle nicht leisten kann:

- **Mehrere Ereignisse desselben Typs.** Wurde ein Objekt 1920 in Zürich *und* 1925 in Bern bearbeitet, lässt sich das in einem Spaltensatz nicht ausdrücken. Im vollständigen Excel-Export werden die Spalten dieses Typs deshalb weggelassen. **Eine leere Ereignis-Zelle bedeutet also zweierlei:** entweder ist kein Ereignis erfasst — oder es sind mehr, als diese Tabellenform tragen kann. Der Download-Dialog weist darauf hin. Die Update-Tabelle enthält gar keine Ereignis-Spalten und ist davon nicht betroffen.
- **Ereignisse löschen.** Der Import legt Ereignisse nur an oder aktualisiert sie; es gibt keinen Weg, eines über die Tabelle zu entfernen.
- **Ein Datum verschieben.** Der Abgleich läuft über *Typ + Objekt + Akteur:in + Beginndatum*. Wird das Datum in der Tabelle geändert, entsteht ein **zweites** Ereignis, das bestehende bleibt stehen.

Gerade die letzten beiden Punkte machen Ereignisse in einem Update unbrauchbar: es liesse sich nur ergänzen, nie korrigieren — und wiederholtes Einspielen würde Ereignisse vermehren. Ereignisse werden darum in Anton selbst gepflegt, nicht über die Tabelle.

Nicht abgebildet sind ausserdem das Freitext-Datierungsfeld (`datierung_text`, in keiner Richtung) und die Ortsadresse (`<typ>_place_address`, nur beim Import und nur wenn die Einstellung `import_addresses` gesetzt ist).

!!! note "Nur über die interne `id`"
    Das Update im Browser findet die Datensätze immer über die interne `id`, nie über die Signatur. Ein Update über die Signatur ist nur über die Kommandozeile möglich (`--update --default-excel-column=identifier`, siehe unten).

## Import über die Kommandozeile


### Einfacher Import

Für den Customer (slug) "besenval" und das Excelfile "test.xlsx" lautet der Import Befehl:

```bash
php artisan anton:import --env=besenval --file="test.xlsx" --import
```

Dabei wird davon ausgegangen, dass `test.xlsx` im Ordner `customers/besenval/metadata_to_import/` liegt. Mit zu importierende Dateien (Medien) müssen sich im Ordner `customers/besenval/assets_to_import/` befinden.

Ohne die Option `--import` wird das file nur validiert.

### Optionen

Der Befehl `anton:import` bietet einige Optionen, die für spezifische Situationen nützlich sein können.

| Option|Beschreibung|
|:---   | :----------|
|--no-backup | dont backup the database before import |
|--import                  |really start import|
|--locale=                 |Inhaltssprache des Laufs (z.B. `de`, `fr`). Ohne Angabe gilt die Archiv-Einstellung, sonst die Hauptsprache des Archivs — siehe [Inhaltssprache des Imports](#inhaltssprache-des-imports)|
|--update                  |bestehende Datensätze aktualisieren statt neu anlegen; Match standardmässig über die `id`|
|--default-excel-column=   |`id` (Standard) oder `identifier` — bestimmt beim `--update`, worüber die Datensätze gefunden werden|
|--dont-validate           |do not validate the file|
|--skip-parent-validation  |to build hierarchies with one excel file|
|--create-actors           |create new actors if they dont exist|
|--create-keywords         |create new keywords if they dont exist|
|--create-places           |create new places if they dont exist|
|--create-locations        |create new locations if they dont exist|
|--create-object-types     |create new object_type terms if they dont exist|
|--show-rules              |show rules for this file|
|--show-columns            |show the original columns of this file|
|--show-column-mapping     |show columns with mapping|
|--show-possible-columns   |show all possible column names|
|--show-mapping            |show mapping for this file|
|--show-separators         |show separators|
|--from-ead                |import file is a xml-ead file (also use --parent and --dont-validate)|
|--parent=                  |if import file is an ead you need a parent|

Beispiel
```bash
php artisan anton:import customers/kr/ead/test_2-ead.xml --from-ead --dont-validate --create-actors --create-places --create-keywords --parent=1 --env=kr -vv --import --no-backup
```
