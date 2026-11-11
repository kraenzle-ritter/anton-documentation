# Anton comme archive numérique

Anton prend en charge les documents numériques avec vérification, identifie et valide leurs formats et consigne dans quelle mesure ils peuvent être conservés. Anton ne modifie un master que là où l'archive l'a configuré ou demandé, par exemple au moyen d'une règle de format lors de la prise en charge ou d'une migration ; les deux sont vérifiés et consignés sur le média. Cela vaut pour Anton [as a Service](anton_as_service.md) comme pour l'exploitation [on Premises](anton_on_premises.md).

## Offre de base et offre complète

Avec Anton as a Service, chaque abonnement comprend l'**offre de base « Archive numérique »** : stockage et sauvegarde en quatre copies sur trois sites, tous les contrôles (sommes de contrôle, virus, identification et validation des formats), les rapports et le remplacement des fichiers endommagés à partir de la sauvegarde. Dans l'offre de base, nous n'agissons pas de notre propre initiative : nous n'examinons pas les journaux, n'évaluons pas les risques liés aux formats et ne migrons des fichiers que sur instruction de l'archive. La responsabilité de l'archivage numérique incombe alors à l'archive ; Anton lui fournit les rapports et les outils nécessaires.

L'**offre complète Archive numérique** peut s'ajouter à tout abonnement. Elle se compose de deux paquets :

- **Sauvegarde supplémentaire :** une sauvegarde supplémentaire et indépendante, avec un autre logiciel, chez un autre fournisseur, en un autre lieu, en Allemagne ou, sur demande, en Suisse. Personne ne peut effacer ni écraser un état de sauvegarde pendant 30 jours, pas même nous.
- **Preservation Management :** nous examinons les journaux chaque mois et clarifions avec l'archive ce qui sort de l'ordinaire, évaluons les risques liés aux formats, tenons à jour la liste et les règles des formats et migrons de notre propre initiative les formats menacés. Nous ne consultons l'archive que si une mesure demande plus d'espace de stockage que celui réservé ou entraîne un effort exceptionnel ; nous estimons cet effort à l'avance et en faisons une offre.

Les prix avec et sans offre complète figurent dans l'[offre sur anton.ch](https://anton.ch/#pricing) ; l'offre complète est facturée à partir de 2027. Dans Anton, le paquet Preservation Management s'appelle encore « Technische Betreuung » (voir le [mandat de conservation](../admin/preservation-mandate.md), en allemand et en anglais).

!!! note "On Premises"
    Qui exploite Anton sur ses propres serveurs assume lui-même le stockage, la redondance et la sauvegarde. L'infrastructure décrite ici et les deux paquets font partie de notre exploitation et ne sont pas fournis avec le logiciel. Nous vous conseillons volontiers pour la mise en place.

## Stockage et sauvegarde

La _bitstream preservation_, c'est-à-dire le stockage et la sauvegarde proprement dits des données, est assurée par l'infrastructure d'exploitation. **Avec Anton as a Service**, les données numériques sont conservées en quatre copies sur trois sites en Suisse : sur le serveur de production, dans un centre de calcul, les données de production et une sauvegarde locale chiffrée, ainsi qu'une sauvegarde sur chacun de deux serveurs de sauvegarde situés sur deux sites à Zurich (voir [Infrastructure](infrastructure.md)). Les deux sites zurichois partagent les risques régionaux. La sauvegarde supplémentaire de l'offre complète ajoute un lieu indépendant de ceux-ci ; elle est en exploitation de test depuis novembre 2026.

