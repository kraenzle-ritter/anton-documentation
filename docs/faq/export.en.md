# Export

## EAD

Data export to EAD (Encoded Archival Description) is aligned with the requirements of the European archives portal.

## TEI

The descriptors (actors, places, subject keywords) can be exported as TEI (Text Encoding Initiative). Anton can also be connected via REST API as an index database for TEI editions. A TEI header can be generated from the entries for the objects. This can be implemented with a customer-specific class so that the TEI header meets the relevant requirements.

## SQL dump

Admins have the option of generating and downloading a full database dump at any time.

## Word finding aids

Classic finding aids in Word format can be generated for individual fonds. Further adaptations are also possible.

## RDF / linked data (CIDOC CRM, RiC-O, Memobase)

Anton is the **only Swiss archival database** that natively exports all three RDF profiles relevant to the archival landscape:

- **CIDOC CRM 7.1.x with RiC-O 1.1 dual typing** — the most widely adopted model internationally for linked data in the cultural heritage sector (Wikidata, Europeana, GND aggregators, ResearchSpace, Linked Art)
- **Pure RiC-O 1.1** (Records in Contexts Ontology of the International Council on Archives, ICA) — for RiC-O-only consumers such as SPA (Swiss Archival Portal), future ICA portals and RDA-compliant archival systems
- **Memobase profile** (RiC-O with a Memobase-specific JSON-LD context) — directly ingestible into [Memobase](https://memobase.ch), Memoriav's Swiss portal for audiovisual heritage, in accordance with Memoriav convention §9

All profiles are generated from the same data basis and are available in **four serialisations**: RDF/Turtle, JSON-LD, RDF/XML, N-Triples. Access via UI, REST API and CLI. More details: [RDF export documentation](../admin/download-rdf.md).

## Static publication and round trip

An entire (sub-)fonds including its media can be packed into *one* ZIP file
— without a running Anton instance being required for display or
restoration:

- **A+ static bundle** — CIDOC/RiC-O graph plus media, filtered for data
  protection and hostable offline (e.g. GitHub Pages). For *publication*.
- **Native round trip** — Anton's own format plus master media,
  **lossless and re-importable** (`anton:export-native` /
  `anton:import-native`). For *backup and migration* between Anton instances.

This allows small archives to use Anton as an editor and to present their
holdings statically on the web at virtually no cost. A concrete comparison of
the two formats (anton format ↔ CIDOC) and the vision of a static viewer:
[Static publication and round trip](../admin/statische-publikation.md).

## OCFL download

Several Swiss long-term archives (UB Basel, DLZA) expect OCFL (Oxford Common File Layout) for the transfer of holdings. Anton supplies OCFL v1.1 as a ZIP package per object or per fonds, including EAD metadata and the Anton import format for round trips. More: [OCFL download documentation](../admin/download-ocfl.md).

## DIP download

OAIS-compliant DIP packages (Dissemination Information Package) as BagIt ZIP for deliveries to end users. More: [DIP documentation](../admin/download-dip.md).
