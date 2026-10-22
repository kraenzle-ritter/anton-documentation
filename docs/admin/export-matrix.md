# Export-Matrix

Übersicht, welche Anton-Daten über welches Export-Format ausgegeben werden — und
welche sich nur über den vollständigen SQL-Dump rekonstruieren lassen.

Wozu welches Artefakt taugt, ordnet [Langzeitarchivierung: Überblick](preservation.md)
ein. Die Kurzfassung: **Nativer Round-Trip und SQL-Dump sind Sicherungen, alles
andere sind Publikations- und Austauschsichten.**

!!! info "Stand"
    Diese Matrix bildet den Stand vom **22. Oktober 2026** ab. Sie wird
    zusammen mit den Exportern gepflegt.

## Verfügbare Formate

| Format | Standard | Umfang | Einstieg |
|---|---|---|---|
| EAD 2002 | apeEAD (`ead.xsd` + `apeEAD.xsd`) | Objekt-Baum ab Bestand | Admin → Export |
| EAD3 | `ead3.rng` | Objekt-Baum ab Bestand | Admin → Export |
| EAD Holding Guide | apeEAD `type=holdings_guide` | Bestandsübersicht | Admin → Export |
| TEI – Normdaten-Listen | TEI-P5 `standOff` | Akteur:innen / Orte / Schlagwörter (gesamt) | `/api/tei/{actors,places,keywords}` |
| TEI – pro Objekt | TEI-P5 | ein Datensatz | API mit `?format=tei` |
| RDF «A+» | CIDOC CRM + RiC-O (dual) | Objekt-Baum, alle Entitäten | Admin → Export, `anton:export-rdf` |
| RDF RiC | reines RiC-O 1.1 (JSON-LD) | Objekt-Baum | Admin → Export |
| RDF Memobase | RiC-O-Subset (JSON-LD) | Objekt-Baum (verlustbehaftet) | Admin → Export |
| RDF «A+» Bundle | CIDOC CRM + RiC-O **+ Mediendateien** als ZIP | Objekt-Baum, offline anzeigbar ohne Anton; mit `--include-protected --include-originals` ein **Migrationspaket** (siehe unten) | Admin → Export, `anton:export-rdf --profile=a-plus-bundle` |
| **Nativer Round-Trip** | `anton-import-format` v0.5 (JSON) **+ Master-Medien** als ZIP | Objekt-Baum, **verlustfrei re-importierbar** | `anton:export-native` / `anton:import-native` |
| Dublin Core | OAI-DC | pro Objekt (nur eingebettet) | Baustein in DIP / OCFL |
| DIP | BagIt | Paket: Medien + Metadaten (Teilbaum) | Taste «DIP» am Datensatz |
| E-ARK DIP | E-ARK DIP 2.2.0 (CSIP) | Paket ab Datensatz samt Teilbaum: *Zugang* = öffentliche Sicht mit Nutzungskopien, *vollständig* = alles mit Mastern und Originalen | Taste «E-ARK DIP» am Datensatz (Zugang), `anton:export-dip --format=eark [--full]` |
| OCFL | Oxford Common File Layout | Paket: Medien + Metadaten (Objekt/Teilbaum) | Taste am Datensatz |
| Excel (voll) | XLSX | aktuelle Trefferliste, alle Felder | Trefferliste → Export |
| Excel (Update-Tabelle) | XLSX | Trefferliste, **nur beschreibbare Felder**, wieder einspielbar | Trefferliste → Export → Update |
| Word / PDF | DOCX / PDF | Findbuch pro Objekt | Taste am Datensatz |
| Paper | HTML-Druckansicht | Trefferliste (max. 1000) | Trefferliste |
| **SQL-Dump** | mysqldump (gzip) | **ganze Mandanten-Datenbank** — ohne Sitzungen, Warteschlangen und Zwischenspeicher, API- und Upload-Tokens leer | Admin → Export |

## Entitäts-Matrix

Legende: ● voll · ◐ teilweise / eingebettet · ○ nicht enthalten

