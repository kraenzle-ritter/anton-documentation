# Passkeys 

## Was sind Passkeys?

Passkeys sind eine moderne und sichere Alternative zum herkömmlichen Passwort. Anstatt sich ein Passwort merken zu müssen, nutzen Sie:

- **Fingerabdruck** (Touch ID)
- **Gesichtserkennung** (Face ID)
- **PIN oder Bildschirmsperre** Ihres Geräts
- **Hardware-Sicherheitsschlüssel** (z.B. YubiKey)

Passkeys sind sicherer als Passwörter, da sie nicht gestohlen, erraten oder durch Phishing-Angriffe erbeutet werden können.

## Voraussetzungen

- Ihr Archiv muss die Passkey-Funktion aktiviert haben
- Ein moderner Browser (Chrome, Safari, Firefox, Edge)
- Ein Gerät mit biometrischer Authentifizierung oder Sicherheitsschlüssel

## Passkey einrichten

1. **Melden Sie sich mit Ihrem Passwort an** (wie gewohnt)
2. **Öffnen Sie Ihr Profil** über das Benutzermenü
3. **Navigieren Sie zu «Sicherheit» oder «Passkeys»**
4. **Klicken Sie auf «Passkey hinzufügen»**
5. **Folgen Sie den Anweisungen Ihres Browsers/Geräts**:
   - Bestätigen Sie mit Fingerabdruck, Face ID oder PIN
   - Der Passkey wird automatisch auf Ihrem Gerät gespeichert
6. **Vergeben Sie einen Namen** für den Passkey (z.B. «MacBook Büro», «iPhone»)

> **Tipp:** Sie können mehrere Passkeys für verschiedene Geräte einrichten.

## Mit Passkey anmelden

1. **Öffnen Sie die Login-Seite** von Anton
2. **Klicken Sie auf «Mit Passkey anmelden»**
3. **Bestätigen Sie mit Ihrem Fingerabdruck, Face ID oder PIN**
4. Sie sind eingeloggt – ohne Passwort!

## Passkey verwalten

In Ihrem Profil können Sie:

- **Alle registrierten Passkeys einsehen**
- **Passkeys umbenennen** (zur besseren Übersicht)
- **Passkeys löschen** (z.B. bei Geräteverlust)

## Häufige Fragen

### Kann ich weiterhin mein Passwort verwenden?
Ja, Passkeys sind eine zusätzliche Anmeldemöglichkeit. Ihr Passwort funktioniert weiterhin.

### Was passiert bei Geräteverlust?
Melden Sie sich mit Ihrem Passwort an und löschen Sie den Passkey des verlorenen Geräts in Ihrem Profil.

### Funktioniert der Passkey auf anderen Geräten?
Passkeys können je nach System (iCloud, Google Password Manager, Windows Hello) geräteübergreifend synchronisiert werden. Sicherheitsschlüssel sind an das physische Gerät gebunden.

### Ist die Zwei-Faktor-Authentifizierung noch nötig?
Passkeys gelten als sehr sicher und können die Zwei-Faktor-Authentifizierung ersetzen – dies hängt von den Einstellungen Ihres Archivs ab.

## Vorteile auf einen Blick

| Passwort | Passkey |
|----------|---------|
| Kann vergessen werden | Immer dabei auf Ihrem Gerät |
| Kann gestohlen werden | Kryptografisch geschützt |
| Phishing-Gefahr | Immun gegen Phishing |
| Komplexe Regeln | Einfache Bedienung |


## Technischer Hintergrund

Passkeys basieren auf dem WebAuthn-Standard (FIDO2). Bei der Registrierung wird ein kryptografisches Schlüsselpaar erstellt:
- Der **private Schlüssel** bleibt sicher auf Ihrem Gerät
- Der **öffentliche Schlüssel** wird in Anton gespeichert

Bei der Anmeldung beweist Ihr Gerät, dass es den privaten Schlüssel besitzt – ohne diesen jemals zu übertragen.

*Stand: Februar 2026*
