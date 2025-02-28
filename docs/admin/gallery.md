# Bildgalerie

Sämtliche Bilder werden über die Route `/gallery` in einer Bildgalerie angezeigt. 

Auswahl Bestände: Es können bestimmte Bestände festgelegt werden, die für die Galerie verwendet werden sollen (Einstellungen `gallery_fonds` und `gallery_fonds_extern`; beide Felder enthalten ein array der IDs der Bestände).

Auswahlfeld Bestände: Ob in der Galerie nach Beständen gefiltert werden kann wird mit der Einstellung `gallery_show_fonds_select` festgelegt.

Auswahlfeld Schlagworte: Ob in der Galerie nach Beständen gefiltert werden kann wird mit der Einstellung `gallery_show_keywords_select` festgelegt.

Wie viele Bilder auf einer Seite der Galerie angezeigt werden sollen, wird mit `list_limit_gallery` festgelegt. Da die Anordnung der Bilder erst nach vollständigem Laden der Bilder erfolgt, ist auszutesten, welche Anzahl für die Userexpirience noch OK ist.

Klickt man auf ein Bild gibt es zwei Optionen: Mit dem Link-Symbol kommt man in die Archivdatenbank, also zum Eintrag der Verzeichnungseinheit, die dieses Bild enthält. Mit dem Lupensymbol öffnet sich ein Modal, in dem mit [Open Seadragon](https://openseadragon.github.io/) eine grössere Version der Bilder angezeigt wird. Für die Vorschau werden thumbs mit 230px Breite verwendet, für die vergrösserten Bilder können entweder die Webversionen (aktuell 1200px Breite) verwendet werden oder die Originale (dafür muss in der Einstellung `gallery_full_images` «master» eingetragen werden). Mit den verschiedenen Einstellungen kann die Galerie etwas angepasst werden.
