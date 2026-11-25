## Zusammenfassung
Mit dem Tabellen-Import kommen Datensätze und ihre Dateien (Medien) aus einer Excel-, ODS- oder CSV-Tabelle nach Anton. Die Tabelle wird hochgeladen, geprüft und dann importiert; die Medien liegen vorher im Reiter «Medien» bereit. Die Hilfe in Anton (Tabellen-Import → Reiter «Dokumentation», `/import/excel/documentation`) zeigt dieselbe Spaltenliste wie diese Seite, dazu die Werte und Trennzeichen des eigenen Archivs.

## Daten-Import `/import`

Alle Import-Wege beginnen unter **Admin → Import / Export → Daten-Import** (`/import`). Die Seite zeigt je Weg eine Kachel:

| Kachel | Inhalt |
|---|---|
| **Tabellen-Import** | Excel-, ODS- oder CSV-Tabelle mit Datensätzen und Medien (das Thema dieser Seite). Reiter: Metadaten, Medien, Update, Dokumentation, Wertelisten. |
| **SIP eCH-0160** | Ablieferungspakete nach eCH-0160, siehe [SIP Ingest](../admin/sip-ingest.md). |
| **Verzeichnis-Import** | Import einer Verzeichnisstruktur (ZIP/GZ). |
| **Agate Sipline Import** | nur wo eingerichtet: Pakete aus agate, siehe [agate SIP](../admin/agate-sip.md). |
| **Prüfliste für Vorschläge**, **Imports**, **DIMAG-Status** | je nach Recht und Einrichtung: Vorschläge prüfen, das [Import-Protokoll](#import-protokoll), der Stand der Übergabe an DIMAG. |

Alte Adressen wie `/import/validation`, `/import/ingest`, `/import/documentation` oder `/sip/validation` führen auf den Tabellen-Import bzw. auf diese Übersicht.

### Detail-Ansicht im Eingangskorb

Pro wartendem SIP im Eingangskorb gibt es einen **Details**-Link. Dahinter steht eine Inspektions-Seite, die nur die `metadata.json` aus dem Paket liest (kein Auspacken der Medien) und zeigt:

- Paketprüfung: BagIt (Manifest, Checksummen) oder E-ARK (Prüfung nach E-ARK)
- Anzahl Datensätze im SIP
- NARA-Objekttyp-Kategorien — mit Hinweis, falls der Tenant für eine Kategorie keinen passenden Typ kennt
- Titel des obersten Datensatzes

So lässt sich vor dem Import sehen, ob das SIP sinnvoll ist, ob das Tenant-Vokabular passt, und das SIP gegebenenfalls verwerfen, bevor etwas in der Datenbank landet.

### Live-Fortschritt

Alle Imports laufen **asynchron im Hintergrund**. Nach dem Klick auf "Importieren" landet man auf einer Fortschritts-Seite, die alle paar Sekunden den aktuellen Stand aktualisiert: Schritt (Sicherung der Datenbank, Lesen, Prüfen, Datensätze anlegen, Mediendateien übernehmen, Fertig), erledigte Zeilen, am Ende ein Link zum **Lauf im Importprotokoll**.

Das gilt für alle Pfade — Excel, SIP, Verzeichnis und Eingangskorb-Finalisieren.

### Signatur für jeden Import

Jeder Import (egal über welchen Pfad) bekommt eine Signatur `IMPORT-{jjjj}-{NNN}` und einen Eintrag im Importprotokoll. Der Eintrag hält fest:

- Ursprünglicher Dateiname
- MD5-Prüfsumme
- Import-Zeitpunkt
- Import-Pfad (Excel / SIP / Verzeichnis / agate)
- die **verwendeten Einstellungen** (siehe unten)
- das Ergebnis, und bei einem Fehlschlag die Meldung

<!-- v0.88.0: Belege im Akzessionsarchiv abgeschafft, Bestand ins Protokoll migriert -->
!!! info "Kein Beleg im Akzessionsarchiv"
    Ein Import legt keine Verzeichnungseinheit als Beleg an. Das Akzessionsarchiv bleibt den echten Übernahmen vorbehalten — physisch eingetroffen, noch nicht erschlossen — und seine Signaturen werden nicht von Importen aufgebraucht.

Die Signatur wird beim Start vergeben. Ein gescheiterter Lauf behält sie also und bleibt mit seinem Fehler im Protokoll stehen — eine gescheiterte Lieferung muss von einer unterscheidbar bleiben, die nie stattfand.

### Import-Protokoll {#import-protokoll}

Unter **`/import/audit`** steht die Liste aller Importläufe: Signatur, Quelldatei, Zeitpunkt, Zahl der erzeugten Datensätze und die verwendete Inhaltssprache. Es ist eine gewöhnliche Anton-Tabelle — sortierbar, mit einstellbarer Seitenlänge, und die Spalten lassen sich wie bei jeder anderen Liste unter *Admin → Formulare* anpassen.

Gezeigt werden standardmässig die erfolgreichen Läufe; ein Filter blendet gescheiterte und abgebrochene ein. Gelöscht wird nie.

Der **Details**-Link führt zum Lauf: Quelldatei, Prüfsumme, verwendete Einstellungen samt Herkunft, wer ihn ausgelöst hat, und die Datensätze, die er angelegt hat.

Die eingespielte Datei bleibt erhalten. Nach einem erfolgreichen Lauf wandert sie nach `metadata_imported/` — damit sie nicht mehr in der Auswahlliste steht — und der Eintrag nennt den Ablageort.

Die Einstellungen werden im Klartext festgehalten, eine Zeile je Einstellung mit Wert und Herkunft. Sie stehen dort dauerhaft — auch ein Jahr später ist damit nachvollziehbar, unter welchen Annahmen eine Lieferung hereingekommen ist.

## Ablauf (Tabellen-Import)

1. **Vorlage holen.** Im Reiter «Dokumentation» liegen eine leere Vorlage und eine Beispieltabelle mit gültigen Zeilen aus dem eigenen Archiv. Gelesen wird nur das erste Tabellenblatt; weitere Blätter meldet die Prüfung als nicht gelesen.
2. **Medien hochladen.** Nennt die Tabelle Dateien (Spalte `media`), diese zuerst im Reiter «Medien» hochladen. Fehlt eine Datei, meldet die Prüfung einen Fehler.
3. **Tabelle hochladen** im Reiter «Metadaten» (`.xlsx`, `.ods` oder `.csv`; alte `.xls`-Dateien kann Anton nicht lesen).
4. **Prüfen.** Das Augen-Symbol in der Liste öffnet die Prüfung: erkannte und ignorierte Spalten, Fehler, Warnungen, was neu angelegt würde und mit welchen Einstellungen (siehe [Vorschau](#vorschau-was-der-import-neu-anlegen-wurde)).
5. **Importieren.** Ist die Prüfung bestanden, startet «Importieren» den Lauf im Hintergrund.

Bestehende Datensätze ändert nur der Reiter «Update» (siehe [unten](#bestehende-datensatze-aktualisieren-update-uber-den-browser)), nie ein Neu-Import: Eine Zeile mit einer bestehenden `id` lehnt die Prüfung ab.

## Inhaltssprache des Imports

Übersetzbare Felder — Titel, Textfelder, neu angelegte Schlagworte, Akteur:innen, Orte und Standorte — brauchen eine Sprache. Das ist eine bewusste Entscheidung, die vor dem Lauf sichtbar ist.

<!-- v0.87.0: Inhaltssprache explizit, vorher richtete sich der Import nach der Oberflächensprache -->
!!! note "Die Oberflächensprache spielt keine Rolle"
    Welche Sprache die Bedienoberfläche gerade zeigt, hat auf den Import keinen Einfluss. Massgeblich ist allein die Inhaltssprache des Laufs.

Die Inhaltssprache wird in dieser Reihenfolge bestimmt — der erste gesetzte Wert gewinnt:

1. die Wahl für diesen Lauf (`--locale` auf der Kommandozeile)
2. die Archiv-Einstellung `import_options.locale`
3. die erste Sprache aus `locales` — die Hauptsprache des Archivs

Die Inspektionsseite nennt vor dem Start die geltende Sprache **und woher sie stammt** («für diesen Lauf gewählt», «Archiv-Einstellung», «Vorgabe»). Nach dem Lauf steht dieselbe Angabe im Protokolleintrag (siehe [Import-Protokoll](#import-protokoll)).

Eine Spalte mit Sprachkürzel (`title_fr`) sticht diese Wahl für ihr Feld aus — siehe [Mehrsprachige Spalten](#mehrsprachige-spalten).

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

Pflicht sind für einen neuen Datensatz `parent` und `level_of_description`, für ein Update `id` oder `uuid`. Die Reihenfolge der Spalten spielt keine Rolle, Gross- und Kleinschreibung der Kopfzeile auch nicht. Eine Spalte, die Anton nicht kennt, wird nicht importiert; die Prüfung nennt sie und schlägt einen ähnlichen Namen vor. Ein Text, der länger ist, als die Datenbank fasst, bricht den Import mit einer Meldung ab, statt still gekürzt zu werden.

Die Tabelle wird aus Anton erzeugt (`anton:import-columns`), aus denselben Regeln, nach denen der Import prüft. Die Trennzeichen sind die Vorgaben einer neuen Installation; jedes Archiv kann sie ändern, die Hilfe in Anton zeigt die eigenen.

<!-- BEGIN generated import columns -->

| Spalte | Inhalt | Art | Neu | Update | Auch erkannt als |
|---|---|---|---|---|---|
| `id` | Interne ID des Datensatzes. Schlüssel einer Update-Tabelle; ein Neu-Import lehnt Zeilen mit einer bestehenden ID ab. | Schlüssel | – | id oder uuid |  |
| `uuid` | Dauerhafte Kennung (UUID) des Datensatzes, wie id ein Schlüssel der Update-Tabelle. | Schlüssel | – | id oder uuid |  |
| `parent` | Übergeordneter Datensatz: seine Signatur oder seine ID. Er muss im Bestand sein oder weiter oben in derselben Tabelle stehen; eine rein numerische Angabe gilt als ID. | Signatur oder ID | Pflicht | – |  |
| `identifier` | Signatur, höchstens 100 Zeichen, im Bestand eindeutig. Leer leitet Anton sie aus dem übergeordneten Datensatz ab, ausser bei Bestandsgruppe und Klasse. | Text, eindeutig | ja | ja | `signatur` |
| `identifier_old` | Alte Signatur, frei. | Text | ja | ja | `altsignatur` |
| `title` | Titel in der Sprache des Imports. | Text | ja | ja | `titel` |
| `title_<lang>` | Titel in einer weiteren Sprache des Archivs, etwa title_fr. | Text | ja | ja |  |
| `level_of_description` | Verzeichnungsstufe aus der Werteliste: Bezeichnung, Name oder ID. | Werteliste | Pflicht | ja | `verzeichnungsstufe` |
| `object_type` | Objekttyp aus der Werteliste. Ein unbekannter wird nur angelegt, wenn die Import-Einstellung create-object-types an ist. | Werteliste | ja | ja | `objekttyp` |
| `object_count` | Anzahl der Einheiten. | ganze Zahl | ja | ja | `umfang_zahl` |
| `creation_date_start` | Beginn der Entstehung: Jahr, Monat oder Tag (1900, 1900-03, 1900-03-12, auch 12.03.1900); «ca.» davor wirkt wie 1 in creation_date_start_ca. Leer heisst kein Datum. Die Zelle als Text formatieren. | Datum | ja | – | `datum_von` |
| `creation_date_start_ca` | 1, wenn der Beginn ungefähr ist (ca.); sonst 0 oder leer. | 0 oder 1 | ja | – | `datum_von_ca` |
| `creation_date_end` | Ende der Entstehung, Datum wie creation_date_start; nicht vor dem Beginn (ein Jahr gilt als ganzes Jahr). Für einen Zeitpunkt Beginn und Ende gleich setzen. | Datum | ja | – | `datum_bis` |
| `creation_date_end_ca` | 1, wenn das Ende ungefähr ist (ca.); sonst 0 oder leer. | 0 oder 1 | ja | – | `datum_bis_ca` |
| `creation_actors` | Akteur:innen der Entstehung: Name, ID oder Normdaten-Kennung (gnd:…). Unbekannte werden angelegt, wenn die Import-Einstellung create-actors an ist, sonst meldet die Prüfung sie als Fehler. | Akteur:innen (getrennt durch `::` `;`) | ja | – | `provenienz_autor` |
| `creation_place` | Orte der Entstehung: Name, «Name / Stadt», ID oder geonames:…. Unbekannte werden angelegt, wenn create-places an ist. | Orte (getrennt durch `::` `;`) | ja | – |  |
| `creation_event_details` | Angaben zum Entstehungsereignis, frei. | Text | ja | – |  |
| `<event>_actors` | Akteur:innen eines anderen Ereignisses; <event> ist einer der Ereignistypen (Liste in der Dokumentation). | Akteur:innen (getrennt durch `::` `;`) | ja | – |  |
| `<event>_place` | Orte eines anderen Ereignisses. | Orte (getrennt durch `::` `;`) | ja | – |  |
| `<event>_date_start` | Beginn eines anderen Ereignisses, Datum wie oben; dazu <event>_date_start_ca. | Datum | ja | – |  |
| `<event>_date_end` | Ende eines anderen Ereignisses, Datum wie oben; dazu <event>_date_end_ca. | Datum | ja | – |  |
| `<event>_event_details` | Angaben zu einem anderen Ereignis, frei. | Text | ja | – |  |
| `note.<name>` | Textfeld des Formulars nach seinem Namen, etwa note.scopecontent oder scopecontent; mit Sprachzusatz (_fr) für weitere Sprachen. | Text | ja | ja |  |
| `languages` | Sprachen des Inhalts als Codes der im Archiv eingerichteten Sprachen. | Sprachcodes (getrennt durch `::`) | ja | ja | `sprache`, `sprachen` |
| `keywords_terms` | Sachschlagwörter: Name oder ID. Unbekannte werden angelegt, wenn create-keywords an ist. | Schlagwörter (getrennt durch `::` `,` `;`) | ja | ja | `keywords`, `sachschlagworte`, `schlagworte` |
| `keywords_actors` | Akteur:innen als Schlagwort, wie creation_actors. | Akteur:innen (getrennt durch `::` `;`) | ja | ja | `schlagworte_akteure`, `schlagworte_names` |
| `keywords_places` | Orte als Schlagwort, wie creation_place. | Orte (getrennt durch `::` `;`) | ja | ja | `schlagworte_orte`, `schlagworte_places` |
| `digitisation_actors` | Wer digitalisiert hat, Akteur:innen wie creation_actors. | Akteur:innen (getrennt durch `::` `;`) | ja | ja | `digitalisiert_von` |
| `location` | Standort: Bezeichnung oder ID. Ein unbekannter wird nur angelegt, wenn create-locations an ist. | Standort | ja | ja | `standort` |
| `location_id` | Standort nur als ID. | ganze Zahl | ja | ja |  |
| `formset` | Formularsatz: Name oder ID. | Formularsatz | ja | ja | `formularsatz` |
| `formset_id` | Formularsatz nur als ID. | ganze Zahl | ja | ja |  |
| `period_of_protection` | Schutzfrist aus der Werteliste: Bezeichnung, Name oder ID; leer heisst keine. | Werteliste | ja | ja | `schutzfrist` |
| `status_of_description` | Status der Verzeichnung aus der Werteliste: Bezeichnung, Name oder ID. | Werteliste | ja | ja | `status_beschreibung` |
| `detail_of_description` | Detailgrad der Verzeichnung aus der Werteliste: Bezeichnung, Name oder ID. | Werteliste | ja | ja | `detail_beschreibung` |
| `vacat` | Vacat aus der Werteliste: Bezeichnung oder ID; 0 und 1 aus älteren Tabellen werden noch verstanden. | Werteliste | ja | ja | `fehlt` |
| `private` | 1 sperrt den Datensatz und alles darunter für die Öffentlichkeit; 0 oder leer nicht. | 0 oder 1 | ja | ja | `privat` |
| `media` | Dateinamen der Medien, genau wie im Reiter «Medien» hochgeladen. Fehlt eine Datei, meldet die Prüfung einen Fehler. | Dateinamen (getrennt durch `::` `,` `;`) | ja | ja | `bilder` |
| `private_media` | Wie media, aber die Medien sind nur angemeldeten Konten mit Berechtigung sichtbar. | Dateinamen (getrennt durch `::` `,` `;`) | ja | ja | `private_bilder` |
| `loan` | Leihnehmer:in: «Nachname, Vorname» oder Benutzer-ID. | Benutzer:in | ja | ja |  |

<!-- END generated import columns -->

### Mehrsprachige Spalten
Der Titel ist ein **übersetzbares Feld**. In welche Sprache er geschrieben wird, entscheidet die [Inhaltssprache des Imports](#inhaltssprache-des-imports) — oder, genauer, die Spaltenbezeichnung selbst:

| Spalte | schreibt nach |
|---|---|
| `titel` bzw. `title` | die Inhaltssprache des Laufs |
| `title_de`, `title_fr`, `title_it`, `title_en` | genau die genannte Sprache |

Mehrsprachige Titel lassen sich also importieren: eine Spalte je Sprache. Beide Formen dürfen nebeneinander stehen; die Spalte mit Sprachkürzel ist die genauere Angabe und gewinnt, und die Inspektionsseite weist darauf hin.

Dasselbe gilt für die **Textfelder**: `scopecontent` schreibt in die Inhaltssprache, `scopecontent_fr` gezielt ins Französische, ohne die anderen Sprachen desselben Textfelds anzutasten.

!!! note "Nur konfigurierte Sprachen"
    Ein Sprachkürzel wird nur erkannt, wenn es in der Einstellung `locales` des Archivs steht (siehe [Sprachkonfiguration](languages.md)). `title_es` in einem Archiv ohne Spanisch ist keine Sprachangabe, sondern eine unbekannte Spalte — und die Inspektion meldet sie als solche.

### Ereignisse

Ereignisse verknüpfen einen Datensatz mit Akteur:innen, Orten und einem Zeitraum. Eine Spaltengruppe gehört zu einem Ereignistyp: vor den Feldnamen `actors`, `place`, `date_start`, `date_start_ca`, `date_end`, `date_end_ca`, `event_details` steht der Typ, für die Entstehung also `creation_actors`, `creation_place`, `creation_date_start`, `creation_date_start_ca`, `creation_date_end`, `creation_date_end_ca`, `creation_event_details`.

Ereignistypen: `creation`, `acquisition`, `reproduction`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. Die Hilfe in Anton zeigt die aktuelle Liste.

Die Datumsspalten nehmen ein Jahr, einen Monat oder einen Tag an: `1900`, `1900-03`, `1900-03-12`, auch `12.03.1900` oder `3. März 1900`. «ca.» vor dem Datum (`ca. 1900`) setzt das ca.-Kennzeichen wie eine 1 in der Spalte `…_ca`. Die Prüfung meldet ein Datum, das sie nicht lesen kann, und ein Bis-Datum vor dem Von-Datum; ein Jahr gilt dabei als ganzes Jahr, `1923` endet also nicht vor `1923-05-15`. Ein leeres Feld bedeutet: kein Datum.

#### Akteur:innen (z.B. creation_actors)

Eine Akteur:in wird über ihren Namen, ihre ID oder eine Normdaten-Kennung mit Präfix gefunden, kleingeschrieben und mit Doppelpunkt ohne Leerzeichen: `gnd:118519522`. Die Lebensdaten in Klammern sind möglich, aber nicht nötig; runde Klammern dürfen nicht für anderes stehen. Mehrere Akteur:innen werden mit dem Trennzeichen des Archivs getrennt (Vorgabe `::` oder `;`):

```
Müller, Martina (1934-1977) :: Rechtsabteilung
```

Ob eine unbekannte Akteur:in neu angelegt wird, entscheidet die Import-Einstellung `create-actors`: an (Vorgabe im Browser), wird sie angelegt, bei einer GND-Kennung mit den Angaben der GND; aus, meldet die Prüfung sie als Fehler. Über die Kommandozeile wird nur mit `--create-actors` angelegt.

#### Orte (z.B. creation_place)

Ein Ort wird über seinen Namen, seine ID oder eine Kennung wie `geonames:2954172` gefunden. Ob ein unbekannter Ort angelegt wird, entscheidet die Import-Einstellung `create-places`.

Orte können folgende Elemente enthalten:  
- Namen (wird durch "/" abgetrennt)  
- Stadt/Gemeinde  
- Kanton/Bundesland (wird in Klammern hinter der Gemeinde gesetzt)

### Spalten mit Wertelisten

Mehrere Spalten nehmen nur Werte an, die im Archiv definiert sind:
`verzeichnungsstufe`, `objekttyp`, `schutzfrist`, `status_of_description`,
`detail_of_description` und `vacat`.

Sie nehmen alle **drei Formen** an, gleichwertig:

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

Unter **Tabellen-Import → Wertelisten** (`/valuelists`) steht eine
Übersicht aller Wertelisten: pro Eintrag Bezeichnung,
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

### vacat

Gibt an, ob die Verzeichnungseinheit ein Platzhalter ist (eine Lücke in der
Zählung, zu der es keine Unterlagen gibt).

Die Spalte führt intern Term-IDs. Angenommen werden die Bezeichnung
(`vacat`), die ID (`56` für vacat, `57` für nicht vacat) und — aus älteren
Tabellen — `1` und `0`.

**Exportiert** wird die Bezeichnung: `vacat` für einen Platzhalter, sonst
eine leere Zelle. Ältere Tabellen mit `56`/`57` lassen sich unverändert
weiterverwenden.

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

Neben dem Neuanlegen können bestehende Verzeichnungseinheiten auch direkt über den Browser aktualisiert werden. Dafür gibt es unter **Tabellen-Import** einen eigenen Reiter **«Update»** (nach *Metadaten* und *Medien*). Dort die Tabelle hochladen — Update-Dateien haben eine eigene Liste, getrennt vom normalen Import — und mit dem Augen-Symbol öffnen. Die Datei wird direkt im Update-Modus geprüft, und es erscheint der Button **«Als Update einspielen»**.

Weil der *Update*-Reiter die Datei ausschliesslich als Update prüft, braucht eine reine Update-Tabelle (nur `id` + zu ändernde Spalten, ohne `parent`) keine Umwege: die beim Neuanlegen nötige `parent`-Spalte wird hier nicht verlangt. Der reguläre *Metadaten*-Reiter bleibt unverändert fürs Neuanlegen.

Ein Update überschreibt die Felder der bestehenden Datensätze «an Ort und Stelle» — es werden dabei **keine neuen Datensätze angelegt**. Damit ein Update sicher und vorhersehbar bleibt, gelten drei Voraussetzungen. Ist eine davon verletzt, wird die Datei blockiert und der Grund auf der Inspektionsseite angezeigt:

1. **Jede Zeile nennt ihren Datensatz mit `id` oder `uuid`.** Die `id` einer Verzeichnungseinheit ist aus dem `permalink` ersichtlich; die Update-Tabelle aus der Trefferliste bringt beide mit.
2. **Keine `parent`- (oder `parent_id`-) Spalte.** Ein Update darf Datensätze nicht verschieben. Um die Hierarchie zu ändern, die Datensätze regulär in Anton umhängen.
3. **Keine Ereignis-Spalten (Antonevents).** Spalten wie `creation_actors`, `creation_date_start` usw. sind im Update nicht erlaubt, damit keine doppelten Ereignisse entstehen. Akteur:innen-/Orts-Verknüpfungen in Anton pflegen.

Was ein Update schreibt:

- **Nur befüllte Felder werden überschrieben.** Leere Zellen lassen den bestehenden Wert unangetastet — es ist also möglich, gezielt nur einzelne Spalten (z.B. nur `titel` oder nur `schutzfrist`) zu aktualisieren.
- **Schlagworte, Akteur:innen, Orte, Sprachen und Textfelder werden ersetzt.** Eine befüllte Zelle ist die *vollständige neue Liste*: Wer einen Eintrag aus der Zelle löscht, löst damit auch die Verknüpfung am Datensatz. Eine leere Zelle ändert nichts. (Beim normalen Import — also beim Neuanlegen — werden Schlagworte weiterhin nur ergänzt.)
- **Medien** werden weiterhin ergänzt.

Dieselbe Datei darf mehrfach als Update eingespielt werden; die sonst geltende Duplikat-Sperre (gleiche Datei = gleiche MD5-Prüfsumme) greift für Updates nicht, da ein Update wiederholbar ist.

Nach dem Start zeigt die Fortschritts-Seite das Update als **«Datenupdate»** an (nicht als Import) und meldet am Schluss, wie viele Datensätze *aktualisiert* wurden.

**Automatische Sicherung.** Bevor ein Update auch nur eine Zeile schreibt, legt Anton einen Dump der Datenbank an (dieselbe Sicherung wie `anton:backup`, abgelegt unter `db_backup/`). Der Schritt erscheint in der Fortschritts-Anzeige als Phase *backup*; der Dateiname des Dumps steht am Lauf. Lässt sich die Sicherung nicht anlegen, **bricht das Update ab** und es wird nichts geändert. Die Sicherung wird auch dann erzwungen, wenn für den Mandanten sonst `no-backup` gesetzt ist — diese Option ist für schnelle Massen-*Neuanlagen* gedacht, wo ein Rückweg trivial ist.

Jeder Update-Lauf steht — wie ein Import — im Importprotokoll, aber mit einer **eigenen Signatur-Serie `UPDATE-{jjjj}-{NNN}`** statt `IMPORT-{jjjj}-{NNN}`. Ein Update ist keine Akzession — es kommt nichts Neues ins Archiv —, und die eigene Serie macht auf einen Blick sichtbar, welche Einträge Updates sind. Der Zähler läuft unabhängig von der Import-Serie und wird pro Kalenderjahr zurückgesetzt.

### Passende Tabelle herunterladen

Damit ein Update nicht von Hand zusammengestellt werden muss, lässt sich die aktuelle **Trefferliste direkt als Update-Tabelle herunterladen**: in der Objektliste rechts oben das Excel-Symbol neben der Druckansicht. Der Download übernimmt genau die Filter, die gerade angezeigt werden.

Die Datei enthält ausschliesslich Spalten, die ein Update auch schreiben darf — `id`, die Feld-Spalten, Sprachen, den Standort (`location_id`), Schlagworte/Akteur:innen/Orte (als IDs) und die Textfeld-Spalten `note.*`. Bewusst **nicht** enthalten sind `parent` und die Ereignis-Spalten, die würden das Update blockieren. Die Spalte `identifier` dient der Orientierung: das Update findet die Datensätze über die `id`. Sie muss eine bestehende Signatur enthalten; eine geänderte Signatur lehnt die Prüfung ab, ändern lässt sich die Signatur über das Update nicht.

!!! tip "Mehrsprachige Archive: eine Titel-Spalte je Sprache"
    Führt das Archiv mehrere Inhaltssprachen, enthält die Update-Tabelle statt `titel` je eine Spalte `title_de`, `title_fr` usw. Nur so ist der Weg hinaus und wieder hinein verlustfrei: Mit einer einzigen Titel-Spalte müsste beim Einspielen die Sprache des Laufs entscheiden, wohin der Wert zurückgeht — und ein französischer Titel landete im deutschen Feld.

    Einsprachige Archive behalten die gewohnte Spalte `titel`; dort gibt es nichts zu unterscheiden. Ältere Tabellen mit `titel` bleiben in jedem Fall einspielbar.

!!! tip "Standorte ändern"
    Für den Standort gibt es **zwei Spalten**, und der Name sagt jeweils, was hineingehört:

    | Spalte | Inhalt |
    |---|---|
    | `location_id` | **nur die ID** des Standorts (steht unter *Admin → Standorte*) |
    | `location` | ID **oder** Bezeichnung |

    Die heruntergeladene Update-Tabelle nutzt `location_id`. Wer lieber mit Bezeichnungen arbeitet, benennt die Spalte in `location` um; dort werden beide Formen akzeptiert. Eine Bezeichnung muss exakt so geschrieben sein wie in der Standort-Verwaltung, inklusive Gross- und Kleinschreibung — die ID ist deshalb der sichere Weg.

    Eine **leere Zelle lässt den Standort unverändert** — zum Umräumen also nur die Zeilen ändern, die wirklich umziehen. Ein Standort, den es noch nicht gibt, muss vorher unter *Admin → Standorte* angelegt werden; sonst meldet die Inspektion ihn als unbekannt und das Update läuft nicht.

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

!!! note "Über die `id` oder die `uuid`"
    Das Update im Browser findet die Datensätze über die interne `id` oder, wenn die Tabelle keine `id`-Spalte hat, über die `uuid`, nie über die Signatur. Eine Zeile mit einer unbekannten `id` oder `uuid` oder mit zwei Angaben, die verschiedene Datensätze nennen, wird abgewiesen; ein Update legt nichts an. Dateien, die der Datensatz schon trägt, werden nicht noch einmal angehängt; dieselbe Tabelle lässt sich also wiederholen. Ein Update über die Signatur ist nur über die Kommandozeile möglich (`--update --default-excel-column=identifier`, siehe unten).

## Import über die Kommandozeile


### Einfacher Import

Für den Customer (slug) "besenval" und das Excelfile "test.xlsx" lautet der Import Befehl:

```bash
php artisan anton:import test.xlsx --env=besenval --import
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
|--default-excel-column=   |`id` (Standard), `uuid` oder `identifier` — bestimmt beim `--update`, worüber die Datensätze gefunden werden|
|--no-validation           |do not validate the file|
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
|--from-ead                |import file is an EAD 2002 or EAD3 file (use with --parent)|
|--parent=                  |the record the fonds goes under (id, UUID or signature)|
|--no-ead-validation        |do not check the EAD file against its schema before the import|
|--show-ead                 |show the rows the EAD file makes|
|--no-ead-import            |check and show only, import nothing|

Beispiel
```bash
php artisan anton:import test_2-ead.xml --from-ead --create-actors --create-places --create-keywords --parent=1 --env=kr --import
```

Die Datei liegt wie eine Excel-Tabelle in `metadata_to_import`. Gelesen wird,
was Antons EAD-2002- und EAD3-Export schreiben: alle ISAD(G)-Textfelder (als
Markdown), Zugangspunkte als Schlagwörter, Akteur:innen und Orte, Sprachen,
Datierung, Umfang, Titel in weiteren Sprachen. Wer unter derselben
GND-Nummer schon im Archiv steht, wird übernommen statt neu angelegt.
Vor dem Import wird die Datei gegen ihr Schema geprüft; eine ungültige Datei
importiert nichts. `anton:import-ead <datei>` prüft eine Datei und zeigt ihre
Zeilen, ohne zu importieren.

## Signaturen abgleichen {#signaturenabgleich}

Unter **Admin → Import / Export → Signaturenabgleich** lässt sich eine Liste von Signaturen mit dem Bestand vergleichen: einfügen oder eine Tabelle hochladen (CSV, Excel, ODS, gelesen wird die erste Spalte), höchstens 50 000 Signaturen. Das Ergebnis steht auf der Seite oder kommt als CSV zum Herunterladen. Was Sie nicht sehen dürfen, gilt als nicht gefunden.
