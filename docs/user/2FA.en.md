## Two-factor authentication (2FA)

For additional security, two-factor authentication can be activated.

### Setting up 2FA

1. Log in to Anton
2. Open **Profile** → **Security**
3. Enter your own password and click **Activate** — both in the same form
4. Scan the QR code with your authenticator app. Where that is not possible, the
   key is printed below it as text and can be typed in by hand
5. **Keep the recovery codes** — they are the way back in if the phone is lost
6. Enter a code from the app under **Check the code**. If it matches, Anton confirms it in green right by the field, and the card carries the badge **Active**. Checking changes nothing

From then on, Anton asks for this six-digit code after your password when you
sign in.

### Supported authenticator apps

Any TOTP-compatible app works. Recommended open source apps:

| App | Platform | Open source |
|-----|-----------|-------------|
| **Aegis Authenticator** | Android | ✓ |
| **2FAS** | Android, iOS | ✓ |
| **Proton Authenticator** | Android, iOS | ✓ |
| **FreeOTP+** | Android | ✓ |
| **Tofu** | iOS | ✓ |
| **KeePassXC** | Windows, macOS, Linux | ✓ |
| **Bitwarden** | All platforms | ✓ |

Other compatible apps: Authy, Google Authenticator, Microsoft Authenticator, 1Password

### Resetting 2FA

When someone has lost the device with their second factor, an admin resets it; a superuser account only a superuser. First the admin makes sure the request really comes from that person (in person, by phone, or by mail from the account's address).

1. In the admin area, go to **Users**, find the person and click **Reset 2FA** (in the table row or under **Edit**).
2. Under **Reason**, note how the person was recognised, e.g. "mail from the address of the account, 23.10.". For a superuser account this is required.
3. **Also remove the passkeys** is ticked: the lost device usually carries one. Untick it only if just the authenticator app is missing.
4. Confirm **Reset 2FA**.

All of the person's sessions are then ended, one on the lost device too. They get a mail at the account's address saying who reset it and when. At their next sign-in they set up the second factor anew. The reset is in the security log, with the reason.

## Troubleshooting

| Problem | Solution |
|---------|--------|
| `401 Unauthorized` | Check the token, is the header formatted correctly? |
| `403 Forbidden` | Check the user permissions |
| `Invalid key supplied` | API token missing or invalid |
| 2FA code is not accepted | Synchronise the time on the device |
