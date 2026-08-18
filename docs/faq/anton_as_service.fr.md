# Anton as a Service

Anton fonctionne sur un serveur loué par k & r auprès d'un hébergeur reconnu (site en Suisse). k & r assure aussi bien la mise en place et la maintenance du serveur (sécurisation, monitoring, mises à jour et mises à niveau du système d'exploitation) que la mise en place et la maintenance d'Anton (mises à jour et mises à niveau).

Une sauvegarde du serveur de production est enregistrée quotidiennement sur deux serveurs situés à deux endroits différents en Suisse. Tous deux fonctionnent en RAID 1. Avec les données de production et la sauvegarde locale chiffrée sur le serveur de production, les données existent ainsi en six exemplaires, répartis sur trois sites (voir [Infrastructure](infrastructure.md)). Un serveur supplémentaire surveille en permanence le fonctionnement des machines concernées (monitoring), de sorte que k & r est informé à tout moment en cas de problème et peut intervenir rapidement.

## Avantages

- le personnel des archives n'a besoin que d'un accès internet et d'un navigateur récent  
- des coûts constants et prévisibles  
- une adéquation optimale entre l'infrastructure (système d'exploitation du serveur, logiciels installés) et l'installation d'Anton  

## Inconvénients

- pour de très grands volumes de données, éventuellement plus coûteux qu'une solution sur serveur propre  
- pour des données sensibles : les données ne se trouvent pas sur le serveur de l'institution  
- pour des données hautement sensibles : les données sont gérées via internet (déconseillé)  

## Coûts

Anton vise précisément à permettre aux archives de petite et moyenne taille de traiter leurs fonds de manière professionnelle et durable. C'est pourquoi l'infrastructure, coûteuse, est partagée entre plusieurs clients d'Anton. Les mises à jour et mises à niveau peuvent ainsi être appliquées rapidement et à moindre coût à tout moment. Pour chaque instance (client·e), un répertoire de données (PDF, images, logo, etc.) et une base de données propres sont créés. Cette structure permet de maintenir des coûts de mise en place et de maintenance relativement bas. Les données des client·e·s restent malgré tout bien cloisonnées et donc faciles à manipuler dans leur ensemble.
