# Recherche au-dessus de la liste

La recherche au-dessus de la liste remplace la page de la recherche avancée : un clic sur la loupe ouvre tous les critères de recherche en un seul endroit, au-dessus du tableau des unités de description. Le tableau en dessous affiche les résultats et garde ses propres filtres. L’archive active la recherche (`record_search`) ; sans ce paramètre, l’ancienne page de la recherche avancée reste en place.

## Filtres au-dessus de chaque liste

Au-dessus de chaque liste d’unités de description figurent deux filtres :

| Filtre | Effet |
|---|---|
| **Filtrer la liste** | Texte qui doit figurer dans la liste |
| **Période** (de, à) | Unités dont la période de création touche cette période ; les unités sans date sont écartées |

Les deux filtres ne restreignent que la liste en dessous, pas le reste de la page. Anton n’affiche la période que là où l’archive l’a choisie (`list_filters`, voir [Paramètres](#parametres)) ; sinon, le filtre de texte reste seul. Le nombre de lignes d’une liste ne se choisit plus au-dessus de la liste, mais dans le [profil](profile.md) sous « Éléments par page ».

## Rechercher

La loupe ouvre la recherche au-dessus du tableau. Elle comprend :

- **Rechercher dans le texte intégral :** le champ de recherche ; il comprend la même notation que la [recherche plein texte](search.md) (guillemets pour les phrases, signe moins pour exclure)
- **Arborescence :** limite la recherche à une partie de l’archive et couvre tout ce qui se trouve en dessous ; **Toute l’arborescence** lève la limitation
- **Filtres :** les facettes de l’archive, par exemple niveau de description, type d’objet ou mots-clés, avec le nombre de résultats
- **Période :** comme au-dessus de la liste
- **Recherche avancée :** des conditions sur des champs précis ; **Ajouter une condition** en ajoute une, **Appliquer** lance la recherche

Tous les critères agissent ensemble. **Masquer la recherche** ferme la zone ; les critères choisis restent sous forme de puces au-dessus du tableau et peuvent y être retirés un par un. **Nouvelle recherche** remet tout à zéro.

La navigation dans la vue détaillée, le retour à la liste et les exports se rapportent aux résultats affichés dans le tableau.

## Texte intégral depuis l’index de recherche

Les archives équipées de [Typesense](../admin/typesense.md) peuvent tirer le texte intégral de cette recherche de l’index de recherche (`record_search_index`). L’index tolère les fautes de frappe et trouve des résultats dans le texte des médias, par exemple des PDF. Arborescence, filtres, période, tri et pages proviennent toujours de la base de données ; le tableau, le nombre de résultats et les exports montrent donc les mêmes unités.

Si l’index trouve plus de 5000 résultats ou ne répond pas, la base de données effectue la recherche. Les comptes internes (à partir du rôle `user_intern`) voient à côté du champ de recherche qui a répondu : « Texte intégral depuis l’index de recherche » ou « Texte intégral depuis la base de données ».

## Paramètres

| Paramètre | Effet | Défaut |
|---|---|---|
| `record_search` | Recherche au-dessus de la liste au lieu de la page de la recherche avancée | désactivé |
| `record_search_index` | Texte intégral de cette recherche depuis l’index (requiert Typesense) | désactivé |
| `list_filters` | Filtres au-dessus des listes pour le personnel, dans l’ordre : `search` (texte), `period` (période) ; vide = aucun | `search` (texte seul) |
| `list_filters_extern` | idem pour le public | `search` (texte seul) |
| `search_facets_extern` | Filtres de la recherche pour le public, clés comme dans `search_facets` | comme `search_facets` |

Les archives dont la recherche est entièrement passée à Typesense (`search_typesense_enabled`) tirent elles aussi le texte intégral de l’index.
