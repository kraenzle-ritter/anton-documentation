# Feedback-Formular

Seit **v0.55.0** können Admins und Superuser direkt aus Anton heraus
Feedback an die Entwicklung schicken. Jede Rückmeldung landet
automatisch als Issue im GitHub-Repository von Anton, samt
technischem Kontext.

Seit **v0.58.0** läuft das Formular auf derselben Upload-Pipeline wie
die übrigen Anton-Eingabemasken (mit Drag-and-Drop / Cmd-V für
Screenshots).

## Wie es benutzt wird

Im Footer ist für Admins/Superuser ein Link **„Feedback"** sichtbar.
Klick öffnet `/feedback`. Das Formular hat:

- **Titel** — kurze Zusammenfassung
- **Beschreibung** — Markdown erlaubt, Fliesstext
- **Screenshots** (optional) — per Drag-and-Drop ins Formular ziehen
  oder mit **Cmd-V / Ctrl-V** irgendwo auf der Seite einfügen.
  Hochladen läuft im Hintergrund, sobald die Datei da ist.

Nach Abschicken legt Anton ein GitHub-Issue im
[`kraenzle-ritter/anton`](https://github.com/kraenzle-ritter/anton)-
Repository an. Das Issue enthält:

- Titel + Beschreibung aus dem Formular
- E-Mail-Adresse des absendenden Users (seit v0.58.0, vorher manueller
  SSH-Lookup nötig)
- Aufgerufener Pfad in Anton
- Anton-Version (Tag)
- Tenant-Slug
- Technischer Kontext (Browser, Bildschirmgrösse, optional)

## Aktivierung pro Tenant

Standardmässig ist das Formular **ausgeschaltet**. Drei Settings:

| Setting | Wert | Bedeutung |
|---|---|---|
| `feedback_enabled` | `true`/`false` | Aktiviert das Formular für den Tenant |
| `feedback_roles` | Array von Rollen | Welche Rollen den Link im Footer sehen (z. B. `['admin', 'superuser']`) |
| `feedback_github_repo` | `owner/repo` | Ziel-Repository, default `kraenzle-ritter/anton` |

Zusätzlich pro Anton-Installation **(env, nicht per-Tenant)**:

- `FEEDBACK_GITHUB_PAT` — Personal Access Token mit
  `issues: write`-Scope auf dem Ziel-Repo. Bot-Account empfohlen,
  damit Issues nachvollziehbar von einem klar identifizierbaren
  Absender kommen.

## Screenshot-Konfiguration

Seit v0.58.0 sind die Upload-Constraints pro Tenant in der DB
konfigurierbar, ohne Code-Änderung:

- **Erlaubte Dateitypen** (Default: `image/png`, `image/jpeg`,
  `image/webp`)
- **Maximale Anzahl** pro Feedback-Eintrag
- **Maximale Grösse** pro Datei

Auch der frühere tenant-weite „Screenshots aus"-Schalter (für
Intranet-Hosts wie ZH) läuft jetzt auf demselben DB-Mechanismus — das
alte `feedback_screenshots_enabled`-Setting ist obsolet.

## Bekannte Eigenheiten

- **Windows Snipping Tool** triggerte vor v0.58.0 zwei identische
  Bilder pro Issue (Doppelpaste). Seit v0.58.0 reagiert das Formular
  auf Paste-Events mit nur noch einem Upload.
- **Anhänge auf GitHub** — alle Bilder werden direkt in das Issue
  hochgeladen (nicht extern verlinkt), so dass sie auch in Jahren
  noch zugänglich sind.

## PAT-Rotation

GitHub-PATs laufen nach 1 Jahr ab. Die aktuelle Rotation steht im
internen Kalender; siehe Memory-Note `reference_feedback_bot_account`
(intern).

Wenn der PAT abläuft, schlägt das Issue-Anlegen still fehl und das
Feedback bleibt nur in der Anton-DB hängen — kein Verlust, aber kein
GitHub-Issue. Ein Admin-Audit (`/admin/feedback/pending`) zeigt
hängengebliebene Einträge.

## Verwandte Themen

- [Notifications](notifications.md) — wenn Feedback-Antworten als
  Notification ins Anton-UI zurückfliessen sollen (separates Feature)
- [API Authentication](authentication.md) — falls eigene Tools per
  API Feedback schicken sollen statt über das UI-Formular
