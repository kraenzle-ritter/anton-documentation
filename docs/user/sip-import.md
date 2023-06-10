## SIP Import

Anton ermöglicht den Import von Submission Information Packages (SIP) gemäss eCH-0160. Dabei werden die Dossiers und die Dokumente in die Archivtektonik importiert. 

Zum Standard: https://ech.ch/de/ech/ech-0160/1.2.0

### Voraussetzungen

- Akzessionsarchiv: Ein (gesperrtes) Archiv, dessen ID in das Setting `accessions_archives_id` eingetragen wird.
- Die Archivhierarchie muss bereits in Anton vorhanden sein.
- Falls die Signaturen in der Archivhierarchie Ein Prefix besitzen, muss dieses gesetzt werden (setting: `sip-import-prefix`)
- Formular: 
  - `sip_id`: Enthält die verlinkte Signatur auf den Eintrag des SIP im Akzessionsarchiv (sollte im Formular `default_intern`  sein)
  - `note.sip_md5sum`, `note.actual_backup` sollte im Formular `default_intern` sein (wird auf Bestandsebene/SIP angezeigt)

### Ablauf Anton

- User: Upload des SIP (zip) (`/sip/uploadsip`)
- User: Validierung des SIP (`/sip/validation`)
  - anton can unzip
  - files exist and each hashsum is correct
  - parents for all dossiers found
- User: Start Ingest (`/sip/ingest`)
  - import SIP (`<dossier>` and `<dokument>`/`<datei>`)
  - identifier are uuids
  - Post Import
    - Update Hierarchy (`path`)
    - Set replace uuid and set correct identifiers; also rename media
    - updateDates and fulltext

### Ablauf Ingest mit Inge und DIMAG

- Anton: 
  - Send request to Inge with SIP and Media-IDs
  - Delete Masterfiles of the SIP from Anton-Media (only keep )
  

- Inge: Ingest files into DIMAG
  - Create loadXML (LoadXmlController($slug, $id))
  - Save Ingest Package (LoadXml and files) to DIMAGs SFTP 

- Inge: Send request to Anton and confirm SIP Ingest (`/sip/{id}/confirm`) or revert it (`/sip/{id}/revert`) 


### Todos
- SIP aus Anton löschen: Im Moment wird nur der SIP Eintrag gelöscht, nicht die Einträge und Medien

### Beispiel:

Das Elternelement (`<ordnungssystemposition>`) des `<dossier>` entspricht dem `parent` in Anton. Der `parent` in Anton wird anhand des Inhalts des Elements `<nummer>` im SIP bestimmt. Wenn also zum Beispiel diese Nummer "0.6.6" lautet, die Archivsignatur aber "A.1.4.0.6.6" ist, ist entsprechend das Prefix mit "A.1.4." auszufüllen.
