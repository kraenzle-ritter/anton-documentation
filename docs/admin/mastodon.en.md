# Mastodon

Anton offers the option of displaying «news» from Mastodon on the home page or on a dedicated news page.

The Anton demo archive (https://kr.anton.ch) uses the server of [Anoxinon e.V.](https://anoxinon.de), an association committed to data protection and free software: [social.anoxinon.de](https://social.anoxinon.de). Setting up an account there is very straightforward.

For the set-up in Anton, the server address (e.g. https://social.anoxinon.de) and the user ID are needed. The user ID can be looked up at [prouser123.me/mastodon-userid-lookup/](https://prouser123.me/mastodon-userid-lookup/). Anton can display the timeline at the bottom left (`"home_left": true`) or bottom right (`"home_right": true`) of the home page, or create a dedicated news page that is then reachable from the main navigation (`"extra_page": true`). We then store these details in the setting `mastodon`:

```json
{
    "instance_uri":"https:\/\/social.anoxinon.de",
    "user_id":"109246771755522189",
    "profile_name":"@anton",
    "extra_page":true,
    "limit": 10
}
```
