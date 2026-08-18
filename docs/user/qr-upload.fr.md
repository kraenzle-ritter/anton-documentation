# Téléversement par code QR

Le téléversement par code QR permet d'envoyer des fichiers directement depuis un smartphone vers un objet d'archives – sans avoir à se connecter sur l'appareil mobile.

## Cas d'usage

- **Sur place aux archives** : photographier rapidement des documents ou des objets et les rattacher directement au bon objet  
- **Travail en équipe** : partager le code QR pour que des collègues puissent téléverser des fichiers vers un objet  
- **Collaborateur·trice·s externes** : accès temporaire au téléversement sans compte Anton 

## Configurer le téléversement par code QR

Le paramètre `upload-qr-lods` contient les niveaux de description pour lesquels le bouton de téléversement QR est affiché, par exemple les dossiers et les pièces `[5,6]`. Pour désactiver le téléversement QR, on enregistre un tableau vide `[]` ou l'on supprime le contenu du champ.

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
| **HEIC → JPEG** | Convertir automatiquement les images iPhone (HEIC/HEIF) en JPEG | `heif-convert` (libheif) |
| **Images → PDF** | Combiner sans perte plusieurs images téléversées en un seul PDF | `img2pdf` |
| **OCR** | Effectuer la reconnaissance de texte (rend les PDF interrogeables) | `ocrmypdf` + Tesseract (deu+eng) |

Ces réglages sont enregistrés et s'appliquent à tous les téléversements.

### Détails de la chaîne de traitement (pour l'administration)

La chaîne s'exécute dans cet ordre :

```
1. AVANT L'IMPORT (synchrone)
   HEIC → heif-convert → JPG
   JPG  → img2pdf      → PDF
   PDF  → ocrmypdf     → PDF avec couche de texte OCR (master)

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

- `heif-convert` (paquet `libheif`/`libheif-tools`)
- `img2pdf` (outil Python)
- `ocrmypdf` avec `tesseract-ocr-deu` et `tesseract-ocr-eng`
- `pdftotext` (paquet `poppler-utils`) — également nécessaire à l'extraction
  plein texte

Anton n'échoue **pas** silencieusement lorsqu'un outil manque — l'étape concernée
de la chaîne est ignorée et consignée dans le journal.
