# Données d'autorité (GND, Wikidata, Metagrid …)

Les acteur·trice·s, les lieux et les mots-clés peuvent être associés à des
notices de bases de données d'autorité et d'ouvrages de référence externes –
par exemple à la
[Gemeinsame Normdatei (GND)](https://gnd.network/), à
[Wikidata](https://www.wikidata.org/) ou à [Metagrid](https://metagrid.ch/).
Metagrid y joue un rôle particulier : il ne s'agit pas d'un ouvrage de référence
isolé, mais d'un **service de mise en relation** qui rassemble les notices
concernant une même personne à travers de nombreuses institutions suisses de
recherche et de mémoire (p. ex. Dictionnaire historique de la Suisse, Dodis,
Archives sociales suisses, Archives économiques suisses).

## Comment naissent les associations

Lors de la modification d'un·e acteur·trice, d'un lieu ou d'un mot-clé, il est
possible de rechercher des notices correspondantes chez les fournisseurs et
d'enregistrer le résultat pertinent comme ressource. Anton dépose alors un lien
dans une table `resources` dédiée – l'association appartient dès lors à la
notice.

!!! note "Copie locale"
    Anton conserve les liens externes sous forme de **copie locale** et les
    affiche depuis celle-ci. À l'ouverture d'un·e acteur·trice, Metagrid, la GND
    ou Wikidata ne sont pas interrogés en direct à chaque affichage de page.
    L'affichage est ainsi rapide et indépendant de la disponibilité des services
    externes – mais cela signifie aussi que les liens externes nouvellement
    ajoutés n'apparaissent qu'après une **synchronisation**.

## Synchronisation

Les liens externes nouvellement ajoutés n'apparaissent dans Anton qu'après une
**synchronisation** avec les fournisseurs. Dans les installations de production,
cette synchronisation s'exécute **automatiquement et de manière récurrente**
comme tâche planifiée ; la fréquence est configurable par installation. Aucune
intervention manuelle par lien nouveau n'est nécessaire – les nouvelles
associations apparaissent d'elles-mêmes, au plus tard lors de la prochaine
exécution planifiée.

!!! info "Pour l'administration"
    La commande sous-jacente `resources:sync` et l'exploitation planifiée sont
    décrites sous
    [Synchronisation des données d'autorité](../admin/authorities.md).

## Deux directions

Pour la collaboration avec un service de mise en relation tel que Metagrid, il
vaut la peine de distinguer deux directions. Elles sont indépendantes l'une de
l'autre.

### Anton comme source : faire connaître de nouveaux acteur·trice·s

Lorsqu'un·e nouvel·le acteur·trice est saisi·e dans Anton, il appartient au
service de mise en relation et aux partenaires concernés de reprendre cette
notice et – le cas échéant – de créer un lien retour vers Anton. La fréquence à
laquelle un partenaire (p. ex. le Dictionnaire historique de la Suisse) met à
jour ses liens est déterminée par ce partenaire ou par le service de mise en
relation, non par Anton.

La contribution d'Anton à cette direction est double :

- l'**association** de l'acteur·trice avec la notice du service de mise en
  relation et
- la mise à disposition des données de personnes via l'
  [API Anton](../api/index.md), afin que les partenaires puissent les collecter
  périodiquement (page par page, filtrées par type d'entité).

!!! warning "Condition : partenariat avec Metagrid"
    Cette direction – rendre ses propres acteur·trice·s visibles pour le service
    de mise en relation – ne fonctionne **que** si l'institution s'est
    préalablement **inscrite comme partenaire auprès de Metagrid**. Sans ce
    partenariat, les personnes saisies dans Anton ne sont pas reprises par
    Metagrid et aucun lien retour n'y apparaît. L'inscription se fait
    directement auprès de [Metagrid](https://metagrid.ch/) et est indépendante
    de la synchronisation technique dans Anton.

!!! tip "En pratique"
    Une notice publiée *avant* l'existence de l'acteur·trice correspondant·e
    dans Anton ne contient d'abord aucun lien retour vers Anton – la notice
    cible n'existait alors pas encore. La mise à jour rétroactive de ces
    anciennes notices dépend du rythme d'actualisation du partenaire concerné.
    Les questions relatives à la fréquence de synchronisation ou aux liens
    retour s'adressent donc au service de mise en relation ou au partenaire.

### Anton comme consommateur : reprendre de nouveaux liens

Lorsque de nouvelles institutions partenaires rejoignent le service de mise en
relation, des possibilités d'association supplémentaires apparaissent pour les
acteur·trice·s existant·e·s. Ces nouveaux liens apparaissent dans Anton
**après la prochaine synchronisation** – c'est-à-dire par l'exécution planifiée
décrite ci-dessus. Aucune démarche manuelle par lien n'est nécessaire ; la
synchronisation récurrente récupère automatiquement les associations
nouvellement disponibles.

## En résumé

- Les liens externes sont enregistrés localement et affichés depuis là.
- Une synchronisation planifiée et récurrente maintient le stock local à jour et
  reprend d'elle-même les liens nouvellement disponibles.
- La rapidité avec laquelle **d'autres** institutions reprennent un·e
  nouvel·le acteur·trice d'Anton est déterminée par ces institutions ou par le
  service de mise en relation – non par Anton.
- Pour que ses propres acteur·trice·s apparaissent dans Metagrid, l'institution
  doit être **inscrite comme partenaire auprès de Metagrid**.
