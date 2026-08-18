# Anton comme archive numérique à long terme

L'archivage numérique à long terme est une tâche très complexe et à multiples facettes, pour laquelle Anton peut être déployé [comme service](anton_as_service.md) ou [on premises](anton_on_premises.md).

Ce que l'on appelle la _bitstream preservation_ – le stockage et la sauvegarde effectifs des données – relève de l'infrastructure d'exploitation et non de l'application. **Avec Anton as a Service**, c'est-à-dire en exploitation sur nos serveurs, les données numériques sont conservées sur une infrastructure appropriée qui en maintient trois copies sur trois sites – soit une redondance sextuple au total.

!!! note "On premises"
    Qui exploite Anton sur ses propres serveurs assume lui-même le stockage, la redondance et la sauvegarde. L'infrastructure décrite ici fait partie de notre exploitation et n'est pas livrée avec le logiciel. Nous conseillons volontiers lors de la mise en place.

Anton conserve une somme de contrôle pour chaque fichier, ce qui permet de vérifier l'intégrité des données – c'est-à-dire de déterminer si des données ont été modifiées ou endommagées. Cette vérification n'est pas un automatisme de l'application : elle est mise en place par installation sous forme de tâche récurrente ; sur nos serveurs, elle est en place pour les grandes archives. Dans les installations dotées d'une archive à long terme connectée (DIMAG), c'est cette dernière qui assure la bitstream preservation. Plus d'informations sous [Archivage à long terme : vue d'ensemble](../admin/preservation.md).

L'accès aux données se fait exclusivement via Anton, qui n'autorise que les accès légitimes. Pour les données juridiquement protégées, des critères supplémentaires – comme la localisation possible ou autorisée du serveur – doivent le cas échéant être clarifiés. Grâce aux métadonnées présentes dans Anton, les données restent à tout moment faciles à retrouver et rapidement disponibles.

Nous accompagnons volontiers notre clientèle dans la préparation de la _prise en charge_ (évaluation, ingest, pre-ingest, etc.) et dans le _preservation planning_.

## Preservation planning

### Identification des formats

L'identification des formats sur la base du type MIME ou de l'extension de fichier est complétée dans Anton par l'intégration de [Siegfried](https://www.itforarchivists.com/siegfried) et/ou [Fido](https://github.com/openpreserve/fido). Ces deux outils identifient les formats de fichiers au moyen des identifiants [PRONOM](https://www.nationalarchives.gov.uk/pronom/). Cela permet une détermination précise des formats en vue de l'archivage numérique à long terme.

### Évaluation des risques

Les identifiants PRONOM nous permettent de tenter de reprendre dans Anton l'évaluation des risques du [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation). Cette évaluation peut aider à décider des mesures de conservation nécessaires.

Dans l'espace d'administration d'Anton, il est possible d'afficher un aperçu des formats de fichiers présents dans les archives, accompagnés de leur évaluation des risques.