| Entität | EAD2002 | EAD3 | TEI | RDF A+ | RiC | Memobase | DC | DIP/OCFL | Excel voll | Excel Update | SQL-Dump |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Verzeichnungseinheit | ● | ● | ◐ | ● | ● | ● | ● | ● | ● | ◐ | ● |
| Hierarchie | ● | ● | ○ | ● | ● | ● | ◐ | ● | ◐ | ○ | ● |
| Medien (Metadaten) | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ○ | ○ | ● |
| Medien (Dateien) | ○ | ○ | ○ | ◐¹ | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| Volltext / OCR | ○ | ○ | ○ | ●¹ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Akteur:innen (eingebettet) | ● | ● | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Akteur:innen (Normdatei) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Orte (eingebettet) | ◐ | ◐ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Orte (Normdatei) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Schlagwörter | ● | ● | ● | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Ereignisse (Graph) | ◐ | ◐ | ◐ | ● | ● | ○ | ○ | ○ | ◐ | ○ | ● |
| Textfelder (ISAD-Felder) | ● | ● | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ● | ● |
| Termselect-Werte | ◐ | ○ | ○ | ● | ○ | ○ | ○ | ◐ | ○ | ○ | ● |
| Seiten / Editionen | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Sprachen / Anzeige-Datum | ● | ● | ○ | ● | ● | ○ | ○ | ○ | ◐ | ◐ | ● |
| Standort (physisch) | ◐² | ◐² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Schutzfrist (strukturiert) | ◐² | ◐² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Kommentare (intern) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ●³ |
| Benutzerkonten | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Einstellungen / Formulare | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| KI-Erschliessungsdaten | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Datei-Provenienz (PRONOM/NARA) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ◐⁴ | ○ | ○ | ● |

² **EAD 2002 und EAD3** schreiben die Schutzfrist als Satz in `<accessrestrict>`,
mit dem Jahr, ab dem die Unterlagen frei sind, neben dem Textfeld
«Zugangsbedingungen». apeEAD lässt dafür kein eigenes, auswertbares Element zu.
Das Textfeld «Standort (Detail)» geht als `<physloc>` hinaus, der Standort-Verweis
nicht.

³ **Kommentare** sind interne Arbeitsnotizen und erscheinen bewusst in keinem
Publikationsformat — auch nicht im nativen Round-Trip. Sie liegen ausschliesslich
im SQL-Dump. Das ist kein Umsetzungsstand, sondern eine Festlegung: Sie werden in
einer eigenen Tabelle geführt, die kein Exporter kennt, damit sie auch nicht
versehentlich in eine Publikation geraten können. Siehe [Kommentare](comments.md).

