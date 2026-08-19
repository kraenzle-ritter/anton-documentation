# Übersetzungen

Die Doku wird viersprachig geführt: **de** (Quellsprache), **en**, **fr**, **it**.
Technisch erledigt das [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n).

## Grundprinzip

Deutsch ist die Quellsprache. Jede Änderung entsteht zuerst auf Deutsch, die
Übersetzungen ziehen nach. Deutsch bleibt unter `/`, die anderen Sprachen liegen
unter `/en/`, `/fr/`, `/it/` — bestehende deutsche URLs ändern sich nicht.

## Dateikonvention

Übersetzungen sind Geschwisterdateien mit Sprach-Suffix:

```
docs/faq/export.md      ← deutsche Quelle
docs/faq/export.en.md
docs/faq/export.fr.md
docs/faq/export.it.md
```

Bilder, Diagramme und andere Assets werden geteilt — die Pfade in den
Übersetzungen bleiben unverändert (`images/markdown_input.png`).

## Sprachumfang pro Bereich

| Bereich | Sprachen | Begründung |
|---|---|---|
| `docs/index.md` | de, en, fr, it | Einstiegsseite |
| `docs/faq/` | de, en, fr, it | Erste Anlaufstelle für Interessierte |
| `docs/user/` | de, en, fr, it | Archivmitarbeitende in der Romandie und im Tessin |
| `docs/admin/` | de, en | Technikpersonal |
| `docs/developer/`, `docs/api/` | de | Technikpersonal |
| `docs/customers/` | de | Kundenspezifisch, nicht in der Navigation |

Stand: `docs/index.md`, `docs/faq/` und `docs/user/` sind in allen vier Sprachen
übersetzt (46 von 106 Seiten). Nicht übersetzt sind `docs/user/settings.md` und
`docs/user/uploads.md` — unfertige Stubs, die nicht in der Navigation stehen.

## Eine Seite übersetzen

1. Übersetzungsdatei anlegen (`seite.fr.md`), Glossar unten beachten.
2. Die Seite in `mkdocs.yml` in die `nav` der betreffenden Sprache aufnehmen.
   Die Navigation jeder Sprache listet **nur, was in dieser Sprache existiert** —
   so sieht man auf einen Blick, was fertig ist.
3. `mkdocs build` und die Seite in allen Sprachen anschauen.

Nicht übersetzte Seiten bleiben in allen Sprachen erreichbar (`fallback_to_default`)
und zeigen dann den deutschen Text. Das hält Querverweise heil; ein französischer
Link auf `../admin/download-rdf.md` landet auf `/fr/admin/download-rdf/` mit
deutschem Inhalt.

### Nicht übersetzte Bereiche in der Navigation

Damit die Hauptmenüpunkte in jeder Sprache vorhanden sind, stehen für
`Developer`, `Admin` und `API` **absolute Links auf die deutsche Fassung** in der
`nav` der Fremdsprachen:

```yaml
- Developer (de): /developer/
- Admin (de): /admin/requirements/
- API (de): /api/
```

Das Sprachkürzel im Label ist Absicht: der Klick führt sichtbar in die deutsche
Site, statt französische Beschriftung mit deutschem Inhalt zu mischen. MkDocs
behandelt absolute Pfade als externe Links (nur eine INFO-Meldung im Build).
Sobald `admin/` auf Englisch vorliegt, wird der Eintrag zu `Admin (en):
/en/admin/requirements/`.

### Anker über Sprachgrenzen

Beim Übersetzen ändert sich die Überschrift und damit ihr Anker. Verweist eine
**deutsche** Seite auf einen Abschnitt einer übersetzten Seite, bricht der Anker
— MkDocs meldet das beim Build («does not contain an anchor»).

Lösung: Der übersetzten Überschrift den deutschen Anker per `attr_list`
mitgeben, damit er sprachunabhängig stabil bleibt:

```markdown
## Il visualizzatore {#der-viewer}
```

So gelöst in `documents.*.md` (`#der-viewer`) und `forms.*.md`
(`#hilfetexte-zu-feldern`). Nach jedem Übersetzungslauf den Build auf
«does not contain an anchor» prüfen.

## Eine bestehende Seite ändern

Wird eine deutsche Seite geändert, sind ihre Übersetzungen veraltet. Der Check
findet das:

```bash
python3 scripts/check-translations.py           # Bericht
python3 scripts/check-translations.py --strict  # Exit 1 bei Drift
```

