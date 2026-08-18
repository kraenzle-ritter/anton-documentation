# Recherche pondérée

La recherche pondérée améliore les résultats dans les vues en liste en triant les résultats selon leur pertinence. Plus un terme recherché correspond à une notice, plus celle-ci apparaît haut dans la liste de résultats.

## Domaines d'application

La recherche pondérée est disponible pour :

- les **acteur·trice·s** (Actors)
- les **lieux** (Places)
- les **mots-clés** (Keywords)

## Fonctionnement

Le système évalue les résultats selon différents critères :

| Type de correspondance | Évaluation |
|------------|-----------|
| **Correspondance exacte** | Pertinence maximale (3×) |
| **Correspondance en début de mot** | Pertinence élevée (2×) |
| **La correspondance contient le terme** | Pertinence de base (1×) |

**Exemple** : lors d'une recherche de «&nbsp;Müller&nbsp;» :

1. Un·e acteur·trice nommé·e «&nbsp;Müller&nbsp;» (exact) apparaît tout en haut
2. Suivi·e de «&nbsp;Müller-Weber&nbsp;» (commence par)
3. Puis de «&nbsp;Anna Müller&nbsp;» (contient)

De plus, les différents champs sont pondérés différemment. Le nom d'un·e acteur·trice compte par exemple davantage qu'une correspondance dans la description.

## Activation

### Dans la vue en liste

1. Ouvrir la vue en liste souhaitée (p. ex. les acteur·trice·s)
2. Saisir un terme dans le champ de filtre
3. Sous le champ de recherche apparaît la case à cocher **«&nbsp;Trier par pertinence&nbsp;»**
4. Cocher la case pour trier les résultats par pertinence

!!! note "Remarque"
    La case à cocher n'apparaît que lorsqu'une recherche est active.

### Comme réglage par défaut dans les paramètres personnels

La recherche pondérée peut être définie comme réglage personnel par défaut :

1. Cliquer sur son profil (en haut à droite)
2. Choisir **Profil / Compte**
3. Aller dans **Paramètres**
4. Sous **«&nbsp;Recherche pondérée&nbsp;»**, choisir l'une des options :
   - **Par défaut** : utilise le réglage global du service
   - **Activée** : la recherche pondérée est toujours active
   - **Désactivée** : la recherche pondérée est toujours inactive

!!! tip "Conseil"
    Avec l'option «&nbsp;Par défaut&nbsp;», le réglage configuré pour le service est repris automatiquement. Les adaptations futures décidées par l'administration s'appliquent alors aussi.

## Conseils

- La recherche pondérée est particulièrement utile pour les **noms fréquents** ou les **termes généraux**
- Pour la recherche de **cotes exactes** ou d'**identifiants**, le tri normal est souvent plus utile
- Le réglage peut être modifié à tout moment pour chaque recherche via la case à cocher
