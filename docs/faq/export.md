# Export 

## EAD 

Der Datenexport nach EAD (Encoding Archival Description) ist auf die Anforderungen des europäischen Archivportals ausgerichtet. 

## TEI

Die Deskriptoren (Akteure, Orte, Sachschlagworte) können als TEI (Text Encoding Inititive) exportiert werden. Anton kann als Register-Datenbank für TEI Editionen ausserdem per REST-API angebunden werden. Aus den Einträgen zu den Objekten kann ein TEI Header erzeugt werden. Dies kann mit einer kundenspezifischen Klasse implementiert werden, so dass der TEI Header den Anforderungen entspricht.

## SQL-Dump

Für admins gibt es die Möglichkeit, jederzeit einen vollen Datenbank-Dump zu erzeugen und herunterzuladen. 

## Word Findbücher

Von einzelnen Beständen können klassische Findbücher im Wordformat erzeugt werden. Weitergehende Anpassungen sind ebenfalls möglich.

## RDF / Linked Data (CIDOC CRM, RiC-O, Memobase)

Anton ist die **einzige Schweizer Archivdatenbank**, die alle drei in der Archivlandschaft relevanten RDF-Profile nativ exportiert:

- **CIDOC CRM 7.1.x mit RiC-O-1.1-Doppel-Typisierung** — das international am breitesten adoptierte Modell für Linked Data im Kulturerbe-Bereich (Wikidata, Europeana, GND-Aggregatoren, ResearchSpace, Linked Art)
- **Pures RiC-O 1.1** (Records in Contexts Ontology des Internationalen Archivrates ICA) — für RiC-O-only-Konsumenten wie SPA (Swiss Archival Portal), zukünftige ICA-Portale, RDA-konforme Archivsysteme
- **Memobase-Profil** (RiC-O mit Memobase-spezifischem JSON-LD-Context) — direkt einspielbar in [Memobase](https://memobase.ch), das Schweizer Portal für audiovisuelles Erbe der Memoriav, gemäss Memoriav-Konvention §9

Alle Profile werden aus derselben Datenbasis erzeugt und sind in **vier Serialisierungen** verfügbar: RDF/Turtle, JSON-LD, RDF/XML, N-Triples. Zugang über UI, REST-API und CLI. Mehr Details: [RDF-Export-Dokumentation](../admin/download-rdf.md).

## OCFL Download

Mehrere Schweizer Langzeitarchive (UB Basel, DLZA) erwarten OCFL (Oxford Common File Layout) für die Übergabe von Beständen. Anton liefert OCFL v1.1 als ZIP-Paket pro Objekt oder pro Bestand, inkl. EAD-Metadaten und Anton-Import-Format für Round-Trips. Mehr: [OCFL-Download-Dokumentation](../admin/download-ocfl.md).

## DIP Download

OAIS-konforme DIP-Pakete (Dissemination Information Package) als BagIt-ZIP für Endnutzer-Lieferungen. Mehr: [DIP-Dokumentation](../admin/download-dip.md).