Er vergleicht den letzten Commit (bzw. den Working Tree) von Quelle und
Übersetzung. Er läuft in der CI mit und meldet Drift, ohne den Build zu
blockieren — sonst bräuchte jede deutsche Korrektur sofort drei Übersetzungen.

## Glossar

Verbindlich ist die Oberfläche der App. Die Begriffe stammen aus dem
Anton-Repo (`~/Sites/anton.test`):

| Quelle | Enthält |
|---|---|
| `resources/lang/{de,en,fr,it}/anton.php` | Kernbegriffe |
| `database/seeders/TermTranslationsLevelOfDescription.php` | Verzeichnungsstufen |
| `database/seeders/InitAntonfieldsEventLabels.php` | Ereignistypen |

Wer hier abweicht, schreibt eine Doku, die nicht zu den Beschriftungen passt,
die Nutzende sehen. Die Labels lassen sich so aus dem Anton-Repo ziehen:

```bash
python3 - <<'EOF'
import re
s = open('database/seeders/InitAntonfieldsEventLabels.php', encoding='utf-8').read()
for b in re.split(r"\$af = Antonfield::find", s)[1:]:
    l = dict(re.findall(r"setTranslation\('label', '(\w\w)', '([^']*)'\)", b))
    if l:
        print(' | '.join(l.get(k, '?') for k in ('de', 'en', 'fr', 'it')))
EOF
```

### Verzeichnungsstufen

| Deutsch | English | Français | Italiano |
|---|---|---|---|
| Archiv | Collection | Archives | Archivio |
| Bestandsgruppe | Recordgroup | Groupe de fonds | Gruppo di fondi |
| Bestand | Fonds | Fonds | Fondo |
| Serie | Series | Série | Serie |
| Klasse | Class | Classe | Classe |
| Dossier | File | Dossier | Unità archivistica |
| Einzelstück | Item | Pièce | Unità documentaria |

### Kernbegriffe

| Deutsch | English | Français | Italiano |
|---|---|---|---|
| Verzeichnungseinheit | Unit of Description | Unité de description | Unità di descrizione |
| Signatur | Reference code | Cote | Segnatura |
| Akteur:in | Actor | Acteur·trice | Attore, Attrice |
| Ort | Place | Lieu | Luogo |
| Schlagwort | Keyword | Mot-clé | Parola chiave |
| Standort | Location | Lieu de conservation | Collocazione |
| Ereignis | Event | Événement | Evento |
| Ereignistyp | Event type | Type d'événement | Tipo di evento |
| Umfang | Extent | Importance matérielle | Consistenza |
| Ressource | Resource | Ressource | Risorsa |
| Sprache | Language | Langue | Lingua |
| Benutzer:in | User | Utilisateur·trice | Utente |
| gesperrt | blocked | non communicable | bloccato |

### Ereignistypen

| Deutsch | English | Français | Italiano |
|---|---|---|---|
| Entstehungszeitraum | Creation Date | Dates de création | Periodo di creazione |
| Ablieferung | Immediate Source of Acquisition or Transfer | Modalités d'entrée | Modalità di acquisizione |
| Kopien/Reproduktionen | Existence and location of copies | Existence (et lieu de conservation) de copies | Copie/Riproduzioni |
| Digitalisiert | Digitized | Numérisation | Digitalizzato |
| Empfang | Reception | Réception | Ricezione |
| Vortrag/Aufführung | Perfomance | Performance | Performance |
| Provenienz | Provenance | Provenance | Provenienza |
| Konservierung | Preservation | Préservation | Conservazione |
| Stecher:in | Engraver | Graveur | Incisore |
| Schreiber:in | Scribe | Scribe | Scrittore |
| Kolorist:in | Colorist | Coloriste | Colorista |
| Verleger:in | Publisher | Éditeur | Editore |
| Produzent:in | Producer | Producteur | Produttore |
| Autor:in (Text) | Author (Text) | Auteur (Texte) | Autore (Testo) |
| Andere Rolle | Other Role | Autre rôle | Altro ruolo |

### ISAD(G)-Informationsbereiche

Die offiziellen Bezeichnungen des Standards, nicht wörtlich zu übersetzen:

