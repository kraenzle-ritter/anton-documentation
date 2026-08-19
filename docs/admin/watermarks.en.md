# Watermarks

Watermarks can be added to all images "on the fly". The corresponding configuration is stored in the setting "watermark".

## Roles
If a "watermark" setting exists, watermarks are always displayed for users who are not logged in. In addition, roles for which watermarks are to be displayed can be defined in an array.  
```
"roles": [  
    "user", "user_intern"  
],  
```
## Watermarks
Several watermarks can be defined in the "watermarks" array. If two watermarks overlap, the one defined further down is drawn over the one defined further up.

### Types
Watermarks can be embedded as *text* or as an *image*.  
Depending on the type, different configuration options are available.
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
#### Image
```
{
	"type": "image", // type of watermark: text|image
	"imagefile": "logo.png", // in customer_folder, subfolder "img"
	"position": "top-left", // top-left|top|top-right|left|center|right|bottom-left|bottom|bottom-right, optional, default top-left
	"hmargin": 10, // horizontal margin, optional, default 0
	"vmargin": 10 // vertical margin, optional, default 0
	}
```
## Example configuration
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
