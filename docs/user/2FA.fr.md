## Authentification à deux facteurs (2FA)

Pour plus de sécurité, l'authentification à deux facteurs peut être activée.

### Configurer la 2FA

1. Se connecter à Anton
2. Ouvrir **Profil** → **Sécurité**
3. Cliquer sur **Activer l'authentification à deux facteurs**
4. Scanner le code QR avec une application d'authentification
5. Saisir le code fourni par l'application pour confirmer

### Applications d'authentification prises en charge

Toute application compatible TOTP fonctionne. Applications open source recommandées :

| Application | Plateforme | Open source |
|-----|-----------|-------------|
| **Aegis Authenticator** | Android | ✓ |
| **2FAS** | Android, iOS | ✓ |
| **Proton Authenticator** | Android, iOS | ✓ |
| **FreeOTP+** | Android | ✓ |
| **Tofu** | iOS | ✓ |
| **KeePassXC** | Windows, macOS, Linux | ✓ |
| **Bitwarden** | Toutes les plateformes | ✓ |

Autres applications compatibles : Authy, Google Authenticator, Microsoft Authenticator, 1Password

### Désactiver la 2FA

L'administration peut réinitialiser la 2FA :

1. Dans la section Admin, aller sur **Utilisateur·trice·s**
2. Trouver la personne dans la liste
3. Cliquer sur le bouton **Reset 2FA** (dans la ligne du tableau)

Autre possibilité, depuis la page de modification de la personne :

1. Dans la section Admin, aller sur **Utilisateur·trice·s**
2. Sélectionner la personne → **Éditer**
3. Cliquer sur le bouton **Reset 2FA**

## Dépannage

| Problème | Solution |
|---------|--------|
| `401 Unauthorized` | Vérifier le jeton ; l'en-tête est-il correctement formaté ? |
| `403 Forbidden` | Vérifier les droits de la personne |
| `Invalid key supplied` | Jeton d'API manquant ou non valide |
| Le code 2FA n'est pas accepté | Synchroniser l'heure de l'appareil |
