# Mots-clés

Les mots-clés décrivent le contenu des unités de description — pour les choses,
les événements, les techniques, les œuvres. Les personnes et les organisations
relèvent en revanche des [acteur·trice·s](actors.md), les indications
géographiques des [lieux](places.md).

On les trouve sous **Admin → Mots-clés** ; ils se rattachent dans le formulaire
de l'objet, au champ **mots-clés (matières)**.

!!! note "Hiérarchie sur demande"
    Par défaut, les mots-clés sont juxtaposés ; le **type** ne fait que les regrouper. Les termes génériques et spécifiques et « voir aussi » s'activent par archive, voir [Termes génériques et spécifiques](#termes-generiques-et-specifiques).

## Types

Les types sont librement définissables par archive et varient fortement d'un
service à l'autre. On rencontre couramment événement, objet, unité de
mesure/monnaie, collection/œuvre d'art, procédé/processus/technique,
livre/manuscrit/publication et autre/divers ; les services aux fonds
particuliers en tiennent nettement plus — par exemple pour les matières
premières et la géologie, les constructions, la flore et la faune ou la
technique militaire. Fait foi la liste de valeurs de son propre service,
consultable sous **Aide → Listes de valeurs**.

## Saisir

Le formulaire comprend le type, le label, d'autres formes du nom, les variantes,
les abréviations, la description, les sources et un commentaire.

La possibilité de saisir le label de manière **multilingue** dépend du paramètre
`translate_keywords`. S'il est désactivé, il n'y a qu'un champ de saisie dans la
langue principale du service.

Anton reconnaît les mots-clés existants à leur label normalisé et les réutilise
au lieu de créer des doublons.

Les mots-clés peuvent aussi être créés **directement depuis le formulaire de
l'objet** : à côté de la liste de sélection du champ **mots-clés** figure un
**+** qui ouvre une fenêtre avec le même formulaire de création. Après la
création, le nouveau mot-clé est sélectionné — l'unité de description elle-même
doit encore être enregistrée ensuite.

## Termes génériques et spécifiques

Si le paramètre `keyword_relations` est activé sous **Admin → Paramètres**, chaque mot-clé porte des **termes génériques**, des **termes spécifiques** et **voir aussi**. Désactivé, ce qui est la valeur par défaut, tout reste comme avant.

Dans le formulaire du mot-clé, on choisit les termes dans trois champs, comme dans le formulaire de l'objet. Un terme spécifique se saisit depuis l'un ou l'autre côté ; Anton enregistre la relation une fois et l'affiche des deux côtés.

Un mot-clé peut avoir **plusieurs termes génériques**. L'un d'eux est le **terme principal** : le mot-clé figure sous lui dans le **chemin** affiché en haut de la page de détail, par exemple « Écriture › Lettre ». Le premier terme générique devient le terme principal ; s'il y en a plusieurs, on le choisit dans le formulaire sous **Terme principal**.

Anton n'admet pas de cercle : un mot-clé ne peut pas se trouver sous l'un de ses propres termes spécifiques, ni être lié à lui-même. Le formulaire revient alors avec un message et n'enregistre rien.

Le bouton **Arborescence des termes**, sur la liste des mots-clés et à côté du chemin d'un mot-clé, montre les termes génériques et spécifiques sous forme d'arbre. Il se charge au fur et à mesure, comme le plan d'archives, et ouvre le chemin vers le mot-clé de départ. Un mot-clé à plusieurs termes génériques ne se déplie que sous son terme principal ; sous les autres, il figure comme renvoi, par exemple «&nbsp;lettre (voir écriture)&nbsp;».

La suppression d'un mot-clé supprime ses relations. Lors de la fusion de deux mots-clés, celui qui reste reprend les relations de l'autre.

## Données d'autorité

Comme les acteur·trice·s et les lieux, les mots-clés peuvent être associés à des
[données d'autorité](authorities.md) — par exemple à Wikidata ou à la GND.

!!! warning "Pas disponible dans tous les services"
    La colonne des données d'autorité n'apparaît sur le mot-clé que si des
    fournisseurs sont configurés pour le service. Si le paramètre manque, aucune
    association n'est possible pour le mot-clé — alors qu'elle le reste pour les
    acteur·trice·s et les lieux.

## Où un mot-clé est utilisé

Sous «&nbsp;apparaît dans&nbsp;», la page de détail affiche toutes les unités de
description qui portent le mot-clé.

Si le mot-clé a des termes spécifiques, le commutateur **Avec les termes spécifiques** ajoute leurs unités de description à la liste. Le même commutateur figure dans la recherche à côté des filtres choisis dès que l'on filtre par un mot-clé.

## Supprimer

Un mot-clé ne peut être supprimé que tant qu'il n'est enregistré sur **aucune
unité de description**. Dans le cas contraire, Anton refuse la suppression et en
indique le motif. Les unités concernées sont présentées sous
«&nbsp;apparaît dans&nbsp;» sur la page de détail ; les attributions doivent y
être retirées au préalable.
