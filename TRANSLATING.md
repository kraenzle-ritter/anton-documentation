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

Verbindlich ist die Oberfläche der App. Die Begriffe stammen aus
`~/Sites/anton.test/resources/lang/{de,en,fr,it}/anton.php` und
`database/seeders/TermTranslationsLevelOfDescription.php`. Wer hier abweicht,
schreibt eine Doku, die nicht zu den Beschriftungen passt, die Nutzende sehen.

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
  «you»/«vous»/«tu».
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
