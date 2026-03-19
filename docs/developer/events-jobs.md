# AntonObject: Events, Jobs & Listeners

## 1. Event → Listener → Job Kette

| Event | Listener | Queue? | Dispatched Jobs |
|-------|----------|--------|-----------------|
| `ObjectMoved` | `ObjectSetPath` | **async** (`ShouldQueue`) | `UpdatePaths` |
| `ObjectChanged` | `ObjectUpdateParents` | **sync** | `UpdateDates` + `RefreshFulltext` |
| `MediumAdded` | `MediumIdentifyAndConvert` | **async** (`ShouldQueue`) | Format-Identifikation, Cloud-Copy, Conversions, `RefreshFulltext` |
| `ImportFinished` | `ImportFinished` | **sync** | Kette: `UpdatePaths` → `ProcessMediaFiles` → `ProcessMediaIdentificationBatch` → `UpdateDates` → `RefreshFulltext` |
| `LoanedObject` | `ObjectUpdatesLoansOnDescendants` | **async** (`ShouldQueue`) | `UpdateLoans` |

## 2. Operationen auf AntonObject → Was passiert?

| Operation | Model-Hook | Events (wenn `$suppressDomainEvents = false`) | Zusätzliche Aktionen |
|-----------|-----------|-----------------------------------------------|---------------------|
| **create** (Einzelobjekt) | `saving` → `created` | `ObjectMoved` → `UpdatePaths` | `fonds_id` setzen |
| | | `ObjectChanged` → `UpdateDates` + `RefreshFulltext` | Cache flush, `updateHasChildren` auf Parent |
| **create_bulk** | `saving` → `created` (pro Objekt) | **unterdrückt** (`$suppressDomainEvents = true`) | Nach Schleife 1× manuell: `UpdatePaths`, `UpdateDates`, `RefreshFulltext` |
| **update** | `updating` → `updated` | `ObjectChanged` → `UpdateDates` + `RefreshFulltext` | `version++`, `real_depth`, `uuid` |
| **update** (mit dirty `private`) | `updating` | — | `UpdateDescendantsPrivate` → alle Nachkommen + Fulltext |
| **update** (mit dirty `release_year`) | `updating` | — | `UpdateDescendantsReleaseDate` → alle Nachkommen |
| **update** (mit dirty `status_of_description_id` auf Fonds) | `updating` | — | `UpdateDescendantsStatusOfDescription` → alle Nachkommen |
| **move** (behind/infrontof/into) | `saving` → `saved` (intern) | **unterdrückt** während Move; danach 1× `ObjectMoved` → `UpdatePaths` | `reorderChildren`, `updateHasChildren`, ggf. Move-Protokoll (wenn `setting('record_move_events')`) |
| **delete** (moveToTrash) | `deleting` → `deleted` | — | Notes löschen, Kinder rekursiv in Papierkorb, Cache flush |
| **addAntonMedium** | — | `MediumAdded` → Format-ID, Conversions, `RefreshFulltext` | Nur wenn `$fire_medium_added_event = true` |

## 3. Jobs im Detail

| Job | Timeout | Retries | Was macht er? |
|-----|---------|---------|---------------|
| `UpdatePaths` | 3600s | — | Aktualisiert das `path[]`-Attribut für Objekte und ihre Nachkommen |
| `UpdateDates` | 7200s | 3× (60s Backoff) | Aggregiert Entstehungsdaten (`artisan anton:update-dates`) |
| `RefreshFulltext` | 14400s | 3× (60s Backoff) | Extrahiert PDF-Text, aktualisiert MySQL-Fulltext-Index (`artisan anton:update-fulltext`). ≤ 50 IDs: in-process `Artisan::call()`. > 50 IDs oder ganze DB: externer PHP-Prozess (Memory-Isolation). |
| `UpdateDescendantsPrivate` | — | — | Setzt `private` auf allen Nachkommen + Fulltext-Update in 1000er-Chunks |
| `UpdateDescendantsStatusOfDescription` | — | — | Setzt `status_of_description_id` auf allen Nachkommen |
| `UpdateDescendantsReleaseDate` | — | — | Aktualisiert `release_year` / `release_year_calculated` auf Nachkommen |
| `UpdateLoans` | — | — | Aktualisiert Ausleih-Status auf Nachkommen |

## 4. `$suppressDomainEvents`

`AntonObject::$suppressDomainEvents` ist ein statisches Flag, das die `ObjectMoved`- und `ObjectChanged`-Events unterdrückt, während Infrastruktur-Events (ClosureTable `insertNode`, `reorderSiblings`) weiterhin feuern. Wird verwendet in:

- **`create_bulk()`** — Events unterdrücken während der Schleife, danach 1× `UpdatePaths`, `UpdateDates`, `RefreshFulltext` für alle IDs
- **`move()`** — Events unterdrücken während der Move-Operation, danach 1× `ObjectMoved`

