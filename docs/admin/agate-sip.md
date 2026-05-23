# agate-SIP-Import

Seit **v0.61.0** kann [agate](https://github.com/kraenzle-ritter/agate)
(das Anton-Vorbereitungs-Tool für SIPs aus losen Datei-Ablagen) BagIt-
Pakete direkt per HTTP an Anton schicken. Anton nimmt das ZIP entgegen,
prüft es, legt ein Backup an, importiert die Inhalte als
Verzeichnungseinheiten unter dem gewählten Bestand und gibt agate
Bescheid wenn alles fertig ist.

Der gesamte Pfad läuft **asynchron** — agate kann parallel
weiterarbeiten oder andere SIPs vorbereiten.

## Workflow

```
┌──────────┐    HTTP-POST     ┌──────────┐
│  agate   │ ───────────────▶ │  Anton   │
│          │   sip.zip        │          │
└──────────┘                  └──────────┘
                                    │
                                    ▼ async Job
                              ┌──────────┐
                              │  Import  │
                              │  BagIt   │
                              │  validate│
                              │  + apply │
                              └──────────┘
```

### Zwei Pfade

1. **Direkt-Import** — Wenn der Filename die Konvention
   `sip-agate-<bestand_id>.zip` einhält, startet der Import sofort
   unter dem angegebenen Bestand.

2. **Eingangskorb** — Sonst landet das SIP im **Eingangskorb** unter
   `/sip/inbox`. Bearbeiter:innen sehen alle wartenden Uploads und
   weisen pro Eintrag manuell einen Bestand zu oder verwerfen das SIP.

Der Eingangskorb verhindert, dass unzugeordnete SIPs den Speicherplatz
still aufessen — Bearbeiter:innen sehen aktiv, was wartet.

## Eingangskorb (`/sip/inbox`)

Sichtbar für Editor- und Admin-Rollen unter **Import / Export → SIP
Inbox**. Pro Zeile:

- SIP-Filename, Hochladedatum
- Vorschau (Anzahl Dateien, BagIt-Validität, NARA-Kategorien)
- Aktionen: **Bestand zuweisen** (öffnet Auswahl) oder **Verwerfen**

## Vokabular-Mapping: NARA → Tenant-Objekttyp

agate spricht intern in NARA-Standard-Kategorien
(StillImage, Audio, Textual, Video, Geospatial …). Anton übersetzt
diese beim Import in die tenant-spezifische Werteliste „Objekttyp"
(Bild, Akte, Foto, Plan, Sammlung …).

Das Mapping ist **pro Tenant konfigurierbar**. Vorteil: agate muss das
spezifische Vokabular des Archivs nicht kennen.

Konfiguration:

```php
Setting::setValue('nara_to_objecttype_map', [
    'StillImage' => 'Bild',
    'Textual'    => 'Akte',
    'Audio'      => 'Tonaufnahme',
    // ...
]);
```

Wenn für eine NARA-Kategorie kein passender Tenant-Typ existiert,
bleibt das `object_type`-Feld leer (statt den Import abzubrechen) und
kann später von Hand vergeben werden.

## HTTP-API

Endpoint: `POST /api/sip/upload`

Request:

- Multipart-Form mit `file`-Feld (`sip.zip` BagIt-Container)
- Header `Authorization: Bearer <api_token>` (Sanctum-Token, siehe
  [API Authentication](authentication.md))

Response: `202 Accepted` mit JSON, das die Job-ID enthält:

```json
{
  "job_id": "01J5XYZ...",
  "status": "queued",
  "callback_url": "https://your-anton.ch/api/sip/status/01J5XYZ..."
}
```

agate pollt anschliessend `callback_url` bis `status: completed` (oder
`failed`).

## Akzessions-Archiv

Wenn der Tenant ein **Akzessions-Archiv** konfiguriert hat
(`setting('accessions_archives_id')`), wird der SIP-Import dort als
neuer Eingang verbucht — mit Datum, agate-Versionsangabe und
Filename-Referenz. Damit ist der Importpfad auch nachträglich
auditierbar.

## Konfigurations-Checkliste

Damit agate-Imports funktionieren:

1. **`setting('enable_sip_anton_import')` auf `true`** setzen (default
   false aus Sicherheitsgründen)
2. **API-Token** für agate erzeugen (siehe
   [API Authentication](authentication.md))
3. **`accessions_archives_id`** auf einen geeigneten Wrapper-Bestand
   setzen, damit die Eingangsbuchung erfolgt
4. **NARA-Mapping** anlegen (siehe oben) — Default-Mapping vorhanden,
   aber tenant-spezifische Werte sind wahrscheinlich nötig
5. **Queue-Worker** muss laufen (Anton-Standard: Supervisor)

## Häufige Stolpersteine

- **Wiederholte Uploads mit gleichem Filename** funktionieren seit
  v0.61.0 — Anton prüft jetzt den Original-Filename, nicht den
  UUID-suffixed Pfad auf Disk.
- **NARA-Kategorie ohne Tenant-Typ** bricht den Import nicht mehr ab
  (seit v0.61.0). Das `object_type` bleibt leer.
- **Wrapper-Datensatz oben am SIP** bekommt keinen Objekttyp
  aufgedrückt — Hardcoded "Agate SIP" wurde entfernt.

## Verwandte Seiten

- [SIP Ingest](sip-ingest.md) — generische SIP-Import-Mechanik
- [Inge / DIMAG Upload](inge.md) — DIMAG-Anbindung für ZH-Gemeinden
- [API Authentication](authentication.md) — Tokens für agate
