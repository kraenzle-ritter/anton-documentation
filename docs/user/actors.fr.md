# Acteur·trice·s

Les acteur·trice·s sont des personnes, des familles et des organisations — des
notices autonomes, saisies une fois puis utilisées par un nombre illimité
d'unités de description. On les trouve sous **Admin → Acteur·trice·s**.

## Deux voies vers l'unité de description

Les acteur·trice·s peuvent être rattaché·e·s à une unité de description de deux
manières :

- **Comme mot-clé** — dans le champ «&nbsp;mots-clés (acteur·trice·s)&nbsp;».
  Cela signifie : cette personne *apparaît dans le contenu*. Sans rôle, sans
  date.
- **Via un [événement](antonevents.md)** — avec rôle, lieu, date et commentaire.
  Cela signifie : cette personne *a fait quelque chose* — elle a rédigé le
  document, gravé l'estampe, versé le fonds.

Qui saisit l'auteur·trice veut l'événement. Qui consigne le fait que quelqu'un
est mentionné dans le texte veut le mot-clé.

Sur la page de détail d'un·e acteur·trice, les deux usages apparaissent
séparément : «&nbsp;est impliqué dans&nbsp;» liste les événements,
«&nbsp;apparaît dans&nbsp;» les unités de description où la personne figure
comme mot-clé.

## Types

Six types sont disponibles de manière fixe : **personne**, **famille**,
**collectivité**, **service**, **groupe** et **logiciel**. Les libellés sont
traduisibles par archive, mais les types eux-mêmes ne sont pas extensibles.

## Saisir

Par défaut, le formulaire comprend le type, le nom, d'autres formes du nom, les
variantes, les abréviations, les dates de vie ou d'activité, la description, les
sources et un commentaire. Les champs affichés dépendent du
[jeu de formulaires](forms.md).

Pour les **dates**, «&nbsp;ca.&nbsp;» peut être coché pour chaque date, et le
jour, le mois ou l'année peuvent être laissés vides individuellement — des
datations incomplètes sont donc possibles.

Les acteur·trice·s peuvent aussi être créé·e·s **directement depuis le
formulaire de l'objet** : à côté de la liste de sélection figure un **+** qui
ouvre une fenêtre avec le même formulaire. Après la création, la nouvelle entrée
est sélectionnée — l'unité de description elle-même doit encore être enregistrée
ensuite.

L'association aux [données d'autorité](authorities.md) telles que la GND ou
Wikidata se fait dans la colonne de droite de la vue de saisie.

## Genre {#geschlecht}

Les personnes ont le champ **Genre**. Ses valeurs viennent de la [liste de valeurs](../admin/valuelists.md) «Genre» : féminin, masculin, divers, inconnu. L'archive peut les renommer et en ajouter. Les autres types que les personnes n'ont pas de genre ; le formulaire y refuse une valeur.

C'est l'archive qui décide si et où le champ apparaît. Anton ne le place dans aucun formulaire existant ; on l'ajoute au formulaire d'édition et au formulaire de détail interne dans l'[éditeur de formulaires](forms.md). Il n'est visible publiquement que si l'archive le place aussi dans le formulaire de détail public. L'API, l'interface MCP et les exports TEI, RDF et RiC suivent la même règle ; les personnes connectées en interne le voient toujours dans l'API. La sauvegarde au format natif l'emporte toujours, voir la [matrice des exports](../admin/export-matrix.md).

Pour chaque valeur, Anton note sa provenance : saisie à la main, tirée d'un commentaire «Geschlecht: …», des données GND ou Wikidata enregistrées, estimée d'après le prénom ou la formule d'appel, ou importée. Modifier la valeur dans le formulaire la marque comme saisie à la main. Les champs vides peuvent être complétés à partir de ces indices avec [`anton:fill-gender`](../admin/console-commands.md).

## Acteur·trice·s bloqué·e·s

Le champ **bloqué** masque entièrement un·e acteur·trice à toutes les personnes
qui ne sont pas connectées en interne — dans les listes, dans la vue de détail,
au niveau des unités de description liées et dans la recherche plein texte. Il
est prévu pour les personnes vivantes et les données sensibles.

## Supprimer

Les acteur·trice·s ne peuvent être supprimé·e·s que tant qu'ils ou elles ne sont
**pas utilisé·e·s**. Anton refuse la suppression dans les deux cas suivants et
signale lequel s'applique :

- la personne participe à un **événement**,
- ou elle est enregistrée comme **descripteur** sur une unité de description
  (voir [Deux voies vers l'unité de description](#deux-voies-vers-lunite-de-description)).

Pour supprimer un·e acteur·trice, il faut d'abord nettoyer les liens — les
événements des unités de description concernées, les descripteurs dans le
registre «&nbsp;est utilisé comme descripteur&nbsp;» de la page de détail.
