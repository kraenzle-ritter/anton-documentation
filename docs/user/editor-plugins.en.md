# Authority data in the XML editor (VS Code, Oxygen)

If you encode editions in TEI, you can take actors, places and keywords straight
from Anton without leaving the editor: select a name, press the shortcut, pick a
hit — the plugin writes the Anton ID into the attribute, e.g.
`<persName ref="sulger-actors-123">`. The search runs live in Anton; a whole
register is never downloaded.

There are two plugins with the same features:

| Editor | Plugin | Installation |
|---|---|---|
| Visual Studio Code | [anton-vs](https://github.com/kraenzle-ritter/anton-vs) | the file `anton-vs-<version>.vsix` from the [releases](https://github.com/kraenzle-ritter/anton-vs/releases/latest) |
| Oxygen XML Editor | [anton-oxy](https://github.com/kraenzle-ritter/anton-oxy) | in Oxygen via **Help → Install new add-ons…** with the address `https://github.com/kraenzle-ritter/anton-oxy/releases/latest/download/updateSite.xml` |

Installation and use are described in each plugin's README on GitHub. This page
covers what has to be set up on the Anton side.

## Public or non-public archive

For a **public** archive, the archive's address is all the plugin needs, e.g.
`https://archive.example.ch`.

A **non-public** archive only hands out its registers if the plugin sends an
**API token**. Without one, the plugin reports:

```
Anton HTTP 401 … {"error":"This archive is not public"}
```

This requires plugin version 1.4.0 or later.

## Creating an API token

A token is created by someone with the role `admin` in the archive. It belongs
to a separate account with the role **`user`**, not to your own administrator
account: a token has the rights of the account it belongs to. On a `user`
account it can search and read, but not change anything.

### 1. Create an account for the plugins

Once per archive; afterwards everyone uses the same account.

1. Under **Admin → Users**, create a new account.
2. Choose any name and username, e.g. "Editor plugins" and `editor-plugins`.
3. An **e-mail address** that no other account uses yet, for example a project
   address. Anton sends an invitation to set a password there; it can be
   ignored, since nobody signs in with this account.
4. **Role: `user`**.

### 2. Generate the token

1. Open the new account under **Admin → Users**.
2. In the **API tokens** section:
    - **Name**: who uses the token for what, e.g. "VS Code Noëmi" or
      "Oxygen Stefan". One token per person — that way each can be revoked on
      its own.
    - **Expires on**: a date, e.g. one year ahead. Empty means no expiry.
3. **Create API token**.
4. **Copy the token right away.** Anton shows it only this once; only a hash is
   stored, so not even Kränzle & Ritter can read it afterwards.

!!! warning "Treat a token like a password"
    Whoever has the token can read everything the account may read. Do not send
    it by e-mail or keep it in files shared with others.

## Entering the token in the plugin

**VS Code**: **Settings → Extensions → Anton**, the API token field (the
setting is called `anton.apiToken`). The archive's address is in the same
section under `anton.baseUrl`. The token is not carried to other computers by
VS Code's Settings Sync; enter it there again.

**Oxygen**: **Anton → Anton-Einstellungen…**, field **API token**; the
archive's address is above it under **Anton base URL**.

## Revoking and replacing

On the account's page, the **API tokens** section lists every token with its
name, last use and expiry date. **Revoke** disables it immediately.

If a token is lost, expired or in the wrong hands: generate a new one, enter it
in the plugin, revoke the old one. If the plugin reports

```
Anton hat den API-Token abgelehnt (falsch, abgelaufen oder Konto gesperrt)
```

("Anton rejected the API token (wrong, expired or account blocked)"), that is
exactly what to do. Setting the account to `blocked` disables all its tokens
at once.
