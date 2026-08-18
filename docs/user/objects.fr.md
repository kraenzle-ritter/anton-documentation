# Unités de description

L'unité de description est la notice centrale dans Anton. Elle occupe toujours
une place précise dans le [plan de classement](hierarchy.md) — comme archives,
fonds, série, dossier ou pièce.

## Créer de nouvelles notices

Anton ne propose pas de formulaire vide «&nbsp;nouvelle notice&nbsp;». Le point
de départ est toujours une notice existante : c'est à partir d'elle que l'on
détermine où les nouvelles unités seront rattachées.

1. Dans la vue de détail ou de saisie, cliquer sur le bouton **Nouveau**. La
   fenêtre «&nbsp;Créer de nouvelles notices&nbsp;» s'ouvre.
2. Indiquer le **nombre** — plusieurs unités de même niveau peuvent être créées
   en une seule opération.
3. Choisir la **position** : **avant**, **dans** ou **après** la notice
   courante. Avec «&nbsp;dans&nbsp;», la notice courante devient l'unité
   supérieure ; avec «&nbsp;avant&nbsp;» et «&nbsp;après&nbsp;», on crée une
   unité de même niveau.
4. Choisir le **niveau de description**. La liste de sélection n'apparaît
   qu'après le choix d'une position et ne contient que les niveaux admis à cet
   endroit — sous un dossier, donc, uniquement dossier et pièce.

![Fenêtre «Créer de nouvelles notices»](images/erschliessen-neu.png)

Avec **Créer**, Anton attribue automatiquement la [cote](identifiers.md) et
ouvre directement le masque de saisie de la première notice créée.

!!! note "Créer des archives"
    Des archives au niveau le plus élevé ne peuvent pas être créées par cette
    voie, celle-ci supposant une notice existante. La configuration initiale est
    effectuée par l'administration.

## Modifier

Le masque de saisie est une liste continue, structurée par des sections sur fond
gris :

![Masque de saisie d'une unité de description](images/erschliessen-edit.png)

Les sections et les champs affichés dépendent du [jeu de formulaires](forms.md)
et sont configurables par archive. Dans le formulaire standard, il s'agit de :
identification, contexte, contenu et structure, conditions d'accès et
d'utilisation, sources complémentaires, notes et contrôle de la description.
Tous les niveaux de description n'affichent pas toutes les sections — au niveau
de la pièce, «&nbsp;contexte&nbsp;» est absent.

Chaque section dispose à droite de son propre bouton **Enregistrer** ; un
bouton supplémentaire figure à la fin du formulaire. C'est toujours l'ensemble
du formulaire qui est enregistré, et non la seule section. Après
l'enregistrement, Anton bascule dans la vue de détail.

!!! warning "Les cotes ne sont pas uniques"
    Anton n'impose pas l'unicité des cotes. Si une cote déjà attribuée est
    saisie, un avertissement apparaît lors de l'enregistrement, avec un renvoi
    aux notices concernées — l'enregistrement a néanmoins lieu. L'avertissement
    n'est délibérément pas bloquant, car les doublons existent dans la pratique.

## Copier

Dans la vue de détail — et non dans le masque de saisie — se trouve le bouton
**Copier**. Dans la fenêtre «&nbsp;Copier la notice&nbsp;», on indique le nombre
de copies. Sont copiés le titre, les champs de texte, les événements, les
acteur·trice·s, les lieux et les mots-clés ; la copie est rattachée comme unité
de même niveau directement après l'original et reçoit une nouvelle cote. Les
médias ne sont pas copiés.

## Supprimer

Le bouton **Supprimer** ouvre la fenêtre «&nbsp;Supprimer la notice&nbsp;» avec
la question «&nbsp;Supprimer réellement cette notice ?&nbsp;». La confirmation
exige la saisie de **son propre mot de passe**.

!!! danger "La suppression est définitive"
    Anton ne tient pas de corbeille. Sont supprimés la notice, toutes les unités
    de description subordonnées et leurs médias, fichiers compris. Une
    restauration n'est possible qu'à partir d'une
    [sauvegarde](../admin/restore.md).
