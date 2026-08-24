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
| `docs/admin/`, `docs/developer/`, `docs/api/` | de, en | Technikpersonal |
| `docs/customers/` | de | Kundenspezifisch, nicht in der Navigation |

Stand: der vorgesehene Umfang ist **vollständig** erfüllt — alles ausser
`docs/customers/` liegt auf Deutsch und Englisch vor, Startseite, FAQ und
`docs/user/` zusätzlich auf Französisch und Italienisch. Nicht übersetzt sind
`docs/user/settings.md` und `docs/user/uploads.md` — unfertige Stubs, die nicht
in der Navigation stehen und darum auch nicht mitgezählt werden.

## Sprachen und Stand-Datum im Seitenkopf

Über der Überschrift steht klein und rechtsbündig, in welchen Sprachen es die
Seite **wirklich** gibt (`de | en | fr | it`), und rechts daneben das Datum des
letzten Commits, der die Datei angefasst hat. Die Angaben liefert
`hooks/page_meta.py`, gerendert werden sie in `overrides/main.html`.

Wichtig dabei:

- Gezählt werden nur **echte Übersetzungen**, nicht die Fallback-Seiten. Eine
  Admin-Seite zeigt darum `de | en`, eine User-Seite `de | en | fr | it`.
- Massgeblich für Beschriftung und Markierung ist die Sprache der **gebauten
  Site**, nicht die der Datei — auf einer deutschen Fallback-Seite unter `/fr/`
  steht das Datum französisch beschriftet, und keine Sprache ist als aktiv
  markiert.
- Das Datum stammt aus **einem** `git log`-Lauf beim Build, nicht aus einem
  Subprozess je Seite. Eine noch nicht committete Seite zeigt kein Datum.
- Der Sprachumschalter in der Kopfleiste ist per CSS ausgeblendet
  (`.md-header__option`) — die Sprachwahl steht neu pro Seite.

## Fusszeile

Der KI-Hinweis in der Fusszeile hängt an `copyright` in `mkdocs.yml`: einmal
global (deutsch) und je Sprache im i18n-Plugin überschrieben. Französisch und
Italienisch brauchen dort **doppelte** Anführungszeichen, weil die Texte
Apostrophe enthalten.

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
`Developer`, `Admin` und `API` **absolute Links auf die nächstbeste vorhandene
Sprache** in der `nav` von Französisch und Italienisch:

```yaml
- Developer (en): /en/developer/
- Admin (en): /en/admin/requirements/
- API (en): /en/api/
```

Das Sprachkürzel im Label ist Absicht: der Klick führt sichtbar in die englische
Site, statt französische Beschriftung mit englischem Inhalt zu mischen. MkDocs
behandelt absolute Pfade als externe Links (nur eine INFO-Meldung im Build).
Käme eine französische Fassung dazu, würde der Eintrag durch die echten
Unterseiten ersetzt — so wie es die englische `nav` inzwischen hat.

### Anker über Sprachgrenzen

Beim Übersetzen ändert sich die Überschrift und damit ihr Anker. Verweist eine
**deutsche** Seite auf einen Abschnitt einer übersetzten Seite, bricht der Anker
— MkDocs meldet das beim Build («does not contain an anchor»).

Lösung: Der übersetzten Überschrift den deutschen Anker per `attr_list`
mitgeben, damit er sprachunabhängig stabil bleibt:

```markdown
## Il visualizzatore {#der-viewer}
```

So gelöst in `documents.*.md` (`#der-viewer`), `forms.*.md`
(`#hilfetexte-zu-feldern`) und `import.*.md` (`#import-protokoll`).

Am häufigsten trifft es Links aus dem Admin- und Developer-Bereich, den es nur
auf Deutsch und Englisch gibt: `fallback_to_default` zieht diese Seiten trotzdem
nach `/fr/` und `/it/`, und von dort zeigt der Link auf die *französische* bzw.
*italienische* Fassung der Zielseite. Der Anker heisst dort anders — der Link
bricht in genau den zwei Sprachen, in denen die verweisende Seite gar nicht
übersetzt ist.

Das prüft ein eigener Check, denn MkDocs meldet es nur als INFO und lässt es
auch unter `--strict` durch:

```bash
python3 scripts/check-anchors.py    # Exit 1 bei gebrochenen Ankern
```

Er läuft in der CI **blockierend** — anders als eine fehlende Übersetzung ist
ein Link ins Leere kein Rückstand, sondern ein Fehler.

## Eine bestehende Seite ändern

Wird eine deutsche Seite geändert, sind ihre Übersetzungen veraltet. Der Check
findet das:

```bash
python3 scripts/check-translations.py             # Bericht
python3 scripts/check-translations.py --strict    # Exit 1 bei Drift
python3 scripts/check-translations.py --lang fr   # nur eine Sprache
```

Die Abdeckung zählt er gegen den **vorgesehenen** Umfang aus der Tabelle oben,
nicht gegen alle Seiten — `docs/admin/` fehlt auf Französisch nicht, es ist dort
gar nicht vorgesehen. Die beiden Stubs `user/settings.md` und `user/uploads.md`
sind ausgenommen. Ändert sich der Sprachumfang, gehört er in `SCOPE` im Skript
nachgeführt, sonst misst der Check gegen ein Soll, das nicht mehr gilt.

Eine fällige, aber noch nicht angelegte Übersetzung meldet er — sie macht aber
auch unter `--strict` kein Exit 1. Sie ist Rückstand, kein Fehler; sonst hätte
eine neue deutsche Seite im selben Moment drei rote Sprachen.

Auf Drift prüft er zweierlei, weil eine Übersetzung auf zwei Arten driftet:

* **Zeitstempel** — die deutsche Seite ist neuer als ihre Übersetzung.
  Verglichen wird der letzte Commit, bzw. der Working Tree, damit der Check
  schon vor dem Commit anschlägt.
* **Form** — beide wurden angefasst, aber die Übersetzung hat einen Abschnitt
  weniger, eine Admonition mehr oder einen expliziten Anker der Quelle nicht
  übernommen. Das fängt den Fall, den der Zeitstempel nicht sieht: eine
  Übersetzung, die im selben Commit nur halb nachgezogen wurde. Verglichen wird
  nie der Text, sondern die Gliederung (Folge der Überschriftenebenen), die Zahl
  der Code-Blöcke, Admonitions und Tabellenzeilen sowie die expliziten Anker.
  Mit `--no-structure` abschaltbar.

Ein expliziter Anker in der Übersetzung, den die deutsche Seite als
automatischen Anker führt, gilt als richtig — das ist ja gerade die Lösung von
oben. Gemeldet wird nur ein Anker, den es auf der Quellseite überhaupt nicht
gibt.

Der Check läuft in der CI mit und meldet Drift, ohne den Build zu blockieren —
sonst bräuchte jede deutsche Korrektur sofort drei Übersetzungen.

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
  ihre Beschreibungen aus `php artisan list` und ist damit ohnehin englisch.
  `scripts/gen-command-reference.py` schreibt in **alle** Sprachfassungen der
  Seite und übersetzt dabei nur den Tabellenkopf (`TABLE_HEADERS`); der
  `--check`-Lauf prüft ebenfalls alle.
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
