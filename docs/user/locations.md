# Standorte

Ein Standort ist der physische Aufbewahrungsort des Originals — Magazin, Depot,
Raum, Regal. Standorte sind eigene Datensätze und werden über
**Admin → Standorte** gepflegt.

!!! note "Nicht für die Öffentlichkeit"
    Der Standort-Datensatz selbst ist ausschliesslich für interne
    Benutzer:innen, Bearbeitende und die Administration sichtbar, nie für
    Aussenstehende — wo etwas liegt, geht die Öffentlichkeit nichts an.

    Das **Feld** «Standort» einer Verzeichnungseinheit ist davon getrennt:
    Neuinstallationen liefern es aus den öffentlichen (externen) Formularen
    entfernt aus, sodass «Standort: …» im öffentlichen Katalog nicht erscheint.
    Bestehende Installationen bleiben unverändert — dort ist das Feld bei Bedarf
    selbst über die [Formulare](../admin/forms.md) aus den externen Formularen
    zu nehmen.

## Erfassen

Der Standort ist bewusst schlank gehalten und kennt nur vier Felder:

| Feld | Zweck |
|---|---|
| ID | wird vergeben |
| Abkürzung | Kurzform, z.B. `M2` |
| Name | Klartext, z.B. «Magazin 2, Regal C» |
| Beschreibung | Freitext |

Keine Typen, keine Koordinaten, keine [Normdaten](authorities.md).

!!! note "Berechtigung"
    Standorte anlegen, ändern und löschen setzt die Rolle `editor` voraus.
    Ansehen können sie interne Benutzer:innen (`user_intern`) — anders als
    Akteur:innen, Orte und Schlagwörter sind Standorte gar nicht öffentlich.

## Zuweisen

Eine Verzeichnungseinheit wird dem Standort im Feld **Standort** zugewiesen. Es
steht im Abschnitt «Sachverwandte Unterlagen» und ist eine Auswahlliste.

Eine Verzeichnungseinheit hat höchstens **einen** Standort. Ob das Feld in der
Maske erscheint, hängt vom [Formularsatz](forms.md) ab — im Standard führen es
Dossier, Serie und Einzelstück, nicht aber Archiv und Bestand.

!!! tip "Standort oder Standortangabe?"
    Nicht zu verwechseln sind zwei Felder mit ähnlichem Namen:

    - **Standort** — die Auswahl aus den erfassten Standorten, eine echte
      Verknüpfung. Danach lässt sich auswerten.
    - **Standort (Detail)** — ein Textfeld für ergänzende Angaben, ohne
      Verknüpfung.

## Was an einem Standort liegt

Die Detailseite eines Standorts listet — wie bei Akteur:innen und Orten — alle
Verzeichnungseinheiten auf, die ihm zugewiesen sind.

## Löschen

Hängen noch Verzeichnungseinheiten an einem Standort, verweigert Anton das
Löschen und meldet dies. Die Zuweisungen sind zuerst zu lösen.

## Signaturen mit Standort

In einzelnen Archiven geht die Abkürzung des Standorts in die
[Signatur](identifiers.md) ein. Ist das eingerichtet, erscheint im Fenster
«Neue Datensätze erstellen» ein zusätzliches Auswahlfeld **Standort**.

!!! note "Archivspezifisch"
    Diese Funktion setzt eine eigens dafür programmierte Signaturbildung voraus.
    Das Standardschema verwendet den Standort nicht — das Auswahlfeld bliebe
    dort wirkungslos. Ob die eigene Installation eine solche Signaturbildung
    mitbringt, weiss bei Anton as a Service k & r.
