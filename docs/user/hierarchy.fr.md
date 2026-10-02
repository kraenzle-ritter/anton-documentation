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

Anton représente le plan de classement en deux parties et, là où l'archive l'a
activé, aussi [en arborescence](#plan-de-classement-en-arborescence) :

- Au-dessus de chaque notice figure le **chemin** — la chaîne des unités
  supérieures, indentée en escalier et cliquable.
- Sous la vue de détail figure la section **contenu** avec la liste des unités
  subordonnées.

### Plan de classement en arborescence

Là où l'archive l'a activé (`archive_plan_modal`, voir
[Paramètres](settings.md)), un bouton portant le nom du plan de classement se
trouve à côté du chemin — sur la page de détail et dans la liste du plan de
classement. Il ouvre l'arborescence dans une fenêtre à part :

- L'arborescence est dépliée jusqu'à la notice courante, mise en évidence et
  centrée. **Localiser** y ramène.
- Chaque ligne affiche cote, titre et niveau de description entre parenthèses,
  comme le chemin. Le chevron déplie et replie un niveau ; le titre ouvre la
  notice.
- Les niveaux comptant beaucoup d'entrées arrivent par blocs de cent :
  **ouvrir les 100 entrées suivantes**, et pour une notice loin dans le niveau
  aussi **ouvrir les 100 entrées précédentes**.
- Les notices que vous ne pouvez pas voir n'apparaissent ni comme ligne ni dans
  le décompte.

Si vous n'avez pas besoin du bouton, masquez-le dans votre profil sous
**Paramètres**.

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
