# Description archivistique

## Description à plusieurs niveaux selon l'ISAD(G)

Anton a été conçu comme une mise en œuvre de la norme ISAD(G) et l'applique intégralement. La description hiérarchique est possible à n'importe quelle profondeur. Les niveaux de description prévus sont les suivants : Archives, Groupe de fonds, Fonds, Série, Classe, Dossier, Pièce. Tous les niveaux à l'exception du fonds peuvent être répétés autant de fois que nécessaire à l'intérieur d'eux-mêmes.

Les différentes zones d'information de l'ISAD(G) sont mises en œuvre sous forme d'un ou plusieurs champs de texte, de listes de valeurs et/ou d'événements Anton.

## Attribution automatique des cotes
Anton attribue automatiquement les cotes à partir de la cote du fonds, mais celles-ci peuvent être remplacées à tout moment. Différentes options existent pour l'attribution des cotes. Il est également possible de programmer de nouveaux générateurs de cotes et de les activer pour des installations particulières.

## Événements Anton
La gestion séparée des acteur·trice·s (personnes, organisations, etc.) et leur mise en relation avec les unités de description au moyen d'événements traduit également des idées conceptuelles de Records in Contexts (cf. [https://www.ica.org/en/records-in-contexts-conceptual-model](https://www.ica.org/en/records-in-contexts-conceptual-model)). Les «&nbsp;événements Anton&nbsp;» contiennent le type d'événement (p. ex. «&nbsp;création&nbsp;»), une date ou une période, éventuellement un acteur·trice, un lieu et une description plus détaillée.

Anton propose des types d'événement prédéfinis, notamment :

- création  
- versement  
- provenance  
- reproduction  
- numérisation  
- réception  
- conférence  

## Calcul automatique des dates extrêmes
L'événement Anton «&nbsp;création&nbsp;» n'est saisi qu'au niveau de description le plus bas. Anton calcule ensuite automatiquement les dates extrêmes des unités de description des niveaux supérieurs.

## Importance matérielle (calcul automatique)
Dans Anton, les mètres linéaires sont saisis par fonds. Ils sont ensuite cumulés pour les groupes de fonds et pour les archives. Pour les dossiers et les pièces, il est recommandé de saisir l'importance matérielle à l'aide des champs type d'objet et importance matérielle (nombre d'unités). Un champ descriptif est également disponible à cet effet.

## Descripteurs
Outre les événements Anton, qui décrivent l'interaction d'un acteur·trice avec l'unité de description, les acteur·trice·s, les lieux et les mots-clés peuvent aussi être utilisés directement comme descripteurs pour décrire le contenu. Ce type de description est particulièrement intéressant pour les collections audiovisuelles.

## Mise en forme et liens dans les champs de texte
Dans ses champs de texte, Anton comprend Markdown ([https://fr.wikipedia.org/wiki/Markdown](https://fr.wikipedia.org/wiki/Markdown)), un langage de balisage simple. Ainsi, les titres et les listes, par exemple, sont mis en forme pour l'affichage dans le navigateur. Il est également facile d'insérer des liens vers des sites externes, vers des unités de description apparentées ou vers d'autres pages d'Anton.

![Saisie de texte en Markdown](images/markdown_input.png)
Saisie de texte en Markdown. Les titres sont marqués par ## ; dans les listes, les lignes commencent simplement par - ou *.

![Texte dans la vue HTML](images/markdown_rendered.png)
Texte dans la vue HTML. Les titres sont affichés comme tels. La liste est également mise en forme.

## Linked data et données d'autorité
Les descripteurs acteur·trice·s, lieux et mots-clés peuvent être liés facilement à des bases de données externes ou à des référentiels d'autorité. Différentes ressources sont disponibles par défaut :

- Wikipedia  
- Wikidata  
- GND  
- Geonames  
- Ortsnamen  
- Metagrid  
- saisie manuelle  

Lorsqu'un lieu est lié à Geonames, les coordonnées géographiques sont également enregistrées et une carte localisant le lieu s'affiche.

D'autres ressources sont liées automatiquement lorsqu'une recherche par l'un des identifiants a abouti.

La saisie manuelle de ressources (liens externes) est également possible.

## Intégration de documents et de médias audiovisuels
Une ou plusieurs images et d'autres médias (PDF, son, vidéo) peuvent être associés à chaque unité de description. L'attribution se fait par glisser-déposer ou par import Excel. Pour décrire les images de manière optimale (p. ex. par indexation), il est recommandé de les saisir au niveau de la pièce. La galerie d'images peut alors être exploitée au mieux (cf. p. ex. [https://archives.georgfischer.com/gallery](https://archives.georgfischer.com/gallery) ou [https://bahnarchiv.ch](https://bahnarchiv.ch)).

La plupart des archives utilisent aussi Anton comme archive numérique à long terme pour leurs médias. Il est alors important que les médias aient été validés au préalable (pre-ingest) et convertis dans des formats appropriés. Anton conserve et gère la version d'archivage (p. ex. TIFF) et crée des copies de consultation (p. ex. JPEG) en différentes résolutions pour les utilisateur·trice·s externes. Les versions d'archivage sont enregistrées avec une somme de contrôle, de sorte que l'intégrité des fichiers peut être vérifiée rapidement par la suite.

## Différents formulaires de saisie et d'affichage
Par défaut, le jeu de formulaires du niveau de description correspondant est attribué à chaque unité de description. Pour les fonds, ce sont ainsi plutôt les champs de la zone d'information «&nbsp;contexte&nbsp;» qui sont affichés, tandis qu'au niveau de la pièce ce sont plutôt les champs relatifs aux caractéristiques matérielles. Il est également possible de créer des jeux de formulaires spécifiques et de les attribuer manuellement à une unité de description. Chaque formulaire peut être adapté rapidement et simplement.

Un jeu de formulaires se compose de 3 formulaires : saisie (Edit), vue interne (détail interne) et vue externe (détail externe). Les formulaires définissent quels champs de données sont visibles dans quel contexte. Le formulaire «&nbsp;détail interne&nbsp;» contient typiquement le champ «&nbsp;remarques internes des archives&nbsp;». Si ce champ n'est pas repris dans le formulaire «&nbsp;détail externe&nbsp;», les «&nbsp;remarques internes des archives&nbsp;» ne sont visibles que pour les utilisateur·trice·s internes, les éditeur·trice·s et les administrateur·trice·s.

## Accroissements
Anton ne dispose pas d'un module d'accroissement dédié. Les fonds nouvellement entrés peuvent en revanche être créés dans Anton en étant bloqués/invisibles pour le public (par exemple dans un sous-fonds invisible) ; l'historique des accroissements d'un fonds peut d'une part être décrit dans le champ accroissements/nouvelles entrées (ISAD(G) 3.3.3). D'autre part, les versements individuels peuvent être documentés au moyen du module de formulaire «&nbsp;versement&nbsp;» (pour chaque versement, une entrée est créée avec la date, le service versant et un commentaire, puis affichée dans la notice du fonds).
