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

Keine Koordinaten, keine [Normdaten](authorities.md). Wo ein Standort im Magazin steht, also Stufe, übergeordneter Platz und Kapazität, steht im Kasten [Magazin](#magazin) auf seiner Seite.

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

## Magazin {#magazin}

Standorte lassen sich zu einem Magazin gliedern: Raum, Regal, Segment, Fach und Karton, oder wie das Archiv sein Magazin aufteilt. Wie viel davon ein Archiv nutzt, entscheidet die Einstellung `locations_mode` unter **Admin → Einstellungen**: `list` behält die flache Liste der Standorte, wie sie war, und ist die Vorgabe; `magazine` schaltet das Magazin ein; `off` blendet die Standorte ganz aus.

**Stufen festlegen.** Unter **Admin → Konfiguration → Magazinstufen** legt die Administration die Stufen fest, von oben nach unten, mit Bezeichnung je Sprache. Eine Stufe lässt sich als **Behältnis** kennzeichnen, etwa der Karton: Ein Behältnis belegt auf dem Platz, auf dem es steht, seine ganze Kapazität, ob voll oder leer. Eine Stufe, die Stellplätzen zugewiesen ist, lässt sich nicht löschen.

**Stellplätze anlegen.** Ein Standort hat ein einziges Formular. Im Magazin zeigt seine Seite zusätzlich Pfad, Stufe, Belegung und die Unterstufen; **Unterstufe anlegen** legt einen neuen Standort darunter an, und Anton schlägt die nächste Stufe vor. Beim Bearbeiten stehen unter Name und Beschreibung der übergeordnete Platz («Liegt in»), die Stufe, die Kapazität in Laufzentimetern und die Reihenfolge. Ein Platz kann nicht in sich selbst oder in einem seiner eigenen Unterplätze liegen.

**Pfad.** Wo ein Standort genannt wird, steht sein Pfad, etwa «Raum 1 › Regal 3 › Fach 4 › Karton 17»: auf dem Datensatz, in der Auswahlliste der Maske und der Sammelbearbeitung, in der Bestellmail und im vollen Excel-Export.

**Belegung.** Gezählt wird der Umfang der Verzeichnungseinheiten, die einem Platz selbst zugewiesen sind, über alle Unterstufen zusammen: der eigene Umfang oder, wo keiner erfasst ist, der Umfang darunter, wie ihn die Detailseite zeigt. Ein Bestand, dessen Dossiers in Kartons stehen, zählt über die Kartons, nicht doppelt. Ein Behältnis mit Kapazität zählt auf seinem Fach mit der ganzen Kapazität. Ohne Kapazität zeigt Anton nur, wie viel belegt ist.

**Gliederung und freie Stellplätze.** Im Magazin hat die Seite **Standorte** drei Reiter: **Liste**, **Gliederung** mit dem Magazin als Baum, mit Belegung und Anzahl Datensätze je Platz, und **Freie Stellplätze** mit den Plätzen mit Kapazität, auf denen noch Platz ist, die leersten zuerst, auf Wunsch nur einer Stufe und mit einem Mindestmass.

**Zuweisen in Menge.** Datensätze kommen über die Sammelbearbeitung oder die Excel-Tabelle an ihren Platz. In der Spalte `standort` steht die ID, die Bezeichnung oder der Pfad, mit `›`, `>` oder `/` zwischen den Stufen. Eine Bezeichnung, die mehrere Plätze tragen, etwa «Fach 4», weist Anton als mehrdeutig zurück, statt zu raten; ein Pfad, den es nicht gibt, wird nicht als neuer Standort angelegt.

## Was an einem Standort liegt

Die Detailseite eines Standorts listet die Verzeichnungseinheiten auf, die ihm oder einem Platz darunter zugewiesen sind: Ein Regal zeigt auch, was in seinen Kartons liegt.

## Löschen

Hängen noch Verzeichnungseinheiten an einem Standort, verweigert Anton das Löschen und meldet dies. Die Zuweisungen sind zuerst zu lösen. Ebenso bleibt ein Standort stehen, unter dem noch Plätze liegen; sie sind zuerst zu löschen oder zu verschieben.

## Signaturen mit Standort

In einzelnen Archiven geht die Abkürzung des Standorts in die
[Signatur](identifiers.md) ein. Ist das eingerichtet, erscheint im Fenster
«Neue Datensätze erstellen» ein zusätzliches Auswahlfeld **Standort**.

!!! note "Archivspezifisch"
    Diese Funktion setzt eine eigens dafür programmierte Signaturbildung voraus.
    Das Standardschema verwendet den Standort nicht — das Auswahlfeld bliebe
    dort wirkungslos. Ob die eigene Installation eine solche Signaturbildung
    mitbringt, weiss bei Anton as a Service k & r.
