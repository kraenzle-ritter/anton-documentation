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

Chaque compte a des limites : 30 propositions par heure au plus et au plus un quart du budget mensuel par jour. L'exploitation fixe ces valeurs pour chaque archive. Les enregistrements sonores et le son des vidéos sont transcrits en arrière-plan ; tant que cela dure, la proposition est faite sans eux, avec un avis. Redemander plus tard, et la transcription est incluse.

## Pour tout ce qui se trouve sous une unité de description

Pour un versement comptant de nombreuses pièces, il existe le **passage IA** : dans la vue détaillée d'une unité de description, le bouton **Passage IA** mène à une page où l'on choisit le profil, le périmètre (uniquement les notices avec médias, ou toutes) et la limite d'appels. En dessous figurent le coût probable, facturé selon la consommation, et ce qui reste du budget mensuel et de sa propre part du jour. Le lancement requiert le rôle `editor`.

Le passage travaille en arrière-plan, notice par notice, selon les mêmes règles que le bouton du formulaire : les notes internes ne vont pas au fournisseur, ni aucune information des notices verrouillées. Il s'arrête lorsque la limite ou le budget est atteint et peut être annulé ; **Reprendre** continue avec la notice suivante.

Avec l’étendue «seulement les notices avec médias», le passage ignore les notices dont aucun fichier ne peut être envoyé à l’IA, par exemple des fichiers Word ou des fichiers manquants ; elles ne coûtent rien et apparaissent sur la page comme «ignorées».

Le passage n'écrit rien dans les notices. Titres, champs de texte (par exemple portée et contenu), datation, langues, mots-clés, acteurs et lieux arrivent comme propositions dans la liste de contrôle, avec la source «KI-Erschliessung» ; on peut les y filtrer par source et par fonds et les confirmer une à une ou ensemble. Si une entrée existe déjà dans Anton, elle est présélectionnée. Le passage ne propose pas de substituts comme «Unbekannt» ou «Nicht angegeben», et une datation seulement là où la notice n’en a pas encore pour cet événement. Il écrit «ß» comme «ss» ; chaque archive peut le désactiver avec le paramètre `ai_swiss_spelling`.

Pour le titre, un champ de texte et la datation, la liste affiche à côté de la proposition ce que contient la notice jusqu'ici. Si le champ est vide, la confirmation reprend la proposition. S'il contient déjà une valeur, il faut choisir dans la ligne : **Remplacer la valeur actuelle** ou, pour un champ de texte, **Ajouter au texte actuel**. Sans ce choix, la valeur actuelle reste, même lors d'une confirmation groupée.

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
