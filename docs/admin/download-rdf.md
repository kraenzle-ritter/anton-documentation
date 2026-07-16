# RDF-Export (CIDOC CRM, RiC-O, Memobase)

Anton exportiert Bestände als RDF in **drei Profilen** — Anton ist das
einzige Archivdatenbank-System in der Schweiz, das alle drei standard­
konform liefert:

- **A+-Profil** — CIDOC CRM 7.1.x als Leitmodell, RiC-O 1.1 selektiv
  mit-annotiert (für die breite Linked-Data-Welt, Wikidata, Europeana etc.)
- **Pure-RiC-O-Profil** — reines RiC-O 1.1, standardkonform, ohne CRM
  (für RiC-O-only-Konsumenten wie SPA / Swiss Archival Portal, künftige
  ICA-Portale)
- **Memobase-Profil** — JSON-LD-Form gemäss `https://api.memobase.ch/context/*`
  (für die Lieferung an Memobase via Memoriav-Konvention §9)

Verfügbar seit **v0.71.0**.

## Drei Profile im Überblick

| Profil | Leitmodell | Format | Zweck |
|---|---|---|---|
| **A+** (Standard) | CIDOC CRM 7.1.x + RiC-O 1.1 selektiv | Turtle (Default), JSON-LD, RDF/XML, N-Triples | LOD-Veröffentlichung, breite Konsumenten (Wikidata, Europeana, GND-Aggregatoren) |
| **RiC-O (pur)** | Reines RiC-O 1.1, Standard-Namespace | JSON-LD (Default), Turtle, RDF/XML, N-Triples | RiC-O-only-Konsumenten (SPA, ICA-Portale, RDA-konforme Archive) |
| **Memobase** | RiC-O 1.1 mit Memobase-`@context` | JSON-LD (Default), Turtle (Debug) | Lieferung an Memobase / Memoriav |

Alle drei Profile sprechen über dieselben Anton-Daten und dieselbe Bestands­hierarchie;
sie unterscheiden sich nur in der Wahl der RDF-Properties, im IRI-Schema und im
JSON-LD-Context.

## Zugriff

### 1. UI — `/export/rdf`

Im Menü **Daten-Export → RDF**. Drei Spalten nebeneinander
(reduziert sich responsive auf eine Spalte unter dem `md`-Breakpoint):

- **A+ (CIDOC CRM + RiC-O)** — Drop-down mit Wurzel-Objekt
  (Collection / Recordgroup / Fonds), Knopf `Erstelle RDF` produziert
  asynchron eine Turtle-Datei in `storage/rdf/<identifier>-cidoc.ttl`.
- **RiC-O (pur)** — gleiches Drop-down, Knopf `Erstelle RiC-O RDF`
  produziert JSON-LD in `storage/rdf/<identifier>-ric.jsonld`.
- **Memobase** — gleiches Drop-down, Knopf `Erstelle Memobase RDF`
  produziert JSON-LD in `storage/rdf/<identifier>-memobase.jsonld`.

Die generierten Dateien erscheinen in der FileTable darunter und lassen
sich direkt herunterladen oder löschen.

### 2. API — `/api/v1/objects/{id}?format=…`

On-demand, ohne Datei-Caching. Authentifizierung via api_token wie bei
allen anderen Anton-API-Calls.

```bash
# A+ (default Turtle)
curl "https://archiv.example/api/objects/42?api_token=TOKEN&format=cidoc-crm"

# A+ als JSON-LD
curl "https://archiv.example/api/objects/42?api_token=TOKEN&format=cidoc-crm&serialization=jsonld"

# A+ als RDF/XML oder N-Triples
curl "...&format=cidoc-crm&serialization=rdfxml"
curl "...&format=cidoc-crm&serialization=ntriples"

# Memobase (default JSON-LD)
curl "...&format=memobase"

# Memobase als Turtle (Debug)
curl "...&format=memobase&serialization=turtle"

# Pure RiC-O (default JSON-LD)
curl "...&format=ric"

# Pure RiC-O als Turtle / RDF-XML / N-Triples
curl "...&format=ric&serialization=turtle"
curl "...&format=ric&serialization=rdfxml"
curl "...&format=ric&serialization=ntriples"
```

Akzeptierte `format`-Werte für das A+-Profil: `cidoc-crm`, `cidoc`, `rdf`
(Aliase). Für das RiC-O-Profil: `ric`, `rico` (Aliase). Akzeptierte
`serialization`-Werte pro Profil:

