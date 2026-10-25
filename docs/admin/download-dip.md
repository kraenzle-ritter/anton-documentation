# DIP Download

Ein **DIP** (Dissemination Information Package) ist ein ZIP, das ein
Objekt mit seinem ganzen Teilbaum — alle untergeordneten Datensätze,
deren Mediendateien und begleitende Metadaten — bündelt. Gedacht für die
klassische Übergabe von Akten an Dritte. Für die preservation-orientierte
Ablieferung siehe [OCFL Download](download-ocfl.md).

## Knopf einbauen und sichtbar machen

Der DIP-Knopf gehört ins Download-Modul (`module_word_download`) der
Detail-internal-Form — dasselbe Modul wie Word, OCFL und die
RDF-Exporte. Er erscheint **nur** für Verzeichnungsstufen, die im
Setting stehen:

| Setting | Bedeutung | Beispiel |
|---|---|---|
| `level_of_description_ids_for_dip_download` | Stufen-Ids mit DIP-Knopf | `[3, 4, 5, 6]` |
| `dip_creator_class` | Erzeuger-Klasse (Default `CreateDip`) | `CreateDip` |

Verzeichnungsstufen-Ids: `1` collection, `2` recordgroup, `3` fonds,
`4` class, `5` file (Dossier), `6` item, `700` series.

Beide Settings sind nicht über `/settings` editierbar — sie werden per
Seeder oder Tinker gesetzt:

```php
\Ottosmops\Settings\Setting::setValue('level_of_description_ids_for_dip_download', [3,4,5,6]);
```

Der Knopf wird automatisch unterdrückt, wenn das Objekt im
Akzessionsbereich liegt (`accessions_archives_id` in seinem Pfad).

