## SIP Ingest

Anton enables the import/ingest of Submission Information Packages (SIP) in accordance with eCH-0160, whereby the files (dossiers) and documents are imported into the archive tectonics.

Zum Standard: [https://ech.ch/de/ech/ech-0160/1.2.0](https://ech.ch/de/ech/ech-0160/1.2.0)

### Requrirements

#### Anton
- Accession archive (Akzessionsarchiv): A (locked) archive whose ID is entered in the `accessions_archives_id` setting.
- The archive hierarchy (parents) must already exist in Anton.
- If the identifiers in the archive hierarchy have a prefix, this must be set (setting: identifier-prefix)
- With the setting strict_sip_validation, Anton issues an error during validation if a file is not found in the SIP.
- Anton Form (default_intern): 
  - sip_id: Contains the linked signature to the entry of the SIP in the accession archive (should be default_internal in the form)
  - note.sip_md5sum, note.actual_backup should be in the default_internal form (displayed at fonds level/SIP)

!!! note "Example for the setting identifier-prefix"
    The parent element (`<ordnungssystemposition>`) of the `<dossier>` corresponds to the `parent` in Anton. The `parent` in Anton is determined based on the content of the `<number>` element in the SIP. For example, if this number is "0.6.6", but the archive signature is "A.1.4.0.6.6", the prefix must be filled in accordingly with "A.1.4.".

<!--
### Requrirements

#### Anton
- Akzessionsarchiv: Ein (gesperrtes) Archiv, dessen ID in das Setting `accessions_archives_id` eingetragen wird.
- Die Archivhierarchie (`parents`) muss bereits in Anton vorhanden sein.
- Falls die Signaturen in der Archivhierarchie ein Prefix besitzen, muss dieses gesetzt werden (setting: `identifier-prefix`)
- Mit dem Setting `strict_sip_validation` gibt Anton bei der Validierung einen Fehler aus, wenn eine Datei im SIP nicht gefunden wird.

- Anton Formular (default_intern): 
    - `sip_id`: Enthält die verlinkte Signatur auf den Eintrag des SIP im Akzessionsarchiv (sollte im Formular `default_intern`  sein)
    - `note.sip_md5sum`, `note.actual_backup` sollte im Formular `default_intern` sein (wird auf Bestandsebene/SIP angezeigt)

!!! note "Beispiel zum identifier-prefix"
    Das Elternelement (`<ordnungssystemposition>`) des `<dossier>` entspricht dem `parent` in Anton. Der `parent` in Anton wird anhand des Inhalts des Elements `<nummer>` im SIP bestimmt. Wenn also zum Beispiel diese Nummer "0.6.6" lautet, die Archivsignatur aber "A.1.4.0.6.6" ist, ist entsprechend das Prefix mit "A.1.4." auszufüllen.
-->
