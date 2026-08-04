# Export-Matrix

Übersicht, welche Anton-Daten über welches Export-Format ausgegeben werden — und
welche sich nur über den vollständigen SQL-Dump rekonstruieren lassen.

Wozu welches Artefakt taugt, ordnet [Langzeitarchivierung: Überblick](preservation.md)
ein. Die Kurzfassung: **Nativer Round-Trip und SQL-Dump sind Sicherungen, alles
andere sind Publikations- und Austauschsichten.**

!!! info "Stand"
    Diese Matrix bildet den Stand vom **4. August 2026** ab (Anton v0.82). Sie wird
    zusammen mit den Exportern gepflegt.

## Verfügbare Formate

| Format | Standard | Umfang | Einstieg |
|---|---|---|---|
| EAD 2002 | apeEAD (`ead.xsd` + `apeEAD.xsd`) | Objekt-Baum ab Bestand | Admin → Export |
| EAD3 | `ead3.rng` | Objekt-Baum (reduziert) | Admin → Export |
| EAD Holding Guide | apeEAD `type=holdings_guide` | Bestandsübersicht | Admin → Export |
| TEI – Normdaten-Listen | TEI-P5 `standOff` | Akteur:innen / Orte / Schlagwörter (gesamt) | `/api/tei/{actors,places,keywords}` |
| TEI – pro Objekt | TEI-P5 | ein Datensatz | API mit `?format=tei` |
| RDF «A+» | CIDOC CRM + RiC-O (dual) | Objekt-Baum, alle Entitäten | Admin → Export, `anton:export-rdf` |
| RDF RiC | reines RiC-O 1.1 (JSON-LD) | Objekt-Baum | Admin → Export |
| RDF Memobase | RiC-O-Subset (JSON-LD) | Objekt-Baum (verlustbehaftet) | Admin → Export |
| RDF «A+» Bundle | CIDOC CRM + RiC-O **+ Mediendateien** als ZIP | Objekt-Baum, offline anzeigbar ohne Anton | `anton:export-rdf --profile=a-plus-bundle` |
| **Nativer Round-Trip** | `anton-import-format` v0.4 (JSON) **+ Master-Medien** als ZIP | Objekt-Baum, **verlustfrei re-importierbar** | `anton:export-native` / `anton:import-native` |
| Dublin Core | OAI-DC | pro Objekt (nur eingebettet) | Baustein in DIP / OCFL |
| DIP | BagIt | Paket: Medien + Metadaten (Teilbaum) | Taste «DIP» am Datensatz |
| OCFL | Oxford Common File Layout | Paket: Medien + Metadaten (Objekt/Teilbaum) | Taste am Datensatz |
| Excel (voll) | XLSX | aktuelle Trefferliste, alle Felder | Trefferliste → Export |
| Excel (Update-Tabelle) | XLSX | Trefferliste, **nur beschreibbare Felder**, wieder einspielbar | Trefferliste → Export → Update |
| Word / PDF | DOCX / PDF | Findbuch pro Objekt | Taste am Datensatz |
| Paper | HTML-Druckansicht | Trefferliste (max. 1000) | Trefferliste |
| **SQL-Dump** | mysqldump (gzip) | **ganze Mandanten-Datenbank** | Admin → Export |

## Entitäts-Matrix

Legende: ● voll · ◐ teilweise / eingebettet · ○ nicht enthalten

