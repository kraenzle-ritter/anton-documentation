# Prise en main

Anton est une base de données archivistique en ligne. Elle suit l'ISAD(G) et
représente les fonds sous forme d'arborescence — des archives aux fonds et
séries jusqu'au document isolé. Pour chaque
[unité de description](objects.md), il est possible de saisir des médias, des
[acteur·trice·s](actors.md), des [lieux](places.md) et des
[mots-clés](keywords.md).

Cette documentation décrit le travail avec Anton du point de vue de la
description archivistique. Pour l'installation et la configuration, voir la
section Admin.

## L'interface

La navigation se trouve en haut. Son contenu est configurable par archive ; on y
trouve en règle générale :

- le **point d'entrée dans le plan de classement**. Chaque service d'archives
  décide de son nom — «&nbsp;catalogue&nbsp;», «&nbsp;plan d'archivage&nbsp;» ou
  le nom du service lui-même.
- **Admin** — malgré son nom, il s'agit de la page collective pour toutes les
  personnes connectées. La page elle-même est intitulée **Administration** et
  mène, sous forme de cartes, aux **entités** (acteur·trice·s, lieux, mots-clés,
  lieux de conservation), aux **utilisateur·trice·s**, aux **informations**, à
  l'**import / export** et aux **paramètres**. Les cartes affichées dépendent du
  rôle.
- **Aide** — l'aide intégrée à l'application ; elle présente les champs, les
  listes de valeurs et les règles de description de **ce** service d'archives
- la **recherche** en haut à droite

!!! note "Les libellés peuvent différer"
    Presque chaque libellé est paramétrable par archive — les entrées de menu
    comme les noms de champs. Cette documentation utilise les désignations du
    formulaire standard ; dans un service donné, elles peuvent différer. Là où
    les écarts prêtent particulièrement à confusion, la remarque figure sur
    place.

## Rôles

Ce que chacun·e voit et peut faire dépend de son rôle. Anton conserve les noms
de rôle non traduits ; ils apparaissent exactement ainsi dans la gestion des
utilisateur·trice·s :

| Rôle | Peut |
|---|---|
| (non connecté·e) | Consulter le catalogue public — pour autant que le service le rende accessible |
| `user` | La même chose, en étant connecté·e ; profil personnel, notifications |
| `user_intern` | En plus, voir les contenus non communicables et les lieux de conservation, emprunter et télécharger les médias originaux |
| `loan_admin` | En plus, gérer les prêts |
| `editor` | Décrire : créer, modifier, déplacer et supprimer des notices (y compris les lieux de conservation) ; import ; médias |
| `admin` | Paramètres, formulaires, comptes utilisateur, export, statistiques |
| `blocked` | Rien — l'accès est bloqué |

Chaque rôle inclut les droits du précédent.

Qui décrit a besoin au minimum du rôle `editor`. Les boutons de création, de
déplacement et de suppression n'apparaissent qu'avec cette autorisation — s'ils
manquent, cela tient au rôle.

!!! note "Superutilisateur·trice·s"
    Au-delà d'`admin`, il existe des superutilisateur·trice·s pour des
    interventions telles que les types de champs, les listes de valeurs et les
    délais de protection. Il ne s'agit pas d'un rôle dans la gestion des
    utilisateur·trice·s, mais d'une liste de comptes tenue séparément.

## Connexion

La connexion se fait avec un nom d'utilisateur·trice et un mot de passe. Selon
le service d'archives, l'[authentification à deux facteurs](2FA.md) et les
[passkeys](passkey.md) sont également disponibles.

## Pour continuer

Le point d'entrée dans le travail quotidien est
[Unités de description](objects.md) ; la structure de l'arborescence et la
manière de rattacher les notices ailleurs sont décrites sous
[Plan de classement et déplacement](hierarchy.md). Pourquoi le masque de saisie
diffère des exemples présentés ici est expliqué dans
[Formulaires et champs](forms.md).
