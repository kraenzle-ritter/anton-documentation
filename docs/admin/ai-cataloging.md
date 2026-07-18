# KI-Erschliessung

Anton kann seit **v0.63.0** auf Knopfdruck Vorschläge für Titel,
Textfelder, Datierung, Akteur:innen, Orte und Schlagwörter generieren — basierend
auf den angehängten Mediendateien (Bilder, PDFs, Audio-Transkripten,
Video-Frames) und dem bestehenden Kontext eines Datensatzes.

Standardmässig ist die Funktion **ausgeschaltet**. Sie wird pro Archiv
separat aktiviert. Default-Provider ist Infomaniak (Schweiz-gehostet,
FADP/GDPR-konform), damit Archivdaten die Schweiz nicht verlassen.

## Aktivierung pro Tenant

Drei Schalter müssen alle gesetzt sein, damit die KI-Erschliessung
ansprechbar ist:

1. **Env-Variable `AI_ENABLED=true`** in der `.env`-Datei des Tenants
   (globaler Kill-Switch via Deployment)
2. **Provider-Keys** im env:
   - `INFOMANIAK_API_KEY` + `INFOMANIAK_TENANT_ID` (Default-Profil)
   - optional `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`
3. **Setting `ai_enabled = true`** im Tenant-Settings-UI

Ohne diese drei Schritte: kein Button, keine Dashboard-Links, kein
Risiko von Provider-Fehlern. Tenants ohne KI-Vertrag merken nichts.

## Der Operator-Workflow

Beim Bearbeiten eines Datensatzes erscheint oben in der Aktionsleiste
ein Button **"🤖 KI-Vorschläge generieren"** (seit v0.65.0 direkt neben
dem Upload-Bereich, sichtbar sobald eine Datei angehängt ist).

Nach Klick:

1. Anton lädt die angehängten Medien zum konfigurierten Provider hoch
   (PDFs werden als Seitenbilder gerendert; Audio wird via Whisper
   transkribiert; Videos werden in 5 gleichmässig verteilte Standbilder
   zerlegt)
2. Provider liefert nach wenigen Sekunden einen strukturierten
   Vorschlag
3. Anton zeigt pro Feld eine **Hinweis-Chip** mit dem KI-Vorschlag
4. Pro Vorschlag drei Aktionen: **Übernehmen**, **Anhängen** (nur bei
   Textfeldern), **Ignorieren**

Speichern erfolgt regulär über den Anton-Speichern-Button. Keine
versteckten DB-Schreibvorgänge — die KI macht nur Vorschläge, der
Mensch entscheidet.

## Was die KI als Input bekommt

- **Bilder** (Fotos, Scans) direkt als Vision-Input
- **PDFs** — Seitenbilder; zusätzlich der OCR-Textlayer wenn vorhanden
  (seit v0.65.0 für bessere Qualität bei getippten Dokumenten)
- **Audio** — Whisper-V3-Transkript über Infomaniak Async-Batch-API.
  Das Transkript kann optional als Textfeld in den Volltext-Index landen.
- **Video** — 5 ffmpeg-Standbilder evenly-spaced über die Laufzeit
- **Bestehender Titel** des Datensatzes als Kontext

## Akteur:innen, Orte, Schlagwörter: zwei Pattern

Die KI unterscheidet zwischen Schöpfer- und Inhalts-Bezügen:

| Pattern | Beispiel | Speicherort in Anton |
|---|---|---|
| **Schöpfer:in / Aufnahmeort** | Fotograf:in einer Aufnahme, Drehort | Neues `AntonEvent` |
| **Im Material genannt / abgebildet** | Personen auf einem Foto, im Text erwähnte Orte | Inhalts-Descriptor (Schlagwort-/Personen-/Orts-Liste) |

Pro Vorschlag ist ersichtlich, ob ein Eintrag schon existiert
(dann wird verknüpft) oder neu angelegt werden müsste (Klick öffnet
das vorausgefüllte Anlegen-Formular). Schlagwörter ohne weitere Details
können mit einem Klick direkt angelegt und verknüpft werden.

## Admin-Dashboard

Unter **Admin → KI-Erschliessung** stehen fünf Tabs:

| Tab | Inhalt |
|---|---|
| **Verbrauch** | Monatsbudget, Kostenstand, letzte 50 Aufrufe pro Datensatz mit Token-Counts und CHF-Kosten |
| **Modelle** | Verfügbare Provider/Modelle mit Beschreibung, Vision-Fähigkeit, Aktiv-Status, Preise pro 1k Tokens |
| **Budget** | Monats-Caps pro Kalendermonat (seit v0.65.0 auch über UI editierbar, vorher nur SQL) |
| **Profile** | Definierte KI-Profile mit Anlegen/Bearbeiten/Löschen |
| **Audit-Trail** | Alle Aufrufe mit Prompt, AI-Antwort und Operator-Entscheidung (übernommen/geändert/ignoriert) |

Der Audit-Tab seit v0.65.0 zeigt nicht nur "Vorschlag generiert",
sondern auch ob er **übernommen, geändert oder ignoriert** wurde — wichtig
für die Qualitätskontrolle und für späteres Prompt-Tuning.

## KI-Profile

Pro Tenant oder Objektform kann ein eigenes Profil mit angepasstem
Prompt-Block angelegt werden. Beispiel für Personenakten:

> *"Du analysierst Personenakten Schweizer Persönlichkeiten. Achte
> besonders auf Geburts-/Sterbedaten, Berufe, Familienverhältnisse,
> Wohnorte."*

Die KI bekommt diesen Block bei jedem Aufruf zusätzlich zur
Standard-Schema-Anleitung.

Profile-Anlegen-Formular bietet:

- **Provider-Auswahl** — Infomaniak (Schweiz), Anthropic (USA),
  Google Gemini (USA/EU)
- **Modell-Auswahl** — passende Modelle je Provider, mit Beschreibung
- **Scope** — global, pro Tenant, pro Objektform, pro Bestand
- **Sprache** — Standard Deutsch
- **Audit-Threshold** — 100 = jeder Aufruf wird gesampelt, 0 = nie

Profile ohne API-Key im env werden im Anlegen-Formular sichtbar (mit
Warnung), erscheinen aber **nicht** in der Operator-Profil-Auswahl —
Anwender:innen sehen nur funktionsfähige Profile.

Seit v0.65.0 ist ein **Standard-Profil pro Tenant** vorkonfiguriert,
so dass die Profil-Auswahl im Operator-Workflow nur noch auf Wunsch
aufklappt.

## Kosten + Budgets

- Default-Modelle: Infomaniak Gemma 4 31B-it (multimodal, 256k Kontext)
  + Mistral Ministral 3 14B
- Optionaler Fallback: Anthropic Claude Sonnet 4.6 (Vision), Google
  Gemini 2.5 — mit Datenschutz-Warnung weil Daten ausserhalb der
  Schweiz verarbeitet werden
- Kosten pro Aufruf werden in der Tabelle `ai_usage_log` festgehalten
  und im Dashboard aufsummiert
- Default-Monatsbudget zum Pilot: 50 CHF. Wird das Cap überschritten,
  blockiert Anton weitere Aufrufe bis zum Monatswechsel.
- **Marge** auf die Provider-Kosten (Default 1.30, also 30% Aufschlag)
  liegt anton-installations-weit in `config/ai.php`, env-overridable
  via `AI_BILLING_MARGIN`

## Datenschutz

Das System verwendet als Standard Schweiz-gehostete Modelle
(Infomaniak). FADP/GDPR-konform. Bei expliziter Auswahl eines
US/EU-Providers (Anthropic, Gemini) erscheint im Operator-UI eine
Datenschutz-Warnung mit Hinweis auf den Datenfluss ausserhalb der
Schweiz.

## Technische Eckdaten

- **6 neue DB-Tabellen**: `ai_profiles`, `ai_profile_versions`,
  `ai_usage_log`, `ai_pricing`, `ai_budgets`, `ai_audit_samples`
- **Cross-Repo-Package**: `kraenzle-ritter/ai-cataloging` (Framework-frei)
- **Profil-Versionierung**: jeder Edit eines Profils erzeugt einen
  Snapshot, damit Audit-Trails reproduzierbar bleiben
- **JS-Chip-Decorator** statt Modal-Stack: Vorschläge erscheinen direkt
  bei den Form-Feldern statt in einem separaten Panel
- **Auto-Save beim Upload** (seit v0.65.0): Drag-and-Drop-Uploads
  speichern den Datensatz automatisch und behalten die Bearbeitungs-
  Seite + Scrollposition