| Entität | EAD2002 | EAD3 | TEI | RDF A+ | RiC | Memobase | DC | DIP/OCFL | Excel voll | Excel Update | SQL-Dump |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Verzeichnungseinheit | ● | ◐ | ◐ | ● | ● | ● | ● | ● | ● | ◐ | ● |
| Hierarchie | ● | ● | ○ | ● | ● | ● | ◐ | ● | ◐ | ○ | ● |
| Medien (Metadaten) | ◐ | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ○ | ○ | ● |
| Medien (Dateien) | ○ | ○ | ○ | ◐¹ | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| Volltext / OCR | ○ | ○ | ○ | ●¹ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Akteur:innen (eingebettet) | ◐ | ◐ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Akteur:innen (Normdatei) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Orte (eingebettet) | ◐ | ○ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Orte (Normdatei) | ○ | ○ | ● | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ● |
| Schlagwörter | ◐ | ◐ | ● | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ● |
| Ereignisse (Graph) | ◐ | ◐ | ◐ | ● | ● | ○ | ○ | ○ | ◐ | ○ | ● |
| Textfelder (ISAD-Felder) | ● | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ● | ● |
| Termselect-Werte | ◐ | ○ | ○ | ● | ○ | ○ | ○ | ◐ | ○ | ○ | ● |
| Seiten / Editionen | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Sprachen / Anzeige-Datum | ● | ◐ | ○ | ● | ● | ○ | ○ | ○ | ◐ | ◐ | ● |
| Standort (physisch) | ○² | ○² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Schutzfrist (strukturiert) | ○² | ○² | ○ | ● | ○ | ○ | ○ | ○ | ● | ● | ● |
| Benutzerkonten | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Einstellungen / Formulare | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| KI-Erschliessungsdaten | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Datei-Provenienz (PRONOM/NARA) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |

² **EAD** gibt Zugangsbestimmungen und Standortangaben nur als Freitext aus —
`<accessrestrict>` und `<originalsloc>` werden aus den gleichnamigen Textfeldern
gespeist, nicht aus dem Feld «Zugangsbestimmungen / Sperrfrist» oder dem
Standort-Verweis. Ein Konsument erhält also das, was jemand hingeschrieben hat,
nicht die auswertbare Frist. `<physloc>` ist nicht implementiert.

¹ Nur im **A+ Bundle**: Der reine A+-Export liefert bundle-relative Medien-Verweise,
Bildmasse, AV-Dauer und OCR-Volltext im Graphen; das ZIP legt zusätzlich die
Derivate (`thumb`/`web`) daneben — **nicht die Master**.

## Gut abgedeckt

**Verzeichnungseinheiten** sind breit unterstützt. **EAD2002** ist das
vollständigste Format: Titel, Signatur, Datierung, Stufe, Umfang, Sprachen und
sämtliche ISAD(G)-Textfelder. **RDF A+** typisiert dasselbe doppelt (CIDOC CRM
*und* RiC-O), inklusive mehrsprachiger Titel.

**Normdaten** haben genau einen strukturierten, eigenständigen Export: die
**TEI-Normdatenlisten** mit allen Namensformen, Lebensdaten, Koordinaten,
Beschreibung, Quellen und externen Links. Zwei Einschränkungen: Nur **freie**,
nicht an Objekte gebundene Normdatensätze werden ausgegeben, und Akteur:innen oder
Orte ohne Typ werden übersprungen. Sonst erscheinen Normdaten nur eingebettet in
Objektexporten.

## Nur im SQL-Dump

Diese Daten überleben **keinen** Formatexport:

- **Benutzerkonten und Authentifizierung** — gehört auch nicht in einen Archivexport
- **Einstellungen, Formulardefinitionen, Standorte, Bestellungen, Nachrichten**
- **Datei-Provenienz** — PRONOM/NARA-Historie und Konversions-Ereignisse, also die
  gesamte Preservation-Historie der Dateien
- **KI-Erschliessungsdaten** — Profile, Verbrauch, Budgets, Audit-Stichproben
- **Editionen** und **Korrespondenzen**
- **Volltext-Index**
- **Der Ereignis-Graph als Relation** — Ereignisse erscheinen nur abgeflacht (Excel)
  oder implizit (EAD, RDF)

## Format-Einschränkungen im Einzelnen

**EAD3** ist deutlich dünner als EAD2002: keine Textfelder, keine Orte, keine
Akteur:innen-Deskriptoren, keine Medien, keine Sprachangaben — nur Signatur, Titel,
Datierung, Urheber:innen und Schlagwörter.

