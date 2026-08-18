# Plan de classement et déplacement

Toutes les unités de description s'inscrivent dans une arborescence, le plan de
classement. Chaque unité a exactement une unité supérieure — à l'exception des
archives situées au niveau le plus élevé.

## Niveaux de description

Les niveaux suivent l'ISAD(G) et déterminent ce qui peut être créé sous une
unité :

| Niveau | Unités subordonnées admises |
|---|---|
| Archives | Groupe de fonds, Fonds |
| Groupe de fonds | Groupe de fonds, Fonds |
| Fonds | Série, Classe, Dossier, Pièce |
| Classe | Série, Classe, Dossier, Pièce |
| Série | Série, Dossier, Pièce |
| Dossier | Dossier, Pièce |
| Pièce | Pièce |

Un fonds à l'intérieur d'un fonds n'est pas admis et est refusé par Anton.

## Navigation dans l'arborescence

Anton ne représente pas le plan de classement sous forme d'arborescence
dépliable, mais en deux parties :

- Au-dessus de chaque notice figure le **chemin** — la chaîne des unités
  supérieures, indentée en escalier et cliquable.
- Sous la vue de détail figure la section **contenu** avec la liste des unités
  subordonnées.

## Déplacer des notices

Le déplacement se fait en deux temps : la notice est d'abord sélectionnée, puis
on rejoint la destination.

1. Sur la notice à déplacer, cliquer sur le bouton **Déplacer**. Un bandeau
   jaune apparaît avec la mention «&nbsp;Notice à déplacer&nbsp;», sa cote et
   son titre. La croix ✕ du bandeau permet d'annuler l'opération.
2. Naviguer jusqu'à la notice de destination. Le bandeau reste visible.
3. Dans le bandeau, choisir l'emplacement souhaité : **avant**, **dans** ou
   **après** cette notice.

!!! tip "Aucun lien visible dans le bandeau ?"
    Les liens n'apparaissent que si le niveau de description est admis à
    l'emplacement visé. Un dossier ne peut pas être déplacé «&nbsp;dans&nbsp;»
    une pièce — le bandeau n'y propose alors aucun choix. Un coup d'œil au
    tableau ci-dessus indique si l'emplacement souhaité est possible.

Plusieurs notices peuvent être déplacées ensemble ; leur ordre est conservé à
destination. Les archives situées au niveau le plus élevé ne peuvent pas être
déplacées. De même, une notice ne peut pas être déplacée dans sa propre
sous-arborescence — Anton le refuse et ignore la notice concernée.

Le déplacement ne modifie **pas** la cote. Celle-ci doit le cas échéant être
adaptée manuellement après coup.
