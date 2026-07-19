# Formulare und Formularsätze

Anton gibt kein festes Feldschema vor. Welche Felder eine Verzeichnungseinheit
hat, wie sie heissen und in welcher Reihenfolge sie stehen, legt jedes Archiv
selbst fest. Gepflegt wird das unter **Admin → Formulare** und
**Admin → Formtypen**.

Wie sich das für die Erschliessung auswirkt, beschreibt
[Formulare und Felder](../user/forms.md) im Benutzerteil.

## Die drei Ebenen

| Ebene | Was sie ist |
|---|---|
| **Antonfield** | Eine Feld*definition* — Name, Typ, Grundbeschriftung. Existiert einmal und wird von beliebig vielen Formularen verwendet. |
| **Formular** | Eine geordnete Auswahl von Feldern für **eine** Ansicht. Legt pro Feld Position und Beschriftung fest. |
| **Formularsatz** | Bündelt fünf Formulare zu einer Einheit — die fünf Ansichten desselben Datensatztyps. |

Ein Feld erscheint also nicht «im Formular», sondern wird **verknüpft** — und
die Verknüpfung trägt die Feinheiten.

## Der Formularsatz und seine fünf Ansichten

| Slot | Wofür |
|---|---|
| Intern — Bearbeiten | Die Erschliessungsmaske |
| Intern — Detail | Detailansicht für angemeldete Benutzer:innen |
| Intern — Liste | Trefferliste für angemeldete Benutzer:innen |
| Extern — Detail | Detailansicht für die Öffentlichkeit |
| Extern — Liste | Trefferliste für die Öffentlichkeit |

Ein externes Bearbeiten-Formular gibt es nicht. Die Trennung intern/extern ist
der Hebel, mit dem gesteuert wird, was Aussenstehende sehen: **Ein Feld
erscheint nur, wenn es im jeweiligen Formular steht.**

!!! warning "Kein Ersatz für Schutzfristen"
    Ein Feld aus dem externen Formular zu nehmen, verbirgt es in der Anzeige —
    es ist keine Zugangskontrolle. Für Schützenswertes sind
    [Schutzfristen](protection-periods.md) und das Kennzeichen «Gesperrt» das
    richtige Mittel.

!!! note "Standort standardmässig nicht öffentlich"
    Neuinstallationen liefern das Feld **Standort** aus den externen Formularen
    (Extern — Detail/Liste) entfernt aus, damit der physische Aufbewahrungsort
    nicht im öffentlichen Katalog erscheint. Bestehende Installationen bleiben
    unverändert; dort lässt sich das Feld hier aus den externen Formularen
    nehmen.

Formularsätze gibt es nicht nur für Verzeichnungseinheiten, sondern auch für
Akteur:innen, Orte, Schlagwörter und Standorte.

## Welcher Formularsatz greift?

Anton entscheidet in dieser Reihenfolge:

1. Ist im Datensatz das Feld **Formularsatz** gesetzt, gilt dieser.
2. Sonst der Formularsatz, dessen Name der **Verzeichnungsstufe** entspricht —
   `fonds`, `file`, `item` und so fort.
3. Sonst der Standardsatz.

Für die meisten Archive genügt deshalb: je einen Satz pro Verzeichnungsstufe
pflegen. Eigene Sätze lohnen sich, wenn ein Bestandstyp andere Felder braucht —
Fotografien, Pläne, Filme.

## Was sich pro Formular überschreiben lässt

Dieselbe Felddefinition kann in jedem Formular anders auftreten. Überschreibbar
sind unter anderem:

- **Beschriftung** — dasselbe Feld kann in der Bearbeitungsmaske anders heissen
  als in der Detailansicht
- **Position** — die Reihenfolge
- **Werteliste** — welche [Werteliste](valuelists.md) ein Auswahlfeld speist
- **Vorgabewert**
- **Typ** — in Ausnahmefällen

Die Werteliste wird dreistufig aufgelöst: Überschreibung im Formular, sonst die
Vorgabe der Felddefinition, sonst ein fest eingebauter Rückfall.

## Abschnitte

Felder vom Typ *section* sind keine Eingabefelder, sondern graue
Zwischenüberschriften. Ein Abschnitt ohne sichtbares Feld wird ganz
weggelassen — leere Abschnitte muss man also nicht von Hand entfernen.

## Feldtypen

Welche Felder überhaupt zur Verfügung stehen und welchen Typ sie haben, zeigt
in der Anwendung die Hilfeseite **Anton Fields**. Sie listet zu jedem Feld die
Beschriftung, den Typ, den Hilfetext und die Formulare, in denen es vorkommt —
und ist damit die verlässlichste Auskunft über das **eigene** Archiv.

!!! note "Standardfelder nicht umbenennen — im technischen Sinn"
    Name und Typ der Anton-Standardfelder sind fest; Code und Import verlassen
    sich darauf. Die **Beschriftung** dagegen ist frei und bleibt bei
    Aktualisierungen erhalten.

## Trefferlisten

Die Listenansichten sind nur eingeschränkt konfigurierbar, weil dort Module
mehrere Angaben in eine Spalte ziehen. Für eine zusätzliche Vorschaubild-Spalte
gibt es die Einstellung `form-objects-list`.

## Konfigurierbare eingebettete Tabellen

Die Detailseiten von Akteur:innen, Orten, Schlagwörtern und Standorten zeigen
eine eingebettete Objektliste — die Verzeichnungseinheiten, die den Datensatz
als Deskriptor verwenden. Diese Liste folgt im Standard einer fest eingebauten
Vorgabe.

Unter **Admin → Formulare** lässt sie sich pro Archiv anpassen: Der Abschnitt
**Konfigurierbare eingebettete Tabellen** bietet eine Aktion **Konfigurieren**,
die die eingebaute Vorgabe in ein editierbares Formular überführt und an den
normalen Spalten-Editor übergibt. Ab da lassen sich Spalten und Beschriftungen
wie bei jedem anderen Formular ändern. Blosses Ansehen ändert nichts — erst
**Konfigurieren** legt das editierbare Formular an.
