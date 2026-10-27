## Zwei-Faktor-Authentifizierung (2FA)

Für zusätzliche Sicherheit kann die Zwei-Faktor-Authentifizierung aktiviert werden.

### 2FA einrichten

1. In Anton einloggen
2. **Profil** → **Sicherheit** öffnen
3. Das eigene Passwort eingeben und **Aktivieren** klicken — beides im selben
   Formular
4. QR-Code mit der Authenticator-App scannen. Geht das nicht, steht der
   Schlüssel darunter als Text und lässt sich von Hand eintippen
5. **Wiederherstellungscodes sichern** — sie sind der Weg zurück, wenn das
   Smartphone verloren geht
6. Einen Code aus der App im Feld **Code prüfen** eingeben. Stimmt er, bestätigt Anton das grün direkt beim Feld, und die Karte trägt das Zeichen **Aktiv**. Geändert wird beim Prüfen nichts

Von da an fragt Anton beim Anmelden nach dem Passwort zusätzlich diesen
sechsstelligen Code.

### Unterstützte Authenticator-Apps

Jede TOTP-kompatible App funktioniert. Empfohlene Open-Source-Apps:

| App | Plattform | Open Source |
|-----|-----------|-------------|
| **Aegis Authenticator** | Android | ✓ |
| **2FAS** | Android, iOS | ✓ |
| **Proton Authenticator** | Android, iOS | ✓ |
| **FreeOTP+** | Android | ✓ |
| **Tofu** | iOS | ✓ |
| **KeePassXC** | Windows, macOS, Linux | ✓ |
| **Bitwarden** | Alle Plattformen | ✓ |

Weitere kompatible Apps: Authy, Google Authenticator, Microsoft Authenticator, 1Password

### 2FA zurücksetzen

Hat jemand das Gerät mit dem zweiten Faktor verloren, setzt ein Admin ihn zurück; ein Superuser-Konto nur ein Superuser. Vorher klärt der Admin, dass die Bitte wirklich von der Person kommt (persönlich, telefonisch oder per Mail von der Adresse des Kontos).

1. Im Bereich Admin auf **Benutzer:innen** gehen, die Person suchen und **2FA zurücksetzen** klicken (in der Tabellenzeile oder unter **Bearbeiten**).
2. Unter **Anlass** festhalten, wie die Person erkannt wurde, etwa «Mail von der hinterlegten Adresse, 23.10.». Bei einem Superuser-Konto ist das Pflicht.
3. **Auch die Passkeys entfernen** ist vorgewählt: Das verlorene Gerät trägt meist einen. Nur abwählen, wenn allein die Authenticator-App fehlt.
4. **2FA zurücksetzen** bestätigen.

Danach sind alle Sitzungen der Person beendet, auch eine auf dem verlorenen Gerät. Sie erhält eine Mail an die Adresse des Kontos: wer zurückgesetzt hat und wann. Bei der nächsten Anmeldung richtet sie den zweiten Faktor neu ein. Der Vorgang steht mit dem Anlass im Sicherheitsprotokoll.

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| `401 Unauthorized` | Token prüfen, Header korrekt formatiert? |
| `403 Forbidden` | Benutzerrechte prüfen |
| `Invalid key supplied` | API-Token fehlt oder ist ungültig |
| 2FA-Code wird nicht akzeptiert | Uhrzeit auf dem Gerät synchronisieren |
