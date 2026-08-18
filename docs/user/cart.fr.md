# Panier

Le panier — appelé **panier de commande** dans l'interface — permet aux
personnes qui consultent de rassembler des unités et d'en envoyer une commande
ou une demande par courriel au service d'archives. C'est une aide à la commande
et non une gestion des prêts ; les [prêts](loans.md) sont gérés séparément.

!!! note "Pas dans tous les services"
    Le panier de commande doit être activé pour le service. Le paramètre n'est
    pas modifiable dans la section Admin, il est défini lors de la mise en place
    de l'installation ; avec Anton as a Service, k & r s'en charge.

## Déroulement

1. Dans la vue de détail d'une unité de description, cliquer sur le **symbole du
   caddie**. Il se trouve à droite au-dessus de la notice et ne porte aucun
   libellé.
2. L'entrée **panier de commande** apparaît dans la navigation — et seulement à
   ce moment-là : tant que le panier est vide, elle n'existe pas dans le menu.
3. Sous **panier de commande** figurent les unités rassemblées. Certaines
   peuvent être retirées, et le panier entier peut être vidé.
4. Remplir le formulaire au-dessus et cliquer sur **Envoyer**.

!!! warning "Uniquement dossiers et pièces"
    Le bouton n'apparaît qu'aux niveaux **dossier** et **pièce**. Les fonds et
    les séries ne peuvent pas être commandés — il faut alors s'adresser au
    service.

## Le formulaire

Par défaut, doivent être indiqués : le **nom**, le **courriel**, la **date de la
visite prévue** et un **message** ; l'**institution** est facultative. Les champs
sont adaptables par archive.

La commande part par courriel vers le service. La personne qui commande y figure
comme adresse de réponse et en reçoit une copie.

## Ce que le service en fait

La commande arrive dans la **boîte de courriel** du service — c'est là qu'elle
est traitée. Anton ne tient **aucune gestion des commandes** : il n'y a ni liste
des commandes en cours, ni statut, ni vue de détail. Seul le nombre fait l'objet
d'une analyse, sous [Statistiques](statistics.md) →
«&nbsp;prêts et commandes&nbsp;».

!!! danger "Vérifier l'adresse du destinataire"
    Si aucune adresse de destinataire n'est enregistrée pour le service, une
    adresse par défaut codée en dur chez k & r prend le relais — la commande
    n'arrive alors pas au service. Lors de la mise en service du panier de
    commande, il faut donc vérifier que l'adresse est bien définie et contrôler,
    au moyen d'une commande test, qu'elle parvient à destination.

## Le panier ne dure pas éternellement

Son contenu est conservé dans la session. Après la déconnexion ou à l'expiration
de la session, il disparaît — un panier de commande ne peut pas être constitué
sur plusieurs jours.
