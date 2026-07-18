# Anton als digitales Langzeitarchiv 

Die digitale Langzeitarchivierung ist eine sehr komplexe und vielschichtige Aufgabe, bei der Anton [as a Service](anton_as_service.md) oder [on Premises](anton_on_premises.md) eingesetzt werden kann.

Die sogenannte _Bitstream Preservation_ – die eigentliche Datenspeicherung und -sicherung – erbringt die Betriebsinfrastruktur, nicht die Anwendung. **Bei Anton as a Service**, also beim Betrieb auf unseren Servern, werden die digitalen Daten auf einer geeigneten Infrastruktur gespeichert, die drei Kopien an drei Standorten vorhält – gesamthaft eine sechsfache Redundanz.

!!! note "On Premises"
    Wer Anton auf eigenen Servern betreibt, verantwortet die Speicherung, die Redundanz und die Sicherung selbst. Die genannte Infrastruktur ist Teil unseres Betriebs und wird mit der Software nicht mitgeliefert. Gerne beraten wir bei der Einrichtung.

Anton hält für jede Datei eine Prüfsumme vor, sodass sich die Integrität der Daten überprüfen lässt – also feststellen, ob Daten verändert oder beschädigt wurden. Diese Prüfung ist kein Automatismus der Anwendung, sondern wird pro Installation als wiederkehrender Auftrag eingerichtet; auf unseren Servern ist sie für die grossen Archive eingerichtet. Bei Installationen mit angebundenem Langzeitarchiv (DIMAG) verantwortet dieses die Bitstream-Sicherung. Mehr dazu unter [Langzeitarchivierung: Überblick](../admin/preservation.md).

Der Zugang zu den Daten erfolgt ausschliesslich über Anton, der nur autorisierte Zugriffe ermöglicht. Bei rechtlich geschützten Daten sind allenfalls zusätzliche Kriterien wie etwa der mögliche/erlaubte Serverstandort abzuklären. Die Daten sind aufgrund der Metadaten in Anton jederzeit einfach und schnell auffindbar und verfügbar. 

Bei der Vorbereitung der _Übernahme_ (Bewertung, Ingest, Preingest etc.) und dem _Preservation Planning_ unterstützen wir unsere Kund:innen gerne.

## Preservation Planning 

### Formaterkennung

Die Formaterkennung auf Grundlage des Mime Types bzw. der Dateiendung wird in Anton durch die Integration von [Siegfried](https://www.itforarchivists.com/siegfried) und/oder [Fido](https://github.com/openpreserve/fido) ergänzt. Beide Tools identifizieren Dateiformate anhand der [PRONOM](https://www.nationalarchives.gov.uk/pronom/) IDs. Dies ermöglicht eine präzise Bestimmung von Dateiformaten für die digitale Langzeitarchivierung.

### Risiko Einschätzung

Mit den PRONOM IDs können wir versuchen, die Risikobewertung des [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation) in Anton zu übernehmen. Diese Bewertung kann helfen, Entscheidungen über notwendige Erhaltungsmaßnahmen zu treffen. 

Im Admin-Bereich von Anton kann eine Übersicht der im Archiv vorhandenen Dateiformate mit ihrer Risikobewertung angezeigt werden.
