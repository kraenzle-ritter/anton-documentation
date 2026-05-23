# Mediendateien — Liste und Bulk-Verwaltung

Unter **Admin → Medien → Liste / Bulk** (`/admin/media/list`) finden
Administrator:innen eine paginierte Liste aller Mediendateien des Archivs
mit Filter-Bar, Per-Row-Schaltern und Bulk-Aktionen. Verfügbar seit
**v0.66.0**.

Die Seite löst den ursprünglichen Wunsch aus dem Gosteli-Archiv: mehrere
hundert Digitalisate "nicht in Galerie" setzen, ohne sie einzeln in der
Verwaltung jedes Datensatzes aufzurufen.

## Was die Liste anzeigt

Pro Mediendatei sieht man:

- **ID**
- **Dateiname** (`media.file_name`)
- **Mime-Typ** (z. B. `application/pdf`, `image/jpeg`)
- **Collection** (`image`, `application`, `video`, …)
- **Record** — der Datensatz, an dem die Datei hängt (klickbar)
- **In Galerie** — Schalter (an/aus) für `media.dont_show_in_gallery`
- **Privat** — Schalter (an/aus) für `media.private_media`

Sortierbar nach ID, Dateiname, Mime, Collection, Bytes, Erstelldatum
(Spalten-Header klicken).

## Filter

Eine Filter-Leiste über der Tabelle:

| Filter | Bedeutung |
|---|---|
| **Dateiname enthält** | Substring-Suche (LIKE), case-insensitive. Geeignet, um etwa nach Bestands-Signaturen im Dateinamen zu filtern. |
| **Mime-Typ** | Alle / Bilder / Dokumente / Video / Audio |
| **Collection** | Alle / dynamische Liste aus den im Archiv tatsächlich vorkommenden Werten |
| **nur aus Galerie ausgeblendete** | Zeigt nur Datensätze mit `dont_show_in_gallery = 1` |
| **nur private** | Zeigt nur Datensätze mit `private_media = 1` |

URL-Parameter werden persistiert (Bookmarking möglich): `?search=…&mime=image&col=image`.

## Auswahl und Bulk-Aktionen

In der Tabellen-Kopfzeile:

- Eine **Checkbox** markiert/demarkiert die *aktuelle Seite*
- Ein **Icon-Knopf** daneben (`bi-check2-all`) markiert *alle vom Filter
  betroffenen Datensätze* (Cap 5000)

Sobald etwas markiert ist, erscheint oben eine hellblaue Aktionsleiste:

- **Aus Galerie ausblenden** — setzt `dont_show_in_gallery = 1` bei
  allen markierten
- **In Galerie einblenden** — setzt `dont_show_in_gallery = 0`
- **Privat setzen** — setzt `private_media = 1`
- **Öffentlich setzen** — setzt `private_media = 0`
- **Auswahl aufheben** — leert die Selektion

Auswahl funktioniert über mehrere Seiten hinweg: man kann Seite 1
markieren, weiterblättern, auf Seite 3 nochmal markieren und am Ende eine
Aktion auf alle anwenden.

## Per-Row-Schalter (Optimistic Update)

Klick auf einen der beiden Schalter pro Zeile speichert sofort (kein
expliziter "Speichern"-Knopf). Cache-Invalidierung für die Galerie läuft
automatisch über den `Media::updated`-Hook — die Galerie-Facetten
aktualisieren sich beim nächsten Aufruf von selbst.

## Berechtigung

Hinter der `admin`-Middleware. Editor:innen sehen die Seite nicht.
Granularere Berechtigung (etwa pro Bestand) ist nicht vorgesehen — bei
Bedarf kann man später eine `MediaPolicy` ergänzen.

## Routen

- `GET /admin/media/list` → Livewire-Komponente `Anton\Http\Livewire\Admin\MediaList`

Die Liste ist als zusätzlicher Tab in `/admin/media` integriert
(Reiter "Liste / Bulk", neben Übersicht, Duplikate, PDF-Seiten).
