# Anton als digitales Langzeitarchiv 

Die digitale Langzeitarchivierung ist eine sehr komplexe und vielschichtige Aufgabe, bei der Anton as a Service oder on Premises eingesetzt werden kann. Für die sogenannte _Bitstream Preservation_, also die eigentliche Datenspeicherung und -sicherung, erfüllt Anton alle Anforderungen: Die digitalen Daten werden auf einer geeigneten Infrastruktur gespeichert, die drei Kopien an drei Standorten vorhält – gesamthaft eine sechsfache Redundanz.

Anton hält für jede Datei eine Prüfsumme vor, sodass sich die Integrität der Daten überprüfen lässt – also feststellen, ob Daten verändert oder beschädigt wurden. Diese Prüfung lässt sich pro Installation als wiederkehrender Auftrag einrichten; für die grossen Archive ist sie eingerichtet. Bei Installationen mit angebundenem Langzeitarchiv (DIMAG) verantwortet dieses die Bitstream-Sicherung. Mehr dazu unter [Langzeitarchivierung: Überblick](../admin/preservation.md).

Der Zugang zu den Daten erfolgt ausschliesslich über Anton, der nur autorisierte Zugriffe ermöglicht. Bei rechtlich geschützten Daten sind allenfalls zusätzliche Kriterien wie etwa der mögliche/erlaubte Serverstandort abzuklären. Die Daten sind aufgrund der Metadaten in Anton jederzeit einfach und schnell auffindbar und verfügbar. 

Bei der Vorbereitung der _Übernahme_ (Bewertung, Ingest, Preingest etc.) und dem _Preservation Planning_ unterstützen wir unsere Kunden gerne.

## Preservation Planning 

### Formaterkennung

Die Formaterkennung auf Grundlage des Mime Types bzw. der Dateiendung wird in Anton durch die Integration von [Siegfried](https://www.itforarchivists.com/siegfried) und/oder [Fido](https://github.com/openpreserve/fido) ergänzt. Beide Tools identifizieren Dateiformate anhand der [PRONOM](https://www.nationalarchives.gov.uk/pronom/) IDs. Dies ermöglicht eine präzise Bestimmung von Dateiformaten für die digitale Langzeitarchivierung.

### Risiko Einschätzung

Mit den PRONOM IDs können wir versuchen, die Risikobewertung des [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation) in Anton zu übernehmen. Diese Bewertung kann helfen, Entscheidungen über notwendige Erhaltungsmaßnahmen zu treffen. 

Im Admin-Bereich von Anton kann eine Übersicht der im Archiv vorhandenen Dateiformate mit ihrer Risikobewertung angezeigt werden.
