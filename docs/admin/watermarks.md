Wasserzeichen können zu allen Bildern "on-the-fly" zugefügt werden. Die entsprechende Konfiguration ist im Setting "watermark" abgelegt.

## Rollen
Wenn ein Setting "watermark" besteht, werden für nicht angemeldete Benutzer:innen Wasserzeichen immer angezeigt. Zusätzlich können in einem Array noch Rollen definiert werden, für die Wasserzeichen angezeigt werden sollen.  
```
"roles": [  
    "user", "user_intern"  
],  
```
## Wasserzeichen
Im Array "watermarks" können mehrere Wasserzeichen definiert werden. Wenn sich zwei Wasserzeichen überlappen, wird das weiter unten definierte über das weiter oben definierte gezeichnet.

### Typen
Wasserzeichen können als *Text* oder als *Bild* eingebettet werden.  
Je nach Typ bestehen unterschiedliche Konfigurationsmöglichkeiten.
#### Text
```
{
	"type": "text", // type of watermark: text|image
	"text": {
		"de": "© K&R | <identifier>", // german version, required, default, allowed placeholders: <identifier>, <permalink>
		"en": "© K&R | <identifier>", // additional languages optional
	},
	"fontfile": "Oswald-Medium.ttf", // in customer_folder, subfolder "fonts"
	"fontsize": 18, //optional, default 18
	"color": "#fff", //optional, default #000
	"angle": 0, //optional, default 0
	"position": "bottom-left", // top-left|top|top-right|left|center|right|bottom-left|bottom|bottom-right, optional, default top-left
	"hmargin": 20, // horizontal margin, optional, default 10
	"vmargin": 20, // vertical margin, optional, default 10
	"background-color": "rgba(0, 0, 0, 0.5)" // optional, default none, use rgba for opacity setting
	}
```
#### Bild
```
{
	"type": "image", // type of watermark: text|image
	"imagefile": "logo.png", // in customer_folder, subfolder "img"
	"position": "top-left", // top-left|top|top-right|left|center|right|bottom-left|bottom|bottom-right, optional, default top-left
	"hmargin": 10, // horizontal margin, optional, default 0
	"vmargin": 10 // vertical margin, optional, default 0
	}
```
## Beispielkonfiguration
```
{
  "roles": [
    "user",
    "user_intern"
  ],
  "watermarks": [
    {
      "type": "text",
      "text": {
        "de": "© K&R | <identifier>"
      },
      "fontfile": "Oswald-Medium.ttf",
      "fontsize": 18,
      "color": "#fff",
      "angle": 0,
      "position": "bottom-left",
      "hmargin": 10,
      "vmargin": 10,
      "background-color": "rgba(0, 0, 0, 0.5)"
    },
    {
      "type": "image",
      "imagefile": "logo.png",
      "position": "top-left",
      "hmargin": 10,
      "vmargin": 10
    }
  ]
}
```