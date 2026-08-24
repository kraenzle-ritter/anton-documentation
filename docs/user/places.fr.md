# Lieux

Les lieux sont des notices autonomes pour les indications géographiques —
villes, cours d'eau, bâtiments, régions. Comme les
[acteur·trice·s](actors.md), ils sont saisis une fois puis utilisés par un
nombre illimité d'unités de description. On les trouve sous **Admin → Lieux**.

Un lieu se rattache à une unité de description de deux manières : comme
**mot-clé** (le lieu apparaît dans le contenu) ou via un
[événement](antonevents.md) (quelque chose y a été produit, reçu, représenté).
La différence est la même que pour les acteur·trice·s.

## Types

Les types suivent les classes d'entités de GeoNames : État/pays/région, cours
et plans d'eau, parcs et surfaces, ville/village, route/ligne ferroviaire,
bâtiment/ferme, montagne/colline, sous-marin ainsi que forêt/champ. D'autres
peuvent être ajoutés par archive.

## Saisir

Le formulaire comprend le type, le nom, d'autres formes du nom, les variantes,
les abréviations, la ville/commune, le canton/land, le pays, l'adresse, la
description, les sources, un commentaire et les coordonnées.

Les lieux peuvent aussi être créés directement depuis le formulaire de l'objet
via le **+** situé à côté de la liste de sélection.

## Géocoordonnées

Si un lieu possède des coordonnées, la vue de détail affiche une carte. Dans la
liste des lieux, une carte d'ensemble peut en outre être affichée via
**afficher la carte** ; elle est couplée à la liste — déplacer ou zoomer la
carte filtre la liste sur la portion visible.

### Via les données d'autorité — la voie la plus simple

Lorsqu'un lieu est [associé](authorities.md) à **GeoNames** ou à
**ortsnamen.ch** dans la vue de saisie, Anton reprend automatiquement les
coordonnées.

### À la main

Dans le champ **coordonnées (lat lng)** d'un lieu **déjà enregistré**, les
valeurs peuvent être saisies directement.

!!! warning "Pas encore lors de la création"
    Les coordonnées saisies dans le formulaire d'un **nouveau** lieu ne sont pas
    enregistrées. Il faut d'abord créer le lieu, puis ajouter les coordonnées
    via **Éditer** — ou les obtenir d'emblée par GeoNames.

Anton reconnaît le format automatiquement et convertit en WGS84 :

| Format | Exemple |
|---|---|
| WGS84 (degrés décimaux) | `47.3769 8.5417` |
| Coordonnées suisses LV95 | `2683141 1247637` ou `2'683'141 1'247'637` |
| Coordonnées suisses LV03 | `683141 247637` |

Le signe, les séparateurs de milliers (`'` ou espace), la séparation par espace
ou virgule et les décimales sont chacun facultatifs.

Si des coordonnées sont présentes, un bouton de suppression apparaît en outre
dans la vue de saisie.

## Supprimer

Un lieu ne peut être supprimé que tant qu'il n'est **pas utilisé**. Anton refuse
la suppression dans les deux cas suivants et signale lequel s'applique :

- le lieu participe à un **événement**,
- ou il est enregistré comme **descripteur** sur une unité de description.

S'il s'agit d'éliminer un doublon, la **fusion** est préférable à la
suppression : les liens migrent alors vers la notice conservée au lieu d'être
perdus (voir ci-dessous).

## Fusionner des doublons

Deux notices pour un même lieu peuvent être fusionnées. Les événements, les
liens vers les données d'autorité et les liens vers les unités de description
migrent alors vers la notice cible. Sont également repris les champs de texte
(description, sources, commentaire) et les formes du nom du lieu supprimé ; ses
coordonnées ne migrent que si la notice cible n'en possède pas encore — celles
qui existent ne sont jamais écrasées. L'ancienne notice est ensuite supprimée.

!!! note "Réservé aux superutilisateur·trice·s"
    La fusion est réservée aux superutilisateur·trice·s ; avec Anton as a
    Service, k & r s'en charge. Un lieu ne peut pas être fusionné avec
    lui-même.
