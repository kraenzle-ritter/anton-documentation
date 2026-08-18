# Caricamento tramite codice QR

Con il caricamento tramite codice QR è possibile inviare file direttamente dallo smartphone a un oggetto d'archivio – senza doversi autenticare sul dispositivo mobile.

## Casi d'uso

- **Sul posto in archivio**: fotografare rapidamente documenti od oggetti e assegnarli direttamente all'oggetto giusto  
- **Lavoro di squadra**: condividere il codice QR affinché colleghe e colleghi possano caricare file su un oggetto  
- **Collaboratori esterni**: accesso temporaneo al caricamento senza account Anton 

## Configurare il caricamento tramite codice QR

L'impostazione `upload-qr-lods` contiene i livelli di descrizione per i quali viene visualizzato il pulsante di caricamento QR, ad esempio unità archivistiche e unità documentarie `[5,6]`. Per disattivare il caricamento QR si salva un array vuoto `[]` oppure si cancella il contenuto del campo.

## Attivare il caricamento

### 1. Aprire l'oggetto

Navigare fino all'unità di descrizione desiderata (ad esempio un'unità archivistica o documentaria).

### 2. Generare il codice QR

1. Fare clic sul pulsante **QR Upload** (simbolo 📱) nella barra degli strumenti
2. Si apre una finestra modale con:
   - un **codice QR** da scansionare
   - un **URL di caricamento** da copiare o condividere
   - un **token** (validità configurabile, valore predefinito: 1 ora)

### 3. Scegliere le opzioni di elaborazione (facoltativo)

Nella finestra modale è possibile attivare opzioni di elaborazione delle immagini:

| Opzione | Descrizione | Strumento sul server |
|--------|-------------|---|
| **HEIC → JPEG** | Convertire automaticamente le immagini iPhone (HEIC/HEIF) in JPEG | `heif-convert` (libheif) |
| **Immagini → PDF** | Combinare senza perdita più immagini caricate in un unico PDF | `img2pdf` |
| **OCR** | Eseguire il riconoscimento del testo (rende i PDF ricercabili) | `ocrmypdf` + Tesseract (deu+eng) |

Queste impostazioni vengono salvate e valgono per tutti i caricamenti.

### Dettagli della pipeline (per l'amministrazione)

La pipeline si svolge in questo ordine:

```
1. PRIMA DELL'IMPORTAZIONE (sincrono)
   HEIC → heif-convert → JPG
   JPG  → img2pdf      → PDF
   PDF  → ocrmypdf     → PDF con livello di testo OCR (master)

2. IMPORTAZIONE
   addAntonMedium() → evento MediumAdded

3. DOPO L'IMPORTAZIONE (asincrono, coda)
   MediumIdentifyAndConvert
   ├─ identificazione PRONOM
   ├─ sincronizzazione cloud (se configurata)
   ├─ generazione delle miniature
   └─ RefreshFulltext
      └─ pdftotext → media_texts (indice full text)
```

La pipeline è gestita centralmente tramite l'impostazione
`image-upload-processing` (array). Valori possibili: `heic2jpg`, `images2pdf`,
`ocr`.

Esempio con tutti e tre i passaggi attivati:

```php
Setting::setValue('image-upload-processing', ['heic2jpg', 'images2pdf', 'ocr']);
```

Prerequisiti sul server:

- `heif-convert` (pacchetto `libheif`/`libheif-tools`)
- `img2pdf` (strumento Python)
- `ocrmypdf` con `tesseract-ocr-deu` e `tesseract-ocr-eng`
- `pdftotext` (pacchetto `poppler-utils`) — necessario anche per l'estrazione
  full text

Anton **non** si interrompe silenziosamente se manca uno strumento — la fase
interessata della pipeline viene saltata e documentata nel log.
