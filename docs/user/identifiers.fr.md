# Cotes

Anton crée les cotes automatiquement. Le schéma standard est décrit ici ; la
formation des cotes est modifiable par archive via le paramètre
`identifier_generator` :

| Valeur | Comportement |
|---|---|
| `standard` | Le schéma décrit ci-dessous |
| `recordgroup_as_base` | Comme standard, mais avec le groupe de fonds au lieu des archives comme base |
| `id_identifier` | Numéro séquentiel |
| `manual_identifiers` | Aucune attribution automatique — la cote est saisie à la main |

Il est en outre possible de programmer une formation de cotes propre à un
service. Le paramètre est choisi lors de la mise en place et n'est pas
modifiable dans la section Admin.

## Niveaux de description

|Niveau de description|Exemple de cote|Description|Peut contenir|
|:--------------------|:--------------|:----------|:------------|
| Archives | KRA | Unité englobante d'une institution. N'a pas d'unité de description supérieure. | Groupe de fonds, Fonds |
| Groupe de fonds | sans incidence sur la cote | Permet d'ordonner logiquement des fonds. | Groupe de fonds, Fonds |
| Fonds | KRA 3 | Unité d'une provenance ou d'un versement. Les fonds sont numérotés séquentiellement par service. | Série, Classe, Dossier, Pièce |
| Classe | sans incidence sur la cote | Permet d'ordonner logiquement des dossiers. | Série, Classe, Dossier, Pièce |
| Série | KRA 3/22 | Se comporte comme un dossier du point de vue des cotes | Série, Dossier, Pièce |
| Dossier | KRA 3/22 | Unité de description standard. Les dossiers, registres officiels et documents analogues sont décrits au niveau du dossier. Les dossiers sont numérotés séquentiellement par fonds. | Dossier, Pièce |
| Pièce | KRA 3/22.1 | Niveau de description le plus bas, par exemple pour les photographies ou les documents isolés. | Pièce |

Les groupes de fonds, classes, séries, dossiers et pièces peuvent contenir des
unités de même nature (sous-dossiers, par exemple). Un fonds à l'intérieur d'un
fonds n'est en revanche pas admis.

Pour les niveaux **archives, groupe de fonds et classe**, Anton n'attribue
aucune cote — ces niveaux sont sans incidence sur la cote et sont, si on le
souhaite, libellés à la main.

## Schéma de la cote
La cote se compose de l'abréviation du service, du numéro de fonds et des
numéros de dossier et de pièce.

```
AbréviationDuService NuméroDeFonds/NuméroDeDossier.NuméroDePièce
```

Le numéro de dossier et le numéro de pièce peuvent être imbriqués davantage.
Chaque niveau supplémentaire est séparé par un point.

### Exemples
> KRA, 22/1.5     (service KRA;  fonds 22; série ou dossier 1; sous-dossier ou pièce 5)

> Test, 1/1       (service Test; fonds  1; série, dossier ou pièce 1)

> HDR, 25/4.7.5   (service HDR;  fonds 25; série ou dossier 4; série ou (sous-)dossier 7; sous-dossier ou pièce 5)

## Modifier une cote à la main

La cote attribuée automatiquement peut être remplacée — le champ **cote** est un
champ de saisie ordinaire.

!!! warning "Les cotes ne sont pas uniques"
    Anton n'impose pas l'unicité des cotes. Si une cote déjà attribuée est
    saisie, un avertissement apparaît lors de l'enregistrement, avec un renvoi
    aux notices concernées — l'enregistrement a néanmoins lieu. L'avertissement
    n'est délibérément pas bloquant, car les doublons existent dans la pratique.

Lors du [déplacement](hierarchy.md) d'une notice, la cote reste inchangée. Elle
doit le cas échéant être adaptée manuellement par la suite.

## Ancienne cote

Pour les cotes et références de dossier abandonnées, un champ propre
**ancienne cote** est disponible. Il est pris en compte par la
[recherche plein texte](search.md).