Ab 500 Medien im Teilbaum (`EXPORT_SYNC_MEDIA`) entsteht das Paket im Hintergrund und erscheint unter [Meine Exporte](../user/my-exports.md), siehe [Grosse Teilbäume](download-rdf.md#grosse-teilbaume).

## Was im Paket steckt (`CreateDip`, Default)

Der Standard erzeugt eine **BagIt-Bag** (ZIP):

```
<full_id>.zip
└── <full_id>/
    ├── data/
    │   ├── content/<Titel>/…        ← Mediendateien, Ordner = Objekt-Titel
    │   └── meta/
    │       ├── <datei>.xml          ← Dublin Core je Medium
    │       └── <full_id>.docx       ← Word-Findbuch (vgl. download-word)
    ├── manifest-sha512.txt          ← SHA-512-Prüfsummen aller Dateien
    ├── manifest-md5.txt             ← MD5-Prüfsummen aller Dateien
    ├── bagit.txt
    └── bag-info.txt                 ← Repository-Angaben, External-Identifier
```

- Prüfsummen: **SHA-512**, wie BagIt empfiehlt, und **MD5** daneben für Empfänger, die nur das prüfen.
- `bag-info.txt` zieht `repository_name`, `repository_address` und
  `repository_email` aus den Settings.
- Dateien sind nach der Signatur benannt, Ordner nach dem Objekt-Titel.

## Vereinfachte Variante (`ZhCreateDip`)

Setzt man `dip_creator_class` auf `ZhCreateDip`, entsteht ein schlankes
ZIP **ohne BagIt, ohne Metadaten**: nur die Ordnerstruktur aus den Titeln
mit den Mediendateien unter ihrem **Originaldateinamen**. Aufgenommen
werden nur Blatt-Objekte (ohne eigene Kinder), die Medien tragen.

Eigene Varianten: Klasse unter `app/Services/Exporter/Dip/` mit
`create(AntonObject $object): string` anlegen und den Klassennamen ins
Setting eintragen.

## Stapel-Export über die Konsole

```bash
php artisan anton:export-dip --env=<slug> --ids=42,77,103 --target-dir=/pfad/zum/ziel
```

`--target-dir` ist optional (Default: Transfer-Verzeichnis). Der
CLI-Export nutzt für das BagIt-DIP immer `CreateDip` und legt die ZIPs im Zielverzeichnis
ab, statt sie wie der Web-Download nach der Auslieferung zu löschen.

!!! note "Sichtbarkeit"
    Der DIP-Download ist nur für eingeloggte interne Nutzer:innen erreichbar.
    Wie die übrige interne Ansicht enthält ein DIP **auch als privat
    markierte Datensätze** — interne Nutzer:innen sollen diese sehen.


## E-ARK DIP

Neben dem BagIt-DIP gibt es ein **E-ARK DIP 2.2.0** nach dem europäischen Standard für Auslieferungspakete (anton#697). Es lässt sich ohne Anton lesen: `METS.xml` beschreibt das Paket, die Repräsentationen liegen unter `representations/`, die Beschreibung unter `metadata/descriptive/`.

### Zwei Umfänge

| | Zugang (Vorgabe) | Vollständig (`--full`) |
|---|---|---|
| Wo | Knopf «E-ARK DIP», Konsole | nur Konsole |
| Datensätze | was ein Gast sieht: ohne gesperrte Datensätze und Entwürfe samt Teilbaum | alle |
| Medien | Nutzungskopien (`web`) in `representations/access/`; ohne private Medien und ohne Medien von Datensätzen mit laufender Schutzfrist (deren Beschreibung bleibt) | Master in `representations/master/`, behaltene Originale in `representations/original/` |
| Beschreibung | EAD3 oder EAD 2002, optional RiC-O und CIDOC CRM | dasselbe, dazu das native Format (`anton-native.json`) |
| PREMIS | Funktion jeder Repräsentation, Format und Herkunft jeder Datei — ohne Ereignisse und ohne Personen | dazu PREMIS je Datensatz mit allen Ereignissen (wie im BagIt-DIP) |
| Word-Findbuch | nein (es filtert nicht) | ja, unter `documentation/` |
| Bestandsprotokoll | «Export ausgeliefert» | «Master heruntergeladen» |

Der Zugangsumfang entsteht immer als öffentliche Sicht, gleich wer ihn herunterlädt. Ein Medium ohne Nutzungskopie fehlt und wird gezählt; `media:conversions` rechnet sie nach. Was fehlt, steht als Anzahl in `documentation/export.txt`, nie mit Titeln.

### Prüfung

Jedes Paket wird nach dem Schreiben gegen E-ARK geprüft (`kraenzle-ritter/eark-ip`). Ein Paket mit Fehlern wird gelöscht und nicht ausgeliefert; die Meldung nennt die verletzten Anforderungen. Warnungen halten es nicht auf.

Wer die Pakete zusätzlich mit commons-ip prüft, dem Java-Validator der E-ARK-Gemeinschaft, bekommt eine Warnung zu CSIP101. Sie ist ein Fehlalarm von commons-ip: Das Paket folgt hier dem Beispiel der Spezifikation und der DILCIS-Testsammlung, und commons-ip meldet dasselbe auch für deren gültiges Beispielpaket (gemeldet als keeps/commons-ip#390).

### Einstellungen

| Setting | Bedeutung | Vorgabe |
|---|---|---|
| `level_of_description_ids_for_eark_dip_download` | Stufen-Ids mit Knopf «E-ARK DIP» | `[]` (kein Knopf) |
| `eark_dip_ead` | `ead3` oder `ead` (EAD 2002) | `ead3` |
| `eark_dip_rdf` | weitere Beschreibungen: `ric`, `cidoc` | leer |
| `eark_dip_sync_limit` | ab wie vielen Medien im Teilbaum das Paket im Hintergrund entsteht | `500` |

Liegt der Teilbaum über `eark_dip_sync_limit`, entsteht das Paket im Hintergrund und erscheint unter **Daten-Export → E-ARK DIP** (`/export/dip`), wo interne Nutzer:innen es herunterladen oder löschen.

### Konsole

```bash
php artisan anton:export-dip --env=<slug> --ids=42 --format=eark --target-dir=/pfad/zum/ziel
php artisan anton:export-dip --env=<slug> --ids=42 --format=eark --full --target-dir=/pfad/zum/ziel
```

Ohne `--format` entsteht wie bisher das BagIt-DIP; `--full` gilt nur mit `--format=eark`. Der vollständige Umfang prüft vorher, ob genug Platz frei ist (etwa die doppelte Grösse der Master).