¹ Nur im **A+ Bundle**: Der reine A+-Export liefert bundle-relative Medien-Verweise,
Bildmasse, AV-Dauer und OCR-Volltext im Graphen; das ZIP legt zusätzlich die
Derivate (`thumb`/`web`) daneben — im Standardfall **nicht die Master**. Mit
`--include-originals` kommen die Master-Dateien dazu, siehe
[Migrations-Export](#migrations-export-das-bundle-als-weg-hinaus).

⁴ **PREMIS 3** je Datensatz mit Medien (anton#661): Formate (PRONOM), Prüfsummen,
behaltene Originale und alle Ereignisse an den Medien mit Werkzeug und Version.
Nicht enthalten ist die NARA-Risikobewertung. Gilt auch für den nativen
Round-Trip, nicht für die ZH-Variante des DIP.

## Gut abgedeckt

**Verzeichnungseinheiten** sind breit unterstützt. **EAD2002** ist das
vollständigste Format: Titel auch in den weiteren Sprachen, Signatur, Datierung
mit Kommentar, Stufe, Umfang, Sprachen und Schrift, Schutzfrist und die
ISAD(G)-Textfelder, die das Formular des Datensatzes öffentlich zeigt.
Zugangspunkte stehen nach Typ (`persname`, `corpname`, `famname`, `subject`,
`geogname`) mit der GND-Nummer, wo eine verknüpft ist. Digitalisate gehen als
Webansicht und Vorschaubild hinaus, nie als Master. Jede Datei wird beim
Schreiben gegen `ead.xsd` und `apeEAD.xsd` geprüft, auch im nächtlichen Lauf; ein
Befund steht im Log und in der Ausgabe von `anton:export`.
Nicht möglich sind mehrsprachige Textfelder: apeEAD erlaubt jedes Textfeld nur
einmal und kennt keine Sprachangabe daran. Hinaus geht die Fassung in der
Hauptsprache des Archivs. **RDF A+** typisiert dasselbe doppelt (CIDOC CRM
*und* RiC-O), inklusive mehrsprachiger Titel.

**Normdaten** haben genau einen strukturierten, eigenständigen Export: die
**TEI-Normdatenlisten** mit allen Namensformen, Lebensdaten, Koordinaten,
Beschreibung, Quellen und externen Links. Zwei Einschränkungen: Nur **freie**,
nicht an Objekte gebundene Normdatensätze werden ausgegeben, und Akteur:innen oder
Orte ohne Typ werden übersprungen. Sonst erscheinen Normdaten nur eingebettet in
Objektexporten.

**Datierungen** von Akteur:innen gehen so genau hinaus, wie sie erfasst sind: ein
Jahr als Jahr, ein Monat als Monat. Eine Zirka-Angabe trägt TEI als
`cert="medium"`, CIDOC CRM über die inneren Grenzen (P81), RiC-O im lesbaren
`expressedDate`. Der native Round-Trip und die Excel-Tabelle der Akteur:innen
nehmen sie mit. CIDOC CRM gibt bei Körperschaften Gründung und Auflösung aus
(ab Anton v0.103.0).

## Nur im SQL-Dump

Diese Daten überleben **keinen** Formatexport:

- **Benutzerkonten und Authentifizierung** — gehört auch nicht in einen Archivexport
- **Einstellungen, Formulardefinitionen, Standorte, Bestellungen, Nachrichten**
- **NARA-Risikobewertung** der Dateien — die übrige Datei-Provenienz (Formate,
  Prüfsummen, Ereignisse) reist seit anton#661 als PREMIS in DIP, OCFL und nativem
  Round-Trip mit
- **KI-Erschliessungsdaten** — Profile, Verbrauch, Budgets, Audit-Stichproben
- **Editionen** und **Korrespondenzen**
- **Volltext-Index**
- **Der Ereignis-Graph als Relation** — Ereignisse erscheinen nur abgeflacht (Excel)
  oder implizit (EAD, RDF)

## Migrations-Export: das Bundle als Weg hinaus

Die Matrix oben beschreibt den **Standardfall**. Der RDF-Export kennt zwei Schalter,
die ihn aus der Publikationsecke herausheben:

| Schalter | Wirkung |
|---|---|
| `--include-protected` | umgeht den Datenschutzfilter — gesperrte Datensätze, nur interne Medien und interne Textfelder kommen mit. Wirkt bei `a-plus`, `ric` und `a-plus-bundle`, **nicht** bei `memobase` |
| `--include-originals` | nur `a-plus-bundle`: packt die **Original-Master** ins ZIP, nicht nur `web`/`thumb` |

```bash
php artisan anton:export-rdf --env=<slug> --root=<id> \
    --profile=a-plus-bundle --include-protected --include-originals
```

Das Ergebnis ist ein standardkonformes Paket aus CIDOC-CRM/RiC-O-Graph, gesperrten
Daten und Originaldateien — geeignet, um einen Bestand in ein **anderes System** zu
überführen. Für den Rückweg nach Anton gibt es kein fertiges Werkzeug — dafür bleibt der
native Round-Trip zuständig. Und es enthält personenbezogene Daten: nicht öffentlich hosten.

## Wer welches Artefakt auslösen kann

| Artefakt | Selfservice in der Oberfläche |
|---|---|
| SQL-Dump | **ja** — Admin → Export |
| EAD, TEI, RDF (Standard), A+ Bundle (Standard), DIP, E-ARK DIP (Zugang), OCFL, Excel, Word/PDF | **ja** |
| E-ARK DIP vollständig (`--full`) | **nein** — nur CLI |
| A+ Bundle mit `--include-protected` / `--include-originals` | **nein** — die UI und die API reichen die Schalter nicht durch, nur CLI |
| Nativer Round-Trip (`anton:export-native` / `anton:import-native`) | **nein** — reines CLI-Kommando |

Bei *Anton as a Service* erzeugt k & r die CLI-Artefakte auf Anfrage; *on premises*
laufen die Kommandos bei der betreibenden Institution.

## Format-Einschränkungen im Einzelnen

**EAD3** enthält dasselbe wie EAD2002, in EAD3 geschrieben und beim Schreiben
gegen `ead3.rng` geprüft: Umfang und Datierung strukturiert, Namen mit
`@identifier` und `@source` des Normdatensatzes, Titel in den weiteren Sprachen
mit `@lang`. Textfelder gehen wie in EAD2002 in der Hauptsprache hinaus. Die
Validierungsseite prüft auch EAD3-Dateien.

**EAD Holding Guide** liefert eine flache Bestandsübersicht ohne Textfelder pro
Knoten.

**Memobase-RDF** ist bewusst verlustbehaftet: keine Akteur:innen, Orte, Schlagwörter
oder Ereignisse — nur Institution, Objekte, Instantiations und rund acht
Textfeldtypen. Eine Instantiation beschreibt die **Zugangskopie** (Link, Dateityp,
Grösse, Bildmasse), nicht den Master: keine Prüfsumme des Originals, und ohne
Zugangskopie kein Link. Ein Export ab einem Teilbaum liefert die übergeordneten
RecordSets mit.

**TEI pro Objekt** kennt keinen Gesamtexport, keine Hierarchie und kaum Medien.

**E-ARK DIP** (anton#697) gibt es in zwei Umfängen. *Zugang* ist eine Publikationssicht: Was ein Gast sehen darf, gleich wer exportiert — gesperrte Datensätze und Entwürfe fehlen samt Teilbaum, Datensätze mit laufender Schutzfrist behalten ihre Beschreibung, aber nicht ihre Medien, private Medien fehlen. Die Medien liegen als Nutzungskopien (`web`) in der Repräsentation `access`, beschrieben in EAD3 oder EAD 2002 (Einstellung `eark_dip_ead`), auf Wunsch zusätzlich RiC-O und CIDOC CRM als Turtle (`eark_dip_rdf`). PREMIS nennt die Funktion jeder Repräsentation und die Herkunft jeder Datei, ohne Ereignisse und ohne Personen. *Vollständig* (`--full`, nur CLI) ist eine Übergabe wie DIP und OCFL: alle Datensätze, Master in `master`, behaltene Originale in `original`, dazu das native Format (`anton-native`), PREMIS je Datensatz und das Word-Findbuch. Jedes Paket wird vor der Auslieferung geprüft; ein ungültiges wird nicht ausgeliefert. Siehe [DIP Download](download-dip.md#e-ark-dip).

**DIP, OCFL und nativer Round-Trip** führen seit anton#661 je Datensatz mit
Medien eine **PREMIS-3-Datei** mit (DIP: `data/meta/<Datensatz>.premis.xml`,
OCFL: `metadata/premis.xml`, nativ: `premis/<Datensatz>.xml`). Darin stehen die
Dateien und behaltenen Originale mit MD5/SHA-512, Grösse und PRONOM-Format, alle
Ereignisse an den Medien (Virenprüfung, Integritäts- und Formatprüfung,
Formaterkennung, Formatregeln, Übergabe an die Cloud, Übernahme mit der
handelnden Person) und die beteiligten Werkzeuge mit Version. METS gibt es nicht.
Die ZH-Variante des DIP enthält nur Mediendateien, keine Metadaten und kein
PREMIS.

**Die beiden Excel-Exporte verfolgen entgegengesetzte Zwecke.** Der *volle*
Export ist eine Auswertungssicht: er nimmt alles mit, was sich flach darstellen
lässt, und lässt sich **nicht** wieder einspielen. Die *Update-Tabelle* ist das
Gegenteil — sie enthält bewusst nur, was ein Datenupdate auch schreiben darf, und
lässt Hierarchie (`parent`) und Ereignisse weg, weil diese beim Zurückspielen
blockiert würden. Der Standort ist enthalten: er wird beim Update
geschrieben, und Umräumen im Magazin ist einer der häufigsten Gründe für ein
Massen-Update. Wer die schmalere Datei
nimmt, verliert also keine Information versehentlich, sondern begrenzt absichtlich
den Wirkungsbereich; im Download-Dialog lässt sich das noch weiter einschränken.

Die Update-Tabelle eines **mehrsprachigen** Archivs führt den Titel
in je einer Spalte pro Inhaltssprache (`title_de`, `title_fr` …) statt in einer
einzigen. Damit ist der Round-Trip auch mehrsprachig verlustfrei: Mit einer
Spalte müsste beim Zurückspielen die Sprache des Laufs entscheiden, wohin der
Wert gehört, und ein französischer Titel landete im deutschen Feld. Einsprachige
Archive behalten die bare Spalte `titel`. Der *volle* Export gibt den Titel
weiterhin einsprachig aus — er ist eine Lesesicht, kein Rückweg.

Beides sind **keine Sicherungen**: Auch der volle Excel-Export führt weder Medien
noch Normdateien noch Formulare. Für einen Rückweg dienen der native Round-Trip
oder der SQL-Dump (siehe unten).

## RDF A+ und nativer Round-Trip sind zwei Produkte

Der **A+-Graph ist eine Discovery-Sicht, kein Backup.** Aus dem Bundle allein
lässt sich kein Anton-Mandant rekonstruieren: Es fehlen die UUIDs, der
Formularsatz, die Rohwerte und die Schutzfristen.

Für den verlustfreien Weg gibt es den **nativen Round-Trip**
(`anton:export-native` → `anton:import-native`): ein Paket im
`anton-import-format` v0.5 samt Master-Medien, das Anton wieder einliest.
Verankert über UUIDs (unbekannt → neu anlegen, bekannt → überspringen, mit
`--update` aktualisieren), Hierarchie über die UUID der übergeordneten Einheit,
alle Sprachen, Ereignisse, Textfelder **aller** Träger einschliesslich privater,
Termselect-Werte, Formularsatz und die Wiederanbindung der Medien. Vor jedem
Schreibvorgang wird das ganze Paket validiert; schlägt es fehl, wird
zurückgerollt.

Auch Akteur:innen, Orte und Schlagwörter tragen eine portable UUID — ein
Re-Import verankert sie daran, statt gleichnamige Normdatensätze zu verschmelzen.

!!! warning "Kommentare gehen beim Round-Trip verloren"
    «Verlustfrei» bezieht sich auf die Erschliessung. Interne
    [Kommentare](comments.md) sind davon ausgenommen: Sie werden in
    einer eigenen Tabelle geführt, die kein Exporter kennt — auch der native
    nicht —, damit sie nicht versehentlich in eine Publikation geraten. Ein
    Export-Import-Zyklus lässt sie zurück.

    Wer sie mitnehmen muss, braucht den **SQL-Dump**. Das ist die Sicherung,
    die wirklich alles enthält.

Nicht enthalten und damit weiterhin SQL-Dump: Benutzerkonten, Einstellungen,
Formulardefinitionen und die KI-Daten.

## Datenschutz-Filter

RDF, TEI und EAD filtern gesperrte Datensätze und Akteur:innen, nur interne
Medien sowie interne Textfeldtypen (Archivinterne Bemerkungen, Informationen des Bearbeiters,
Kommentar) heraus.

**EAD** zeigt immer die öffentliche Sicht, wer die Datei auch erzeugt: keine
gesperrten Verzeichnungen und Entwürfe samt allem, was darunter liegt, keine
gesperrten Akteur:innen, auch nicht als Urheber:in. Die Datei eines öffentlichen
Bestands liefert Anton über OAI-PMH an alle aus. Bis v0.100.0 enthielt sie, was
die erzeugende Person sehen durfte, und immer auch die gesperrten Urheber:innen
(anton#616).

!!! warning "Reine Flag-Logik"
    Der Filter wertet das `private`-Kennzeichen aus — er ist **keine
    Rollenprüfung**. Der Download einer erzeugten RDF-Datei prüft ausser dem
    Dateinamen keine weiteren Berechtigungen.

## Kernaussage

**Beschreibungsmetadaten** sind über offene Standards exzellent abgedeckt und
paketierbar. **Normdaten** haben genau einen eigenständigen Export (TEI).
**Datei-Provenienz** reist als PREMIS in DIP, OCFL und nativem Round-Trip mit.
**Ereignisgraph, Benutzer:innen, Konfiguration und KI-Daten** haben keinen
standardbasierten Export und lassen sich nur über den vollständigen SQL-Dump
sichern.
