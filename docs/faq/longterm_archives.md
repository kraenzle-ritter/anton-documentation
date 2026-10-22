# Anton als digitales Langzeitarchiv 

Anton übernimmt digitale Unterlagen geprüft, erkennt und prüft ihre Formate und hält fest, wie gut sie sich erhalten lassen. Einen Master verändert Anton nur, wo das Archiv es eingerichtet oder veranlasst hat, etwa durch eine Format-Regel bei der Übernahme oder durch eine Migration; beides wird geprüft und am Medium festgehalten. Das gilt für Anton [as a Service](anton_as_service.md) wie für den Betrieb [on Premises](anton_on_premises.md).

Die sogenannte _Bitstream Preservation_, also die eigentliche Datenspeicherung und -sicherung, erbringt die Betriebsinfrastruktur. **Bei Anton as a Service**, also beim Betrieb auf unseren Servern, liegen die digitalen Daten in vier Kopien an drei Standorten: auf dem Produktivserver in einem Rechenzentrum in der Schweiz die Produktionsdaten und eine verschlüsselte lokale Sicherung, dazu je eine Sicherung auf zwei Backupservern an zwei Standorten in Zürich (siehe [Infrastruktur](infrastructure.md)). Die beiden Zürcher Standorte teilen sich die regionalen Risiken; einen weiteren, davon unabhängigen Standort gibt es vorerst nicht.

!!! note "On Premises"
    Wer Anton auf eigenen Servern betreibt, verantwortet die Speicherung, die Redundanz und die Sicherung selbst. Die genannte Infrastruktur ist Teil unseres Betriebs und wird mit der Software nicht mitgeliefert. Gerne beraten wir bei der Einrichtung.

Anton hält für jede Datei eine Prüfsumme vor, sodass sich die Integrität der Daten überprüfen lässt: Ein Prüflauf stellt fest, ob Daten verändert oder beschädigt wurden, und protokolliert das Ergebnis. Den Rhythmus legt ein wiederkehrender Auftrag pro Installation fest; auf unseren Servern läuft er für die grossen Archive. Bei Installationen mit angebundenem Langzeitarchiv (DIMAG) verantwortet dieses die Bitstream-Sicherung. Mehr dazu unter [Langzeitarchivierung: Überblick](../admin/preservation.md).

Der Zugang zu den Daten erfolgt ausschliesslich über Anton, der nur autorisierte Zugriffe ermöglicht. Bei rechtlich geschützten Daten sind allenfalls zusätzliche Kriterien wie etwa der mögliche/erlaubte Serverstandort abzuklären. Die Daten sind aufgrund der Metadaten in Anton jederzeit einfach und schnell auffindbar und verfügbar. 

Bei der Vorbereitung der _Übernahme_ (Bewertung, Ingest, Preingest etc.) und dem _Preservation Planning_ unterstützen wir unsere Kund:innen gerne.

## Preservation Planning 

### Formaterkennung

Die Formaterkennung auf Grundlage des Mime Types bzw. der Dateiendung wird in Anton durch die Integration von [Siegfried](https://www.itforarchivists.com/siegfried) und/oder [Fido](https://github.com/openpreserve/fido) ergänzt. Beide Tools identifizieren Dateiformate anhand der [PRONOM](https://www.nationalarchives.gov.uk/pronom/) IDs. Dies ermöglicht eine präzise Bestimmung von Dateiformaten für die digitale Langzeitarchivierung.

### Risiko Einschätzung

Aus der PRONOM-ID leitet Anton die Risikobewertung des [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation) ab. Sie ist die Grundlage für Entscheidungen über Erhaltungsmassnahmen, etwa die Überführung in ein anderes Format. 

Das [Preservation Planning](../admin/preservation-planning.md) im Admin-Bereich zeigt die im Archiv vorhandenen Dateiformate mit ihrer Risikobewertung. Die Ansicht muss man selbst aufrufen; eine Meldung, wenn ein Format veraltet, gibt es nicht.
