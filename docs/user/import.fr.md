## Résumé
Il est possible d'importer dans Anton des données et les fichiers associés (médias). Les données de description (fichier Excel) sont saisies dans une feuille Excel (imposée) et chargées sur le serveur avec les fichiers. Les données sont ensuite validées et, si la validation a réussi, l'import/ingest peut avoir lieu (données de description et médias). Voir aussi la documentation dans Anton sous `/import/documentation`.

## Hub d'import `/import`

Depuis la **v0.62.0**, toutes les voies d'import sont regroupées à une seule adresse : `/import` (dans le menu sous **Import / Export → Import**). La page comporte quatre onglets :

| Onglet | Contenu |
|---|---|
| **Boîte d'entrée** (par défaut) | SIP agate en attente, auxquels il manque encore un fonds parent. Lorsque quelque chose est en attente, un badge compteur apparaît à côté dans le menu Admin. |
| **SIP** | Téléversement SIP direct (paquets BagIt) avec validation et ingest. Voir [SIP Ingest](../admin/sip-ingest.md) et [agate SIP](../admin/agate-sip.md). |
| **Excel** | Imports Excel (le thème principal de cette page, voir ci-dessous). |
| **Répertoire** | Import d'une arborescence de répertoires (ZIP/GZ) comme entrée dans les archives d'accroissement. |

Les anciennes URL (`/sip/validation`, `/sip/ingest`, `/import/validation`, `/import/ingest`, `/sip/inbox`) redirigent de manière transparente vers l'onglet correspondant — les signets et les liens externes restent valables.

### Vue de détail dans la boîte d'entrée

Pour chaque SIP en attente dans la boîte d'entrée, il existe un lien **Détails**. Derrière se trouve une page d'inspection qui ne lit que le `metadata.json` du BagIt (sans décompresser les médias) et affiche :

- la validité BagIt (manifeste, sommes de contrôle)
- le nombre de notices dans le SIP
- les catégories de types d'objets NARA — avec une indication si le tenant ne connaît aucun type approprié pour une catégorie
- le titre de la notice la plus élevée

On peut ainsi voir avant l'import si le SIP est pertinent, si le vocabulaire du tenant convient, et le cas échéant écarter le SIP avant que quoi que ce soit n'arrive dans la base de données.

### Progression en direct

Depuis la v0.62.0, tous les imports s'exécutent **de manière asynchrone en arrière-plan**. Après un clic sur «&nbsp;Importer&nbsp;», on arrive sur une page de progression qui actualise l'état courant toutes les quelques secondes : phase (préparation / création des notices / lecture des médias), lignes traitées, et à la fin un lien vers la **cote d'accroissement** créée dans les archives.

Cela vaut pour toutes les voies — Excel, SIP, répertoire et finalisation de la boîte d'entrée.

### Une cote d'accroissement pour chaque import

Chaque import (quelle que soit la voie) crée une notice annexe dans les archives d'accroissement (AKZ) portant le numéro `AKZ {année}/{N}`. L'entrée consigne :

- le nom de fichier d'origine
- la somme de contrôle MD5
- le moment de l'import
- la voie d'import (Excel / SIP / répertoire / agate)
- les **réglages utilisés**, depuis la v0.87.0 (voir ci-dessous)

Les imports échoués ne laissent **aucun trou** dans la numérotation AKZ — le numéro n'est attribué qu'à l'issue d'un import réussi.

### Journal des imports

Sous **`/import/audit`** se trouve la liste de toutes les exécutions d'import : cote, fichier source, moment, nombre de notices créées et langue de contenu utilisée. Depuis la **v0.87.0**, il s'agit d'un tableau Anton ordinaire — triable, avec une longueur de page paramétrable, et les colonnes peuvent être adaptées sous *Admin → Formulaires* comme pour n'importe quelle autre liste.

Le lien **Détails** conduit à la notice d'accroissement. Depuis la v0.87.0, sa vue ne montre plus que ce qui décrit un import — fichier source, somme de contrôle, réglages utilisés avec leur provenance, le fichier téléversé comme média, et qui a déclenché l'exécution. Les champs sans objet pour un accusé d'import (*prêt*, *déplacé*) n'y apparaissent plus.

Les réglages sont consignés en clair, une ligne par réglage avec sa valeur et sa provenance. Ils y restent durablement — même un an plus tard, il est ainsi possible de retracer sous quelles hypothèses un versement est entré.

