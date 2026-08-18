## Prêt d'objets

### Prêter des objets
Pour voir les prêts sur un objet et pouvoir marquer un objet comme prêté, le champ prêt (id : 47) doit figurer dans le formulaire utilisé.

Après un clic sur le plus, un prêt à un·e utilisateur·trice peut être enregistré. Cette personne est alors liée à l'objet. Le jour du prêt est saisi à cette occasion. Des indications complémentaires peuvent être consignées dans un commentaire (but du prêt, date de retour prévue).

### Retour des objets
Ce n'est qu'au retour que la date de fin est renseignée. Le prêt est ainsi clos.

### Liste des prêts en cours
La section Admin comporte une liste des prêts en cours (`/loans`), c'est-à-dire des prêts sans date de retour. De là, on peut aussi bien sauter vers les utilisateur·trice·s — pour enregistrer par exemple les prêts d'une personne comme rendus — que vers les objets prêtés.

### Affichage chez chaque utilisateur·trice
Chez chaque utilisateur·trice (`/users/{user_id}`), les prêts sont présentés dans un tableau.

### Rôles
Les prêts peuvent être gérés par `editor`, `admin` et `loan_admin`.

<!-- 
Actuellement pas encore possible : définir des durées de prêt ; il faudrait pour cela probablement modifier le modèle de données des prêts.
-->
