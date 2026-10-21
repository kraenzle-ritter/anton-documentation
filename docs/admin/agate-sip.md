# agate-SIP-Import

[agate](https://github.com/kraenzle-ritter/agate) (das
Anton-Vorbereitungs-Tool für SIPs aus losen Datei-Ablagen) kann SIPs
(BagIt oder E-ARK) direkt per HTTP an Anton schicken. Anton nimmt das ZIP entgegen,
prüft es, legt ein Backup an, importiert die Inhalte als
Verzeichnungseinheiten unter dem gewählten Bestand und gibt agate
Bescheid wenn alles fertig ist.

Der gesamte Pfad läuft **asynchron** — agate kann parallel
weiterarbeiten oder andere SIPs vorbereiten.

## BagIt oder E-ARK

agate liefert ein SIP als BagIt-Bag oder als E-ARK-SIP 2.2.0, je nach Einstellung in agate. Beide tragen dieselbe `metadata.json`. Anton erkennt die Form am Inhalt des ZIP (`bagit.txt` oder `METS.xml`); der Dateiname bleibt `sip-agate-<bestand_id>.zip`, und beide nehmen dieselben Wege: Direkt-Import, Eingangskorb, Upload auf `/import/sip-anton` und `anton:import --from-sip`.

| | BagIt | E-ARK |
|---|---|---|
| `metadata.json` | `data/meta/metadata.json` | dmdSec mit `OTHERMDTYPE="anton-import-format"`, meist `metadata/descriptive/metadata.json` |
| Dateien | `data/content/` | `representations/rep1/data/` |
| Prüfung vor dem Import | Manifeste des Bags | Prüfsummen im METS, für `metadata.json` und jede Datei, die sie nennt |
| Prüfbericht | — | Prüfung nach E-ARK (eark-ip) als Prüf-Ereignis beim Lauf |

Eine fehlende oder veränderte Datei bricht den Import ab, bevor etwas geschrieben ist. Der E-ARK-Prüfbericht hält den Import nicht auf: Ob die Dateien unverändert sind, entscheiden die Prüfsummen. Ein E-ARK-SIP aus einem anderen Werkzeug (nur EAD oder Dublin Core, ohne `anton-import-format`) nimmt Anton noch nicht an.

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

Dasselbe gilt für den manuellen Upload im Reiter **Manueller Upload** von **SIP-Import (anton-import-format)**: Ein SIP mit `sip-agate-<bestand_id>.zip` erscheint in der Liste und wird mit **Importieren** gestartet, jedes andere landet im Eingangskorb. Ein SIP, dessen Inhalt schon importiert ist oder gerade importiert wird, nimmt der Upload nicht an.

## Eingangskorb (`/sip/inbox`)

Sichtbar für Editor- und Admin-Rollen unter **Import / Export → SIP
Inbox**. Pro Zeile:

- SIP-Filename, Hochladedatum
- Vorschau (Anzahl Dateien, Paketprüfung BagIt oder E-ARK, NARA-Kategorien)
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

- Multipart-Form mit `file`-Feld (`sip.zip`, BagIt oder E-ARK)
- Header `Authorization: Bearer <api_token>` (Sanctum-Token, siehe
  [API-Authentifizierung](../api/authentication.md))

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

## Importprotokoll

Jeder agate-SIP-Import steht als Lauf im Importprotokoll — mit Signatur
`IMPORT-{jjjj}-{NNN}`, Dateiname, Prüfsumme, Zeitpunkt, Ergebnis und den
angelegten Datensätzen. Damit ist der Importpfad auch nachträglich
auditierbar; ein Akzessions-Archiv braucht es dafür nicht.

## Formatumwandlung in agate

Anton wendet auf SIPs keine Format-Regel an: Die Prüfsummen eines SIP
belegen, dass die gelieferten Dateien unverändert angekommen sind. agate
wendet die Format-Regeln des Archivs deshalb selbst an, bevor es ein SIP
abschliesst; die Schalter liest es über die API aus Anton.

Was agate mit einer Datei getan hat, steht in `metadata.json` beim
Dateieintrag (`format_normalization`). Anton legt dafür am Medium je Regel ein
Ereignis `format-normalization` an, wie bei einer Umwandlung in Anton selbst.
Es nennt die Regel, die Werkzeugversionen und die Prüfsummen vor und nach der
Umwandlung. Die Prüfsumme der Datei, wie sie bei agate ankam, bleibt damit
erhalten.

## Original und Nutzungskopie

Ab anton-import-format 0.6 kann ein SIP zu einer Datei mehr als den Master liefern: die Datei vor einer Umwandlung (`versions`, Rolle `original`) und eine Nutzungskopie (`access_copy`). Der Master bleibt das Medium.

- **Original:** Anton bewahrt es hinter dem Medium auf (Fassung «Original», mit eigenen Prüfsummen und Ereignissen, in DIMAG über `media:versions-to-cloud`), nie als eigenes Medium. Hat agate die Datei umgewandelt und das Original behalten, verweist das Ereignis `format-normalization` auf diese Fassung.
- **Nutzungskopie:** Die Einstellung `import_access_copy` entscheidet. `derive` (Vorgabe): Anton rechnet die Webfassung selbst, die gelieferte Kopie wird nicht gespeichert. `adopt`: Anton übernimmt sie als Webfassung, wenn sie zum Master passt (Bild → JPEG, PDF → PDF, Video → MP4, Audio → MP3) und die Prüfsumme stimmt; sonst rechnet es selbst. Der Entscheid steht als Ereignis «Nutzungskopie» am Medium. Eine übernommene Webfassung ersetzt `media:conversions` nur mit `--replace-supplied`. Das Vorschaubild rechnet Anton immer selbst.
- **Prüfung:** Original und Nutzungskopie werden vor dem Import geprüft wie der Master: Virenprüfung, Prüfsumme, bei E-ARK gegen das METS ihrer Repräsentation (`representations/<source>/data/`). Ein Fehler bricht den Import ab, bevor etwas geschrieben ist.
- **Formatversion:** agate fragt Anton über `GET /api/import-format`, welche Version des Formats sein Import liest, und schreibt Original und Nutzungskopie nur, wenn Anton 0.6 oder neuer meldet. Ein `metadata.json` in einer neueren Version, als Anton liest, weist Anton ab.

## Konfigurations-Checkliste

Damit agate-Imports funktionieren:

1. **`setting('enable_sip_anton_import')` auf `true`** setzen (default
   false aus Sicherheitsgründen)
2. **API-Token** für agate erzeugen (siehe
   [API-Authentifizierung](../api/authentication.md))
3. **NARA-Mapping** anlegen (siehe oben) — Default-Mapping vorhanden,
   aber tenant-spezifische Werte sind wahrscheinlich nötig
4. **Queue-Worker** muss laufen (Anton-Standard: Supervisor)

## Häufige Stolpersteine

- **Wiederholte Uploads mit gleichem Filename** funktionieren — Anton
  prüft den Original-Filename, nicht den UUID-suffixed Pfad auf Disk.
- **NARA-Kategorie ohne Tenant-Typ** bricht den Import nicht ab. Das
  `object_type` bleibt leer.
- **Wrapper-Datensatz oben am SIP** bekommt keinen Objekttyp
  aufgedrückt — Hardcoded "Agate SIP" wurde entfernt.

## Verwandte Seiten

- [SIP Ingest](sip-ingest.md) — generische SIP-Import-Mechanik
- [Inge / DIMAG Upload](inge.md) — DIMAG-Anbindung für ZH-Gemeinden
- [API-Authentifizierung](../api/authentication.md) — Tokens für agate
