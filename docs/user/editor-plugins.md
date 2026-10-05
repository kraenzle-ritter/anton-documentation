# Normdaten im XML-Editor (VS Code, Oxygen)

Wer Editionen in TEI auszeichnet, kann Akteure, Orte und Schlagwörter direkt aus
Anton übernehmen, ohne den Editor zu verlassen: Name markieren, Tastenkürzel,
Treffer wählen — das Plugin schreibt die Anton-ID in das Attribut, etwa
`<persName ref="sulger-actors-123">`. Gesucht wird live in Anton, es wird nie
ein ganzes Register heruntergeladen.

Es gibt zwei Plugins mit demselben Funktionsumfang:

| Editor | Plugin | Installation |
|---|---|---|
| Visual Studio Code | [anton-vs](https://github.com/kraenzle-ritter/anton-vs) | Datei `anton-vs-<Version>.vsix` aus den [Releases](https://github.com/kraenzle-ritter/anton-vs/releases/latest) |
| Oxygen XML Editor | [anton-oxy](https://github.com/kraenzle-ritter/anton-oxy) | in Oxygen über **Help → Install new add-ons…** mit der Adresse `https://github.com/kraenzle-ritter/anton-oxy/releases/latest/download/updateSite.xml` |

Installation und Bedienung beschreibt die README des jeweiligen Plugins auf
GitHub. Hier geht es um das, was auf der Seite von Anton einzurichten ist.

## Öffentliches oder nicht öffentliches Archiv

Bei einem **öffentlichen** Archiv genügt im Plugin die Adresse des Archivs, etwa
`https://archiv.example.ch`.

Ein **nicht öffentliches** Archiv gibt seine Register nur heraus, wenn das
Plugin einen **API-Token** mitschickt. Ohne Token meldet das Plugin:

```
Anton HTTP 401 … {"error":"This archive is not public"}
```

Dafür braucht es die Plugin-Version 1.4.0 oder neuer.

## Einen API-Token erstellen

Einen Token erstellt, wer im Archiv die Rolle `admin` hat. Er gehört an ein
eigenes Konto mit der Rolle **`user`**, nicht an das eigene Administrationskonto:
Ein Token hat die Rechte des Kontos, an dem er hängt. An einem `user`-Konto
kann er suchen und lesen, aber nichts ändern.

### 1. Ein Konto für die Plugins anlegen

Einmal pro Archiv, danach für alle Personen dasselbe Konto.

1. Unter **Admin → Benutzer:innen** ein neues Konto anlegen.
2. Name und Benutzername frei wählen, etwa «Editor-Plugins» und
   `editor-plugins`.
3. Eine **E-Mail-Adresse**, die noch keinem anderen Konto gehört, zum Beispiel
   eine Projektadresse. Anton schickt dorthin eine Einladung, ein Passwort zu
   setzen; sie kann liegen bleiben, denn mit diesem Konto meldet sich niemand an.
4. **Rolle: `user`**.

### 2. Den Token erzeugen

1. Unter **Admin → Benutzer:innen** das neue Konto öffnen.
2. Im Abschnitt **API-Tokens**:
    - **Bezeichnung**: wer den Token wofür benutzt, etwa «VS Code Noëmi» oder
      «Oxygen Stefan». Für jede Person einen eigenen Token — so lässt sich einer
      einzeln widerrufen.
    - **Läuft ab am**: ein Datum, etwa in einem Jahr. Leer heisst unbefristet.
3. **API-Token erstellen**.
4. Den angezeigten Token **sofort kopieren**. Anton zeigt ihn nur dieses eine
   Mal; gespeichert wird nur ein Hash, auch Kränzle & Ritter kann ihn danach
   nicht mehr lesen.

!!! warning "Einen Token behandeln wie ein Passwort"
    Wer den Token hat, kann alles lesen, was das Konto lesen darf. Nicht per
    Mail weitergeben, nicht in Dateien legen, die mit anderen geteilt werden.

## Den Token im Plugin eintragen

**VS Code**: **Einstellungen → Erweiterungen → Anton**, das Feld zum API-Token
(die Einstellung heisst `anton.apiToken`). Im selben Abschnitt steht unter
`anton.baseUrl` die Adresse des Archivs. Der Token wird nicht mit der
Einstellungs-Synchronisation von VS Code auf andere Rechner übertragen; dort ist
er erneut einzutragen.

**Oxygen**: **Anton → Anton-Einstellungen…**, Feld **API token**, darüber die
Adresse des Archivs unter **Anton base URL**.

## Widerrufen und ersetzen

Auf der Seite des Kontos listet der Abschnitt **API-Tokens** jeden Token mit
Bezeichnung, letzter Nutzung und Ablaufdatum. **Widerrufen** macht ihn sofort
unwirksam.

Ist ein Token verloren, abgelaufen oder in falsche Hände geraten: einen neuen
erzeugen, im Plugin eintragen, den alten widerrufen. Meldet das Plugin

```
Anton hat den API-Token abgelehnt (falsch, abgelaufen oder Konto gesperrt)
```

ist genau das zu tun. Wird das Konto auf `blocked` gesetzt, sind alle seine
Tokens auf einen Schlag unwirksam.
