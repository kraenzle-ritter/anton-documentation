# SIP Ingest (eCH-0160)

Anton ermöglicht den Import/Ingest von Submission Information Packages (SIP) nach eCH-0160, wobei die Dossiers und Dokumente in die Archivtektonik übernommen werden.

Zum Standard: [https://ech.ch/de/ech/ech-0160/1.2.0](https://ech.ch/de/ech/ech-0160/1.2.0)

!!! note "Unified Import Hub"
    Alle Import-Pfade — SIP, Excel, Verzeichnis, agate — sind unter `/import` zusammengefasst (vier Tabs). Die alten URLs (`/sip/validation`, `/sip/ingest`, `/sip/inbox`) leiten transparent auf den passenden Tab um. Siehe [user/import.md](../user/import.md) für die UI-Übersicht.

!!! note "agate-SIP-Import"
    BagIt-SIPs, die von agate (Anton-Vorbereitungs-Tool) per HTTP geschickt werden, laufen über einen eigenen Pfad mit NARA-Kategorie-Mapping und Eingangskorb. Details: [agate-sip.md](agate-sip.md).

### Voraussetzungen

#### Anton
- Akzessionsarchiv: nicht nötig. Ein SIP-Ingest steht als Lauf im Importprotokoll (siehe [Import](../user/import.md#import-protokoll)).
- Die Archivhierarchie (`parents`) muss bereits in Anton vorhanden sein.
- Falls die Signaturen in der Archivhierarchie ein Prefix besitzen, muss dieses gesetzt werden (Setting: `identifier-prefix`).
- Mit dem Setting `strict_sip_validation` gibt Anton bei der Validierung einen Fehler aus, wenn eine Datei im SIP nicht gefunden wird.
- Anton-Formular (`default_intern`):
    - `sip_id`: verlinkt auf den Lauf im Importprotokoll, aus dem dieser Datensatz stammt (sollte im Formular `default_intern` sein).

!!! note "Beispiel zum identifier-prefix"
    Das Elternelement (`<ordnungssystemposition>`) des `<dossier>` entspricht dem `parent` in Anton. Der `parent` in Anton wird anhand des Inhalts des Elements `<nummer>` im SIP bestimmt. Wenn also zum Beispiel diese Nummer "0.6.6" lautet, die Archivsignatur aber "A.1.4.0.6.6" ist, ist entsprechend das Prefix mit "A.1.4." auszufüllen.

### Ablauf

1. **Validieren:** Anton prüft Schema, Dateien und Prüfsummen, die Elternelemente und die Importdaten. Der gespeicherte Prüfbericht führt Fehler und Warnungen vollständig auf, erfolgreich geprüfte Dateien als eine Zahl. Die Zeile je Datei zeigt `php artisan sip:check --path=<datei> --validate --env=<slug>`.
2. **Importieren:** Der Import läuft im Hintergrund als Lauf im [Importprotokoll](../user/import.md#import-protokoll). Anton zeigt den Lauf mit seinem Fortschritt; scheitert er, steht der Grund dort.
