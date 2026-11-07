# Lieux de conservation

Un lieu de conservation est l'emplacement physique de l'original — magasin,
dépôt, salle, rayonnage. Les lieux de conservation sont des notices propres et
se gèrent sous **Admin → Lieux de conservation**.

!!! note "Pas pour le public"
    La notice de lieu de conservation elle-même n'est visible que par les
    utilisateur·trice·s internes, les personnes chargées de la description et
    l'administration, jamais par des personnes extérieures — l'endroit où se
    trouve un document ne regarde pas le public.

    Le **champ** «&nbsp;lieu de conservation&nbsp;» d'une unité de description
    est distinct : les nouvelles installations sont livrées avec ce champ retiré
    des formulaires publics (externes), de sorte que
    «&nbsp;Lieu de conservation : …&nbsp;» n'apparaît pas dans le catalogue
    public. Les installations existantes restent inchangées — le champ doit
    alors, au besoin, être retiré des formulaires externes via les
    [formulaires](../admin/forms.md).

## Saisir

Le lieu de conservation est délibérément sobre et ne comporte que quatre champs :

| Champ | Usage |
|---|---|
| ID | attribué automatiquement |
| Abréviation | forme courte, p. ex. `M2` |
| Nom | en clair, p. ex. «&nbsp;Magasin 2, rayonnage C&nbsp;» |
| Description | texte libre |

Pas de coordonnées, pas de [données d'autorité](authorities.md). La place d’un lieu de conservation dans le magasin, son niveau, l’emplacement supérieur et sa capacité, figure dans l’encadré [Magasin](#magazin) de sa page.

!!! note "Autorisation"
    Créer, modifier et supprimer des lieux de conservation suppose le rôle
    `editor`. Les utilisateur·trice·s internes (`user_intern`) peuvent les
    consulter — contrairement aux acteur·trice·s, aux lieux et aux mots-clés,
    les lieux de conservation ne sont pas publics du tout.

## Attribuer

Une unité de description est rattachée au lieu de conservation dans le champ
**lieu de conservation**. Il figure dans la section
«&nbsp;sources complémentaires&nbsp;» et prend la forme d'une liste de
sélection.

Une unité de description a au maximum **un** lieu de conservation. La présence
du champ dans le masque dépend du [jeu de formulaires](forms.md) — par défaut,
le dossier, la série et la pièce le portent, mais pas les archives ni le fonds.

!!! tip "Lieu de conservation ou précision ?"
    Deux champs aux noms voisins ne doivent pas être confondus :

    - **Lieu de conservation** — le choix parmi les lieux enregistrés, un
      véritable lien. Il peut faire l'objet d'analyses.
    - **Lieu de conservation (détail)** — un champ de texte pour des indications
      complémentaires, sans lien.

## Magasin {#magazin}

Les lieux de conservation peuvent être structurés en magasin : salle, étagère, segment, case et carton, ou selon la manière dont l’archive divise son magasin. Le paramètre `locations_mode` sous **Admin → Paramètres** décide de ce qu’une archive en utilise : `list` garde la liste plate des lieux de conservation telle qu’elle était et constitue la valeur par défaut ; `magazine` active le magasin ; `off` masque entièrement les lieux de conservation.

**Définir les niveaux.** Sous **Admin → Configuration → Niveaux du magasin**, l’administration définit les niveaux, de haut en bas, avec une désignation par langue. Un niveau peut être marqué comme **contenant**, par exemple le carton : un contenant occupe toute sa capacité sur l’emplacement où il se trouve, plein ou vide. Un niveau attribué à des emplacements ne peut pas être supprimé.

**Créer des emplacements.** Un lieu de conservation a un seul formulaire. Dans le magasin, sa page affiche en plus le chemin, le niveau, l’occupation et les niveaux inférieurs ; **Ajouter un niveau inférieur** crée un nouveau lieu en dessous, et Anton propose le niveau suivant. En modification, l’emplacement supérieur (« Se trouve dans »), le niveau, la capacité en centimètres linéaires et l’ordre suivent le nom et la description. Un emplacement ne peut pas se trouver en lui-même ni dans l’un de ses propres niveaux inférieurs.

**Chemin.** Partout où un lieu de conservation est nommé figure son chemin, p. ex. « Salle 1 › Étagère 3 › Case 4 › Carton 17 » : dans l’unité de description, dans la liste de sélection du masque et de l’édition groupée, dans le courriel de commande et dans l’export Excel complet.

**Occupation.** On compte l’étendue des unités de description attribuées à l’emplacement lui-même, sur tous les niveaux inférieurs : leur propre étendue ou, à défaut, l’étendue en dessous, telle que la page de détail l’affiche. Un fonds dont les dossiers se trouvent dans des cartons compte par les cartons, pas deux fois. Un contenant avec une capacité compte sur sa case avec toute sa capacité. Sans capacité, Anton indique seulement l’occupation.

**Structure et emplacements libres.** Dans le magasin, la page **Lieux** a trois onglets : **Liste**, **Structure** avec le magasin sous forme d’arbre, l’occupation et le nombre d’unités de description par emplacement, et **Emplacements libres** avec les emplacements dotés d’une capacité où il reste de la place, les plus vides d’abord, au besoin d’un seul niveau et avec un minimum.

**Attribuer en masse.** Les unités de description arrivent à leur place par l’édition groupée ou le tableau Excel. La colonne `standort` accepte l’ID, la désignation ou le chemin, avec `›`, `>` ou `/` entre les niveaux. Une désignation que portent plusieurs emplacements, p. ex. « Case 4 », est refusée comme ambiguë au lieu d’être devinée ; un chemin inexistant n’est pas créé comme nouveau lieu.

## Ce qui se trouve dans un lieu de conservation

La page de détail d’un lieu de conservation liste les unités de description qui lui sont attribuées ou qui le sont à un emplacement en dessous : une étagère montre aussi ce qui se trouve dans ses cartons.

## Supprimer

Si des unités de description sont encore attribuées à un lieu de conservation, Anton refuse la suppression et le signale. Les attributions doivent d’abord être levées. De même, un lieu sous lequel se trouvent encore des emplacements est conservé ; ceux-ci doivent d’abord être supprimés ou déplacés.

## Cotes intégrant le lieu de conservation

Dans certains services, l'abréviation du lieu de conservation entre dans la
[cote](identifiers.md). Lorsque cela est configuré, un champ de sélection
supplémentaire **lieu de conservation** apparaît dans la fenêtre
«&nbsp;Créer de nouvelles notices&nbsp;».

!!! note "Propre au service"
    Cette fonction suppose une formation des cotes programmée spécialement. Le
    schéma standard n'utilise pas le lieu de conservation — le champ de
    sélection y resterait sans effet. Avec Anton as a Service, k & r sait si une
    installation donnée dispose d'une telle formation des cotes.
