# DIMAG-Upload-Status

Für Archive mit DIMAG-Anbindung (ZH-Kanton-Gemeinden wie Opfikon,
Lindau, Dürnten) zeigt Anton seit **v0.65.0** den Übertragungs-Status
jeder Mediendatei sichtbar in der UI — und meldet strukturelle Fehler
sofort per E-Mail an die Administration.

Hintergrund: Vorher konnte es passieren, dass eine Datei lokal
gespeichert, aber nicht erfolgreich an DIMAG übertragen wurde
(abgelaufenes Passwort, fehlende Schreibrechte, DIMAG nicht
erreichbar). Operator:innen sahen ein grünes „Datensatz aktualisiert"
und merkten erst beim nächsten DIMAG-Audit, dass nichts angekommen
war. Auslöser für die Implementierung war ein Vorfall am 20.05.2026:
ein rotiertes Passwort führte zu 30 Minuten stiller Ausfallzeit.

## Was Operator:innen sehen

### Warnung nach dem Speichern

Wenn die DIMAG-Übertragung fehlschlägt, erscheint nach dem Speichern
des Datensatzes ein **gelber Warnbalken**:

> *"Datei wurde gespeichert, aber Übertragung an DIMAG ist
> fehlgeschlagen. Administration wurde benachrichtigt."*

So sieht man unmittelbar, dass etwas nicht in Ordnung ist.

### Status-Badge pro Datei

In der Datei-Liste eines Datensatzes (Tab „Dateien") und in der
ausgeklappten Medien-Ansicht zeigt Anton pro Datei ein kleines Badge:

| Badge | Status | Bedeutung |
|---|---|---|
| 🟢 **DIMAG** | ok | Datei erfolgreich im DIMAG angekommen |
| 🟡 **wartet auf DIMAG** | pending | Übertragung läuft noch (Queue-Job aktiv) |
| 🔴 **DIMAG-Fehler** | failed | Übertragung fehlgeschlagen — Tooltip zeigt Fehlermeldung |

Das Badge ist nur für **eingeloggte Anton-Nutzer:innen** sichtbar,
nicht für externe Katalog-Besucher:innen. Bewusst nicht in
Galerie-Views eingebaut (würde die Public-Ansicht stören).

## Admin-Benachrichtigung

Bei strukturellen Fehlern (Passwort abgelaufen, DIMAG unerreichbar,
fehlende Berechtigungen) schickt Anton automatisch eine E-Mail an die
hinterlegte Administrations-Adresse:

- **Wer wird benachrichtigt:** Adresse aus `setting('admin_email')`
  (oder dem Tenant-Konfig-Default)
- **Was steht drin:** Fehlerkategorie, Datei-ID, Datensatz-ID, Anton-URL
- **Drosselung:** Pro Fehlertyp ein eigener Rate-Limit-Bucket
  (`email-exceptions:dimag:auth_failed`, `:permission_denied`,
  `:unreachable`, `:unknown`), 10 Mails pro Minute pro Bucket.
  Damit blockiert eine 401-Storm nicht das Alert-Budget für andere
  Probleme.

## Fehlerkategorien

`DimagIngestException::classifyMessage()` ordnet eingehende Fehler in
vier Kategorien ein:

| Kategorie | Triggers (Beispiele) |
|---|---|
| `auth_failed` | HTTP 401, "Access to DIMAG failed" |
| `permission_denied` | "Permission denied", "not writable" |
| `unreachable` | Timeout, Connection refused, DNS-Fehler |
| `unknown` | alles andere |

Die Kategorie steht im Mail-Subject und im Issue-Tracker-Eintrag (falls
das Feedback-Modul verbunden ist).

## Daten-Modell: `media_events`

Status-Events werden seit v0.65.0 in einer eigenen Tabelle
`media_events` gespeichert (append-only). Schema:

| Spalte | Inhalt |
|---|---|
| `media_id` | FK auf `media.id`, ON DELETE CASCADE |
| `event_type` | z. B. `dimag_upload`, `pdf_validation` |
| `status` | `ok` / `failed` / `info` |
| `category` | `dimag-ingest` / `pdf-validation` / nullable |
| `details` | JSON |
| `created_at` | Timestamp |

Die Tabelle ersetzt das frühere `media.custom_properties.events[]`-JSON-Blob,
das 5+ Klassen mit unterschiedlichen Schemata befüllt haben.

Helper:

```php
MediumEvent::record($medium, $type, $status, $category, $details);
Media::ingestStatus(?string $category)  // → 'ok' | 'pending' | 'failed' | null
Media::latestIngestEvent(?string $category)  // → MediumEvent | null
```

`pending` wird nur für `category=dimag-ingest` zurückgegeben, wenn die
Datei `original_location='inge'` hat aber noch keine Events.

## Troubleshooting

| Symptom | Ursache | Massnahme |
|---|---|---|
| Alle Uploads sind 🔴 mit „401 Unauthorized" | DIMAG-Passwort rotiert | Neues Passwort im `.env` setzen, Queue-Worker neu starten |
| Uploads bleiben 🟡 „wartet auf DIMAG" | Queue-Worker steht | Supervisor checken: `supervisorctl status` |
| Badge fehlt komplett | Tenant ist kein DIMAG-Tenant (`setting('cloud') !== 'inge'`) | Erwartungsgemäss — Badge erscheint nur bei inge-Cloud |
| Mail-Storm bei wiederholten Fehlern | Rate-Limit-Bucket greift trotzdem nicht | Cache-Treiber prüfen — Rate-Limit braucht funktionierende Cache (Redis/DB, nicht `array`) |

## SIP-Status-Tab

Ergänzend zum Per-File-Status gibt es seit v0.65.0/v0.66.0 unter
**SIP Import → Status** einen Admin-Tab `/sip/status` (nur bei
`cloud === 'inge'`), der die aktuelle Inge-URL und das Token-Setup
anzeigt und einen „Run infrastructure check now"-Button bietet. Derselbe
Check steht als Befehl `inge:check-infrastructure` bereit.

## Verwandte Themen

- [Inge / DIMAG-Anbindung](inge.md) — Grund-Konfiguration der
  DIMAG-Cloud
- [SIP Ingest (eCH-0160)](sip-ingest.md) — Übernahme von SIP-Paketen
- [Notifications](notifications.md) — wenn dimag-Events zusätzlich als
  in-App-Notification angezeigt werden sollen
