# Standorte

Ein Standort ist der physische Aufbewahrungsort des Originals — Magazin, Depot,
Raum, Regal. Standorte sind eigene Datensätze und werden über
**Admin → Standorte** gepflegt.

!!! note "Nie öffentlich"
    Standorte sind die einzigen Normdaten, die Aussenstehenden nie angezeigt
    werden. Sie sind ausschliesslich für interne Benutzer, Bearbeitende und die
    Administration sichtbar — wo etwas liegt, geht die Öffentlichkeit nichts an.

## Erfassen

Der Standort ist bewusst schlank gehalten und kennt nur vier Felder:

| Feld | Zweck |
|---|---|
| ID | wird vergeben |
| Abkürzung | Kurzform, z.B. `M2` |
| Name | Klartext, z.B. «Magazin 2, Regal C» |
| Beschreibung | Freitext |

Keine Typen, keine Koordinaten, keine [Normdaten](authorities.md).

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
