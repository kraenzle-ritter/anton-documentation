---
name: anton-doku-audit
description: "Prüft, ob die öffentliche Doku (dieses Repo) den letzten Anton-Code-Änderungen hinterherhinkt. Aktivieren, wenn jemand fragt »schau die letzten Anton-Commits an und prüfe, ob wir die Doku anpassen müssen«, »driftet die Doku?«, »Doku-Audit«, »was hat sich in Anton geändert, das dokumentiert werden muss«, oder nach einem Anton-Release / vor einem Doku-Deploy. Das ist der Doku-seitige Gegenpart zum app-seitigen Skill `anton-docs`: dieser hier ZIEHT die Anton-Änderungen herein und gleicht sie gegen die Doku-Seiten ab. Die Anton-App liegt in einem SEPARATEN Repo (`~/Sites/anton.test`) — die beiden können keinen gemeinsamen Commit teilen, Sync ist immer ein eigener Schritt."
---

# Anton-Doku-Audit — hinkt die Doku dem Code hinterher?

Die App **Anton** (`~/Sites/anton.test`, Laravel/Livewire) und ihre öffentliche
Doku (**dieses Repo**, `~/Sites/anton-documentation`, → documentation.anton.ch)
sind getrennte Git-Repos. Ein Code-Change und sein Doku-Update können darum
**nie im selben Commit** liegen — die Doku driftet leise. Dieser Skill ist der
regelmäßige Abgleich: *Welche Anton-Commits seit dem letzten Audit betreffen
etwas, das die Doku beschreibt — und stimmt die Doku dazu noch?*

Gegenstück auf der App-Seite: `~/Sites/anton.test/.claude/skills/anton-docs`
erinnert beim App-Coden daran, die Doku nachzuziehen. Beide Naht-Regeln stehen
auch in Antons `CLAUDE.md`.

## Workflow

### 1. Audit-Fenster bestimmen und einlesen

Der zuletzt auditierte Anton-Commit steht in `state/last-audited.sha`. Das
Helfer-Skript zeigt alles seither — Commits (kompakt + voll) **und** den
kuratierten `[Unreleased]`-Abschnitt aus Antons `CHANGELOG.md`:

```bash
.claude/skills/anton-doku-audit/scripts/anton-changes.sh          # seit letztem Audit
.claude/skills/anton-doku-audit/scripts/anton-changes.sh <ref>    # seit SHA/Tag
.claude/skills/anton-doku-audit/scripts/anton-changes.sh -n 25    # letzte 25 Commits
```

Der **`[Unreleased]`-Changelog ist der wertvollste Input** — er ist bereits die
menschlich kuratierte Destillation genau der benutzer:innen-/admin-sichtbaren
Änderungen (Keep-a-Changelog: Added/Changed/Fixed/Removed/Security). Die
rohen Commits daneben fangen das, was noch nicht im Changelog steht, und die
Datei-Stats zeigen, *welche* Bereiche berührt sind.

### 2. Änderungen klassifizieren — was ist doku-relevant?

Für jede Änderung entscheiden: berührt sie etwas, das die **öffentliche** Doku
(für Archivar:innen und Administrator:innen) beschreibt?

**Relevant (auditieren):**
- `feat` / `fix`, das **benutzer:innen- oder admin-sichtbares Verhalten** ändert
  (neue Buttons/Modals, geänderte Formular-Logik, neue Einstellungen, Rollen-/
  Berechtigungs-Wechsel, neue/geänderte Suche).
- **Artisan-Command** hinzugefügt / entfernt / umbenannt / Beschreibung geändert
  (`app/Console/Commands/**`) → Command-Referenz (siehe unten).
- **Exportformat** geändert oder was es emittiert → `docs/admin/export-matrix.md`.
- **Labels / i18n**, die eine Doku-Seite wörtlich nennt (`i18n(de)`, umbenannte
  Felder, gegenderte Rollen) → Seite, die das Label zeigt.
- **Einstellungen / Rollen / Feldnamen**, die eine Doku-Seite nennt.

**Überspringen (nicht doku-relevant):**
- `test`, `chore`, `ci`, reine interne `refactor` ohne Verhaltensänderung.
- `docs(skills)`, `docs(claude)` — App-interne Doku/Skills, nicht die öffentliche.
- Kundenspezifisches (`gf:`, `gosteli:`, `ballyana:`, `koeniz:` …) — außer es
  betrifft eine `docs/customers/*`-Seite.
- Rein technische Fixes ohne sichtbare Wirkung (interne Null-Guards, DB-Migration
  ohne UI-Folge). **Aber:** ein „unsichtbarer“ Fix, der ein *dokumentiertes*
  Verhalten wiederherstellt (z. B. „Suche findet Titel wieder“), ist relevant,
  wenn die Doku den kaputten Zustand beschrieb oder das Feature bewirbt.

### 3. Auf Doku-Seiten abbilden

Grobe Landkarte Anton-Bereich → Doku-Seite(n). Nicht abschließend — im Zweifel
`grep` über `docs/` nach dem Feld-/Label-/Command-Namen.

