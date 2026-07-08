# Schnelle Suche

Die schnelle Suche (`/search-v2`) ist eine Sofortsuche: Treffer
erscheinen schon während des Tippens, lassen sich über eine Seitenleiste
filtern und sind als gemischte, nach Relevanz sortierte Liste aus
Objekten **und** PDF-Volltext aufbereitet.

!!! info "Pro-Feature"
    Die schnelle Suche steht Pro-Kunden zur Verfügung und läuft parallel
    zur klassischen [Volltextsuche](search.md). Was durchsucht wird und wie
    sich die Suche grundsätzlich verhält (Wortanfänge, UND-Verknüpfung,
    interne Sicht), ist dort beschrieben und gilt hier ebenso.

## Suchen

Suchbegriff oben eingeben — die Trefferliste aktualisiert sich sofort.
Jeder Treffer zeigt:

- ein Typ-Kennzeichen (**Objekt** mit Objekttyp, oder **PDF** für einen
  Volltext-Treffer in einem Dokument),
- die Erschliessungsstufe und den Pfad (Bestand → Serie → …),
- einen hervorgehobenen Textausschnitt der Fundstelle,
- ein Vorschaubild, falls vorhanden.

Bei leerer Eingabe wird (sofern aktiviert) eine Browse-Liste der neuesten
Datensätze gezeigt, sodass die Seite nie leer ist.

## Filtern (Seitenleiste)

Die Seitenleiste bietet Facetten mit Trefferzahlen. Je nach Archiv
verfügbar:

- **Erschliessungsstufe**, **Objekttyp**, **Medien** (mit/ohne)
- **Akteur:innen**, **Schlagwörter**, **Orte** — bei vielen Werten mit
  einem Suchfeld zum schnellen Eingrenzen
- **Zeitraum** — ein Schieber mit zwei Griffen (von/bis); die Werte
  lassen sich auch direkt eintippen

Mehrere Werte innerhalb einer Facette wirken als „oder", verschiedene
Facetten als „und". **Filter zurücksetzen** leert die Auswahl.

!!! note "Nur sichtbare Facetten"
    Facetten, für die ein Archiv keine Werte führt (z. B. keine Orte),
    werden automatisch ausgeblendet.

## Sortieren

Über das Sortier-Menü: **Relevanz** (Standard), **Datum (neueste
zuerst)** oder **Datum (älteste zuerst)**.

## Teilen & Verlinken

Der komplette Suchzustand steht in der Adresszeile — Suchbegriff, Filter,
Zeitraum und Sortierung. Die URL kann **gespeichert oder geteilt** werden
und stellt die Suche samt Filtern wieder her.

## Weitere Hilfen

- **Autocomplete** in der Navigationsleiste schlägt schon beim Tippen
  Treffer vor.
- **„Meinten Sie …?"** bietet bei wenig/keinen Treffern eine korrigierte
  Schreibweise an.
- Die **letzten Suchen** werden lokal im Browser angeboten.

## Sichtbarkeit

Wie in der klassischen Suche sehen Sie nur, was Sie sehen dürfen.
Gesperrte (embargierte) PDF-Inhalte erscheinen nicht in der öffentlichen
Suche, auch wenn die beschreibenden Daten zum Suchbegriff passen.
