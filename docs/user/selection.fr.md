# Sélection et actions groupées

Plusieurs unités de description peuvent être cochées dans les listes de résultats et traitées ensemble. Il existe deux actions à cet effet : le [déplacement](hierarchy.md), à partir du rôle `admin`, et la [modification groupée](#sammelbearbeitung), à partir du rôle `editor`.

!!! note "Seulement dans certains services"
    Les actions groupées doivent être activées. Elles ne constituent pas un standard ; le paramètre n'est pas modifiable dans la section Admin, et avec Anton as a Service, k & r s'en charge. Qui n'en a pas besoin peut en outre les désactiver dans son propre [profil](profile.md).

## D'abord l'action, ensuite la sélection

L'ordre est inverse de l'habitude et constitue l'écueil le plus fréquent :

1. **D'abord** choisir l'action dans le champ de sélection **actions** : **déplacer** ou **modifier**. Auparavant, rien ne peut être coché ; les cases restent sans effet.
2. **Ensuite** cocher les unités. L'icône représentant une liste sur presse-papier au-dessus de la liste de résultats — elle indique le nombre d'unités sélectionnées — permet de consulter la sélection courante à tout moment.
3. Exécuter l'action. **Vider** abandonne la sélection.

!!! warning "Changer d'action vide la sélection"
    Si le champ de sélection est modifié après coup, la sélection existante est abandonnée. L'action doit donc être définie avant de cocher.

## Ce qui peut être sélectionné ensemble

Pour le **déplacement**, uniquement des unités qui **pourraient être de même niveau**. Dès qu'un dossier est coché, un fonds ne peut plus être ajouté — Anton empêche les sélections qui ne pourraient pas être déplacées ensemble. Qui ne parvient pas à cocher une unité devrait donc vérifier les niveaux déjà sélectionnés. Pour la **modification**, toutes les unités peuvent être sélectionnées ensemble.

Si une opération de déplacement est déjà en cours, la sélection est verrouillée jusqu'à ce que celle-ci soit achevée ou annulée.

## Modification groupée {#sammelbearbeitung}

Avec l'action **modifier**, le bouton **Modifier (nombre)** de la sélection mène à la page **Modification groupée**. Une modification y vaut pour toutes les unités sélectionnées, 500 au maximum à la fois.

- **Définir une liste de valeurs** : lieu de conservation, type d'objet, statut ou niveau de détail de la description, ou le vider ; au choix **seulement si vide**.
- **Définir un champ de texte** : dans une langue, **remplacer**, remplir **seulement si vide** ou **ajouter à la fin** un texte (nouveau paragraphe).
- **Mot-clé** : **ajouter** ou **retirer** un mot-clé existant.
- **Rechercher et remplacer** : dans le titre ou un champ de texte (toutes les langues), au choix en respectant la casse et pour des mots entiers seulement.

Seuls les champs des formulaires d'édition de l'archive sont proposés. La recherche est littérale, sans caractères génériques. La cote, le niveau de description et le délai de protection ne se modifient pas de façon groupée.

Le déroulement : d'abord l'**aperçu** (nombre d'unités qui changent, les 20 premières modifications avant et après ; il n'écrit rien), puis **Exécuter**, seulement après un aperçu de exactement ces réglages. L'exécution se fait en arrière-plan : Anton fait d'abord une **sauvegarde de la base de données** ; si elle échoue, rien n'est modifié. **Dernières exécutions** indique l'état, le nombre d'unités modifiées, les erreurs et le nom de la sauvegarde. Chaque modification figure dans l'historique de l'unité, au nom de la personne qui a lancé l'exécution ; on l'annule par la sauvegarde, ce qui relève de l'administration.

## À ne pas confondre avec le panier de commande

La sélection et le [panier de commande](cart.md) se ressemblent et constituent pourtant deux listes distinctes qui ne s'influencent jamais. La sélection sert au traitement, le panier de commande à la commande. Une sélection ne peut pas être reprise dans le panier de commande.
