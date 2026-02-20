# Bildgalerie

Die Galerie ist ein Anton-Modul, das einen besonderen Zugang zu ausgewählten Medien (Bilder, PDFs, Audio, Video) ermöglicht.

## Inhalt und Titel

- `gallery_title` (Home): Benutzerdefinierter Titel für die Galerie

## Bestände

- `gallery_fonds`: Array von Bestands-IDs für interne Benutzer
- `gallery_fonds_extern`: Array von Bestands-IDs für externe Benutzer
- `gallery_show_fonds_select`: Zeigt/verbirgt das Bestands-Dropdown

## Filter

- `gallery_show_keywords_select`: Zeigt/verbirgt das Stichwort-Dropdown
- `gallery_show_media_type_filter`: Zeigt/verbirgt das Medientyp-Dropdown
- `gallery_media_types`: Array der verfügbaren Medientypen, z.B. `{"image/": "Bilder", "application/pdf": "Dokumente"}`. Diese Einschränkung gilt auch wenn das Dropdown ausgeblendet ist.

## Darstellung

- `list_limit_gallery`: Anzahl Medien pro Seite (Standard: 25)
- `gallery_image_width`: Bildbreite in Pixel (Standard: 215)
- `gallery_full_images`: Welche Bildversion verlinkt wird: `web` oder `master`

## Funktionen

Die Galerie bietet:

- Volltextsuche (durchsucht Objekttitel und PDF-Inhalte)
- Facettierte Filter für Bestände, Stichwörter und Medientypen
- Modale Ansichten für Bilder, PDFs, Audio und Video
- Masonry-Layout für optimale Bildanordnung

## Link

Der Link zur Galerie: `/gallery`
