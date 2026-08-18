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

Pas de types, pas de coordonnées, pas de
[données d'autorité](authorities.md).

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

## Ce qui se trouve dans un lieu de conservation

La page de détail d'un lieu de conservation liste — comme pour les
acteur·trice·s et les lieux — toutes les unités de description qui lui sont
rattachées.

## Supprimer

Si des unités de description sont encore rattachées à un lieu de conservation,
Anton refuse la suppression et le signale. Les rattachements doivent d'abord
être défaits.

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