| Profil | turtle | jsonld | rdfxml | ntriples |
|---|---|---|---|---|
| `cidoc-crm` | ✓ (Default) | ✓ | ✓ | ✓ |
| `ric` | ✓ | ✓ (Default) | ✓ | ✓ |
| `memobase` | ✓ (Debug) | ✓ (Default) | ✗ HTTP 400 | ✗ HTTP 400 |

### 3. CLI — `anton:export-rdf`

```bash
# Ganzer Tenant, A+, Turtle, auf stdout
php artisan anton:export-rdf --env=kr > kr.ttl

# Ein Teilbaum (z.B. Fonds mit id 42)
php artisan anton:export-rdf --env=kr --root=42 > fonds_42.ttl

# Memobase-Profil
php artisan anton:export-rdf --env=gf --root=1 --profile=memobase --format=jsonld > gf.jsonld

# Pure RiC-O
php artisan anton:export-rdf --env=kr --root=1 --profile=ric --format=jsonld > kr-ric.jsonld

# JSON-LD vom A+-Profil
php artisan anton:export-rdf --env=kr --format=jsonld > kr.jsonld
```

Optionen:

| Option | Default | Bedeutung |
|---|---|---|
| `--root=<id>` | leer | Beschränkt den Export auf den Closure-Table-Teilbaum unter dem AntonObject mit dieser ID. Ohne `--root=` werden alle Root-Objekte exportiert. |
| `--format=<wert>` | `turtle` (a-plus), `jsonld` (memobase + ric) | Serialisierung |
| `--profile=<wert>` | `a-plus` | `a-plus`, `memobase` oder `ric` (alias `rico`) |

## Was im A+-Profil drinsteht

CRM trägt das volle Detail, RiC-O die wichtigsten Klassen + Skelett.
Stichworte:

- **AntonObject** → `crm:E73_Information_Object` (`E22` für physische Objekte,
  `E33`/`E36`/`E31` je nach `object_type`) + `rico:RecordSet`/`Record`
  je nach Verzeichnungsstufe.
- **Hierarchie** → `crm:P46`/`P46i` + `rico:isOrWasIncludedIn`.
- **AntonEvent** → 17 verifizierte Eventtypen (creation, acquisition,
  reception, digitisation, …) auf die passenden CRM-Klassen (`E12_Production`,
  `E8_Acquisition`, `E10_Transfer_of_Custody`, …) plus Anton-Term redundant
  als `crm:P2_has_type`.
