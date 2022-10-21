````
{
      "roles": [
        "user", "user_intern" // user roles for which the watermark should be shown. Always shown for guests
      ],
      "texts": [
        {
          "text": {
            "de": "© K&R | <identifier>" // allowed placeholders: <identifier>, <permalink>
          },
          "fontfile": "Oswald-Medium.ttf", // in customer_folder, subfolder "fonts"
          "fontsize": 18, //optional, default 18
          "color": "#fff", //optional, default #000
          "angle": 0, //optional, default 0
          "position": "bottom-left", // top-left|top|top-right|left|center|right|bottom-left|bottom|bottom-right, optional, default top-left
          "hmargin": 20, // horizontal margin, optional, default 10
          "vmargin": 20, // vertical margin, optional, default 10
          "background-color": "rgba(0, 0, 0, 0.5)" // optional, default none, use rgba for opacity setting
        },
        {
          [...]
        }
      ],
      "images": [
        {
          "imagefile": "logo.png", // in customer_folder, subfolder "img"
          "position": "top-left", // top-left|top|top-right|left|center|right|bottom-left|bottom|bottom-right, optional, default top-left
          "hmargin": 10, // horizontal margin, optional, default 0
          "vmargin": 10 // vertical margin, optional, default 0
        },
        {
          [...]
        }
      ]
    }
````