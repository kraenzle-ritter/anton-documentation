# Anton als Digitales Archiv

Anton übernimmt digitale Unterlagen geprüft, erkennt und prüft ihre Formate und hält fest, wie gut sie sich erhalten lassen. Einen Master verändert Anton nur, wo das Archiv es eingerichtet oder veranlasst hat, etwa durch eine Format-Regel bei der Übernahme oder durch eine Migration; beides wird geprüft und am Medium festgehalten. Das gilt für Anton [as a Service](anton_as_service.md) wie für den Betrieb [on Premises](anton_on_premises.md).

## Grundangebot und Vollausbau

Bei Anton as a Service enthält jedes Abonnement das **Grundangebot «Digitales Archiv»**: Speicher und Sicherung in vier Kopien an drei Standorten, alle Prüfungen (Prüfsummen, Viren, Formaterkennung, Formatprüfung), die Berichte und den Ersatz beschädigter Dateien aus der Sicherung. Im Grundangebot handeln wir nicht von uns aus: Wir sehen die Protokolle nicht durch, werten die Formatrisiken nicht aus und migrieren Dateien nur auf Vorgabe des Archivs. Die Verantwortung für die digitale Archivierung liegt dann beim Archiv; Anton stellt ihm dafür die Berichte und Werkzeuge bereit.

Der **Vollausbau Digitales Archiv** lässt sich zu jedem Abonnement dazubuchen. Er besteht aus zwei Paketen:

- **Zusätzliche Sicherung:** eine weitere, unabhängige Sicherung, mit anderer Software, bei einem anderen Anbieter, an einem anderen Ort, in Deutschland oder auf Anfrage in der Schweiz. Jeder Sicherungsstand lässt sich 30 Tage lang von niemandem löschen oder überschreiben, auch nicht von uns.
- **Preservation Management:** Wir sehen die Protokolle monatlich durch und klären Auffälliges mit dem Archiv, werten die Formatrisiken aus, pflegen Formatliste und Formatregeln und migrieren gefährdete Formate von uns aus. Rücksprache halten wir nur, wenn eine Massnahme mehr Speicher braucht als gebucht oder aussergewöhnlichen Aufwand verursacht; diesen schätzen wir vorab und offerieren ihn.

