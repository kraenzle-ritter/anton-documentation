# DIP Download

Die Möglichkeit, DIPs einzelner Dossiers als ZIP herunterzuladen, können in das Formular (default, internal, detail) eingebaut werden: `module_word_download`. Der Download wird aber nur für die Verzeichnungsstufen angezeigt die im Setting `level_of_description_ids_for_dip_download` angegeben sind. Für Dossier: `[5]`

Mit dem Setting `dip_creator_class` lässt sich eine Klasse für die Erstellung des Dips angeben. Im Moment gibt es den Standard `CreateDip` (default), der eine Bag erstellt. D.h. es gibt ein md5-manifest, das sämtliche Dateien mit Checksum auflistet. Ausserdem wird eine Worddatei erstellt, die den Inhalt des DIP beschreibt mit weiteren Metadaten (vgl. [Word Findbücher](/admin/download-word)). Sämtliche Verzeichnungseinheiten erstellen Ordner (mit dem Titel als Ordnernamen). In den Ordnern werden die Dateien abgelegt. Diese sind nach der Signatur benannt.

Ausserdem gibt es eine vereinfachte Version (`ZhCreateDip`), die die Ordnerstruktur aus den Titeln erstellt. Wenn eine Verzeichnungseinheit keine Kinder hat, entfällt der Ordner; dafür werden die Medien direkt mit originalem Dateinamen gespeichert.
