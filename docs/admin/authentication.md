# Anmeldung

## Zwei-Faktor-Authentifizierung

### Aktivieren

Die Zwei-Faktor-Authentifizierung wird über einen Eintrag in der `.env`-Datei eingeschaltet:

```
2FA=1
```

In den Einstellungen (`two-factor-auth-role`) lässt sich eine Rolle festlegen, ab der die 2FA verbindlich ist. Steht dort beispielsweise editor, ist die 2FA für Editor:innen und Admins Pflicht.

Die Prüfung ist also **hierarchisch**, und das ist die Stelle, an der man sich
leicht vertut: `user_intern` verpflichtet nicht nur diese eine Rolle, sondern
user_intern, loan_admin, editor und admin — vier Rollen. Ein leerer Wert oder
`none` schaltet die Pflicht ab.

!!! warning "Ohne `2FA=1` bleibt die Einstellung wirkungslos"
    Die Umgebung hat das letzte Wort. Ist die Zwei-Faktor-Anmeldung dort nicht
    eingeschaltet, registriert Anton die Routen zur Einrichtung gar nicht — eine
    Rolle, die sie dann einrichten müsste, könnte es nicht, und die Anmeldung
    liefe im Kreis. Anton verlangt sie darum nicht, wo sie sich nicht einrichten
    lässt.

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
