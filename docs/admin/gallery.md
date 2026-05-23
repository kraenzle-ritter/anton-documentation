# Mediengalerie

Die Galerie ist ein Anton-Modul mit einem facettenbasierten Zugang zu
ausgewählten Medien (Bilder, PDFs, Audio, Video). Seit der v0.41–v0.45-
Serie ist sie aus der reinen Bildergalerie zu einer vollwertigen
**Mediengalerie** mit PDF.js-Viewer, Video-Kapiteln und konfigurierbarem
Filter-Layout ausgebaut.

Erreichbar unter `/gallery`.

## Inhalt und Titel

- `gallery_title` (in `Home`-Tabelle, mehrsprachig): Benutzerdefinierter
  Titel der Galerie-Seite

## Bestände

- `gallery_fonds`: Array von Bestands-IDs, deren Medien für interne
  Benutzer:innen sichtbar sind
- `gallery_fonds_extern`: Array von Bestands-IDs, deren Medien öffentlich
  sichtbar sind
- `gallery_show_fonds_select`: Zeigt/verbirgt das Bestands-Dropdown

## Filter

- `gallery_show_keywords_select`: Zeigt/verbirgt das Stichwort-Dropdown
- `gallery_show_media_type_filter`: Zeigt/verbirgt das Medientyp-Dropdown
- `gallery_media_types`: Welche Medientypen wählbar sind, z. B.
  ```json
  {"image/": "Bilder", "application/pdf": "Dokumente"}
  ```
  Diese Einschränkung gilt auch wenn das Dropdown ausgeblendet ist.
- **Zeitraum-Filter (Von / Bis)** mit flexibler Datumseingabe — wird
  konfiguriert über `gallery_filter_fields` (siehe nächster Abschnitt).
- **Volltextsuche** durchsucht Objekttitel und den Volltext der
  Mediendateien (PDF-Textebene über `media_texts`, siehe
  [Weighted Search](weighted-search.md)). Seit v0.51.0 arbeitet die
  Galerie-Volltextsuche mit **Präfix-Matching**: ein Suchbegriff wie
  `alkohol` findet auch `Alkoholkonsum`, `alkoholisch` usw. Wortteile in
  der Mitte werden nicht gefunden (`alkohol` findet **nicht**
  `Methylalkohol`). Mehrere Begriffe werden als AND verknüpft.
- **PDF-Viewer übernimmt Suchbegriff**: Klick auf ein Treffer-PDF
  öffnet PDF.js direkt mit dem aktuellen Suchbegriff vorbelegt (seit
  v0.51.0).

### Konfigurierbares Filter-Layout

Seit v0.42.0 ist das Filter-Bar-Layout pro Tenant konfigurierbar über
das Setting `gallery_filter_fields`. Damit lassen sich Reihenfolge,
Breite und Sichtbarkeit der Filter steuern. Beispiel:

```php
Setting::setValue('gallery_filter_fields', [
    ['name' => 'search',     'width' => 4, 'visible' => true],
    ['name' => 'fonds',      'width' => 3, 'visible' => true],
    ['name' => 'media_type', 'width' => 2, 'visible' => true],
    ['name' => 'date_from',  'width' => 2, 'visible' => true],
    ['name' => 'date_to',    'width' => 2, 'visible' => true],
    ['name' => 'keywords',   'width' => 3, 'visible' => false],
]);
```

Breitenangaben sind Bootstrap-Spalten (1–12). Die Reset-Schaltfläche
ist immer sichtbar (seit v0.42.0).

## Modale Ansichten

Klick auf ein Medium öffnet eine modale Detailansicht. Pro Medientyp:

| Typ | Anzeige |
|---|---|
| **Bild** | Lightbox mit Zoom |
| **PDF** | PDF.js-Viewer mit **integrierter Volltextsuche** (übernimmt den aktuellen Galerie-Suchbegriff als Vorbelegung) |
| **Video** | HTML5-Player mit **Kapitelübersicht** (sofern Kapitel-Daten in `media.custom_properties` hinterlegt sind) |
| **Audio** | HTML5-Player mit **Audio-Overlay**: Titel immer sichtbar, Icons nur bei Hover |

Tooltips für die Medien-Icons sind in vier Sprachen übersetzt
(de/en/fr/it).

## Darstellung

- `list_limit_gallery`: Anzahl Medien pro Seite (Default 25)
- `gallery_image_width`: Bildbreite in Pixel (Default 215)
- `gallery_full_images`: Welche Bildversion beim Modal verlinkt wird:
  `web` (default) oder `master`

**Masonry-Layout** sorgt für optimale Bildanordnung; Bilder werden
nicht abgeschnitten.

## Sichtbarkeit pro Tenant

- **Interne Galerie** (`/gallery`) ist für eingeloggte Nutzer:innen
  sichtbar
- **Öffentliche Galerie** (`/gallery?extern=1` oder direkt `gallery_fonds_extern`)
  zeigt nur Bestände aus `gallery_fonds_extern`. Wird typischerweise
  über eine separate Domain oder ein Menü-Item für externe Besucher:innen
  freigegeben.

Wenn ein Medium das Flag `dont_show_in_gallery = 1` trägt, taucht es
nicht in der Galerie auf — auch wenn der zugehörige Datensatz öffentlich
ist. Verwaltung dieses Flags ist seit v0.66.0 in
[Bulk Media List](bulk-media-list.md) komfortabel pro Filter machbar.

## Performance

- Redundantes Feld `objects.fonds_id` (seit v0.41.0): erlaubt
  schnelle Galerie-Abfragen ohne Closure-Table-Join
- Galerie-Facetten werden in einem **per-Tenant Cache** gehalten
  (`{slug}.gallery.facets.intern` / `…extern`) und über den
  `Media::updated`-Hook invalidiert, wenn `private_media` oder
  `dont_show_in_gallery` sich ändert

## Verwandte Themen

- [Bulk Media List](bulk-media-list.md) — `dont_show_in_gallery` und
  `private_media` pro Filter ein-/ausschalten
- [Weighted Search](weighted-search.md) — Volltext-Indexierung
