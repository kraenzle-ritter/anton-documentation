# DIP herunterladen

Ein **DIP** (Dissemination Information Package) ist ein ZIP-Paket, mit
dem sich ein Datensatz samt allem, was darunter hängt, in einem Schritt
weitergeben lässt — etwa für die Übergabe von Akten an Dritte.

## So geht's

In der Detailansicht eines Datensatzes erscheint — sofern für diese
Erschliessungsstufe freigeschaltet — im Download-Bereich ein Knopf
**„DIP“**. Ein Klick erzeugt das Paket und lädt es sofort herunter. Der
Dateiname ist die Signatur des Datensatzes (z. B. `A.42.1.zip`).

Erscheint kein Knopf, ist der DIP-Download für diese Stufe nicht
vorgesehen. Welche Stufen freigeschaltet sind, legt die Administration
fest.

## Was drin ist

Das ZIP bildet den Datensatz und alle untergeordneten Einheiten als
Ordnerstruktur ab:

- **Mediendateien** aller enthaltenen Einheiten, in Ordnern, die nach den
  Titeln benannt sind,
- ein **Word-Findbuch**, das den Inhalt mit Metadaten beschreibt,
- zu jeder Mediendatei eine kleine **Metadaten-Datei** (Dublin Core),
- **Prüfsummen** (BagIt-Manifest), mit denen sich die Vollständigkeit des
  Pakets später überprüfen lässt.

!!! tip "Grösse"
    Ein DIP enthält **alle** Medien des Datensatzes und seiner
    Untereinheiten. Bei umfangreichen Beständen kann das Paket gross
    werden und die Erstellung einen Moment dauern.

!!! note
    Je nach Archiv kann das Paket auch in einer vereinfachten Form ohne
    Findbuch und Metadaten ausgeliefert werden — dann enthält es nur die
    Ordnerstruktur mit den Originaldateien.
