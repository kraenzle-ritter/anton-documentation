# Sélection et actions groupées

Plusieurs unités de description peuvent être cochées dans les listes de
résultats et traitées ensemble. Il existe actuellement **une** action à cet
effet : le [déplacement](hierarchy.md).

!!! note "Seulement dans certains services"
    Les actions groupées doivent être activées et supposent le rôle `admin`.
    Elles ne constituent pas un standard ; le paramètre n'est pas modifiable
    dans la section Admin, et avec Anton as a Service, k & r s'en charge. Qui n'en
    a pas besoin peut en outre les désactiver dans son propre profil.

## D'abord l'action, ensuite la sélection

L'ordre est inverse de l'habitude et constitue l'écueil le plus fréquent :

1. **D'abord** choisir l'action dans le champ de sélection **actions** — est
   disponible le **déplacement**. Auparavant, rien ne peut être coché ; les cases
   restent sans effet.
2. **Ensuite** cocher les unités. L'icône représentant une liste sur presse-papier
   au-dessus de la liste de résultats — elle indique le nombre d'unités
   sélectionnées — permet de consulter la sélection courante à tout moment.
3. Exécuter l'action. **Vider** abandonne la sélection.

!!! warning "Changer d'action vide la sélection"
    Si le champ de sélection est modifié après coup, la sélection existante est
    abandonnée. L'action doit donc être définie avant de cocher.

## Ce qui peut être sélectionné ensemble

Uniquement des unités qui **pourraient être de même niveau**. Dès qu'un dossier
est coché, un fonds ne peut plus être ajouté — Anton empêche les sélections qui
ne pourraient pas être déplacées ensemble. Qui ne parvient pas à cocher une unité
devrait donc vérifier les niveaux déjà sélectionnés.

Si une opération de déplacement est déjà en cours, la sélection est verrouillée
jusqu'à ce que celle-ci soit achevée ou annulée.

## À ne pas confondre avec le panier de commande

La sélection et le [panier de commande](cart.md) se ressemblent et constituent
pourtant deux listes distinctes qui ne s'influencent jamais. La sélection sert au
traitement, le panier de commande à la commande. Une sélection ne peut pas être
reprise dans le panier de commande.