**EAD Holding Guide** liefert eine flache Bestandsübersicht ohne Textfelder pro
Knoten.

**Memobase-RDF** ist bewusst verlustbehaftet: keine Akteur:innen, Orte, Schlagwörter
oder Ereignisse — nur Institution, Objekte, Instantiations und rund acht
Textfeldtypen.

**TEI pro Objekt** kennt keinen Gesamtexport, keine Hierarchie und kaum Medien.

**DIP und OCFL** führen kein PREMIS und kein METS; die Preservation-Metadaten
beschränken sich auf das OCFL-Inventory. Die ZH-Variante des DIP enthält nur
Mediendateien, keine Metadaten.

**Die beiden Excel-Exporte verfolgen entgegengesetzte Zwecke.** Der *volle*
Export ist eine Auswertungssicht: er nimmt alles mit, was sich flach darstellen
lässt, und lässt sich **nicht** wieder einspielen. Die *Update-Tabelle* ist das
Gegenteil — sie enthält bewusst nur, was ein Datenupdate auch schreiben darf, und
lässt Hierarchie (`parent`), Ereignisse und Standort weg, weil diese beim
Zurückspielen blockiert würden oder wirkungslos blieben. Wer die schmalere Datei
nimmt, verliert also keine Information versehentlich, sondern begrenzt absichtlich
den Wirkungsbereich; im Download-Dialog lässt sich das noch weiter einschränken.

Beides sind **keine Sicherungen**: Auch der volle Excel-Export führt weder Medien
noch Normdateien noch Formulare. Für einen Rückweg dienen der native Round-Trip
oder der SQL-Dump (siehe unten).

## RDF A+ und nativer Round-Trip sind zwei Produkte

Der **A+-Graph ist eine Discovery-Sicht, kein Backup.** Aus dem Bundle allein
lässt sich kein Anton-Mandant rekonstruieren: Es fehlen die UUIDs, der
Formularsatz, die Rohwerte und die Schutzfristen.

Für den verlustfreien Weg gibt es den **nativen Round-Trip**
(`anton:export-native` → `anton:import-native`): ein Paket im
`anton-import-format` v0.4 samt Master-Medien, das Anton wieder einliest.
Verankert über UUIDs (unbekannt → neu anlegen, bekannt → überspringen, mit
`--update` aktualisieren), Hierarchie über die UUID der übergeordneten Einheit,
alle Sprachen, Ereignisse, Textfelder **aller** Träger einschliesslich privater,
Termselect-Werte, Formularsatz und die Wiederanbindung der Medien. Vor jedem
Schreibvorgang wird das ganze Paket validiert; schlägt es fehl, wird
zurückgerollt.

Auch Akteur:innen, Orte und Schlagwörter tragen seit v0.79 eine portable UUID — ein
Re-Import verankert sie daran, statt gleichnamige Normdatensätze zu verschmelzen.

Nicht enthalten und damit weiterhin SQL-Dump: Benutzerkonten, Einstellungen,
Formulardefinitionen und die KI-Daten.

## Datenschutz-Filter

RDF, TEI und EAD filtern private Objekte, Akteur:innen und Medien sowie private
Textfeldtypen (Archivinterne Bemerkungen, Informationen des Bearbeiters,
Kommentar) heraus.

!!! warning "Reine Flag-Logik"
    Der Filter wertet das `private`-Kennzeichen aus — er ist **keine
    Rollenprüfung**. Der Download einer erzeugten RDF-Datei prüft ausser dem
    Dateinamen keine weiteren Berechtigungen.

## Kernaussage

**Beschreibungsmetadaten** sind über offene Standards exzellent abgedeckt und
paketierbar. **Normdaten** haben genau einen eigenständigen Export (TEI).
**Ereignisgraph, Benutzer:innen, Konfiguration, KI-Daten und Datei-Provenienz** haben
keinen standardbasierten Export und lassen sich nur über den vollständigen
SQL-Dump sichern.
