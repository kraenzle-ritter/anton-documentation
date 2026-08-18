# Décrire le contenu d'un film

Pour les médias vidéo et audio, le contenu peut être décrit dans le temps : au
lieu d'une description de l'ensemble du film, on crée une **table des matières**
composée d'entrées assorties d'un repère temporel — comparables à des chapitres.

!!! note "Pas dans tous les masques"
    La table des matières est un composant de formulaire et doit être prévue
    dans le [jeu de formulaires](forms.md). Sur les unités de description sans
    vidéo, elle se masque d'elle-même.

## Saisir

Le lecteur vidéo se trouve au-dessus du tableau. Le déroulement est délibérément
conçu pour accompagner la lecture :

1. Lancer la vidéo et la mettre en pause à l'endroit souhaité.
2. Le bouton **+** crée une nouvelle entrée **à la position de lecture
   actuelle**.
3. Taper la description directement dans la cellule. Elle est enregistrée dès
   que l'on quitte le champ.

Sont également disponibles : le symbole de la **punaise** place le repère
temporel d'une entrée existante sur la position de lecture actuelle, le **✕** la
supprime, et la **poignée** à gauche permet de réordonner les entrées à la
souris.

!!! warning "Chaque modification prend effet immédiatement"
    La table des matières n'a pas de bouton d'enregistrement — chaque saisie est
    enregistrée immédiatement. La suppression d'une entrée se fait sans demande
    de confirmation et ne peut pas être annulée.

La saisie suppose le rôle `editor`.

## Dans la vue de détail

La table des matières y apparaît sous forme de liste avec description et
indication de temps. **Un clic sur une entrée fait sauter la vidéo à cet
endroit** et lance la lecture — la table des matières devient ainsi un moyen de
naviguer dans le film. La même liste est disponible dans la
[galerie de médias](gallery.md).
