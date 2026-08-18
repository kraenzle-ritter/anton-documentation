# Export

## EAD

L'export des données en EAD (Encoded Archival Description) est aligné sur les exigences du portail européen des archives.

## TEI

Les descripteurs (acteur·trice·s, lieux, mots-clés matière) peuvent être exportés en TEI (Text Encoding Initiative). Anton peut en outre être connecté par API REST comme base d'index pour des éditions TEI. Un en-tête TEI peut être généré à partir des notices des objets. Cela peut être mis en œuvre au moyen d'une classe propre au client, afin que l'en-tête TEI réponde aux exigences requises.

## Dump SQL

Les administrateur·trice·s ont la possibilité de générer et de télécharger à tout moment un dump complet de la base de données.

## Instruments de recherche Word

Des instruments de recherche classiques au format Word peuvent être générés pour certains fonds. Des adaptations plus poussées sont également possibles.

## RDF / linked data (CIDOC CRM, RiC-O, Memobase)

Anton est la **seule base de données archivistique suisse** à exporter nativement les trois profils RDF pertinents pour le paysage archivistique :

- **CIDOC CRM 7.1.x avec double typage RiC-O 1.1** — le modèle le plus largement adopté au niveau international pour le linked data dans le domaine du patrimoine culturel (Wikidata, Europeana, agrégateurs GND, ResearchSpace, Linked Art)
- **RiC-O 1.1 pur** (Records in Contexts Ontology du Conseil international des archives, ICA) — pour les consommateurs exclusivement RiC-O tels que SPA (Swiss Archival Portal), les futurs portails de l'ICA et les systèmes archivistiques conformes à RDA
- **Profil Memobase** (RiC-O avec un contexte JSON-LD propre à Memobase) — directement intégrable dans [Memobase](https://memobase.ch), le portail suisse du patrimoine audiovisuel de Memoriav, conformément à la convention Memoriav §9

Tous les profils sont générés à partir des mêmes données et sont disponibles en **quatre sérialisations** : RDF/Turtle, JSON-LD, RDF/XML, N-Triples. Accès via l'interface, l'API REST et la CLI. Plus de détails : [documentation de l'export RDF](../admin/download-rdf.md).

## Publication statique et round trip

Un fonds (ou sous-fonds) entier, médias compris, peut être empaqueté dans *un
seul* fichier ZIP — sans qu'une instance Anton en fonctionnement soit
nécessaire pour l'affichage ou la restauration :

- **A+ Static Bundle** — graphe CIDOC/RiC-O et médias, filtrés selon les
  exigences de protection des données et hébergeables hors ligne (p. ex. sur
  GitHub Pages). Pour la *publication*.
- **Round trip natif** — le format propre à Anton et les médias master,
  **sans perte et réimportables** (`anton:export-native` /
  `anton:import-native`). Pour la *sauvegarde et la migration* entre instances
  Anton.

Les petites archives peuvent ainsi utiliser Anton comme éditeur et présenter
leur fonds de manière statique sur le web pour un coût quasi nul. Une
comparaison concrète des deux formats (format anton ↔ CIDOC) et la vision d'un
visualiseur statique : [Publication statique et round trip](../admin/statische-publikation.md).

## Téléchargement OCFL

Plusieurs archives suisses de conservation à long terme (UB Bâle, DLZA) attendent le format OCFL (Oxford Common File Layout) pour la remise de fonds. Anton livre OCFL v1.1 sous forme de paquet ZIP par objet ou par fonds, métadonnées EAD et format d'import Anton compris pour les round trips. Plus : [documentation du téléchargement OCFL](../admin/download-ocfl.md).

## Téléchargement DIP

Paquets DIP conformes à l'OAIS (Dissemination Information Package) sous forme de ZIP BagIt pour les livraisons aux utilisateur·trice·s finaux. Plus : [documentation DIP](../admin/download-dip.md).
