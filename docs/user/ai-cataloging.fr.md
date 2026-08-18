# Description assistée par IA

Anton peut faire générer des propositions de description par un modèle de
langage : celui-ci lit les médias associés et propose des titres, des champs de
texte, des événements, des mots-clés, des acteur·trice·s, des lieux et des
langues.

!!! note "À activer au préalable"
    La description assistée par IA n'est actuellement pas activée par défaut.
    Elle suppose deux choses : une autorisation dans la configuration du serveur,
    inaccessible depuis la section Admin — avec Anton as a Service, c'est k & r
    qui la pose — et l'interrupteur dans le service lui-même. Un plafond de coûts
    doit en outre être enregistré ; s'il manque, toutes les requêtes sont
    interrompues.

## Générer des propositions

Le masque de saisie comporte le bloc **Description par IA** ; le bouton du même
nom en haut y conduit. Un clic sur **générer des propositions IA** envoie la
requête ; les propositions apparaissent ensuite sous forme de pastilles à côté
des champs concernés, chacune assortie de **reprendre**, **ajouter** et
**ignorer**.

Rien n'est écrit automatiquement dans la base de données — les propositions
arrivent dans le formulaire et ne sont enregistrées qu'avec le bouton
d'enregistrement habituel. La génération suppose le rôle `editor`.

## Ce qu'Anton reprend de lui-même — et ce qu'il ne reprend pas

Les valeurs par défaut sont délibérément inégales :

| Proposition | Valeur par défaut |
|---|---|
| Acteur·trice, lieu, mot-clé — **déjà existant** | est associé |
| Acteur·trice, lieu, mot-clé — **à créer** | est rejeté |
| **Titres et champs de texte** | sont rejetés |

Cela signifie : **l'IA ne modifie jamais le titre d'elle-même.** Qui veut une
proposition doit la reprendre explicitement. Et de nouvelles notices d'autorité
ne naissent pas en passant — la barrière pour les nouveaux acteur·trice·s et
mots-clés reste délibérément haute.

Anton crée les événements proposés comme **Dates de création**. S'il s'agit d'un
autre type d'événement, il faut le corriger à la main après la reprise.

## Protection des données

Anton signale chaque profil d'IA selon le lieu de traitement des données : 🇨🇭
pour les modèles hébergés en Suisse, ⚠️ pour tous les autres. Avec un profil non
suisse, un avertissement rouge apparaît :

> **⚠️ Attention — protection des données**
> Ce profil traite des données hors de Suisse et n'est PAS conforme à la
> LPD/RGPD. Ne l'utilisez que pour des données que vous publieriez aussi
> ouvertement.

Un profil suisse est préréglé. En choisir un autre est une décision délibérée au
cas par cas : la sélection est repliée, ne vaut que pour la requête en cours et
n'est pas mémorisée.

!!! danger "Vérifier avant l'envoi"
    Avec la requête, les contenus de l'unité de description — médias compris —
    quittent le service. Pour les fonds bloqués, les données personnelles et tout
    ce qui est soumis à un délai de protection, cela n'est pas admissible avec un
    profil non suisse.

Chaque requête est journalisée ; la consommation, les coûts et une piste d'audit
figurent sous **Admin → Description par IA**.
