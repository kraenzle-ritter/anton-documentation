## Import

## Zusammenfassung

Es ist möglich, Daten und dazugehörige Dateien (media) in Anton zu importieren. Die Erschliessungsdaten (Excel-File) werden in einem (vorgegeben) Excelsheet erfasst und mit den Dateien auf den Server geladen. Danach werden die Daten validiert und falls die Validierung erfolgreich war, kann der Import/Ingest erfolgen (Erschliessungsdaten und media).

## Ablauf

Zunächst ist ein Excel-File nach den folgenden Massgaben zu erstellen. Dieses ist unter "Upload Metadata" hochzuladen und dazugehörige Mediendateien sind unter "Upload Medien" hochzuladen. Abschliessend kann das Excel-File unter "Validation" überprüft werden. Die Validierung zeigt Fehler an und gibt Warnugen aus. Importieren kann man die Daten erst, wenn die Validierung fehlerfrei ist. Der Import wird unter "Ingest" ausgelöst und kann je nach Umfang einige Minuten dauern.

!!! note "Wichtig"

    Vor jedem Import wird ein Backup der Datenbank erstellt.


## Spalten

Das File darf zusätzliche Spalten enthalten; diese werden jedoch nicht importiert. Zur Vereinfachung dürfen Spalten gelöscht werden. Das endgültige File muss folgende Spalten enthalten:

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

!!! Bug "Achtung"
    Der Import mehrsprachiger Titel ist zurzeit nicht möglich.

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

Das Feld kann mehrere Sprachen enthalten. Die Sprachen mmüssen exakt wie in der vorgegebenen Liste geschrieben sein. Mehrere Sprachen werden können mit folgenden Zeichen getrennt (Komma und Strichpunkt sind nicht möglich):

```
    ::
```

### standort (location)

Das Feld muss einen bereits verwendeten Standort enthalten. Wenn ein neuer Standort verwendet werden soll, erst in Admin-Standorte hinzufügen.

### vacat

Das Feld darf nur 0 (nein) oder 1 (ja) enthalten. Enthält vacat keinen Wert, wird 0 gesetzt.

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

## Import über die Kommandozeile


### Einfacher Import

Für den Customer (slug) "besenval" und das Excelfile "test.xlsx" lautet der Import Befehl:

.. code:: bash

    php artisan anton:import --env=besenval --file="test.xlsx" --import

Dabei wird davon ausgegangen, dass `test.xlsx` im Ordner `custumers/besenval/metadata_to_import/` liegt. Mit zu importierende Dateien (Medien) müssen sich im Ornder `customers/besenval/assets_to_import/` befinden.

Ohne die Option `--import` wird das file nur validiert.

### Optionen

Der Befehl `anton:import` bietet einige Optionen, die für spezifische Situationen nützlich sein können.

| Option|Beschreibung|
|:---   | :----------|
|--no-backup | dont backup the database before import |
|--import                  |really start import|
|--update                  |only update antonobjects (identifier is required)|
|--dont-validate           |do not validate the file|
|--skip-parent-validation  |to build hierarchies with one excel file|
|--create-actors           |create new actors if they dont exist|
|--create-keywords         |create new keywords if they dont exist|
|--create-places           |create new places if they dont exist|
|--show-rules              |showe rules for this file|
|--show-columns            |showe the original columns of this file|
|--show-column-mapping     |show columns with mapping|
|--show-possible-columns   |show all pssible column names|
|--show-mapping            |show mapping for this file|
|--show-separators         |show separators|
