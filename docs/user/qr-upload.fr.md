# Téléversement par code QR

Le téléversement par code QR permet d'envoyer des fichiers directement depuis un smartphone vers un objet d'archives – sans avoir à se connecter sur l'appareil mobile.

## Cas d'usage

- **Sur place aux archives** : photographier rapidement des documents ou des objets et les rattacher directement au bon objet  
- **Travail en équipe** : partager le code QR pour que des collègues puissent téléverser des fichiers vers un objet  
- **Collaborateur·trice·s externes** : accès temporaire au téléversement sans compte Anton 

## Configurer le téléversement par code QR

Le paramètre `upload-qr-lods` contient les niveaux de description pour lesquels le bouton de téléversement QR est affiché, par exemple les dossiers et les pièces `[5,6]`. Pour désactiver le téléversement QR, on enregistre un tableau vide `[]` ou l'on supprime le contenu du champ.

Le bouton est affiché aux comptes ayant le rôle **Editor** ou **Admin**, comme pour le téléversement par le formulaire. Un code de téléversement vaut pour une seule notice et expire après `upload-qr-token-minutes` (60 minutes, sauf autre réglage).

## Activer le téléversement

### 1. Ouvrir l'objet

Naviguer jusqu'à l'unité de description souhaitée (par exemple un dossier ou une pièce).

### 2. Générer le code QR

1. Cliquer sur le bouton **QR Upload** (symbole 📱) dans la barre d'outils
2. Une fenêtre modale s'ouvre avec :
   - un **code QR** à scanner
   - une **URL de téléversement** à copier ou à partager
   - un **jeton** (durée de validité configurable, par défaut : 1 heure)

### 3. Choisir les options de traitement (facultatif)

Des options de traitement des images peuvent être activées dans la fenêtre modale :

| Option | Description | Outil sur le serveur |
|--------|-------------|---|
| **HEIC → JPEG** | Convertir automatiquement les images iPhone (HEIC/HEIF) en JPEG ; le JPEG devient le master, le HEIC n'est conservé qu'avec « Conserver le fichier livré » | ImageMagick (`magick`, avec libheif) |
| **Images → PDF** | Combiner sans perte plusieurs images téléversées en un seul PDF | `img2pdf` |
| **OCR** | Effectuer la reconnaissance de texte (rend les PDF interrogeables) ; les numérisations deviennent PDF/A-2b, un PDF avec texte reste PDF ; le PDF avec sa couche de texte devient le master, le PDF livré n'est conservé qu'avec « Conserver le fichier livré » | `ocrmypdf` + Tesseract (deu+eng) |

En dessous figure **Conserver le fichier livré**, désactivé par défaut. HEIC → JPEG et OCR font partie de la prise en charge (préingest, voir [Préservation à long terme](../admin/preservation.md#speicherung)) : leur résultat est le master, et le fichier livré est remplacé. L'événement du média consigne la conversion avec l'outil et les sommes de contrôle des deux fichiers. Avec la coche, le fichier tel que livré est conservé comme version du média. Avec « Images → PDF », les images livrées sont toujours conservées.

Ces réglages sont enregistrés et s'appliquent à tous les téléversements.

Après l'enregistrement, la page indique que les fichiers ont été reçus. Ils sont traités et déposés en arrière-plan et apparaissent dans l'objet dès que c'est fait, après quelques minutes pour de nombreuses numérisations avec OCR. Une exécution OCR s'arrête après 600 secondes (`OCRMYPDF_TIMEOUT`) ; le fichier est alors déposé sans couche de texte.

### Détails de la chaîne de traitement (pour l'administration)

La chaîne s'exécute dans cet ordre :

```
0. DANS LA REQUÊTE
   vérifier le jeton et les fichiers → job ProcessTokenUpload

1. AVANT L'IMPORT (file d'attente, ProcessTokenUpload)
   HEIC → magick       → JPG (HEIC conservé comme version seulement avec
                         « Conserver le fichier livré »)
   JPG  → img2pdf      → PDF
   PDF  → ocrmypdf     → PDF/A-2b pour les numérisations, sinon PDF, avec couche de texte OCR (master ;
                         le PDF livré conservé seulement avec « Conserver le fichier livré »)

2. IMPORT
   addAntonMedium() → événement MediumAdded

3. APRÈS L'IMPORT (asynchrone, file d'attente)
   MediumIdentifyAndConvert
   ├─ identification PRONOM
   ├─ synchronisation cloud (si configurée)
   ├─ génération des vignettes
   └─ RefreshFulltext
      └─ pdftotext → media_texts (index plein texte)
```

La chaîne est pilotée de manière centralisée via le paramètre
`image-upload-processing` (tableau). Valeurs possibles : `heic2jpg`,
`images2pdf`, `ocr`.

Exemple avec les trois étapes activées :

```php
Setting::setValue('image-upload-processing', ['heic2jpg', 'images2pdf', 'ocr']);
```

Prérequis sur le serveur :

- ImageMagick avec prise en charge HEIF (libheif)
- `img2pdf` (outil Python)
- `ocrmypdf` avec `tesseract-ocr-deu` et `tesseract-ocr-eng`
- `pdftotext` (paquet `poppler-utils`) — également nécessaire à l'extraction
  plein texte

Anton n'échoue **pas** silencieusement lorsqu'un outil manque — l'étape concernée
de la chaîne est ignorée et consignée dans le journal.
