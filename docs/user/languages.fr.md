# Configuration linguistique dans Anton

## Vue d'ensemble

Anton prend en charge des contenus multilingues (DE, EN, FR et IT) pour différents champs (titre, champs de texte, mots-clés, etc.). Ce document décrit les réglages disponibles et donne des recommandations pour la configuration.

## Types de langue

Anton connaît deux concepts distincts de «&nbsp;langue&nbsp;» :

1. **Langue de l'interface** (`app.locale`) : la langue de l'interface utilisateur (menus, libellés, messages)
2. **Langues de contenu** (`locales`) : les langues dans lesquelles les données archivistiques peuvent être saisies

## Paramètre système : `locales`

| Propriété | Valeur |
|------------|------|
| Type | Tableau |
| Portée | `localisation` |
| Exemple | `["de", "en", "fr"]` |

Définit les langues disponibles pour les champs traduisibles.

**Important :** la **première langue du tableau est la langue principale** et sert de solution de repli lorsqu'aucune valeur n'existe pour une autre langue.

**Champs traduisibles :**
- Titre (AntonObject)
- Champs de texte (Note)
- Mots-clés (name, use_for)
- Lieux (description)

## Paramètre utilisateur : `show_all_locales_in_edit_forms`

| Propriété | Valeur |
|------------|------|
| Type | Booléen |
| Valeur par défaut | `false` |
| Emplacement | Profil → Paramètres → Saisie |

**Lorsqu'il est activé (`true`) :**
- Les formulaires de saisie affichent des **champs séparés pour chaque langue configurée**
- Exemple : titre (DE), titre (EN), titre (FR)

**Lorsqu'il est désactivé (`false`) :**
- **Un seul champ** est affiché (pour la langue actuelle de l'interface)
- Les valeurs déjà saisies dans d'autres langues sont indiquées à titre informatif, mais ne sont pas modifiables

## Langue lors de l'import

Un import possède sa propre **langue de contenu**, indépendante de la langue de l'interface. Elle détermine dans quelle langue sont écrits les titres, les champs de texte et les données d'autorité nouvellement créées — et dans quelle langue Anton recherche les acteur·trice·s et lieux existants.

La langue est choisie délibérément et est visible avant l'exécution.

Les champs traduisibles peuvent aussi être adressés **par langue** dans l'import — `title_de`, `title_fr`, `scopecontent_it`. Des titres multilingues sont ainsi importables, et le tableau de mise à jour d'un service multilingue sort et rentre sans perte.

Les deux aspects sont décrits en détail sous [Import → Langue de contenu de l'import](import.md#langue-de-contenu-de-limport).

## Comportement de repli

Lorsqu'aucune valeur n'existe pour la langue courante :
1. Anton utilise la valeur de la **première langue** de `setting('locales')`
2. Si rien n'y figure non plus : recherche dans les autres langues configurées

Dans la vue de détail, les personnes chargées de la description voient de quelle langue provient la valeur (p. ex. «&nbsp;Titre (DE)&nbsp;»).

## Recommandation : une langue par champ

**Notre recommandation est de n'enregistrer qu'une seule langue par champ** (`show_all_locales_in_edit_forms = false`).

### Raisons

1. **Cohérence** : si les titres sont saisis dans plusieurs langues, toutes les traductions doivent être maintenues. Lorsque l'original est modifié, les traductions ne sont souvent pas mises à jour.

2. **Normes archivistiques** : dans la pratique archivistique, les documents sont normalement décrits dans leur langue d'origine, non traduits.

3. **Recherche** : la recherche plein texte (colonne `full_text`) contient toutes les versions linguistiques. Cela peut donner des résultats déroutants.

4. **Charge de maintenance** : la tenue de données multilingues exige nettement plus de ressources.

### Quand le multilinguisme a du sens

- Services d'archives à public international (p. ex. collections scientifiques)
- Fonds comportant des documents en différentes langues, où le titre est saisi dans la langue d'origine
- Institutions soumises à une obligation légale de multilinguisme

## Exemples de configuration

### Service monolingue 

```php
// Setting: locales
["de"]
```
```php
// UserSettings
show_all_locales_in_edit_forms: false
```

### Service bilingue (DE/FR)

```php
// Setting: locales
["de", "fr"]
```
```php
// UserSettings (selon les besoins)
show_all_locales_in_edit_forms: false  // Recommandé
```

### Service international

```php
// Setting: locales
["en", "de", "fr", "it"]
```
```php
// UserSettings (pour les traducteur·trice·s)
show_all_locales_in_edit_forms: true
```
