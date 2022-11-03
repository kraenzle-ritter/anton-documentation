# Mastodon

Anton hat die Möglichkeit «News» von Mastodon auf der Homepage oder auf einer eigenen News-Seite anzuzeigen. 

Das Anton Demo-Archiv (https://kr.anton.ch) nutzt den Server von [Anoxinon e.V.](https://anoxinon.de), einem Verein, der sich für Datenschutz und freie Software einsetzt: [social.anoxinon.de](https://social.anoxinon.de). Die Kontoeinrichtung ist dann ganz einfach.

Für die Einrichtung auf Anton benötigt man die Serveradresse (z.B. https://social.anoxinon.de) und die User-ID. Die User-Id kann man auf [prouser123.me/mastodon-userid-lookup/](https://prouser123.me/mastodon-userid-lookup/) nachschlagen. Anton kann die Timeline auf der Homepage links (`"home_left": true`) oder rechts (`"home_right": true`) unten einblenden oder eine eigene News Seite erstellen, die dann über in der Haupnavigation erreichbar ist (`"extra_page": true`). Diese Angaben werden von uns dann im Setting `mastodon` gespeichert:

```json
{
    "instance_uri":"https:\/\/social.anoxinon.de",
    "user_id":"109246771755522189",
    "profile_name":"@anton",
    "extra_page":true,
    "limit": 10
}
```