## Déroulement (import Excel)
Il faut d'abord créer un fichier Excel selon les prescriptions ci-dessous. Celui-ci est à téléverser sous «&nbsp;Upload Metadata&nbsp;» et les fichiers médias associés sous «&nbsp;Upload Medien&nbsp;». Le fichier Excel peut ensuite être contrôlé sous «&nbsp;Validation&nbsp;». La validation signale les erreurs et émet des avertissements. Les données ne peuvent être importées que lorsque la validation est exempte d'erreurs. L'import est déclenché sous «&nbsp;Ingest&nbsp;» et peut prendre quelques minutes selon le volume.

## Langue de contenu de l'import

Les champs traduisibles — titres, champs de texte, mots-clés, acteur·trice·s, lieux et lieux de conservation nouvellement créés — ont besoin d'une langue. Depuis la **v0.87.0**, il s'agit d'une décision délibérée, visible avant l'exécution.

!!! warning "Changement de comportement"
    Jusqu'à la v0.86.x, Anton suivait la **langue de l'interface**. Qui avait l'interface en anglais et chargeait un tableau créait pour chaque notice une traduction *anglaise* du titre — contenant le texte allemand inchangé. La notice paraissait correcte en anglais et n'avait plus de titre en allemand. À partir de la v0.87.0, la langue de l'interface ne joue plus aucun rôle.

La langue de contenu est déterminée dans cet ordre — la première valeur définie l'emporte :

1. le choix pour cette exécution (`--locale` en ligne de commande)
2. le réglage d'archive `import_options.locale`
3. la première langue de `locales` — la langue principale du service