Lors de la prise en charge, Anton calcule deux sommes de contrôle pour chaque fichier et vérifie une fois par mois l'ensemble des fonds de chaque archive par rapport à celles-ci. Si le contrôle trouve un fichier modifié, nous le remplaçons par la version inchangée tirée de la sauvegarde et le vérifions à nouveau. Chaque nouveau fichier passe un contrôle antivirus avant la prise en charge ; les fichiers infectés sont mis en quarantaine. Dans les installations dotées d'une archive à long terme connectée (DIMAG), c'est cette dernière qui assure la bitstream preservation. Plus d'informations sous [Archivage à long terme : vue d'ensemble](../admin/preservation.md).

L'accès aux données se fait exclusivement par Anton, qui ne permet que les accès autorisés. Pour les données protégées par la loi, des critères supplémentaires, comme l'emplacement possible ou autorisé du serveur, peuvent devoir être clarifiés. Grâce aux métadonnées dans Anton, les données peuvent être retrouvées et consultées facilement et rapidement à tout moment.

Nous accompagnons volontiers nos clients dans la préparation de la _prise en charge_ (évaluation, ingest, pre-ingest, etc.) et du _preservation planning_.

## Preservation planning

### Identification des formats

L'identification des formats sur la base du type MIME ou de l'extension de fichier est complétée dans Anton par l'intégration de [Siegfried](https://www.itforarchivists.com/siegfried) et/ou de [Fido](https://github.com/openpreserve/fido). Les deux outils identifient les formats de fichiers à l'aide des identifiants [PRONOM](https://www.nationalarchives.gov.uk/pronom/). Cela permet de déterminer précisément les formats de fichiers pour l'archivage à long terme. Anton ouvre en outre chaque nouveau fichier et vérifie s'il peut être lu entièrement ; il contrôle l'ensemble des fonds une fois par an.

### Évaluation des risques

À partir de l'identifiant PRONOM, Anton déduit l'évaluation des risques du [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation). Elle sert de base aux décisions sur les mesures de conservation, par exemple le transfert vers un autre format.

Anton réévalue chaque nuit les formats des fonds et signale dans le rapport mensuel les nouveaux formats et les risques accrus. Le [preservation planning](../admin/preservation-planning.md) de l'espace d'administration affiche les formats de fichiers présents dans l'archive, accompagnés de leur évaluation des risques. Sans offre complète, l'archive évalue elle-même le rapport et commande les migrations ; avec l'offre complète, nous nous en chargeons. Le fichier livré est conservé dans tous les cas.

## Modèle OAIS

Le modèle de référence OAIS (Open Archival Information System, ISO 14721) décrit les fonctions d'une archive numérique et les paquets dans lesquels les documents entrent et sortent : le paquet d'information à verser (SIP), le paquet d'information archivé (AIP) et le paquet d'information diffusé (DIP). Anton couvre les fonctions comme suit :

| Fonction | Ce que fait Anton |
|---|---|
| Entrées (Ingest) | Import depuis Excel, selon eCH-0160 et E-ARK ; téléversement dans le navigateur ou par code QR ; contrôle antivirus, deux sommes de contrôle, identification des formats selon PRONOM, contrôle de lisibilité, conversion selon les règles de format |
| Stockage (Archival Storage) | Quatre copies sur trois sites, sauvegarde chaque nuit, contrôle mensuel avec réparation à partir de la sauvegarde ; avec l'offre complète, la sauvegarde supplémentaire |
| Gestion de données (Data Management) | Description selon ISAD(G), données d'autorité (GND, Geonames, Wikidata), adresses pérennes, événements de conservation selon PREMIS |
| Planification de la pérennisation (Preservation Planning) | Liste et règles des formats par archive, évaluation des risques selon NARA, migration ; avec l'offre complète, nous évaluons les risques et migrons de notre propre initiative |
| Accès (Access) | Recherche publique, commande et prêt ; OAI-PMH et REST ; export en EAD, Dublin Core, RiC-O, CIDOC CRM et PREMIS ; paquets selon E-ARK et OCFL |
| Administration | Comptes, rôles et autorisations ; journal de toutes les modifications ; rapport mensuel ; avec l'offre complète, nous examinons le rapport mensuel |

Le paquet d'information archivé n'existe pas dans Anton en tant que fichier distinct : il se compose du master sur le stockage ainsi que de la description, des sommes de contrôle et des événements de conservation dans la base de données. Il ne devient un paquet qu'à l'export, selon E-ARK ou OCFL.

Vue d'ensemble en PDF : [Archive numérique dans Anton et modèle OAIS](https://anton.ch/docs/anton-oais-modell.pdf) (en allemand).

## Niveaux NDSA

Les « Levels of Digital Preservation » de la National Digital Stewardship Alliance (NDSA, États-Unis), version 2.1, sont une référence répandue pour mesurer dans quelle mesure une institution conserve ses documents numériques. Ils divisent la conservation en cinq domaines (stockage, intégrité, contrôle, métadonnées, formats de fichiers) et chaque domaine en quatre niveaux, de « connaître ses documents » à « conserver ses documents dans la durée ». Un niveau n'est atteint que si toutes ses exigences sont remplies.

Nous avons évalué nous-mêmes Anton as a Service selon ces niveaux, avec une preuve pour chaque exigence ; il ne s'agit pas d'une certification par un organisme externe. L'offre de base atteint le niveau le plus élevé dans deux domaines sur cinq (intégrité et métadonnées). Avec l'offre complète, elle l'atteint dans les cinq : la sauvegarde supplémentaire concerne le stockage, le Preservation Management le contrôle et les formats de fichiers. Les niveaux ne mesurent pas le travail professionnel de l'archive, par exemple si un fonds est entièrement décrit et correctement évalué.

Les exigences en détail figurent dans deux PDF (en allemand) :

- [Das Digitale Archiv in Anton und die NDSA-Stufen](https://anton.ch/docs/anton-ndsa-stufen.pdf) : les 38 exigences avec notre mesure
- [Kurzfassung](https://anton.ch/docs/anton-ndsa-kurzfassung.pdf) (résumé)

Dans les deux documents, les parties de l'offre complète figurent encore séparément, comme « Paket Zusätzliche Sicherung » (sauvegarde supplémentaire) et « Paket Preservation Management ».
