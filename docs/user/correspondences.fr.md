# Correspondances

La vue des correspondances regroupe les lettres en échanges épistolaires : elle
montre qui a correspondu avec qui, combien de lettres sont conservées et sur
quelle période. De là, l'échange peut être parcouru chronologiquement — avancer
et reculer reste à l'intérieur du même échange.

La vue se trouve sous `/correspondences`. Elle n'est pas liée dans la
navigation ; les services qui l'utilisent l'ajoutent eux-mêmes au menu.

## Un échange se constitue de lui-même

Il n'y a rien à cliquer ni à créer. Anton déduit les échanges
**automatiquement des [événements](antonevents.md)** :

> Si une unité de description porte un événement **Dates de création** avec
> l'acteur·trice A et un événement **Réception** avec l'acteur·trice B, elle est
> considérée comme une lettre de A à B.

La personne expéditrice est donc saisie comme acteur·trice de l'événement de
création, la personne destinataire comme acteur·trice de l'événement de
réception. Dès qu'un nombre suffisant de telles paires existe, l'échange
apparaît dans la liste. Inversement : qui veut utiliser cette vue doit saisir
systématiquement les deux événements lors de la description — une lettre à
laquelle manque l'événement de réception n'apparaît nulle part.

Le niveau de description n'a aucune importance.

!!! note "Nombre minimal de lettres"
    Une paire d'acteur·trice·s n'apparaît qu'à partir d'un nombre minimal de
    lettres — cinq par défaut. Les lettres isolées restent donc de côté. Le seuil
    est paramétrable par archive, mais n'est pas modifiable dans la section
    Admin ; avec Anton as a Service, k & r s'en charge.

## Pour qui cela en vaut la peine

La vue s'adresse aux services conservant des fonds de lettres — legs,
collections de correspondances savantes. Elle est présente dans chaque
installation mais reste vide tant que la description ne suit pas cette
systématique. Pour un service sans lettres, elle est sans utilité.
