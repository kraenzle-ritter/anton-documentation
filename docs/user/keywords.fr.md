# Mots-clés

Les mots-clés décrivent le contenu des unités de description — pour les choses,
les événements, les techniques, les œuvres. Les personnes et les organisations
relèvent en revanche des [acteur·trice·s](actors.md), les indications
géographiques des [lieux](places.md).

On les trouve sous **Admin → Mots-clés** ; ils se rattachent dans le formulaire
de l'objet, au champ **mots-clés (matières)**.

!!! note "Pas de hiérarchie"
    Les mots-clés sont juxtaposés. Anton ne gère pas de thésaurus : il n'y a ni
    termes génériques ni termes spécifiques, ni renvois entre mots-clés. Le
    **type** ne fait que les regrouper.

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

## Supprimer

Un mot-clé ne peut être supprimé que tant qu'il n'est enregistré sur **aucune
unité de description**. Dans le cas contraire, Anton refuse la suppression et en
indique le motif. Les unités concernées sont présentées sous
«&nbsp;apparaît dans&nbsp;» sur la page de détail ; les attributions doivent y
être retirées au préalable.

!!! note "Différent jusqu'à la v0.82.0"
    Jusque-là, un mot-clé utilisé était supprimé — et avec lui ses attributions :
    Anton dissolvait d'abord tous les liens, puis supprimait le terme. Le travail
    de description qui se trouvait derrière disparaissait ainsi en une seule
    opération, sans demande de confirmation.
