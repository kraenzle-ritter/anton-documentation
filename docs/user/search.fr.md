# Recherche plein texte

La recherche plein texte interroge simultanément tous les champs pertinents des notices archivistiques : titres, cotes, champs de texte, acteur·trice·s, lieux et mots-clés associés — ainsi que le texte reconnu par OCR dans les PDF et les images.

## Ce qui est interrogé

Pour chaque objet d'archives, les éléments suivants sont réunis pour la recherche :

- **Titres** de l'objet et de toutes les unités supérieures (fonds → série → dossier → document)
- **Cotes** (actuelles et anciennes) ainsi que l'identifiant interne
- **Désignations** du niveau de description, du type d'objet, du lieu de conservation
- **Datations**
- **Mots-clés associés** dans toutes les variantes linguistiques existantes
- **Lieux associés**
- **Acteur·trice·s associé·e·s** (uniquement celles et ceux visibles publiquement)
- **Champs de texte** visibles dans le formulaire externe
- **Texte OCR** issu des médias (PDF, images)

!!! note "Vue étendue pour le personnel interne"
    Pour les personnes connectées à partir du rôle `user_intern`, sont en outre interrogés :

    - les acteur·trice·s privé·e·s
    - tous les champs de texte (y compris ceux visibles en interne seulement)
    - les objets marqués comme privés

## Comportement de la recherche

### Les débuts de mots sont reconnus automatiquement

Les caractères génériques (`*`) ne sont pas nécessaires — la recherche trouve automatiquement tous les mots qui **commencent** par le terme saisi.

| Recherche | Trouve |
|---|---|
| `alkohol` | «&nbsp;Alkohol&nbsp;», «&nbsp;Alkoholverbot&nbsp;», «&nbsp;alkoholisch&nbsp;» |
| `müller` | «&nbsp;Müller&nbsp;», «&nbsp;Müller-Weber&nbsp;», «&nbsp;Müllers&nbsp;» |

!!! warning "Mais pas au milieu d'un mot"
    `kohol` ne trouve **pas** «&nbsp;Alkohol&nbsp;». La recherche n'agit qu'en début de mot.

### Plusieurs mots sont combinés par ET

| Recherche | Trouve |
|---|---|
| `alkohol verbot` | Les notices dans lesquelles **les deux** termes apparaissent — ils peuvent être éloignés l'un de l'autre |

### Guillemets pour les expressions exactes

| Recherche | Trouve |
|---|---|
| `"rudolf leder"` | Uniquement les notices où cette suite de mots apparaît **exactement ainsi** |
| `#rudolf leder#` | Identique — `#` est une notation alternative pour `"` |

Pour une expression, la recherche par début de mot n'est **pas** appliquée automatiquement — l'expression doit apparaître à l'identique.

!!! warning "Les mots très courts sont ignorés y compris dans les expressions"
    Les mots de moins de 3 caractères et quelques mots vides anglais (`the`, `for`, `and`) sont écartés de la comparaison même à l'intérieur de guillemets. Une expression telle que `"AG Reinach"` ne correspond donc en fait qu'à «&nbsp;Reinach&nbsp;».

### Termes avec trait d'union

Les termes comportant un trait d'union (p. ex. `Arp-Hagenbach`) sont automatiquement traités comme une expression : la recherche porte sur les deux parties directement accolées.

## Ce qui ne fonctionne pas

- **Les termes de moins de 3 caractères** sont ignorés (`ag`, `zb`).
- **Les mots courts très fréquents** tels que «&nbsp;und&nbsp;», «&nbsp;der&nbsp;», «&nbsp;die&nbsp;» sont exclus de l'index de recherche de la base de données (mots vides).
- **La recherche au milieu d'un mot** n'est pas possible (voir ci-dessus).

## Distinction avec la recherche pondérée

La recherche plein texte interroge les **objets d'archives**. La [recherche pondérée](weighted-search.md) est une autre fonction et concerne les vues en liste des **acteur·trice·s, lieux et mots-clés** — les résultats y sont triés par pertinence.
