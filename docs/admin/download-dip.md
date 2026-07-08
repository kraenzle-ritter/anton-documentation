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
    ├── manifest-md5.txt             ← MD5-Prüfsummen aller Dateien
    ├── bagit.txt
    └── bag-info.txt                 ← Repository-Angaben, External-Identifier
```

- Prüfsummen: **MD5** (das BagIt-Default SHA-512 ist bewusst entfernt).
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
CLI-Export nutzt immer `CreateDip` und legt die ZIPs im Zielverzeichnis
ab, statt sie wie der Web-Download nach der Auslieferung zu löschen.

!!! note "Sichtbarkeit"
    Der DIP-Download ist nur für eingeloggte interne Nutzer erreichbar.
    Wie die übrige interne Ansicht enthält ein DIP **auch als privat
    markierte Datensätze** — interne Nutzer sollen diese sehen.
