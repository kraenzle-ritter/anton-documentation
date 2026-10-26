# Caricamento tramite codice QR

Con il caricamento tramite codice QR è possibile inviare file direttamente dallo smartphone a un oggetto d'archivio – senza doversi autenticare sul dispositivo mobile.

## Casi d'uso

- **Sul posto in archivio**: fotografare rapidamente documenti od oggetti e assegnarli direttamente all'oggetto giusto  
- **Lavoro di squadra**: condividere il codice QR affinché colleghe e colleghi possano caricare file su un oggetto  
- **Collaboratori esterni**: accesso temporaneo al caricamento senza account Anton 

## Configurare il caricamento tramite codice QR

L'impostazione `upload-qr-lods` contiene i livelli di descrizione per i quali viene visualizzato il pulsante di caricamento QR, ad esempio unità archivistiche e unità documentarie `[5,6]`. Per disattivare il caricamento QR si salva un array vuoto `[]` oppure si cancella il contenuto del campo.

Il pulsante è visibile agli account con il ruolo **Editor** o **Admin**, come per il caricamento tramite il modulo. Un codice di caricamento vale per una sola registrazione e scade dopo `upload-qr-token-minutes` (60 minuti, salvo diversa impostazione).

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
| **HEIC → JPEG** | Convertire automaticamente le immagini iPhone (HEIC/HEIF) in JPEG; l'HEIC è conservato come versione del media | ImageMagick (`magick`, con libheif) |
| **Immagini → PDF** | Combinare senza perdita più immagini caricate in un unico PDF | `img2pdf` |
| **OCR** | Eseguire il riconoscimento del testo (rende i PDF ricercabili); le scansioni diventano PDF/A-2b, un PDF con testo resta PDF; il PDF consegnato è conservato come versione del media | `ocrmypdf` + Tesseract (deu+eng) |

Sotto si trova **Conservare il file consegnato**, attivo per impostazione predefinita. Quando Anton converte un HEIC in JPEG o scrive il testo OCR in un PDF, il file così come è stato consegnato resta come versione del media. Senza spunta viene sostituito; l'evento del media conserva le somme di controllo di entrambi i file. Con «Immagini → PDF» le immagini consegnate restano sempre.

Queste impostazioni vengono salvate e valgono per tutti i caricamenti.

Dopo il salvataggio, la pagina segnala che i file sono stati ricevuti. Vengono elaborati e archiviati in background e appaiono nell'oggetto non appena ciò è avvenuto, dopo alcuni minuti per molte scansioni con OCR. Un'esecuzione OCR si interrompe dopo 600 secondi (`OCRMYPDF_TIMEOUT`); il file viene allora archiviato senza livello di testo.

### Dettagli della pipeline (per l'amministrazione)

La pipeline si svolge in questo ordine:

```
0. NELLA RICHIESTA
   verificare token e file → job ProcessTokenUpload

1. PRIMA DELL'IMPORTAZIONE (coda, ProcessTokenUpload)
   HEIC → magick       → JPG (HEIC conservato come versione, salvo se «Conservare
                         il file consegnato» è disattivato)
   JPG  → img2pdf      → PDF
   PDF  → ocrmypdf     → PDF/A-2b per le scansioni, altrimenti PDF, con livello di testo OCR (master;
                         il PDF consegnato conservato come versione)

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

- ImageMagick con supporto HEIF (libheif)
- `img2pdf` (strumento Python)
- `ocrmypdf` con `tesseract-ocr-deu` e `tesseract-ocr-eng`
- `pdftotext` (pacchetto `poppler-utils`) — necessario anche per l'estrazione
  full text

Anton **non** si interrompe silenziosamente se manca uno strumento — la fase
interessata della pipeline viene saltata e documentata nel log.
