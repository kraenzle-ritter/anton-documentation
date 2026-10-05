# Données d'autorité dans l'éditeur XML (VS Code, Oxygen)

Qui encode des éditions en TEI peut reprendre les acteur·trice·s, les lieux et
les mots-clés directement depuis Anton, sans quitter l'éditeur : sélectionner
un nom, raccourci clavier, choisir un résultat — le plugin écrit l'ID Anton dans
l'attribut, par exemple `<persName ref="sulger-actors-123">`. La recherche se
fait en direct dans Anton ; aucun registre n'est jamais téléchargé en entier.

Il existe deux plugins aux fonctions identiques :

| Éditeur | Plugin | Installation |
|---|---|---|
| Visual Studio Code | [anton-vs](https://github.com/kraenzle-ritter/anton-vs) | le fichier `anton-vs-<version>.vsix` des [releases](https://github.com/kraenzle-ritter/anton-vs/releases/latest) |
| Oxygen XML Editor | [anton-oxy](https://github.com/kraenzle-ritter/anton-oxy) | dans Oxygen via **Help → Install new add-ons…** avec l'adresse `https://github.com/kraenzle-ritter/anton-oxy/releases/latest/download/updateSite.xml` |

L'installation et l'utilisation sont décrites dans le README de chaque plugin
sur GitHub. Cette page traite de ce qu'il faut configurer du côté d'Anton.

## Archive publique ou non publique

Pour une archive **publique**, l'adresse de l'archive suffit au plugin, par
exemple `https://archive.example.ch`.

Une archive **non publique** ne livre ses registres que si le plugin envoie un
**jeton API**. Sans jeton, le plugin affiche :

```
Anton HTTP 401 … {"error":"This archive is not public"}
```

Il faut pour cela la version 1.4.0 du plugin ou une version plus récente.

## Créer un jeton API

Un jeton est créé par une personne ayant le rôle `admin` dans l'archive. Il
appartient à un compte distinct avec le rôle **`user`**, et non à votre propre
compte d'administration : un jeton a les droits du compte auquel il est
rattaché. Sur un compte `user`, il peut chercher et lire, mais rien modifier.

### 1. Créer un compte pour les plugins

Une fois par archive ; ensuite, tout le monde utilise le même compte.

1. Sous **Admin → Utilisateurs·trices**, créer un nouveau compte.
2. Nom et nom d'utilisateur au choix, par exemple « Plugins éditeur » et
   `editor-plugins`.
3. Une **adresse e-mail** qu'aucun autre compte n'utilise encore, par exemple
   une adresse de projet. Anton y envoie une invitation à définir un mot de
   passe ; on peut l'ignorer, car personne ne se connecte avec ce compte.
4. **Rôle : `user`**.

### 2. Générer le jeton

1. Ouvrir le nouveau compte sous **Admin → Utilisateurs·trices**.
2. Dans la section **Jetons API** :
    - **Nom** : qui utilise le jeton et pour quoi, par exemple « VS Code Noëmi »
      ou « Oxygen Stefan ». Un jeton par personne — ainsi chacun peut être
      révoqué séparément.
    - **Expire le** : une date, par exemple dans un an. Vide signifie sans
      échéance.
3. **Créer un jeton API**.
4. **Copier le jeton immédiatement.** Anton ne l'affiche que cette seule fois ;
   seul un hash est enregistré, même Kränzle & Ritter ne peut plus le lire
   ensuite.

!!! warning "Traiter un jeton comme un mot de passe"
    Qui possède le jeton peut lire tout ce que le compte a le droit de lire. Ne
    pas l'envoyer par e-mail ni le conserver dans des fichiers partagés.

## Saisir le jeton dans le plugin

**VS Code** : **Paramètres → Extensions → Anton**, le champ du jeton API (le
paramètre s'appelle `anton.apiToken`). L'adresse de l'archive se trouve dans
la même section sous `anton.baseUrl`. Le jeton n'est pas transmis à d'autres
ordinateurs par la synchronisation des paramètres de VS Code ; il faut l'y
saisir à nouveau.

**Oxygen** : **Anton → Anton-Einstellungen…**, champ **API token** ;
l'adresse de l'archive figure au-dessus sous **Anton base URL**.

## Révoquer et remplacer

Sur la page du compte, la section **Jetons API** liste chaque jeton avec son
nom, sa dernière utilisation et sa date d'échéance. **Révoquer** le désactive
immédiatement.

Si un jeton est perdu, échu ou tombé en de mauvaises mains : en générer un
nouveau, le saisir dans le plugin, révoquer l'ancien. Si le plugin affiche

```
Anton hat den API-Token abgelehnt (falsch, abgelaufen oder Konto gesperrt)
```

(« Anton a refusé le jeton API (erroné, échu ou compte bloqué) »), c'est
exactement ce qu'il faut faire. Passer le compte à `blocked` désactive tous ses
jetons d'un coup.
