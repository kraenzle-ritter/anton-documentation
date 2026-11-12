# Suche über der Liste

Die Suche über der Liste ersetzt die Seite der erweiterten Suche: Ein Klick auf die Lupe öffnet über der Verzeichnungstabelle alle Suchkriterien an einem Ort. Die Tabelle darunter zeigt die Treffer und behält ihre eigenen Filter. Das Archiv schaltet die Suche ein (`record_search`); ohne diese Einstellung bleibt die bisherige Seite der erweiterten Suche.

## Filter über jeder Liste

Über jeder Liste von Verzeichnungseinheiten stehen zwei Filter:

| Filter | Wirkung |
|---|---|
| **Liste filtern** | Text, der in der Liste vorkommen muss |
| **Zeitraum** (von, bis) | Verzeichnungseinheiten, deren Entstehungszeitraum diesen Zeitraum berührt; Einheiten ohne Datierung fallen heraus |

Beide Filter grenzen nur die Liste darunter ein, nicht die übrige Seite. Wie viele Zeilen eine Liste zeigt, steht nicht mehr über der Liste, sondern im [Profil](profile.md) unter «Einträge pro Seite».

## Suchen

Die Lupe öffnet die Suche über der Tabelle. Sie hat:

- **Volltext durchsuchen:** das Suchfeld; es versteht dieselbe Schreibweise wie die [Volltextsuche](search.md) (Anführungszeichen für Phrasen, Minus zum Ausschliessen)
- **Archivbaum:** grenzt die Suche auf einen Teil des Archivs ein und erfasst alles darunter; **Ganzer Archivbaum** hebt die Eingrenzung auf
- **Filter:** die Facetten des Archivs, etwa Verzeichnungsstufe, Objekttyp oder Schlagwörter, mit der Zahl der Treffer
- **Zeitraum:** wie über der Liste
- **Erweiterte Suche:** einzelne Bedingungen auf bestimmte Felder; **Bedingung hinzufügen** fügt eine weitere hinzu, **Anwenden** sucht

Alle Kriterien wirken zusammen. **Suche ausblenden** schliesst den Bereich; die gewählten Kriterien bleiben als Chips über der Tabelle stehen und lassen sich dort einzeln entfernen. **Neue Suche** setzt alles zurück.

Blättern in der Detailansicht, der Weg zurück zur Liste und die Exporte beziehen sich auf die Treffer, die die Tabelle zeigt.

## Volltext aus dem Suchindex

Archive mit [Typesense](../admin/typesense.md) können den Volltext dieser Suche aus dem Suchindex holen (`record_search_index`). Der Suchindex toleriert Tippfehler und findet Treffer im Text von Medien, etwa in PDFs. Archivbaum, Filter, Zeitraum, Sortierung und Seiten kommen weiterhin aus der Datenbank; Tabelle, Trefferzahl und Exporte zeigen darum dieselben Verzeichnungseinheiten.

Findet der Suchindex mehr als 5000 Treffer oder antwortet er nicht, sucht die Datenbank. Interne Konten (ab der Rolle `user_intern`) sehen beim Suchfeld, wer geantwortet hat: «Volltext aus dem Suchindex» oder «Volltext aus der Datenbank».

## Einstellungen

| Einstellung | Wirkung | Vorgabe |
|---|---|---|
| `record_search` | Suche über der Liste statt Seite der erweiterten Suche | aus |
| `record_search_index` | Volltext dieser Suche aus dem Suchindex (setzt Typesense voraus) | aus |
| `list_filters` | Filter über den Listen für Mitarbeitende, in Reihenfolge: `search` (Text), `period` (Zeitraum); leer = keine | beide |
| `list_filters_extern` | dasselbe für die Öffentlichkeit | beide |
| `search_facets_extern` | Filter der Suche für die Öffentlichkeit, Schlüssel wie `search_facets` | wie `search_facets` |

Archive, deren Suche ganz auf Typesense umgestellt ist (`search_typesense_enabled`), holen den Volltext ebenfalls aus dem Suchindex.