## 5. Performance-Hinweis: Sync-Queue

Mit `QUEUE_DRIVER=sync` laufen **alle** Jobs synchron. Das bedeutet:

- **Ein einzelnes `create`** feuert `ObjectMoved` + `ObjectChanged` → löst synchron `UpdatePaths` + `UpdateDates` + `RefreshFulltext` aus — **3 schwere Prozesse pro Objekt**
- **`create_bulk`** unterdrückt das und macht es **1× am Ende** für alle IDs
- **`move`** unterdrückt Events während der Operation, feuert `ObjectMoved` **1× am Ende** (kein `ObjectChanged`, daher kein `UpdateDates`/`RefreshFulltext` beim Move)

## 6. Relevante Dateien

| Datei | Beschreibung |
|-------|-------------|
| `app/Models/AntonObject.php` | Model-Events (`booted()`), `move()`, `$suppressDomainEvents` |
| `app/Events/ObjectMoved.php` | Event-Klasse für Verschiebungen |
| `app/Events/ObjectChanged.php` | Event-Klasse für Änderungen (inkl. Create) |
| `app/Events/MediumAdded.php` | Event-Klasse für neue Medien |
| `app/Events/ImportFinished.php` | Event-Klasse für abgeschlossene Importe |
| `app/Listeners/ObjectSetPath.php` | Listener: `ObjectMoved` → `UpdatePaths` |
| `app/Listeners/ObjectUpdateParents.php` | Listener: `ObjectChanged` → `UpdateDates` + `RefreshFulltext` |
| `app/Listeners/MediumIdentifyAndConvert.php` | Listener: `MediumAdded` → Identifikation, Conversions |
| `app/Listeners/ImportFinished.php` | Listener: `ImportFinished` → Job-Kette |
| `app/Jobs/UpdatePaths.php` | Job: Pfade aktualisieren |
| `app/Jobs/UpdateDates.php` | Job: Daten aggregieren |
| `app/Jobs/RefreshFulltext.php` | Job: Fulltext-Index aktualisieren |
| `app/Providers/EventServiceProvider.php` | Event-Listener-Mapping |
| `app/Http/Controllers/ObjectsController.php` | `create_bulk()` mit Event-Unterdrückung |

## 7. Derived Attributes Pipeline (Doctor)

Die Pipeline im Doctor-Dashboard repariert abgeleitete Felder in strikter Abhängigkeitsreihenfolge. Jeder Step hängt von den vorherigen ab.

### Reparatur-Reihenfolge

| Step | Feld(er) | Artisan Command | Beschreibung |
|------|----------|-----------------|--------------|
| 1 | `object_closure` | `anton:repair-closure-table` | ClosureTable: Parent-Child-Beziehungen |
| 2 | `path`, `fonds_id` | `anton:update-path` | Pfad-Arrays und Fonds-Zuordnung |
| 3 | `real_depth` | `anton:update-path --real-depth` | Tatsächliche Tiefe im Baum |
| 4 | `has_children` | `anton:update-has_children` | Flag: Objekt hat Kinder |
| 5 | `release_year_calculated` | `anton:update-release-year` | Kaskadiert release_year top-down |
| 6 | `object_creation_min/max` | `anton:update-all-dates` | Aggregiert Entstehungsdaten bottom-up |
| 7 | `full_text`, `full_text_intern` | `anton:update-fulltext` | MySQL-Fulltext-Index |

### Jobs

| Job | Beschreibung |
|-----|--------------|
| `RepairAllDerivedAttributes` | Führt alle 7 Steps in der richtigen Reihenfolge aus. Wird über Doctor "Repair All" oder direkt dispatched. |

### PipelineStepLog

`Anton\Helpers\PipelineStepLog` protokolliert pro Step wann zuletzt ausgeführt (`last_run`) und wann zuletzt fehlerfrei (`last_ok`). Gespeichert als JSON in `storage/app/logs/pipeline_steps.json`.

### Dateien

| Datei | Beschreibung |
|-------|--------------|
| `app/Jobs/RepairAllDerivedAttributes.php` | Job: alle 7 Reparatur-Schritte in Reihenfolge |
| `app/Helpers/PipelineStepLog.php` | JSON-Log für Pipeline-Step-History |
| `app/Console/Commands/AntonUpdateReleaseYear.php` | Command: release_year kaskadieren |
| `app/Http/Controllers/Help/AntonDoctorController.php` | Doctor-Controller mit Pipeline-Checks und Repairs |
| `resources/views/doctor/tabs/pipeline.blade.php` | Pipeline-View mit Status, Details, Log-Daten |
| `resources/views/doctor/tabs/manual.blade.php` | Manuelle Reparaturen (Nested Fonds, Positions) |
