# Mes exports

Certains exports sont trop volumineux pour un téléchargement direct. Anton les crée alors en arrière-plan et dépose le fichier sous **Export de données → Mes exports** (`/export/mine`).

## Quels exports

| Export | en arrière-plan au-delà de |
|---|---|
| Inventaire Word | 1 000 notices dans la sous-arborescence |
| EAD, CIDOC CRM, RiC, Memobase (zone de téléchargement d’une notice) | 1 000 notices dans la sous-arborescence |
| DIP (BagIt), OCFL | 500 médias |
| Export Excel d’une liste de résultats, y compris le tableau de mise à jour | 1 000 lignes |

En dessous, le téléchargement arrive tout de suite, comme avant. L’exploitation fixe les limites pour chaque archive ; les valeurs ci-dessus sont celles par défaut. Le DIP E-ARK a son propre réglage et apparaît sous **Export de données → DIP E-ARK** (voir [Télécharger un DIP](download-dip.md)).

## Déroulement

1. Lancer le téléchargement comme d’habitude.
2. Au lieu du fichier, un message indique que l’export est créé en arrière-plan, avec un lien vers **Mes exports**.
3. Dès que l’export est prêt, il figure dans la liste, avec son nom, sa taille et sa date. La liste se met à jour d’elle-même.
4. Le télécharger ou le supprimer.

Qui relance le même export avant que le premier soit terminé reçoit un avis ; l’export n’est pas créé deux fois.

## Qui voit quoi

La liste ne montre que vos propres exports. Un export est créé avec les droits de la personne qui l’a lancé et contient la même chose que le téléchargement direct.

Les fichiers sont supprimés après **7 jours**.