Avant le démarrage, la page d'inspection indique la langue en vigueur **et sa provenance** («&nbsp;choisie pour cette exécution&nbsp;», «&nbsp;réglage d'archive&nbsp;», «&nbsp;valeur par défaut&nbsp;»). Après l'exécution, la même indication figure dans la notice d'accroissement (voir [Journal des imports](#journal-des-imports)).

Une colonne comportant un code de langue (`title_fr`) l'emporte sur ce choix pour son propre champ — voir [titel](#titel-title).

### Pourquoi la langue compte aussi lors de la recherche

La langue de contenu détermine non seulement où l'écriture a lieu, mais aussi **dans quoi Anton recherche les acteur·trice·s et lieux existants**. Si l'on choisit une langue dans laquelle le fonds n'est pas décrit, le rapprochement ne trouve rien — et, si la création est activée, crée une nouvelle notice pour chaque nom.

Anton effectue donc la recherche en deux tours : d'abord dans la langue de l'exécution, puis dans la langue principale du service. Un résultat issu du second tour est consigné dans le journal. Et l'aperçu (voir ci-dessous) indique le nombre de créations avant que quoi que ce soit ne soit écrit — si la langue ne correspond pas au fonds, presque tous les acteur·trice·s y apparaissent d'emblée comme «&nbsp;nouveaux&nbsp;».

### Où se trouvent les réglages

Les réglages d'import relèvent du service (`import_options`) et sont consultés là où ils agissent : sur la page d'inspection du fichier téléversé, chacun avec la **valeur en vigueur**, sa provenance et une explication. Sont affichés la langue de contenu et les interrupteurs déterminant si les acteur·trice·s, lieux, mots-clés, lieux de conservation et types d'objets inconnus sont créés.

Il n'existe délibérément **aucun** second emplacement dans le profil utilisateur : une valeur dont on n'a besoin qu'à l'import appartient à un seul endroit — et cet endroit la nomme avec sa provenance, au lieu de dire simplement «&nbsp;valeur par défaut&nbsp;».

## Aperçu : ce que l'import créerait

Avant le démarrage, la page d'inspection indique combien d'entrées d'autorité **distinctes** l'exécution créerait : acteur·trice·s, lieux, mots-clés, lieux de conservation, types d'objets. Ainsi que les noms eux-mêmes.

Le nombre compte des entrées distinctes, non des lignes : une actrice inconnue apparaissant dans 500 lignes constitue **une** création.

Les noms importent plus que le nombre. Un séparateur erroné se manifeste par le fait que «&nbsp;Muster, Hans; Beispiel, Anna&nbsp;» figure comme *un seul* nom dans la liste — dans un simple nombre, cela resterait invisible.

Si la création est désactivée pour une catégorie, les mêmes entrées apparaissent comme **non attribuables**, avec l'indication que ces liens seront purement et simplement abandonnés lors de l'exécution. C'est là aussi un résultat que l'on veut connaître d'avance.

Si le nombre de créations d'une catégorie dépasse la moitié des lignes, un **avertissement** apparaît. Cela signale plus souvent un problème de séparateur, de langue ou de colonne qu'un accroissement réel. L'avertissement ne bloque rien — l'exécution peut être lancée.

!!! note "L'aperçu n'écrit rien"
    Il ne fait que lire. Aucune notice n'est créée, pas même une qu'il faudrait supprimer ensuite.

## Colonnes
Le fichier peut contenir des colonnes supplémentaires ; celles-ci ne sont toutefois pas importées. Par souci de simplicité, des colonnes peuvent être supprimées. Le fichier définitif doit contenir au moins les colonnes suivantes :

    parent
    verzeichnungsstufe

## Explication et règles pour chaque colonne / champ

### parent

Le champ `parent` indique où la notice à importer est rattachée. Le champ ne doit pas être vide. Il peut contenir au maximum 100 caractères. Il doit contenir une cote existant déjà dans la base de données.

Comme Anton peut comporter des unités de description sans cote (par exemple des classes, des groupes de fonds), il est également possible d'indiquer le `parent` via l'`id`. Si le `parent` contient un nombre entier (integer), l'importeur considère qu'il s'agit du `parent_id`. L'`id` d'une unité de description est visible dans le `permalink`.

### Verzeichnungsstufe (level_of_description)

Le champ ne doit pas être vide. Il doit contenir un niveau de description existant :

    Archiv
    Bestandsgruppe
    Bestand
    Klasse
    Serie
    Dossier
    Einzelstück

### signatur (identifier)

Le champ peut contenir au maximum 100 caractères. Chaque cote ne peut apparaître qu'une seule fois. Si aucune cote n'est indiquée, une nouvelle cote unique est générée par Anton.

### altsignatur (identifier_old)

Le champ peut contenir au maximum 100 caractères.

### titel (title)

Le champ peut contenir du texte libre.

Le titre est un **champ traduisible**. La langue dans laquelle il est écrit est déterminée par la [langue de contenu de l'import](#langue-de-contenu-de-limport) — ou, plus précisément, par la désignation de la colonne elle-même :

| Colonne | écrit vers |
|---|---|
| `titel` ou `title` | la langue de contenu de l'exécution |
| `title_de`, `title_fr`, `title_it`, `title_en` | exactement la langue indiquée |

Depuis la **v0.87.0**, des titres multilingues peuvent donc être importés : une colonne par langue. Les deux formes peuvent coexister ; la colonne comportant un code de langue est l'indication la plus précise et l'emporte, et la page d'inspection le signale.

Il en va de même pour les **champs de texte** : `scopecontent` écrit dans la langue de contenu, `scopecontent_fr` spécifiquement en français, sans toucher aux autres langues du même champ.

!!! note "Uniquement les langues configurées"
    Un code de langue n'est reconnu que s'il figure dans le réglage `locales` du service (voir [configuration linguistique](languages.md)). `title_es` dans un service sans espagnol n'est pas une indication de langue mais une colonne inconnue — et l'inspection la signale comme telle.

### Antonevents
Les Antonevents relient les unités de description aux acteur·trice·s et aux lieux. Ils se composent des champs suivants : `actors, place, date_start, date_start_ca, date_end, date_end_ca, date_event_details`. Pour importer un Antonevent, l'EventType doit désormais être placé devant le nom du champ dans la désignation de la colonne, par exemple pour la création (dates extrêmes) :  `creation_actors, creation_place, creation_date_start, creation_date_start_ca, creation_date_end, creation_date_end_ca, creation_date_event_details`.

Il existe de nombreux Antonevents : `creation`, `acquisition`, `accumulation`, `destruction`, `validation`, `migration`, `reproduction`, `publication`, `digitisation`, `ingest`, `reception`, `performance`, `provenance`, `loaned`, `preservation`, `engravation`, `writing`, `coloring`, `edition`, `production`, `other`, `text_author`. 

#### Acteur·trice·s (p. ex. creation_actors)

Le champ peut contenir au maximum 500 caractères. L'indication de la période d'existence (dates de vie) entre parenthèses n'est pas obligatoire, mais possible. Les parenthèses ne doivent toutefois pas être utilisées à d'autres fins. Plusieurs acteur·trice·s devraient être séparés par `::`.

Exemple pour deux acteur·trice·s : 

```
Müller, Martina (1934-1977) :: Rechtsabteilung
```

Le format n'est pas validé au préalable ! Les acteur·trice·s sont créés s'ils ne sont pas trouvés dans Anton (la recherche se fait sur le nom).

Réglage d'import `create-actors` : les acteur·trice·s sont créés s'ils ne sont pas trouvés dans Anton.

Si un·e acteur·trice est déjà enregistré·e dans Anton, il ou elle peut aussi être référencé·e par son ID (integer).

Si un·e acteur·trice a été saisi·e avec une GND ou une autre ressource, il ou elle peut aussi être reconnu·e par cette ressource, en assortissant l'indication d'un préfixe (en minuscules et avec deux points, sans espace) : «&nbsp;gnd:118519522&nbsp;» (la ressource doit toutefois être unique au sein d'Anton). Si l'acteur·trice n'existe pas encore, il ou elle est créé·e à partir des données de la GND.

#### Places
Le champ peut contenir un lieu ou un places-id (integer). Réglage d'import `create-places` : les lieux sont créés s'ils ne sont pas trouvés dans Anton. Si un lieu est déjà enregistré dans Anton, il peut aussi être référencé par son ID (integer).

Les lieux peuvent contenir les éléments suivants :  
- le nom (séparé par «&nbsp;/&nbsp;»)  
- la ville / commune  
- le canton / land (placé entre parenthèses après la commune)

### Colonnes avec listes de valeurs

Plusieurs colonnes n'acceptent que des valeurs définies dans le service :
`verzeichnungsstufe`, `objekttyp`, `schutzfrist`, `status_of_description`,
`detail_of_description` et `vacat`.

Depuis la **v0.87.0**, elles acceptent toutes **trois formes**, de manière
équivalente (`vacat` déjà depuis la v0.86.4) :

| Forme | Exemple |
|---|---|
| Désignation | `Bestand` |
| Nom interne | `fonds` |
| ID | `3` |

L'ID est la forme la plus stable — elle survit à un changement de nom. Là où
une désignation ressemble par hasard à un nombre, la désignation l'emporte.

!!! tip "Les valeurs admises figurent dans le message d'erreur"
    Lorsqu'une valeur n'est pas reconnue, le contrôle nomme non seulement le
    problème, mais aussi la solution :

    > «&nbsp;Schachtel&nbsp;» ne figure pas dans la liste de valeurs. Sont
    > admis : Archiv (collection), Bestandsgruppe (recordgroup), Bestand
    > (fonds), Klasse (class), Dossier (file), Einzelstück (item), Serie
    > (series)

    La désignation vient en premier, le nom interne entre parenthèses. Il n'est
    donc pas nécessaire de consulter les listes au préalable.

#### Consulter toutes les listes de valeurs

Depuis la **v0.87.0**, une vue d'ensemble de toutes les listes de valeurs est
disponible sous **Import de tableau → Listes de valeurs** (`/valuelists`) :
pour chaque entrée la désignation, le nom interne et l'ID, ainsi que la colonne
d'import à laquelle la liste appartient. Un champ de recherche filtre toutes
les listes simultanément.

La page est en lecture seule et ouverte à toutes les personnes autorisées à
importer. Les listes modifiables sous *Admin → Listes de valeurs* exigent en
revanche le droit de **modifier** une liste — en dehors de l'administration du
système, peu de personnes en disposent, et seulement pour deux des dix-sept
listes. Qui voulait simplement consulter se heurtait auparavant à une porte
fermée.

Également sur la page : les **ID des lieux de conservation** pour la colonne
`location_id` du tableau de mise à jour.

Les mots-clés, acteur·trice·s et lieux n'y figurent *pas* — ce sont des notices
d'autorité dotées de leurs propres pages interrogeables, non des listes à
parcourir.

### objekttyp (object_type)

Le champ doit contenir un type d'objet existant déjà :

```
Akte
Bild
Band
Film
...
```

La liste des valeurs admises dépend des types d'objets que le service concerné a définis.

### umfang_zahl (object_count)

Le champ doit contenir un nombre entier (integer). L'indication se rapporte au type d'objet.

### sprache (languages)

Le champ peut contenir plusieurs langues. Les langues doivent soit correspondre au [code de langue ISO 639-2/B](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-2) («&nbsp;ger&nbsp;» et non «&nbsp;deu&nbsp;», «&nbsp;fre&nbsp;» et non «&nbsp;fra&nbsp;»), soit être écrites exactement comme dans la liste existante. Plusieurs langues peuvent être séparées par les caractères suivants (la virgule et le point-virgule ne sont pas possibles) :

```
    ::
```

### standort (location)

Le champ doit contenir un lieu de conservation déjà utilisé. Si un nouveau lieu de conservation doit être utilisé, il faut d'abord l'ajouter sous Admin - Lieux de conservation.

Il existe deux colonnes, et le nom indique dans chaque cas ce qui doit y figurer : **`location_id`** n'accepte que l'ID, **`location`** (également : `standort`) accepte l'ID *ou* la désignation. Si les deux sont présentes, `location_id` l'emporte.

### formularsatz (formset)

Détermine quel jeu de formulaires est utilisé pour la notice — donc quels champs apparaissent et dans quel ordre. Le champ est **facultatif** : s'il reste vide, Anton résout le jeu de formulaires par le niveau de description. Il n'est nécessaire que si une notice s'en écarte délibérément, par exemple le jeu de formulaires `letter` sur des pièces.

Comme pour le lieu de conservation, deux colonnes : **`formset`** (également : `formularsatz`) accepte le nom *ou* l'ID, **`formset_id`** uniquement l'ID. Les noms des jeux de formulaires disponibles figurent sous *Administration → Jeux de formulaires* — dans une installation standard par exemple `fonds`, `class`, `series`, `file`, `item`, `collection`, `recordgroup`, `default`.

Le tableau de mise à jour téléchargé comporte la colonne `formset` et écrit le **nom**. Une cellule vide laisse le jeu de formulaires inchangé.

!!! note "Avant la v0.86, la colonne était silencieusement écartée"
    Les versions antérieures ne connaissaient pas `formset` : la colonne était signalée comme inconnue puis ignorée sans conséquence, et l'exécution annonçait un succès. Qui a défini le jeu de formulaires par tableau et s'étonne que rien ne se soit produit — voilà la raison.

### vacat

Indique si l'unité de description est un espace réservé (une lacune dans la
numérotation à laquelle ne correspond aucun document).

La colonne porte en interne des identifiants de termes. Sont acceptés la
désignation (`vacat`), l'ID (`56` pour vacat, `57` pour non vacat) et — issus
de tableaux plus anciens — `1` et `0`.

Depuis la **v0.87.0**, ce qui est **exporté** est la désignation : `vacat` pour
un espace réservé, sinon une cellule vide. Auparavant figurait là le numéro
interne, qui ne signifiait rien dans une colonne dont le nom ne comporte pas
`_id` et ressemblait à une valeur modifiée par erreur. Les tableaux plus
anciens comportant `56`/`57` peuvent continuer d'être utilisés sans
modification.

!!! warning "Avant la v0.86.4"
    Jusque-là, le tableau de mise à jour exportait le numéro interne, mais le
    contrôle n'admettait que `0` et `1`. Un tableau de mise à jour non modifié
    n'était donc pas chargeable, et le message nommait une valeur que personne
    n'avait saisie. Si vous tombez sur une version plus ancienne : désélectionnez
    la colonne `vacat` dans la boîte de dialogue de téléchargement.


### bilder (media)

Le champ peut contenir au maximum 500 caractères. Plusieurs noms de fichiers (assets) peuvent être séparés par les caractères suivants :

```
, ; ::
```


Exemple :

```
erstes_bild.tif::zweites_bild.tif
```

### schutzfrist (period_of_protection)

Le champ doit contenir un délai de protection existant :

```
public
standard
prolonged
```

### private

Le champ ne peut contenir que 0 (non) ou 1 (oui). Si private ne contient aucune valeur, 0 est défini.


### status_of_description

Le champ ne peut contenir que des noms de la liste de valeurs correspondante :

```
draft
final
```

### detail_of_description

Le champ ne peut contenir que des noms de la liste de valeurs correspondante ::

```
minimal
partial
full
```

### Autres champs

Les autres champs sont des champs de texte libre ::

    Neuzugänge (note.accruals)
    Bewertung und Kassation (note.appraisal)
    Informationen des Bearbeiters (note.archivists_notes)
    Ordnung und Klassifikation (note.arrangement)
    Verwaltungsgeschichte / Biographie (note.bioghist)
    Zugangsbedingungen (note.condition_of_access)
    Reproduktionsbestimmungen (note.condition_of_reproduction)
    Bestandsgeschichte (note.custod_hist)
    Kommentar zur Datierung (note.date_comment)
    Umfang (Beschreibung) (note.extent_text)
    Findmittel (note.finding_aids)
    Allgemeine Anmerkungen (note.general_note)
    Archivinterne Bemerkungen (note.internal_note)
    Sprache/Schrift (note.language_script)
    Standort (Detail) (note.location_details)
    Physische Beschaffenheit und technische Anforderungen (note.physical_description)
    Provenienz (note.provenance)
    Publikationen (note.publications)
    Verwandte Verzeichnungseinheiten (note.related_units)
    Kopien/Reproduktionen (note.reproductions)
    Verzeichnungsgrundsätze (note.rules_note)
    Form und Inhalt (note.scopecontent)

## Mettre à jour des notices existantes (mise à jour via le navigateur)

!!! warning "Fonction expérimentale"
    La mise à jour des données est signalée comme **expérimentale** (badge dans l'onglet et sur la page de téléversement). Elle modifie directement des notices existantes. Anton crée donc **automatiquement une sauvegarde de la base de données avant chaque mise à jour** (voir ci-dessous) ; contrôlez néanmoins le résultat par échantillonnage.

Outre la création de nouvelles notices, les unités de description existantes peuvent aussi être mises à jour directement via le navigateur. Un onglet propre **«&nbsp;Update&nbsp;»** existe à cet effet sous **Import de tableau** depuis la **v0.81.2** (après *Métadonnées* et *Médias*). Y téléverser le tableau — les fichiers de mise à jour ont leur propre liste, distincte de l'import normal — et l'ouvrir avec **«&nbsp;Détails&nbsp;»**. Le fichier est contrôlé directement en mode mise à jour, et le bouton **«&nbsp;Charger comme mise à jour&nbsp;»** apparaît.

Comme l'onglet *Update* contrôle le fichier exclusivement en tant que mise à jour, un tableau de mise à jour pur (uniquement `id` + les colonnes à modifier, sans `parent`) n'exige aucun détour : la colonne `parent`, nécessaire à la création, n'est pas requise ici. L'onglet *Métadonnées* régulier reste inchangé pour la création.

Une mise à jour écrase les champs des notices existantes «&nbsp;sur place&nbsp;» — **aucune nouvelle notice n'est créée** dans ce processus. Pour qu'une mise à jour reste sûre et prévisible, trois conditions s'appliquent. Si l'une d'elles est violée, le fichier est bloqué et le motif est affiché sur la page d'inspection :

1. **Chaque ligne a besoin d'un `id` numérique.** C'est par cet `id` que la notice à mettre à jour est trouvée. L'`id` d'une unité de description est visible dans le `permalink`.
2. **Pas de colonne `parent` (ni `parent_id`).** Une mise à jour ne doit pas déplacer de notices. Pour modifier la hiérarchie, rattacher les notices ailleurs dans Anton de manière régulière.
3. **Pas de colonnes d'événement (Antonevents).** Les colonnes telles que `creation_actors`, `creation_date_start` etc. ne sont pas admises dans une mise à jour, afin qu'aucun événement en double ne soit créé. Gérer les liens vers les acteur·trice·s et les lieux dans Anton.

Ce qu'écrit une mise à jour :

- **Seuls les champs remplis sont écrasés.** Les cellules vides laissent la valeur existante intacte — il est donc possible de ne mettre à jour que certaines colonnes (p. ex. uniquement `titel` ou uniquement `schutzfrist`).
- **Les mots-clés, acteur·trice·s, lieux, langues et champs de texte sont remplacés.** Une cellule remplie constitue la *nouvelle liste complète* : qui supprime une entrée de la cellule dissout du même coup le lien sur la notice. Une cellule vide ne change rien. (Lors de l'import normal — donc à la création — les mots-clés continuent d'être uniquement ajoutés.)
- Les **médias** continuent d'être ajoutés.

Le même fichier peut être chargé plusieurs fois comme mise à jour ; le blocage des doublons applicable par ailleurs (même fichier = même somme de contrôle MD5) ne s'applique pas aux mises à jour, une mise à jour étant répétable.

Après le démarrage, la page de progression affiche la mise à jour comme **«&nbsp;mise à jour de données&nbsp;»** (et non comme import) et indique à la fin combien de notices ont été *mises à jour*.

**Sauvegarde automatique.** Avant qu'une mise à jour n'écrive ne serait-ce qu'une ligne, Anton crée un dump de la base de données (la même sauvegarde que `anton:backup`, déposée sous `db_backup/`). L'étape apparaît dans l'affichage de progression comme phase *backup* et est journalisée comme entrée distincte nommant le fichier du dump. Si la sauvegarde ne peut pas être créée, **la mise à jour est interrompue** et rien n'est modifié. La sauvegarde est également imposée lorsque `no-backup` est par ailleurs défini pour le mandant — cette option est prévue pour des *créations* de masse rapides, où le retour en arrière est trivial.

Chaque exécution de mise à jour est journalisée — comme un import — dans les archives d'accroissement, mais avec une **série de cotes propre `UPDATE-{aaaa}-{NNN}`** au lieu de `IMPORT-{aaaa}-{NNN}` ou `AKZ {aaaa}/{N}`. Une mise à jour n'est pas un accroissement — rien de nouveau n'entre dans les archives — et la série distincte rend visible d'un coup d'œil, dans la liste des accroissements, quelles entrées sont des mises à jour. Le compteur est indépendant de la série d'import et est réinitialisé à chaque année civile.

### Télécharger un tableau adéquat

Pour ne pas devoir composer une mise à jour à la main, la **liste de résultats courante peut être téléchargée directement comme tableau de mise à jour** : dans la liste des objets, en haut à droite, le symbole Excel à côté de l'aperçu avant impression. Le téléchargement reprend exactement les filtres actuellement affichés.

Le fichier ne contient que des colonnes qu'une mise à jour est autorisée à écrire — `id`, les colonnes de champs, les langues, le lieu de conservation (`location_id`), les mots-clés / acteur·trice·s / lieux (sous forme d'ID) et les colonnes de champs de texte `note.*`. Ne sont délibérément **pas** inclus `parent` ni les colonnes d'événement, qui bloqueraient la mise à jour. La colonne `identifier` ne sert qu'à l'orientation : la mise à jour trouve les notices par l'`id`, et les modifications de la cote restent sans effet.

!!! tip "Services multilingues : une colonne de titre par langue"
    Si le service tient plusieurs langues de contenu, le tableau de mise à jour contient depuis la **v0.87.0**, au lieu de `titel`, une colonne `title_de`, `title_fr` etc. Ce n'est qu'ainsi que l'aller-retour est sans perte : avec une unique colonne de titre, la langue de l'exécution devrait décider, au chargement, vers quel champ la valeur retourne — et un titre français aboutirait dans le champ allemand.

    Les services monolingues conservent la colonne habituelle `titel` ; il n'y a rien à distinguer. Les tableaux plus anciens comportant `titel` restent chargeables en toute hypothèse.

!!! tip "Modifier les lieux de conservation"
    Pour le lieu de conservation, il existe **deux colonnes**, et le nom indique dans chaque cas ce qui doit y figurer :

    | Colonne | Contenu |
    |---|---|
    | `location_id` | **uniquement l'ID** du lieu de conservation (figure sous *Admin → Lieux de conservation*) |
    | `location` | ID **ou** désignation |

    Le tableau de mise à jour téléchargé utilise `location_id`. Qui préfère travailler avec des désignations renomme la colonne en `location` ; les deux formes y sont acceptées. Une désignation doit être écrite exactement comme dans la gestion des lieux de conservation, majuscules et minuscules comprises — l'ID est donc la voie sûre.

    Une **cellule vide laisse le lieu de conservation inchangé** — pour un déménagement, ne modifier donc que les lignes réellement concernées. Un lieu de conservation qui n'existe pas encore doit être créé au préalable sous *Admin → Lieux de conservation* ; sinon l'inspection le signale comme inconnu et la mise à jour ne s'exécute pas.

!!! warning "Avant la v0.87.0, le bouton ne téléchargeait rien"
    Le bouton de téléchargement de la boîte de dialogue des colonnes fermait la
    boîte de dialogue, mais interrompait dans le même mouvement le transfert —
    sans message d'erreur. On avait l'impression que quelque chose s'était
    produit ; rien n'arrivait dans le dossier de téléchargement. La v0.86.4 a
    corrigé une partie du problème, mais le bouton restait sans effet ; ce n'est
    que depuis la v0.87.0 qu'il s'agit d'un véritable téléchargement.

Au clic s'ouvre une boîte de dialogue permettant de **sélectionner les colonnes**. C'est plus qu'une commodité : ce qui ne figure pas dans le fichier, une mise à jour ne peut pas non plus l'écrire. Qui veut seulement corriger un titre isolé sélectionne `id` et `titel` — rien d'autre ne peut alors être endommagé au chargement. `id` est toujours inclus et ne peut pas être désélectionné.

!!! warning "Le tableau est un instantané"
    Le moins de temps possible devrait s'écouler entre le téléchargement et la mise à jour. Le fichier contient l'état au moment du téléchargement. S'il n'est chargé que quelques jours plus tard, ses anciennes valeurs écrasent tout ce qui a été modifié entre-temps sur ces notices — y compris les modifications que d'autres personnes ont apportées délibérément et qui doivent être conservées. Ne pas conserver un tableau téléchargé pour le réutiliser plus tard, mais l'exporter à nouveau pour chaque série de corrections. Moins de colonnes sont sélectionnées, plus le risque est faible.

    **Anton le contrôle.** Lors de l'export, le moment est inscrit dans le fichier (dans les propriétés du document, non dans une colonne — il survit aussi au changement de nom). La page d'inspection le compare à la date de modification des notices concernées et indique concrètement lesquelles ont été éditées depuis : *«&nbsp;3 notices ont été éditées depuis l'export du tableau (20.07.2026 08:30) — la mise à jour écraserait ces modifications : SIG-1, SIG-7, …&nbsp;»*. Cela ne bloque pas la mise à jour ; il peut y avoir de bonnes raisons de la charger malgré tout. Si aucun moment ne peut être déterminé (par exemple pour un tableau créé à la main), la page le dit également — l'absence d'indication ne signifie donc jamais automatiquement «&nbsp;tout est en ordre&nbsp;».

Le bouton est réservé aux administrateur·trice·s et peut être masqué dans son propre profil sous *Paramètres*. À côté figure l'**export Excel complet** (tous les champs, y compris `parent` et les colonnes d'événement) — celui-ci est destiné aux analyses et *ne peut pas* être rechargé comme mise à jour.

### Pourquoi les événements ne suivent pas dans une mise à jour

Les colonnes d'événement (`creation_actors`, `creation_date_start`, `acquisition_place` …) sont **verrouillées** dans une mise à jour. La raison réside dans la structure : dans Anton, un événement est un tuple *acteur·trice, lieu, période et type* — une ligne par acteur·trice. Un tableau ne peut en représenter, par objet et par type d'événement, qu'**une seule combinaison** : un lieu, une période, un texte de détail, partagés par un nombre quelconque d'acteur·trice·s.

Il en découle trois choses qu'un tableau ne peut pas assurer :

- **Plusieurs événements du même type.** Si un objet a été traité en 1920 à Zurich *et* en 1925 à Berne, cela ne peut pas s'exprimer dans un seul jeu de colonnes. Dans l'export Excel complet, les colonnes de ce type sont donc omises. **Une cellule d'événement vide signifie donc deux choses :** soit aucun événement n'est enregistré — soit il y en a plus que cette forme de tableau ne peut en porter. La boîte de dialogue de téléchargement le signale. Le tableau de mise à jour ne contient aucune colonne d'événement et n'est pas concerné.
- **Supprimer des événements.** L'import ne fait que créer ou mettre à jour des événements ; il n'existe aucun moyen d'en supprimer un via le tableau.
- **Décaler une date.** Le rapprochement s'effectue par *type + objet + acteur·trice + date de début*. Si la date est modifiée dans le tableau, un **second** événement apparaît et l'existant subsiste.

Ce sont surtout les deux derniers points qui rendent les événements inutilisables dans une mise à jour : on ne pourrait qu'ajouter, jamais corriger — et un chargement répété multiplierait les événements. Les événements sont donc gérés dans Anton même, non via le tableau.

Ne sont en outre pas représentés le champ de datation en texte libre (`datierung_text`, dans aucun sens) et l'adresse du lieu (`<typ>_place_address`, uniquement à l'import et uniquement si le réglage `import_addresses` est défini).

!!! note "Uniquement par l'`id` interne"
    La mise à jour dans le navigateur trouve toujours les notices par l'`id` interne, jamais par la cote. Une mise à jour par la cote n'est possible qu'en ligne de commande (`--update --default-excel-column=identifier`, voir ci-dessous).

## Import en ligne de commande


### Import simple

Pour le client (slug) «&nbsp;besenval&nbsp;» et le fichier Excel «&nbsp;test.xlsx&nbsp;», la commande d'import est :

```bash
php artisan anton:import --env=besenval --file="test.xlsx" --import
```

On suppose que `test.xlsx` se trouve dans le dossier `customers/besenval/metadata_to_import/`. Les fichiers à importer avec lui (médias) doivent se trouver dans le dossier `customers/besenval/assets_to_import/`.

Sans l'option `--import`, le fichier est uniquement validé.

### Options

La commande `anton:import` offre plusieurs options qui peuvent être utiles dans des situations spécifiques.

| Option|Description|
|:---   | :----------|
|--no-backup | dont backup the database before import |
|--import                  |really start import|
|--locale=                 |langue de contenu de l'exécution (p. ex. `de`, `fr`). Sans indication, le réglage d'archive s'applique, sinon la langue principale du service — voir [langue de contenu de l'import](#langue-de-contenu-de-limport)|
|--update                  |mettre à jour des notices existantes au lieu d'en créer ; rapprochement par défaut via l'`id`|
|--default-excel-column=   |`id` (par défaut) ou `identifier` — détermine, avec `--update`, par quoi les notices sont trouvées|
|--dont-validate           |do not validate the file|
|--skip-parent-validation  |to build hierarchies with one excel file|
|--create-actors           |create new actors if they dont exist|
|--create-keywords         |create new keywords if they dont exist|
|--create-places           |create new places if they dont exist|
|--create-locations        |create new locations if they dont exist|
|--create-object-types     |create new object_type terms if they dont exist|
|--show-rules              |show rules for this file|
|--show-columns            |show the original columns of this file|
|--show-column-mapping     |show columns with mapping|
|--show-possible-columns   |show all possible column names|
|--show-mapping            |show mapping for this file|
|--show-separators         |show separators|
|--from-ead                |import file is a xml-ead file (also use --parent and --dont-validate)|
|--parent=                  |if import file is an ead you need a parent|

Exemple
```bash
php artisan anton:import customers/kr/ead/test_2-ead.xml --from-ead --dont-validate --create-actors --create-places --create-keywords --parent=1 --env=kr -vv --import --no-backup
```
