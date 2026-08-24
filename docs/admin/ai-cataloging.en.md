# AI-assisted cataloguing

Anton can generate suggestions for titles, text fields,
dating, actors, places and keywords at the push of a button — based on the
attached media files (images, PDFs, audio transcripts, video frames) and the
existing context of a record.

By default the function is **switched off**. It is activated separately per
archive. The default provider is Infomaniak (hosted in Switzerland,
FADP/GDPR-compliant), so that archival data does not leave Switzerland.

## Activation per tenant

Three switches all have to be set for AI-assisted cataloguing to be available:

1. **Env variable `AI_ENABLED=true`** in the tenant's `.env` file (global kill
   switch via deployment)
2. **Provider keys** in the env:
   - `INFOMANIAK_API_KEY` + `INFOMANIAK_TENANT_ID` (default profile)
   - optionally `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`
3. **Setting `ai_enabled = true`** in the tenant settings UI

Without these three steps: no button, no dashboard links, no risk of provider
errors. Tenants without an AI contract notice nothing.

## The operator workflow

When editing a record, a button **"🤖 Generate AI suggestions"** appears at the
top of the action bar (directly next to the upload area, visible as soon as a
file is attached).

After clicking:

1. Anton uploads the attached media to the configured provider (PDFs are
   rendered as page images; audio is transcribed via Whisper; videos are split
   into 5 evenly distributed stills)
2. Within a few seconds, the provider delivers a structured suggestion
3. Anton shows a **hint chip** with the AI suggestion for each field
4. Three actions per suggestion: **apply**, **append** (text fields only),
   **ignore**

Saving takes place as usual via the Anton save button. No hidden database
writes — the AI only makes suggestions, the human decides.

## What the AI receives as input

- **Images** (photographs, scans) directly as vision input
- **PDFs** — page images; additionally the OCR text layer if present (for
  better quality with typed documents)
- **Audio** — Whisper V3 transcript via the Infomaniak async batch API. The
  transcript can optionally end up in the full-text index as a text field.
- **Video** — 5 ffmpeg stills, evenly spaced across the running time
- **The existing title** of the record as context

## Actors, places, keywords: two patterns

The AI distinguishes between creator relationships and content relationships:

| Pattern | Example | Where it is stored in Anton |
|---|---|---|
| **Creator / place of recording** | Photographer of a shot, filming location | New `AntonEvent` |
| **Named or depicted in the material** | People in a photograph, places mentioned in the text | Content descriptor (keyword/person/place list) |

For each suggestion it is apparent whether an entry already exists (in which
case it is linked) or would have to be newly created (a click opens the
prefilled creation form). Keywords without further details can be created and
linked directly with one click.

## Admin dashboard

Under **Admin → AI cataloguing** there are five tabs:

| Tab | Content |
|---|---|
| **Consumption** | Monthly budget, cost status, last 50 calls per record with token counts and CHF costs |
| **Models** | Available providers/models with description, vision capability, active status, prices per 1k tokens |
| **Budget** | Monthly caps per calendar month, editable via the UI |
| **Profiles** | Defined AI profiles with create/edit/delete |
| **Audit trail** | All calls with prompt, AI response and operator decision (applied/changed/ignored) |

The audit tab shows not only "suggestion generated" but also
whether it was **applied, changed or ignored** — important for quality control
and for later prompt tuning.

## AI profiles

A separate profile with an adapted prompt block can be created per tenant or
object form. Example for personal files:

> *"You are analysing personal files of Swiss public figures. Pay particular
> attention to dates of birth and death, professions, family relationships and
> places of residence."*

The AI receives this block on every call in addition to the standard schema
instruction.

The profile creation form offers:

- **Provider selection** — Infomaniak (Switzerland), Anthropic (USA), Google
  Gemini (USA/EU)
- **Model selection** — suitable models per provider, with description
- **Scope** — global, per tenant, per object form, per fonds
- **Language** — German by default
- **Audit threshold** — 100 = every call is sampled, 0 = never

Profiles without an API key in the env are visible in the creation form (with a
warning) but do **not** appear in the operator profile selection — users only
see profiles that work.

A **default profile per tenant** is preconfigured, so that the profile
selection in the operator workflow only unfolds on request.

## Costs and budgets

- Default models: Infomaniak Gemma 4 31B-it (multimodal, 256k context) +
  Mistral Ministral 3 14B
- Optional fallback: Anthropic Claude Sonnet 4.6 (vision), Google Gemini 2.5 —
  with a data protection warning, because data is processed outside Switzerland
- The cost per call is recorded in the table `ai_usage_log` and totalled in the
  dashboard
- Default monthly budget for the pilot: 50 CHF. If the cap is exceeded, Anton
  blocks further calls until the turn of the month.
- The **margin** on the provider costs (default 1.30, that is, a 30 % surcharge)
  is set installation-wide in `config/ai.php` and can be overridden in the env
  via `AI_BILLING_MARGIN`

## Data protection

By default the system uses models hosted in Switzerland (Infomaniak).
FADP/GDPR-compliant. If a US/EU provider (Anthropic, Gemini) is explicitly
selected, a data protection warning appears in the operator UI pointing out the
data flow outside Switzerland.

## Technical key facts

- **6 new database tables**: `ai_profiles`, `ai_profile_versions`,
  `ai_usage_log`, `ai_pricing`, `ai_budgets`, `ai_audit_samples`
- **Cross-repo package**: `kraenzle-ritter/ai-cataloging` (framework-free)
- **Profile versioning**: every edit of a profile creates a snapshot, so that
  audit trails remain reproducible
- **JS chip decorator** instead of a modal stack: suggestions appear directly at
  the form fields rather than in a separate panel
- **Auto-save on upload**: drag-and-drop uploads save the record
  automatically and keep the editing page and scroll position
