# Galerie de médias

La galerie de médias présente les images d'un service d'archives sous forme de
grille de vignettes — une porte d'entrée visuelle à côté de la
[recherche](search.md). Elle se trouve sous `/gallery`.

!!! note "Pas liée partout"
    Anton n'ajoute pas lui-même la galerie à la navigation. Chaque service
    décide si elle apparaît dans le menu ; sinon, elle n'est accessible que par
    son adresse.

## Deux variantes

| Variante | Filtre |
|---|---|
| Galerie classique | Une ligne de filtres au-dessus de la grille ; les champs qu'elle contient sont configurables par archive |
| Galerie V2 | Une barre latérale avec facettes et **nombre de résultats** par fonds, mot-clé et type de média, ainsi qu'une plage d'années |

La V2 requiert un moteur de recherche Typesense et est introduite
progressivement ; la variante utilisée par un service est paramétrée. Les
vignettes et l'affichage agrandi sont identiques dans les deux cas.

## Ce qui apparaît dans la galerie

Une image n'apparaît que si **toutes** les conditions sont réunies :

- Elle n'est pas marquée «&nbsp;ne pas montrer dans la galerie&nbsp;». Ce
  marquage vaut pour **tout le monde**, y compris les personnes connectées
  chargées de la description.
- Elle n'est pas marquée comme média bloqué.
- Pour les personnes extérieures en plus : l'unité de description n'est pas
  bloquée, son statut n'est pas «&nbsp;brouillon&nbsp;» et le
  [délai de protection](access.md) est échu.

Les utilisateur·trice·s connecté·e·s en interne voient donc plus que le public —
mais le marquage «&nbsp;ne pas montrer dans la galerie&nbsp;» l'emporte sur tout
rôle.

Il est en outre possible de restreindre par archive les fonds que la galerie
présente — séparément pour l'usage interne et public.

## Retirer des images de la galerie

Le marquage se pose dans la gestion des médias sous **Admin → Médias**. C'est la
bonne voie pour les images qui sont décrites mais ne méritent pas la vitrine —
versos, erreurs d'exposition, prises de vue techniques.

Pour les images qui ne peuvent pas être montrées pour des raisons juridiques,
c'est en revanche le [délai de protection](access.md) ou le blocage du média qui
constitue le moyen approprié : le marquage de galerie est une décision
d'affichage, non une restriction d'accès.
