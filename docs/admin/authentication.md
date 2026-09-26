# Anmeldung

## Passwörter

Ein neues Passwort muss, egal auf welchem Weg es gesetzt wird (Profil,
Benutzerverwaltung, «Passwort vergessen», `anton:add-user`, `anton:upwd`):

- mindestens **8 Zeichen** lang sein,
- höchstens **72 Bytes** lang sein; Umlaute zählen doppelt, länger kann das
  Verfahren nicht speichern,
- mehr enthalten als Wörter, die zu Anton oder zum Archiv gehören: «Archiv2026!»,
  «Anton-Ritter» und Name oder Kürzel des Archivs werden abgewiesen,
- nicht aus einem **Datenleck** bekannt sein.

Die letzte Prüfung fragt bei *Have I Been Pwned* an. Dabei verlassen nur die
ersten fünf Zeichen des Hashs die Maschine, nie das Passwort. Ist der Dienst
nicht erreichbar, wird das Passwort angenommen. Installationen ohne
Internetzugang schalten die Prüfung in der `.env`-Datei ab:

```
PASSWORD_CHECK_BREACHED=false
```

Bestehende Passwörter bleiben gültig. Die Regel greift erst beim nächsten
Wechsel.

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

Ein Code gilt bis zu 90 Sekunden: der laufende 30-Sekunden-Schritt und je
einer davor und danach, damit ein Handy mit leicht falsch gehender Uhr nicht
scheitert.

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

## Dienstkonten

Das Konto `anton` gibt es auf jeder Installation. Es trägt den API-Token von
Skripten und ist für keine Person gedacht. Anton lässt es deshalb **im Browser
nicht anmelden**: weder mit Passwort noch mit Passkey, und eine Sitzung, die
noch besteht, endet beim nächsten Aufruf. Die abgewiesenen Versuche stehen im
Sicherheitsprotokoll. Der **API-Token** und die Kommandozeile funktionieren
weiter.

Welche Konten Dienstkonten sind, legt `AUTH_SERVICE_ACCOUNTS` in der `.env`
fest (kommagetrennt, Vorgabe `anton`, leer für keines, etwa auf einer
Demo-Installation, die sich als `anton` anmeldet).
