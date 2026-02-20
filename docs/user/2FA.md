## Zwei-Faktor-Authentifizierung (2FA)

Für zusätzliche Sicherheit kann die Zwei-Faktor-Authentifizierung aktiviert werden.

### 2FA einrichten

1. In Anton einloggen
2. **Profil** → **Sicherheit** öffnen
3. **Zwei-Faktor-Authentifizierung aktivieren** klicken
4. QR-Code mit Authenticator-App scannen 
5. Code aus der App eingeben zur Bestätigung

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

1. Im Bereich Admin auf **Benutzerinnen und Benutzer** gehen
2. Benutzer:in in der Liste finden
3. **Reset 2FA** Button klicken (in der Tabellenzeile)

Alternativ auch in der Benutzer:in-Bearbeitungsseite:

1. Im Bereich Admin auf **Benutzerinnen und Benutzer** gehen
2. Benutzer:in auswählen → **Bearbeiten**
3. **Reset 2FA** Button klicken

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| `401 Unauthorized` | Token prüfen, Header korrekt formatiert? |
| `403 Forbidden` | Benutzerrechte prüfen |
| `Invalid key supplied` | API-Token fehlt oder ist ungültig |
| 2FA-Code wird nicht akzeptiert | Uhrzeit auf dem Gerät synchronisieren |
