# Einstellungen

Anton wird über Einstellungen konfiguriert — rund 180 Stück, jede ein
Schlüssel-Wert-Paar. Gepflegt werden sie über die Admin-Seite unter
**Einstellungen**.

## Aufbau

Jede Einstellung hat neben Schlüssel und Wert:

| Angabe | Bedeutung |
|---|---|
| **Typ** | `boolean`, `string`, `integer` oder `array` (JSON) — bestimmt, wie der Wert eingegeben wird |
| **Bereich** | Die thematische Zuordnung: `theme`, `export`, `search`, `gallery`, `import`, `inge` und weitere |
| **Editierbar** | Ob sich der Wert über die Oberfläche ändern lässt |
| **Beschreibung** | Wozu die Einstellung dient |

Die Beschreibung in der Oberfläche ist die verlässlichste Auskunft über die
**eigene** Installation — sie steht an der Einstellung selbst.

## Wer was ändern darf

| Einstellung | Ändern durch |
|---|---|
| editierbar | Rolle `admin` |
| nicht editierbar | nur Superuser |

Nicht editierbare Einstellungen sind solche, die beim Aufsetzen festgelegt
werden und den Betrieb grundlegend prägen — etwa die Signaturbildung, die
Anbindung an ein Langzeitarchiv oder der Bestellkorb. Sie erscheinen in der
Liste, das Bearbeitungsformular bleibt aber verschlossen. Bei Anton as a Service
ist für Änderungen daran k & r zuständig.

## Leer heisst Vorgabe

Ist eine Einstellung leer, greift die eingebaute Vorgabe — das ist nicht
dasselbe wie «ausgeschaltet». Bei Einstellungen vom Typ `array` ersetzt ein
eigener Wert die Vorgabe zudem **vollständig**; er ergänzt sie nicht.

## Abo und Speicherplatz

| Einstellung | Wert |
|---|---|
| `abo` | `basic`, `standard` oder `pro` |
| `maximum_storage` | Vereinbarter Speicherplatz in GB |

`maximum_storage` wird von `anton:check-disk-space` ausgewertet und erscheint in
den Statistiken unter «Überblick».

## Wo die einzelnen Themen stehen

Die meisten Einstellungen gehören zu einem Thema und sind dort beschrieben:

- [Formulare und Formularsätze](forms.md) — auch das Listen-Layout
  (`form-objects-list`)
- [Wertelisten](valuelists.md) und [Schutzfristen](protection-periods.md)
- [Suchfelder](searchfields.md), [Schnelle Suche](typesense.md),
  [Gewichtete Suche](weighted-search.md)
- [Mediengalerie](gallery.md), [Wasserzeichen](watermarks.md),
  [Dokumente](documents.md)
- [Startseite und Navigation](home.md), [Logo und Favicons](logo.md)
- [Normdaten-Abgleich](authorities.md), [Inge und DIMAG](inge.md),
  [KI-Erschliessung](ai-cataloging.md)

## Die .env-Datei

Ein Teil der Konfiguration liegt nicht in den Einstellungen, sondern in der
Umgebungsdatei der Installation — Datenbankzugang, Mailversand, Serverpfade und
Schalter wie die Freigabe der KI-Erschliessung. Sie ist über die Oberfläche
nicht erreichbar und wird bei der [Installation](installation.md) gesetzt.
