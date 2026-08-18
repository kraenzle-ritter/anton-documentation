# Markdown

Dans Anton, les textes des champs de texte peuvent être mis en forme avec le langage de balisage [Markdown](https://fr.wikipedia.org/wiki/Markdown). Markdown est simple et rapide à apprendre. Les données textuelles restent en outre relativement propres, car très peu de caractères et de conventions supplémentaires suffisent à permettre la mise en forme.

[ [Informations détaillées](https://www.markdownguide.org/basic-syntax/) ]


Les principales possibilités de mise en forme dans Anton :

### Nouvelles lignes, nouveaux paragraphes

Les nouvelles lignes s'obtiennent avec deux espaces en fin de ligne.

Les nouveaux paragraphes au moyen d'une ligne vide.

### Titres

Les titres se créent avec `#` en début de ligne : un `#` suivi d'une espace marque un titre de premier niveau, deux `##` suivis d'une espace un titre de deuxième niveau, et ainsi de suite :

```markdown
# Titre niveau 1
## Titre niveau 2
```
Donne :
<div class="myframe">
<h1>Titre niveau 1</h1>
<h2>Titre niveau 2</h2>
</div>

### Listes

Les listes se créent avec `-` ou `*` en début de ligne ou, si elles sont numérotées, avec `1.`, `2.` suivis d'une espace. Des sous-points sont également possibles ; ils sont alors indentés.

```markdown
- Philosophes grecs
    - Aristote
    - Platon
- Philosophes romains
    - Cicéron
```

### Liens externes

Le texte à transformer en lien est placé entre crochets. La cible du lien suit entre parenthèses.

```markdown
[Ce texte sera transformé en lien](https://cible_du_lien.ch)
```

### Renvois à l'intérieur d'Anton

Les renvois à l'intérieur d'Anton fonctionnent comme les liens. On indique comme cible l'URL relative correspondante :

```markdown
[Anton](/actors/2)
```

Le renvoi mène alors à l'acteur·trice portant l'identifiant 2. Les unités de
description se lient de manière très semblable ; la cible est alors
`/objects/123`.

### Les cotes sont liées automatiquement

En règle générale, les cotes n'ont pas besoin d'être liées à la main : lorsqu'une
cote est mentionnée dans un champ de texte, Anton la reconnaît dans la
**vue de détail** et en fait un renvoi vers la recherche. Dans la vue de saisie,
le texte reste intact afin de demeurer modifiable.

!!! note "Pas dans tous les services"
    La reconnaissance s'appuie sur un motif de recherche enregistré par archive.
    Si aucun n'est configuré, les cotes présentes dans le texte restent sans
    lien.

### Mises en évidence

Pour les mises en évidence, on peut utiliser `*italique*` (*italique*) ou `**` (**gras**) ou `***` (***gras et italique***).
