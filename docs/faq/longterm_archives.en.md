# Anton as a digital archive

Anton ingests digital records with verification, identifies and validates their formats and records how well they can be preserved. Anton changes a master only where the archive has set it up or asked for it, for example through a format rule on ingest or through a migration; both are verified and recorded on the medium. This applies to Anton [as a Service](anton_as_service.md) as well as to operation [on premises](anton_on_premises.md).

## Basic offer and full package

With Anton as a Service, every subscription includes the **basic offer "Digital Archive"**: storage and backup in four copies at three locations, all checks (checksums, viruses, format identification, format validation), the reports and the replacement of damaged files from the backup. In the basic offer we do not act on our own initiative: we do not review the logs, do not assess the format risks and migrate files only on the archive's instruction. Responsibility for digital preservation then lies with the archive; Anton provides it with the reports and tools for this.

The **full Digital Archive package** can be added to any subscription. It consists of two packages:

- **Additional backup:** a further, independent backup, with different software, at a different provider, in a different place, in Germany or, on request, in Switzerland. No one can delete or overwrite a backup state for 30 days, not even we.
- **Preservation management:** we review the logs every month and clarify anything unusual with the archive, assess the format risks, maintain the format list and format rules and migrate endangered formats on our own initiative. We consult the archive only when a measure needs more storage than booked or causes exceptional effort; we estimate and quote that effort in advance.

Prices with and without the full package are listed in the [offer on anton.ch](https://anton.ch/#pricing); the full package is charged from 2027. In Anton itself, the preservation management package is still called "Technical care" (see [preservation mandate](../admin/preservation-mandate.md)).

!!! note "On premises"
    If you run Anton on your own servers, you are responsible for storage, redundancy and backup yourself. The infrastructure described here and the two packages are part of our operation and are not supplied with the software. We are happy to advise on the setup.

## Storage and backup

So-called _bitstream preservation_, that is the actual storage and backup of the data, is provided by the operating infrastructure. **With Anton as a Service**, the digital data are held in four copies at three locations in Switzerland: on the production server in a data centre, the production data and an encrypted local backup, plus one backup each on two backup servers at two locations in Zurich (see [infrastructure](infrastructure.md)). The two Zurich locations share the regional risks. The additional backup of the full package adds a location independent of them; it has been in trial operation since November 2026.

On ingest, Anton calculates two checksums for every file and checks the entire holdings of each archive against them once a month. If the check finds a changed file, we replace it with the unchanged version from the backup and check it again. Every new file goes through a virus check before ingest; infected files are quarantined. In installations with a connected long-term archive (DIMAG), the latter is responsible for bitstream preservation. More under [long-term preservation: overview](../admin/preservation.md).

Access to the data is only possible through Anton, which allows authorised access only. For legally protected data, additional criteria such as the possible or permitted server location may need to be clarified. Thanks to the metadata in Anton, the data can be found and accessed easily and quickly at any time.

We are happy to support our customers in preparing _ingest_ (appraisal, ingest, pre-ingest etc.) and _preservation planning_.

## Preservation planning

### Format identification

Format identification based on the MIME type or file extension is supplemented in Anton by the integration of [Siegfried](https://www.itforarchivists.com/siegfried) and/or [Fido](https://github.com/openpreserve/fido). Both tools identify file formats by their [PRONOM](https://www.nationalarchives.gov.uk/pronom/) IDs. This allows file formats to be determined precisely for long-term preservation. Anton also opens every new file and checks whether it can be read completely; it checks the entire holdings once a year.

### Risk assessment

From the PRONOM ID, Anton derives the risk assessment of the [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation). It is the basis for decisions on preservation measures, such as conversion to another format.

Anton reassesses the formats of the holdings every night and lists new formats and increased risks in the monthly report. [Preservation planning](../admin/preservation-planning.md) in the admin area shows the file formats present in the archive with their risk assessment. Without the full package, the archive assesses the report itself and commissions migrations; with the full package we do this. The file as delivered is kept in every case.

## OAIS model

The OAIS reference model (Open Archival Information System, ISO 14721) describes the functions of a digital archive and the packages in which records come in and go out: the submission information package (SIP), the archival information package (AIP) and the dissemination information package (DIP). Anton covers the functions as follows:

| Function | What Anton does |
|---|---|
| Ingest | Import from Excel, according to eCH-0160 and E-ARK; upload in the browser or by QR code; virus check, two checksums, format identification by PRONOM, check for readability, conversion according to the format rules |
| Archival storage | Four copies at three locations, backup every night, monthly check with repair from the backup; with the full package the additional backup |
| Data management | Description according to ISAD(G), authority data (GND, Geonames, Wikidata), persistent addresses, preservation events according to PREMIS |
| Preservation planning | Format list and format rules per archive, risk assessment by NARA, migration; with the full package we assess the risks and migrate on our own initiative |
| Access | Public search, ordering and lending; OAI-PMH and REST; export to EAD, Dublin Core, RiC-O, CIDOC CRM and PREMIS; packages according to E-ARK and OCFL |
| Administration | Accounts, roles and permissions; log of all changes; monthly report; with the full package we review the monthly report |

The archival information package does not exist in Anton as a separate file: it consists of the master in storage and of the description, checksums and preservation events in the database. It becomes a package only on export, according to E-ARK or OCFL.

Overview as PDF (German): [Das Digitale Archiv in Anton und das OAIS-Modell](https://anton.ch/docs/anton-oais-modell.pdf).

## NDSA levels

The "Levels of Digital Preservation" of the National Digital Stewardship Alliance (NDSA, USA), version 2.1, are a widely used yardstick for how well an institution preserves digital records. They divide preservation into five areas (storage, integrity, control, metadata, content) and each area into four levels, from "know your content" to "renew and sustain your content". A level counts as reached only when all its requirements are met.

We have assessed Anton as a Service against these levels ourselves, with evidence for every requirement; this is not a certification by an outside body. The basic offer reaches the highest level in two of five areas (integrity and metadata). With the full package it reaches it in all five: the additional backup concerns storage, preservation management concerns control and content. The levels do not measure the archive's professional work, such as whether holdings are fully described and correctly appraised.

The individual requirements are set out in two PDFs (German):

- [Das Digitale Archiv in Anton und die NDSA-Stufen](https://anton.ch/docs/anton-ndsa-stufen.pdf): all 38 requirements with our measure
- [Kurzfassung](https://anton.ch/docs/anton-ndsa-kurzfassung.pdf) (summary)

In both papers the parts of the full package still appear separately, as "Paket Zusätzliche Sicherung" (additional backup) and "Paket Preservation Management".