| Anton-Bereich / Scope | Wahrscheinliche Doku-Seite(n) |
|---|---|
| `forms` (Erschliessungsformular, Hilfetexte, eingebettete Tabellen) | `docs/user/forms.md`, `docs/admin/forms.md`, `docs/developer/forms.md` |
| `keywords` / Schlagwörter | `docs/user/keywords.md` |
| `places` / Orte | `docs/user/places.md` |
| `locations` / Standorte | `docs/user/locations.md`, `docs/admin/*` (Berechtigungen) |
| `actors` / Akteur:innen | `docs/user/actors.md`, `docs/user/authorities.md` |
| `search` / `typesense` / Volltext / Gewichtung | `docs/user/search.md`, `docs/user/search-v2.md`, `docs/user/weighted-search.md`, `docs/admin/weighted-search.md`, `docs/admin/typesense.md` |
| `cart` / Bestellkorb / Auswahl / Selection | `docs/user/cart.md`, `docs/user/selection.md` |
| Rollen / Berechtigungen / Zugriff | `docs/user/access.md`, `docs/admin/users.md`, `docs/admin/authentication.md` |
| Einstellungen / Settings / Profil | `docs/user/settings.md` |
| Export (SIP, DIP, RDF, Word, Memobase, TEI, OCFL) | `docs/admin/export-matrix.md`, `docs/admin/sip-ingest.md`, `docs/admin/download-*.md`, `docs/faq/export.md` |
| Import / Upload / AKZ / Directory-Import | `docs/user/import.md`, `docs/user/uploads.md`, `docs/faq/import.md` |
| Artisan-Command (irgendein Namespace) | `docs/admin/console-commands.md` (generiert — siehe unten) |
| Medien / Derivate / Gallery | `docs/user/media.md`, `docs/user/gallery.md`, `docs/admin/gallery.md` |
| i18n / Übersetzungen sichtbarer Labels | die Seite, die das Label zeigt (grep) |

### 4. Pro Kandidat die Doku wirklich prüfen

Nicht raten — die kandidierende Seite **lesen / grep**en und feststellen, in
welchem der drei Zustände sie ist:

- **VERALTET/WIDERSPRUCH** — Doku beschreibt altes Verhalten, das jetzt falsch
  ist. → Konkrete Änderung vorschlagen.
- **LÜCKE** — neues benutzer:innen-sichtbares Feature, in der Doku noch gar nicht
  erwähnt. → Wo es hingehört + Kurzentwurf.
- **BEREITS ABGEDECKT / IRRELEVANT** — Doku stimmt noch, oder Änderung ist nicht
  benutzer:innen-sichtbar. → Kurz notieren, warum, damit klar ist, dass geprüft
  wurde.

### 5. Sonderfälle mit fixem Verfahren

- **Command-Referenz** (`docs/admin/console-commands.md`): den generierten Block
  **nie von Hand** editieren. Neu erzeugen:
  ```bash
  python3 scripts/gen-command-reference.py          # Block neu schreiben
  python3 scripts/gen-command-reference.py --check   # Exit 1 bei Drift
  ```
  Braucht DDEV in `../anton.test`. Für einen *operativ wichtigen* neuen Command
  zusätzlich einen kuratierten Prosa-Eintrag in der passenden Aufgabengruppe. Neuer
  Admin-Namespace? Filter im Generator anpassen. (Details: Memory
  `reference_command_docs_sync`.)
- **Export-Matrix** (`docs/admin/export-matrix.md`): bei Exportformat-Änderungen
  aktualisieren — **inklusive `Stand:`-Datum** auf der Seite.

### 6. Bericht + State fortschreiben

Ergebnis als **Checkliste** ausgeben, sortiert nach Dringlichkeit:

```
## Anton-Doku-Audit — <Fenster>, <n> Commits geprüft

### Doku anpassen
- [ ] <Änderung (#issue)> → docs/…/x.md — <VERALTET|LÜCKE>: <konkret was tun>

### Bereits abgedeckt / nicht doku-relevant
- <Änderung> — <warum kein Doku-Change nötig>
```

Den State (`state/last-audited.sha`) **erst dann** auf Antons aktuellen HEAD
setzen, wenn das Audit abgeschlossen *und* die daraus folgenden Doku-Änderungen
gelandet (committet) sind — sonst fallen offene Punkte beim nächsten Audit
durchs Raster. State fortschreiben:

```bash
git -C ~/Sites/anton.test rev-parse HEAD > \
  .claude/skills/anton-doku-audit/state/last-audited.sha
```

Diese Datei mitcommitten — sie ist der Audit-Wasserstand, geteilt übers Team.

## Warum ein State-Wasserstand und nicht „letzte N Commits“

Die zwei Repos teilen keinen Commit, es gibt also keinen natürlichen „seit“-Marker.
Ein festgeschriebener SHA (`state/last-audited.sha`) macht das Audit
lückenlos und wiederholbar: jeder Commit wird genau einmal geprüft, egal wie viele
zwischen zwei Audits liegen. Fällt beim Audit ein offener Doku-Punkt an, bleibt der
State **stehen**, bis der Punkt erledigt ist — so verschwindet nichts im Tail.
