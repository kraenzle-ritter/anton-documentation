# Télécharger un DIP

Un **DIP** (Dissemination Information Package) est un paquet ZIP permettant de
transmettre en une seule opération une notice et tout ce qui en dépend — par
exemple pour remettre des dossiers à des tiers.

## Comment procéder

Dans la vue de détail d'une notice apparaît — pour autant que cela soit activé
pour ce niveau de description — un bouton **«&nbsp;DIP&nbsp;»** dans la zone de
téléchargement. Un clic génère le paquet et le télécharge immédiatement. Le nom
du fichier est la cote de la notice (p. ex. `A.42.1.zip`).

Si aucun bouton n'apparaît, le téléchargement DIP n'est pas prévu pour ce
niveau. Les niveaux activés sont déterminés par l'administration.

## Ce qu'il contient

Le ZIP reproduit la notice et toutes les unités subordonnées sous forme
d'arborescence de dossiers :

- les **fichiers médias** de toutes les unités contenues, dans des dossiers
  nommés d'après les titres,
- un **instrument de recherche Word** décrivant le contenu avec les métadonnées,
- pour chaque fichier média un petit **fichier de métadonnées** (Dublin Core),
- des **sommes de contrôle** (manifeste BagIt) permettant de vérifier
  ultérieurement l'intégralité du paquet.

!!! tip "Taille"
    Un DIP contient **tous** les médias de la notice et de ses unités
    subordonnées. Pour des fonds volumineux, le paquet peut devenir lourd et sa
    création prendre un moment.

!!! note
    Selon le service, le paquet peut aussi être livré sous une forme simplifiée,
    sans instrument de recherche ni métadonnées — il ne contient alors que
    l'arborescence de dossiers avec les fichiers originaux.
