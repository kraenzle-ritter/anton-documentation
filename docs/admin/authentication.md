# Anmeldung

## Zwei-Faktor-Authentifizierung

### Aktivieren

Die Zwei-Faktor-Authentifizierung wird über einen Eintrag in der `.env`-Datei eingeschaltet:

```
2FA=1
```

In den Einstellungen (`two-factor-auth-role`) lässt sich eine Rolle festlegen, ab der die 2FA verbindlich ist. Steht dort beispielsweise editor, ist die 2FA für Editor:innen und Admins Pflicht.

### 2FA für eine Person zurücksetzen

Hat jemand das Zwei-Faktor-Geheimnis verloren und auch keinen Wiederherstellungscode mehr, lässt es sich beim Benutzerkonto entfernen. Die 2FA kann danach neu eingerichtet werden.

## Registrierung

Ebenfalls über die `.env`-Datei lässt sich die Selbstregistrierung freigeben:

```
REGISTRATION=1
```

## Passkeys

Für Passkeys genügt es, die Einstellung `passkeys_enabled` auf true zu setzen. Bei Betrieb unter Subdomains ist zusätzlich `WEBAUTHN_ID` in der `.env`-Datei zu setzen, zum Beispiel:

```
WEBAUTHN_ID=kba.anton.ch
```