- **Notes** typisiert als `crm:E33_Linguistic_Object` UND zusätzlich als
  matching `rico:scopeAndContent`/`rico:history`/`rico:conditionsOfAccess`
  etc. auf der Entität (A+-„Loss-#2-Fix").
- **Authority-Links** (GND/VIAF/Wikidata/GeoNames) → `owl:sameAs` /
  `skos:exactMatch` auf die externe URI.
- **Privates wird gefiltert**: `objects.private`, `media.private_media`,
  `actors.private` plus private Note-Types (`internal_note`,
  `archivists_notes`, `comment`).

Vollständige Spec: <https://github.com/kraenzle-ritter/anton-cidoc>.

## Was im RiC-O-(pur)-Profil drinsteht

Reines RiC-O 1.1, kein CIDOC CRM, keine Memobase-Aliase. Standard
`rico:`-Namespace, Multilinguale Literale als `@language`-getagte
Werte (de/fr/it/en/rm — alle Locales bleiben erhalten).

- **AntonObject** → `rico:Record` (Items) bzw. `rico:RecordSet` (alle
  anderen Stufen).
- **Title** als eigenes Node via `rico:hasOrHadTitle` → `rico:Title`
  mit `rico:title` (multilingual).
- **Identifier** als eigenes Node via `rico:hasOrHadIdentifier` → `rico:Identifier`
  (zwei Nodes wenn `identifier_old` gesetzt).
- **Hierarchie** via `rico:isOrWasIncludedIn`.
- **AntonEvent** → eigenständiges `rico:Activity`-Node mit
  `rico:hasActivityType` (Term-URI), `rico:hasParticipant` (Record),
  `rico:hasOrHadAgent` (Person), `rico:hasOrHadLocation` (Place),
  `rico:hasBeginningDate`/`hasEndDate` → eigene `rico:Date`-Nodes
  mit `rico:expressedDate` (Text) + `rico:normalizedDateValue`
  (typed `xsd:date`/`gYear`).
- **Actor** → `rico:Person`/`Family`/`CorporateBody` mit
  `rico:hasOrHadName` → eigene `rico:Name`-Nodes für Hauptname +
  Varianten + Alternativnamen.
- **Place** → `rico:Place` mit `rico:hasOrHadName` und
  `rico:hasOrHadLocation` → Blank-Node mit `geo:asWKT` (lon/lat-
  korrigiert).
- **Keywords** als `rico:Concept` + `skos:Concept`, referenziert
  via `rico:hasOrHadSubject`.
- **Media** als `rico:Instantiation` mit `ebucore:hasMimeType`/
  `hasHash`/`size` immer, plus AV-EBUcore-Properties wenn die
  `av_*`-Spalten gefüllt sind.
- **IRI-Schema**: `https://<tenant>.anton.ch/id/<entity-type>/<tenant-slug>-<id>`
  (überschreibbar via `setting('ric_base_iri')` pro Mandant oder
  `config('exporter_rdf.ric.base_iri')` global).
- **Authority-Links** als `schema:sameAs` auf GND/VIAF/Wikidata/GeoNames.

Der Hauptunterschied zum A+-Profil: A+ schreibt die "RiC-O-Skelett"-
Beziehungen (`isOrWasIncludedIn`, `hasCreator`) zusätzlich neben dem
CRM-Detail; pure RiC-O liefert echte `rico:Activity`-Nodes mit allen
Rollen — ein RiC-O-only-Konsument sieht damit die Events vollständig.

## Was im Memobase-Profil drinsteht

Schlanker und Memobase-spezifisch:

- Klassen-Trio **Institution / RecordSet / Record** (Anton-Tenant ↦
  Institution, Anton-Objekt-Level `item` ↦ Record, alles andere ↦
  RecordSet).
- IRI-Schema `https://memobase.ch/(institution|recordSet|record|digital)/<inst-slug>-<id>`
  (konfigurierbar via `memobase_slug`-Setting; Fallback ist der Tenant-Slug).
- **Sprach-suffigierte Property-Aliase** statt `@language`-Tags:
  `titleDe`/`titleFr`/`titleIt`, `scopeAndContentDe`,
  `conditionsOfAccessFr` etc. **Nur Deutsch/Französisch/Italienisch** —
  Englisch und Rätoromanisch werden gedroppt (englisch-only-Werte landen
  als Fallback unter dem nackten Alias-Namen).
- **Memoriav-Sponsoring-Hinweis** `rdau:P60451 → https://www.memoriav.ch/`
  auf jedem RecordSet und Record, sobald
  `setting('memobase_sponsoring_memoriav')` auf `1` gesetzt ist
  (Memoriav-Konvention §9).
- **EBUcore für AV-Material**: `ebucore:hasMimeType`, `ebucore:hasHash`,
  `ebucore:size` immer. Wenn die `av_*`-Spalten in der `media`-Tabelle
  befüllt sind (siehe unten), zusätzlich `ebucore:duration`,
  `ebucore:hasCodec`, `ebucore:bitRate`, `ebucore:videoTrack`,
  `ebucore:samplingRate`, `ebucore:aspectRatio`.

Der JSON-LD-Context ist als Snapshot eingefroren — Memobase könnte ihn
serverseitig ändern, wir merken das durch ein deliberatives Audit, nicht
zur Export-Laufzeit.

## Per-Tenant-Settings für Memobase

| Setting | Pflicht? | Bedeutung |
|---|---|---|
| `repository_name` | ✓ | Institutionsname (wird zu `nameDe`) |
| `repository_isil` | empfohlen | ISIL-Code (`wdt:P791` am Institution-Node) |
| `repository_email` | empfohlen | Kontakt-Email (`wdt:P968`) |
| `repository_url` | empfohlen | Offizielle Website (`wdt:P856`) |
| `memobase_slug` | optional | Memobase-Slug im IRI (Default: Tenant-Slug) |
| `memobase_sponsoring_memoriav` | für Memoriav-Kunden | `1` aktiviert den Sponsor-Hinweis auf jedem Record |

Alle Settings werden über `/settings` oder per Tinker (`setting('key', 'value')`) gepflegt.

## AV-Metadaten

Anton hat seit v0.71.0 sechs neue Spalten in `media`:
`av_duration_seconds`, `av_codec`, `av_bitrate`, `av_resolution`,
`av_sample_rate`, `av_aspect_ratio`.

Sie werden automatisch befüllt:

- **Bei neuem Upload**: Listener `MediumIdentifyAndConvert` ruft direkt
  nach der PRONOM-Identifikation `media:extract-av-metadata` für das
  einzelne neue Medium auf. Inline, ~50ms, blockiert nichts; bei
  ffprobe-Fehler nur Warn-Log.
- **Bei Bestandsdaten**: einmaliger Backfill-Lauf via
  `php artisan media:extract-av-metadata --env=<slug>` (siehe
  [Console Commands](console-commands.md#mediaextract-av-metadata)).

Bei Bildern (`image/*`) wird nur `av_resolution` aus Breite × Höhe
befüllt — kein Codec, keine Dauer. Das reicht damit der Memobase-Export
das `ebucore:videoTrack`-Element mit `width`/`height` für jedes Foto
emittieren kann.

Im Frontend (Objekt-Detail-Ansicht, Media-Tab) erscheint pro Medium eine
kleine Zeile mit den vorhandenen Werten — `1:08`, `1246x1020 (623:510)`,
`h264`, `903 kbps`, … — sofern befüllt.

## Per-Objekt-Buttons in der Detail-Ansicht

Zusätzlich zum `/export/rdf`-Tab (Job-basiert, asynchron) kann jedes
Objekt in der Detail-Ansicht synchron-downloadbar gemacht werden über
das **Download-Modul** (Antonfield id 1105, seit v0.71.0 von
`word_download` umbenannt). Das Modul rendert bis zu **acht Buttons**
in der internen Detail-Ansicht — welche erscheinen, steuert pro Format
ein eigenes Setting:

| Button | Setting | Inhalt |
|---|---|---|
| WORD | `level_of_description_ids_for_word_download` | Word-Findbuch via `WordController` |
| DIP | `level_of_description_ids_for_dip_download` | OAIS-DIP-Paket (BagIt-ZIP) |
| OCFL | `level_of_description_ids_for_ocfl_download` | OCFL-Objekt (ZIP) |
| OCFL (Bestand) | `level_of_description_ids_for_ocfl_subtree_download` | OCFL-Storage-Root |
| **EAD** | `level_of_description_ids_for_ead_download` | EAD-XML für dieses Objekt |
| **CIDOC CRM** | `level_of_description_ids_for_cidoc_download` | A+ Turtle für diesen Subtree |
| **RiC-O** | `level_of_description_ids_for_ric_download` | Pure RiC-O JSON-LD |
| **Memobase** | `level_of_description_ids_for_memobase_download` | Memobase-JSON-LD |

Jedes Setting ist eine Liste von `level_of_description_id`-Werten. Default
ist überall `[]` — bei einer frischen Installation sieht der User **keinen**
neuen Button bis ein Admin via `/settings` (oder Tinker) die LoDs einträgt.

Beispiel: alle vier neuen Buttons auf Fonds/Series/File/Item aktivieren:

```bash
ddev artisan tinker --env=<slug> --execute='
use Ottosmops\Settings\Setting;
foreach (["ead", "cidoc", "ric", "memobase"] as $k) {
    Setting::setValue("level_of_description_ids_for_".$k."_download", [3, 4, 5, 6]);
}
'
```

Die Buttons hängen alle an synchrone Inline-Download-Routes
(`/objects/{id}/download/{format}` mit Format `ead|cidoc-crm|ric|memobase`)
und respektieren die `mayBeShown()`-Privacy-Logik der bestehenden
Detail-Ansicht (private Objekte sind nur für Admins zugänglich).

> **Hinweis zum Rename:** Bis v0.72.0 bleibt eine Backwards-Compat-Klasse
> `WordDownload extends Download` bestehen, damit kundenspezifische
> Form-Konfigurationen, die noch `word_download` referenzieren, weiter
> rendern. Ab v0.73.0 wird der Alias entfernt — Tenants mit
> customer-spezifischen Forms müssen bis dahin auf `download` umgestellt
> haben.

## Was nicht im Export landet

- Volltext (`objects.full_text`) — gehört nicht zu den ISAD-Feldern
- Interne Notizen (Notetypes `internal_note`, `archivists_notes`,
  `comment`) — werden im A+ und im Memobase-Profil gleich gefiltert
- Private Datensätze (`private = 1`) — Subtree-Kinder werden zwar
  exportiert, aber die Hierarchie-Verbindung zum privaten Eltern-Objekt
  fehlt

## Bezugspunkte

- Spec-Repo CIDOC CRM + RiC-O: <https://github.com/kraenzle-ritter/anton-cidoc>
- Memobase-API: <https://api.memobase.ch> (LOD), <https://memobase.ch> (Frontend)
- Memoriav-Konvention §9 zur Erschliessungs-Lieferpflicht — abrufbar via
  den jeweiligen Memoriav-Projekt-Vertrag der Institution