Die Preise mit und ohne Vollausbau stehen im [Angebot auf anton.ch](https://anton.ch/#pricing); verrechnet wird der Vollausbau ab 2027. In Anton selbst heisst das Paket Preservation Management noch «Technische Betreuung» (siehe [Erhaltungsauftrag](../admin/preservation-mandate.md)).

!!! note "On Premises"
    Wer Anton auf eigenen Servern betreibt, verantwortet die Speicherung, die Redundanz und die Sicherung selbst. Die genannte Infrastruktur und die beiden Pakete sind Teil unseres Betriebs und werden mit der Software nicht mitgeliefert. Gerne beraten wir bei der Einrichtung.

## Speicherung und Sicherung

Die sogenannte _Bitstream Preservation_, also die eigentliche Datenspeicherung und -sicherung, erbringt die Betriebsinfrastruktur. **Bei Anton as a Service** liegen die digitalen Daten in vier Kopien an drei Standorten in der Schweiz: auf dem Produktivserver in einem Rechenzentrum die Produktionsdaten und eine verschlüsselte lokale Sicherung, dazu je eine Sicherung auf zwei Backupservern an zwei Standorten in Zürich (siehe [Infrastruktur](infrastructure.md)). Die beiden Zürcher Standorte teilen sich die regionalen Risiken. Einen davon unabhängigen Ort bringt die Zusätzliche Sicherung des Vollausbaus; sie läuft seit November 2026 im Testbetrieb.

Anton berechnet für jede Datei bei der Übernahme zwei Prüfsummen und prüft den ganzen Bestand jedes Archivs einmal im Monat dagegen. Findet die Prüfung eine veränderte Datei, ersetzen wir sie durch die unveränderte Fassung aus der Sicherung und prüfen sie erneut. Jede neue Datei durchläuft vor der Übernahme eine Virenprüfung; befallene Dateien kommen in Quarantäne. Bei Installationen mit angebundenem Langzeitarchiv (DIMAG) verantwortet dieses die Bitstream-Sicherung. Mehr dazu unter [Langzeitarchivierung: Überblick](../admin/preservation.md).

Der Zugang zu den Daten erfolgt ausschliesslich über Anton, der nur autorisierte Zugriffe ermöglicht. Bei rechtlich geschützten Daten sind allenfalls zusätzliche Kriterien wie etwa der mögliche oder erlaubte Serverstandort abzuklären. Die Daten sind aufgrund der Metadaten in Anton jederzeit einfach und schnell auffindbar und verfügbar.

Bei der Vorbereitung der _Übernahme_ (Bewertung, Ingest, Preingest etc.) und dem _Preservation Planning_ unterstützen wir unsere Kund:innen gerne.

## Preservation Planning

### Formaterkennung

Die Formaterkennung auf Grundlage des Mime Types bzw. der Dateiendung wird in Anton durch die Integration von [Siegfried](https://www.itforarchivists.com/siegfried) und/oder [Fido](https://github.com/openpreserve/fido) ergänzt. Beide Tools identifizieren Dateiformate anhand der [PRONOM](https://www.nationalarchives.gov.uk/pronom/) IDs. Dies ermöglicht eine präzise Bestimmung von Dateiformaten für die digitale Langzeitarchivierung. Anton öffnet zudem jede neue Datei und prüft, ob sie sich vollständig lesen lässt; den ganzen Bestand prüft er einmal im Jahr.

### Risiko Einschätzung

Aus der PRONOM-ID leitet Anton die Risikobewertung des [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation) ab. Sie ist die Grundlage für Entscheidungen über Erhaltungsmassnahmen, etwa die Überführung in ein anderes Format.

Anton bewertet die Formate des Bestands jede Nacht neu und nennt im Monatsbericht neue Formate und gestiegene Risiken. Das [Preservation Planning](../admin/preservation-planning.md) im Admin-Bereich zeigt die im Archiv vorhandenen Dateiformate mit ihrer Risikobewertung. Ohne Vollausbau wertet das Archiv den Bericht selbst aus und gibt Migrationen in Auftrag; mit dem Vollausbau übernehmen wir das. Die abgelieferte Datei bleibt in jedem Fall erhalten.

## OAIS-Modell

Das Referenzmodell OAIS (Open Archival Information System, ISO 14721) beschreibt die Funktionen eines digitalen Archivs und die Pakete, in denen Unterlagen hinein- und hinausgehen: das Übernahmepaket (SIP), das Archivpaket (AIP) und das Auslieferungspaket (DIP). Anton deckt die Funktionen so ab:

| Funktion | Was Anton leistet |
|---|---|
| Übernahme (Ingest) | Import aus Excel, nach eCH-0160 und E-ARK; Upload im Browser oder per QR-Code; Virenprüfung, zwei Prüfsummen, Formaterkennung nach PRONOM, Prüfung auf Lesbarkeit, Umwandlung nach den Formatregeln |
| Archivspeicher (Archival Storage) | Vier Kopien an drei Orten, Sicherung jede Nacht, monatliche Prüfung mit Reparatur aus der Sicherung; mit Vollausbau die Zusätzliche Sicherung |
| Datenverwaltung (Data Management) | Verzeichnung nach ISAD(G), Normdaten (GND, Geonames, Wikidata), dauerhafte Adressen, Erhaltungsereignisse nach PREMIS |
| Erhaltungsplanung (Preservation Planning) | Formatliste und Formatregeln je Archiv, Risikobewertung nach NARA, Migration; mit Vollausbau werten wir die Risiken aus und migrieren von uns aus |
| Zugang (Access) | Öffentliche Recherche, Bestellung und Ausleihe; OAI-PMH und REST; Export nach EAD, Dublin Core, RiC-O, CIDOC CRM und PREMIS; Pakete nach E-ARK und OCFL |
| Administration | Konten, Rollen und Befugnisse; Protokoll aller Änderungen; Monatsbericht; mit Vollausbau sehen wir den Monatsbericht durch |

Das Archivpaket liegt in Anton nicht als eigene Datei vor: Es besteht aus dem Master auf dem Speicher und aus Verzeichnung, Prüfsummen und Erhaltungsereignissen in der Datenbank. Als Paket entsteht es erst beim Export, nach E-ARK oder OCFL.

Übersicht als PDF: [Das Digitale Archiv in Anton und das OAIS-Modell](https://anton.ch/docs/anton-oais-modell.pdf).

## NDSA-Stufen

Die «Levels of Digital Preservation» der National Digital Stewardship Alliance (NDSA, USA), Fassung 2.1, sind ein verbreiteter Massstab dafür, wie gut eine Einrichtung digitale Unterlagen erhält. Sie teilen die Erhaltung in fünf Bereiche (Speicher, Integrität, Kontrolle, Metadaten, Dateiformate) und jeden Bereich in vier Stufen, von «Unterlagen kennen» bis «Unterlagen auf Dauer erhalten». Eine Stufe gilt erst als erreicht, wenn alle ihre Anforderungen erfüllt sind.

Wir haben Anton as a Service nach diesen Stufen selbst bewertet, mit Beleg für jede Anforderung; das ist keine Zertifizierung durch eine aussenstehende Stelle. Das Grundangebot erreicht die oberste Stufe in zwei von fünf Bereichen (Integrität und Metadaten). Mit dem Vollausbau sind es alle fünf: Die Zusätzliche Sicherung betrifft den Speicher, das Preservation Management die Kontrolle und die Dateiformate. Nicht messen die Stufen die fachliche Arbeit des Archivs, etwa ob ein Bestand vollständig erschlossen und richtig bewertet ist.

Die Anforderungen im Einzelnen stehen in zwei PDFs (Deutsch):

- [Das Digitale Archiv in Anton und die NDSA-Stufen](https://anton.ch/docs/anton-ndsa-stufen.pdf): alle 38 Anforderungen mit unserer Massnahme
- [Kurzfassung](https://anton.ch/docs/anton-ndsa-kurzfassung.pdf)

In den beiden Papieren stehen die Teile des Vollausbaus noch einzeln, als «Paket Zusätzliche Sicherung» und «Paket Preservation Management».
