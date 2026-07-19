# Das Formularsystem

Die Kernidee: **Welche Felder eine Verzeichnungseinheit hat, steht in Daten,
nicht in Code.** Ein Archiv gestaltet seine Erschliessungsmasken selbst — und
zwei Installationen können mit derselben Codebasis völlig verschieden aussehen.
Das erklärt einen grossen Teil des Aufwands im Umfeld der Formulare.

Aus Sicht der Administration ist dasselbe unter
[Formulare und Formularsätze](../admin/forms.md) beschrieben; diese Seite geht
auf das Warum und die Erweiterungsnaht.

## Drei Ebenen

| Ebene | Modell | Tabelle | Was sie ist |
|---|---|---|---|
| **Antonfield** | `Antonfield` | `antonfields` | Eine Felddefinition: Name, Typ, Grundbeschriftung |
| **Formular** | `Objectform` | `forms` | Eine geordnete Feldauswahl für **eine** Ansicht |
| **Formularsatz** | `Objectformtype` | `formsets` | Bündelt die fünf Ansichten desselben Datensatztyps |

Ein Feld erscheint nicht «im Formular», sondern wird über die Pivot-Tabelle
`antonfields_forms` **verknüpft** — und die Verknüpfung trägt die pro-Formular-
Feinheiten: Position, Beschriftung, Werteliste, Vorgabewert, notfalls den Typ.

!!! note "Historische Tabellennamen"
    Die Modellklasse heisst `Objectformtype`, die Tabelle wurde aber zu
    `formsets` umbenannt; `forms` hiess früher `objectforms`. Wer nach dem alten
    Namen sucht, findet die falsche Fährte.

## Warum drei Ebenen

Die Trennung löst drei Anforderungen auf einmal:

- **Wiederverwendung** — dieselbe Felddefinition erscheint in vielen Formularen;
  eine Änderung am Feld wirkt überall.
- **Kontext** — dasselbe Feld darf je Ansicht anders heissen und an anderer
  Stelle stehen. Das ist der Grund für die Pivot-Overrides.
- **Sichtbarkeit** — die fünf Slots eines Formularsatzes (intern
  Liste/Detail/Bearbeiten, extern Liste/Detail) steuern, was Aussenstehende
  sehen. Ein Feld erscheint nur, wenn es im jeweiligen Formular steht. Ein
  externes Bearbeiten-Formular gibt es nicht.

!!! warning "Sichtbarkeit ist keine Zugangskontrolle"
    Ein Feld aus dem externen Formular zu lassen, verbirgt es in der Anzeige —
    es schützt nichts. Zugang regeln Schutzfristen und das `private`-Kennzeichen.

## Auflösung

Welcher Formularsatz für einen Datensatz greift, entscheidet sich in dieser
Reihenfolge: das Feld `formset_id` am Datensatz, sonst der Satz mit dem Namen der
Verzeichnungsstufe (`fonds`, `file` …), sonst der Standard.

Feldwerte werden dreistufig aufgelöst — Override im Formular, sonst Vorgabe der
Felddefinition, sonst ein fest eingebauter Rückfall. Das gilt für Beschriftung,
Werteliste, Vorgabewert und Typ gleichermassen.

## Die V2-Rendering-Engine

Ein Feld wird nicht direkt als Blade-Template gerendert, sondern durchläuft
`AntonForms\V2\AntonFormsElement`, das aus Typ und Ansicht einen *display mode*
bestimmt (`discoverDisplayMode()`) und daraus die Komponente auflöst. Zwei
Konsequenzen sind wichtig:

- **Ein Feld deckt Bearbeiten und Detail ab.** Einfache Eingabetypen (`text`,
  `select`, `radio` …) schalten in Detail- und Listenansicht automatisch auf
  `display`. Man braucht keine doppelte Definition.
- **Module lösen sich über den Namen auf.** Komplexe Felder haben den Typ
  `module`; die Komponente ergibt sich aus dem Feldnamen
  (`module_actors` → das Actors-Modul). So kommen Titel, Ereignisse,
  Deskriptoren, Medien, Standort und weitere in die Maske.

Welche Feldtypen und Module es tatsächlich gibt, ist **datengetrieben** und
steht in der Anwendung unter **Hilfe → Anton Fields** — pro Installation immer
aktuell. Eine feste Liste an dieser Stelle würde nur veralten.

## Felddefinitionen und ID-Bereiche

Antonfields mit **ID < 5000** sind Kernfelder: Name und Typ sind fest, weil Code
und die Enums `Eventtype`/`Notetype` darauf verweisen. Die **Beschriftung** ist
frei und wird bei `anton:update` bewusst nicht überschrieben — so überleben
mandantenspezifische Anpassungen jede Aktualisierung.

Felder mit **ID ≥ 5000** stammen aus alten kundenspezifischen Konfigurationen
und sollten nach `anton:update` nicht mehr existieren; `anton:check-customer-fields`
prüft das.

## DB-Override mit PHP-Rückfall

Nicht jedes Formular liegt in der Datenbank. `AbstractForms::get()` liefert bei
fehlender oder leerer `Objectform`-Zeile den versionierten PHP-Default zurück,
sofern die Subklasse über `phpFallback()` einen deklariert — sonst wird
weiterhin `FormNotFoundException` geworfen. So bleiben die eingebauten Vorgaben
die Quelle der Wahrheit, bis ein Archiv sie bewusst überschreibt; bestehende
DB-Formulare verhalten sich unverändert.

Die eingebettete «als Deskriptor verwendet»-Objektliste (geteilt von Akteur-,
Ort-, Schlagwort- und Standort-Detailseiten) rendert auf diese Weise aus dem
PHP-Default, ohne dass ein Seeder nötig ist. Über **Admin → Formulare**
materialisiert die Aktion «Konfigurieren» diesen Default in eine editierbare
`Objectform`-Zeile (idempotent, reservierter ID-Bereich ≥ 5000) und übergibt an
den normalen Spalten-Editor — siehe
[Konfigurierbare eingebettete Tabellen](../admin/forms.md#konfigurierbare-eingebettete-tabellen)
im Admin-Teil.

## Woran ein Archiv seine Formulare ändert

Über die Oberfläche unter **Admin → Formulare** / **Formtypen**, oder — für
Deployments reproduzierbar — über Seeder. Seeder überschreiben bestehende
Formulare bewusst nicht (`if ($form->antonfields()->count() > 0) return;`), damit
sie ausgelieferte Konfigurationen nicht zerstören.