| Deutsch | English | Français | Italiano |
|---|---|---|---|
| Identifikation | Identity statement | Identification | Identificazione |
| Kontext | Context | Contexte | Contesto |
| Inhalt und innere Ordnung | Content and structure | Contenu et structure | Contenuto e struttura |
| Zugangs- und Benutzungsbestimmungen | Conditions of access and use | Conditions d'accès et d'utilisation | Condizioni di accesso e uso |
| Sachverwandte Unterlagen | Allied materials | Sources complémentaires | Documentazione collegata |
| Anmerkungen | Notes | Notes | Note |
| Verzeichnungskontrolle | Description control | Contrôle de la description | Controllo della descrizione |

### Begriffe ohne App-Entsprechung

Diese kommen in der Oberfläche nicht vor; die Doku legt sie fest:

| Deutsch | English | Français | Italiano |
|---|---|---|---|
| Laufzeit | date range | dates extrêmes | estremi cronologici |
| Textfeld | text field | champ de texte | campo di testo |
| Formularsatz | form set | jeu de formulaires | set di formulari |
| Erschliessung | cataloguing | description archivistique | descrizione archivistica |
| Tektonik | archival arrangement | plan de classement | struttura archivistica |
| Laufmeter | linear metres | mètres linéaires | metri lineari |
| Findbuch | finding aid | instrument de recherche | strumento di ricerca |
| Warenkorb | cart | panier | carrello |

## Sprachliche Konventionen

- **Keine direkte Anrede.** Auch in den Übersetzungen neutral formulieren, kein
  «you»/«vous»/«tu». Wo die deutsche Quelle bereits die Sie-Form verwendet
  (`comments.md`, `passkey.md`), behält die Übersetzung deren Register
  («you», «vous»); Italienisch löst das unpersönlich.
- **Spaltennamen und Codebeispiele bleiben unangetastet.** In `import.md` sind
  Überschriften wie `### titel (title)` oder `### objekttyp (object_type)` die
  tatsächlichen Excel-Spalten — sie werden in keiner Sprache übersetzt. Das hält
  zugleich die Anker (`#titel-title`) sprachübergreifend stabil. Ebenso bleiben
  die Werte in Wertelisten-Beispielen (`Bestand`, `fonds`, `Akte`) deutsch bzw.
  intern, weil Anton genau diese Zeichenfolgen erwartet.
- **Gendergerecht analog zur App.** Deutsch: Doppelpunkt-Form (Benutzer:in),
  sonst Plural oder neutral. Französisch: Mittelpunkt-Form wie in der App
  (`Acteur·trice·s`, `Utilisateur·trice·s`). Italienisch: neutrale oder
  Pluralformen, bei Bedarf Doppelform («attori e attrici»).
- **Eigennamen bleiben stehen.** Institutionsnamen, Paketnamen, Produktnamen und
  Standards (EAD, ISAD(G), OCFL) werden nicht übersetzt.

## Offene Punkte

- **Screenshots sind deutsch.** `scripts/docshots.mjs` nimmt bereits ein
  `locale` entgegen; für eigene Screenshots pro Sprache müsste das Skript in
  vier Durchläufen mit je eigenem Zielverzeichnis laufen.
- **Die generierte Command-Referenz** (`docs/admin/console-commands.md`) bezieht
  ihre Beschreibungen aus `php artisan list` und ist damit ohnehin englisch;
  nur die Tabellenköpfe sind deutsch. `scripts/gen-command-reference.py` schreibt
  bisher nur in die deutsche Seite.
- **Die Suche** liefert für noch nicht übersetzte Inhalte deutsche Treffer,
  weil die Fallback-Seiten aus dem Index dedupliziert werden.
- **Zwei Begriffe in den italienischen App-Sprachdateien wirken falsch:**
  `extent` steht als «Ambito di applicazione» (= Anwendungsbereich; archivisch
  ist es «Consistenza»), `location` als «Posizione» statt «Collocazione». Die
  Doku verwendet die archivisch korrekten Begriffe — die App-Sprachdateien
  müssten nachgezogen werden, damit Doku und Oberfläche wieder zusammenpassen.
  Ebenso ist `actor` im Italienischen rein feminin («Attrice|Attrici»), während
  Französisch die Doppelform führt.
- **Build-Ausgabe nicht mit `--site-dir ./…` erzeugen.** MkDocs löst relative
  Pfade gegen das Verzeichnis der Konfigurationsdatei auf, nicht gegen das
  Arbeitsverzeichnis — die Ausgabe landet dann im Repo. `site` und `site-test`
  sind in `.gitignore`.
