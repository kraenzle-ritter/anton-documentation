# Formulaires et champs

Anton n'impose pas de schéma de champs fixe. Les champs dont dispose une unité
de description, leur ordre et leur nom sont déterminés par chaque service
d'archives. Cela explique pourquoi les masques diffèrent d'un service à l'autre
— et pourquoi les exemples de cette documentation peuvent s'écarter de
l'installation utilisée.

## Jeux de formulaires

Un **jeu de formulaires** regroupe cinq formulaires pour un même objet :

| Formulaire | Usage |
|---|---|
| Interne — Saisie | Le masque de description |
| Interne — Détail | La vue de détail pour les personnes connectées |
| Interne — Liste | La liste de résultats pour les personnes connectées |
| Externe — Détail | La vue de détail pour le public |
| Externe — Liste | La liste de résultats pour le public |

La séparation interne/externe explique pourquoi les personnes extérieures voient
moins que le service lui-même : un champ n'apparaît que s'il figure dans le
formulaire concerné. Il n'existe pas de formulaire de saisie pour le public.

Des jeux de formulaires existent non seulement pour les unités de description,
mais aussi pour les [acteur·trice·s](actors.md), les [lieux](places.md), les
[mots-clés](keywords.md) et les lieux de conservation.

## Quel jeu de formulaires s'applique ?

Anton décide dans cet ordre :

1. Si le champ **jeu de formulaires** est renseigné dans la notice, c'est
   celui-là qui s'applique.
2. Sinon s'applique le jeu de formulaires portant le même nom que le
   [niveau de description](hierarchy.md) — pour un dossier, donc,
   «&nbsp;file&nbsp;».
3. Sinon s'applique le jeu par défaut.

Le champ **jeu de formulaires** figure tout en haut du masque de description et
reste en règle générale vide. C'est la solution de repli pour les cas
particuliers : si un fonds contient des photographies nécessitant d'autres
champs que le reste, un jeu de formulaires propre peut être créé et attribué
spécifiquement.

## Champs

Un champ n'apparaît que s'il figure dans le formulaire **et** qu'il a une valeur
— les champs vides sont masqués dans la vue de détail plutôt qu'affichés comme
ligne vide. Dans le masque de saisie, en revanche, ils sont toujours visibles.

Un même champ se comporte différemment selon la vue : ce qui est un champ de
saisie ou une liste de sélection lors de l'édition apparaît comme simple texte
dans la vue de détail.

Des **sections** sur fond gris structurent le masque. Elles ne sont pas
elles-mêmes des champs ; une section sans champ visible est entièrement omise.

## Textes d'aide sur les champs {#hilfetexte-zu-feldern}

Un texte d'aide peut être associé à un champ — la règle de description propre au
service pour ce champ. S'il est renseigné, il apparaît dans le masque de saisie
sous forme d'une petite indication directement sous le champ.

Cet affichage en ligne peut être activé ou désactivé par chaque personne dans
son propre profil ; par défaut il est **désactivé**. Indépendamment de cela,
tous les textes d'aide sont consultables ensemble sur la page d'aide
**Anton Fields** de l'application.

## Modifier

Les jeux de formulaires et les formulaires se gèrent sous
**Admin → Formulaires** et **Admin → Types de formulaires**. On peut y ajouter,
supprimer, réordonner et renommer des champs par formulaire — le libellé d'un
champ peut donc différer entre le masque de saisie et la vue de détail. Les
champs effectivement disponibles sont présentés sur la page d'aide
**Anton Fields** de l'application.
