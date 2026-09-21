# Anton comme archive numérique à long terme

Anton prend en charge les documents numériques avec vérification, conserve les masters sans les modifier et surveille leurs formats. Cela vaut pour Anton [comme service](anton_as_service.md) comme pour l'exploitation [on premises](anton_on_premises.md).

Ce que l'on appelle la _bitstream preservation_, c'est-à-dire le stockage et la sauvegarde effectifs des données, relève de l'infrastructure d'exploitation. **Avec Anton as a Service**, c'est-à-dire en exploitation sur nos serveurs, les données numériques sont conservées sur une infrastructure appropriée qui en maintient trois copies sur trois sites – soit une redondance sextuple au total.

!!! note "On premises"
    Qui exploite Anton sur ses propres serveurs assume lui-même le stockage, la redondance et la sauvegarde. L'infrastructure décrite ici fait partie de notre exploitation et n'est pas livrée avec le logiciel. Nous conseillons volontiers lors de la mise en place.

Anton conserve une somme de contrôle pour chaque fichier, ce qui permet de vérifier l'intégrité des données : un contrôle détermine si des données ont été modifiées ou endommagées et en consigne le résultat. Sa fréquence est fixée par une tâche récurrente propre à chaque installation ; sur nos serveurs, elle tourne pour les grandes archives. Dans les installations dotées d'une archive à long terme connectée (DIMAG), c'est cette dernière qui assure la bitstream preservation. Plus d'informations sous [Archivage à long terme : vue d'ensemble](../admin/preservation.md).

L'accès aux données se fait exclusivement via Anton, qui n'autorise que les accès légitimes. Pour les données juridiquement protégées, des critères supplémentaires – comme la localisation possible ou autorisée du serveur – doivent le cas échéant être clarifiés. Grâce aux métadonnées présentes dans Anton, les données restent à tout moment faciles à retrouver et rapidement disponibles.

Nous accompagnons volontiers notre clientèle dans la préparation de la _prise en charge_ (évaluation, ingest, pre-ingest, etc.) et dans le _preservation planning_.

## Preservation planning

### Identification des formats

L'identification des formats sur la base du type MIME ou de l'extension de fichier est complétée dans Anton par l'intégration de [Siegfried](https://www.itforarchivists.com/siegfried) et/ou [Fido](https://github.com/openpreserve/fido). Ces deux outils identifient les formats de fichiers au moyen des identifiants [PRONOM](https://www.nationalarchives.gov.uk/pronom/). Cela permet une détermination précise des formats en vue de l'archivage numérique à long terme.

### Évaluation des risques

À partir de l'identifiant PRONOM, Anton déduit l'évaluation des risques du [NARA Digital Preservation Framework](https://www.archives.gov/preservation/digital-preservation). Elle sert de base aux décisions sur les mesures de conservation, par exemple la conversion d'un fichier dans un autre format.

Le [preservation planning](../admin/preservation-planning.md) de l'espace d'administration affiche les formats de fichiers présents dans les archives, accompagnés de leur évaluation des risques.
