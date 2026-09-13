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
6. Einen Code aus der App im Feld **Code prüfen** eingeben. Anton sagt, ob er
   stimmt; geändert wird dabei nichts

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

### 2FA deaktivieren

Admins können die 2FA zurücksetzen:

1. Im Bereich Admin auf **Benutzer:innen** gehen
2. Benutzer:in in der Liste finden
3. **Reset 2FA** Button klicken (in der Tabellenzeile)

Alternativ auch in der Benutzer:in-Bearbeitungsseite:

1. Im Bereich Admin auf **Benutzer:innen** gehen
2. Benutzer:in auswählen → **Bearbeiten**
3. **Reset 2FA** Button klicken

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| `401 Unauthorized` | Token prüfen, Header korrekt formatiert? |
| `403 Forbidden` | Benutzerrechte prüfen |
| `Invalid key supplied` | API-Token fehlt oder ist ungültig |
| 2FA-Code wird nicht akzeptiert | Uhrzeit auf dem Gerät synchronisieren |
