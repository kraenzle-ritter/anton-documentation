# Accès et délais de protection

Anton règle l'accès à trois niveaux : par le rôle de la personne, par le
paramètre indiquant si le service est public, et par les délais de protection
attachés à chaque notice.

## Le service est-il public ?

Le paramètre **public_access** détermine si les personnes extérieures voient le
catalogue. S'il est désactivé, la base de données n'est ouverte qu'aux personnes
connectées. S'il est activé, le catalogue est public — ce que montrent les
notices individuelles relève alors des délais de protection.

Ce que chaque rôle peut faire figure dans la
[Prise en main](index.md#roles).

## Délais de protection

Si une unité de description est encore soumise à un délai de protection, la
notice reste visible, mais pas les images ni les documents.

Anton calcule **une** année de libération par notice. Font foi :

1. **Le champ «&nbsp;protégé jusqu'à&nbsp;»** (année de libération). Cette
   valeur prime et **se transmet vers le bas dans l'arborescence** à toutes les
   unités subordonnées.
2. **Sinon le délai de protection du type choisi**, compté à partir de la date
   de création. Les délais liés au type ne valent **que pour la notice
   elle-même** et ne se transmettent pas.

Le champ **conditions d'accès / délai de protection** sélectionne le type. Trois
sont fournis par défaut :

| Type | Délai |
|---|---|
| public | aucun — librement accessible immédiatement |
| délai de protection standard | 30 ans |
| délai de protection prolongé | 70 ans |

Les délais sont configurables par archive : les types peuvent être renommés,
complétés et modifiés dans leur durée ; «&nbsp;ne jamais libérer&nbsp;» est
également possible. La gestion est réservée aux superutilisateur·trice·s ; avec
Anton as a Service, k & r s'en charge.

!!! note "L'année de libération affichée"
    Ce qui est affiché est la première année où l'unité est **libre** — pour une
    création en 1990 et un délai de 30 ans, donc 2021 et non 2020.

## Bloquer sans limite de durée

Les **médias isolés** peuvent être bloqués sans limite de durée dans le masque
de saisie.

Les **notices entières** sont bloquées par le champ **bloqué**. Il agit sur la
notice, sur toutes les unités subordonnées et sur leurs médias ; ceux-ci ne
restent visibles que pour les utilisateur·trice·s internes, les personnes
chargées de la description et l'administration.

## Ouvrir certains secteurs

Une personne ayant le rôle d'utilisateur·trice peut se voir ouvrir l'accès à
certaines branches. Les identifiants des notices sont pour cela saisis dans la
gestion des utilisateur·trice·s sous forme de liste séparée par des virgules. Un
identifiant vaut toujours pour **toute la branche** qui en dépend.

## Statut de la description

Le champ est prévu pour les fonds. Si un fonds est au statut
**brouillon**, il n'est accessible qu'aux utilisateur·trice·s internes, aux
personnes chargées de la description et à l'administration.
