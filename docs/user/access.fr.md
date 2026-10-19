# Accès, notices non publiées et délais de communicabilité

Anton règle l'accès à trois niveaux : par le rôle de la personne, par le
paramètre indiquant si le service est public, et pour chaque notice par deux
choses distinctes — la **non-publication** de la notice et le **délai de
communicabilité**.

## Le service est-il public ?

Le paramètre **public_access** détermine si les personnes extérieures voient le
catalogue. S'il est désactivé, la base de données n'est ouverte qu'aux personnes
connectées. S'il est activé, le catalogue est public — ce que montrent les
notices individuelles relève alors de la non-publication et des délais de
communicabilité.

Ce que chaque rôle peut faire figure dans la
[Prise en main](index.md#roles).

## Notice non publiée et délai de communicabilité

> Le **délai de communicabilité** protège les documents ; la notice reste
> trouvable. La **non-publication** retire toute la notice, description
> comprise.

| | Notice non publiée | Délai de communicabilité |
|---|---|---|
| Description (titre, dates, description archivistique) | invisible | visible et trouvable |
| Images et documents | invisibles | seulement à partir de «&nbsp;Communicable dès&nbsp;» |
| Unités subordonnées | toujours non publiées aussi | type : non ; «&nbsp;Communicable dès&nbsp;» saisi à la main : oui |
| Limité dans le temps | non | oui |

Les deux restent visibles pour les utilisateur·trice·s internes, les personnes
chargées de la description et l'administration. Un service peut avoir renommé
les champs ; depuis Anton 0.108, les noms standard sont ceux employés ici.

## Notice non publiée

Le champ **Notice non publiée** retire toute la notice de la consultation
publique : description, médias et toutes les unités subordonnées. Elle
n'apparaît ni dans la recherche ni par les interfaces (API, OAI, plan du site).
La non-publication se transmet toujours vers le bas — sous une notice non
publiée, il n'y a pas de notice publique.

## Délai de communicabilité

Le délai de communicabilité protège uniquement les documents et les
numérisations : si une unité de description y est encore soumise, la notice
reste visible et trouvable, mais pas les images ni les documents.

Anton calcule **une** année par notice à partir de laquelle elle est
communicable. Font foi :

1. **Le champ «&nbsp;Communicable dès&nbsp;».** Cette valeur prime et **vaut
   vers le bas dans l'arborescence** pour toutes les unités subordonnées.
2. **Sinon le délai de communicabilité du type choisi**, compté à partir de la
   date de création. Les délais liés au type ne valent **que pour la notice
   elle-même** et ne se transmettent pas.

Le champ **Délai de communicabilité** sélectionne le type. Trois sont fournis
par défaut :

| Type | Délai |
|---|---|
| public | aucun — communicable immédiatement |
| délai standard | 30 ans |
| délai prolongé | 70 ans |

Les délais sont configurables par archive : les types peuvent être renommés,
complétés et modifiés dans leur durée ; «&nbsp;jamais communicable&nbsp;» est
également possible. La gestion est réservée aux superutilisateur·trice·s ; avec
Anton as a Service, k & r s'en charge.

!!! note "«&nbsp;Communicable dès&nbsp;» est la première année libre"
    Pour une création en 1990 et un délai de 30 ans, on y lit 2021 : dès 2021,
    les documents sont communicables. Jusqu'à 0.107, le champ s'appelait
    «&nbsp;Délai de protection jusqu'à&nbsp;» — la valeur a toujours été la
    première année libre.

## Médias isolés : interne seulement

Les **médias isolés** peuvent être définis comme **interne seulement** dans le
masque de saisie. Cela vaut sans limite de durée et pour ce seul média ; la
notice et ses autres médias restent tels quels.

## Ouvrir certains secteurs

Une personne ayant le rôle d'utilisateur·trice peut se voir ouvrir l'accès à
certaines branches. Les identifiants des notices sont pour cela saisis dans la
gestion des utilisateur·trice·s sous forme de liste séparée par des virgules. Un
identifiant vaut toujours pour **toute la branche** qui en dépend.

## Statut de la description

Le champ est prévu pour les fonds. Si un fonds est au statut
**brouillon**, il n'est accessible qu'aux utilisateur·trice·s internes, aux
personnes chargées de la description et à l'administration.
