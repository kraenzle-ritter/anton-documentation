## Two-factor authentication (2FA)

For additional security, two-factor authentication can be activated.

### Setting up 2FA

1. Log in to Anton
2. Open **Profile** → **Security**
3. Click **Activate two-factor authentication**
4. Scan the QR code with an authenticator app
5. Enter the code from the app to confirm

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

### Deactivating 2FA

Admins can reset 2FA:

1. In the admin area, go to **Users**
2. Find the user in the list
3. Click the **Reset 2FA** button (in the table row)

Alternatively, also on the user's edit page:

1. In the admin area, go to **Users**
2. Select the user → **Edit**
3. Click the **Reset 2FA** button

## Troubleshooting

| Problem | Solution |
|---------|--------|
| `401 Unauthorized` | Check the token, is the header formatted correctly? |
| `403 Forbidden` | Check the user permissions |
| `Invalid key supplied` | API token missing or invalid |
| 2FA code is not accepted | Synchronise the time on the device |
