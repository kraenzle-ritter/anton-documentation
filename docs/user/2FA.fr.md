## Authentification à deux facteurs (2FA)

Pour plus de sécurité, l'authentification à deux facteurs peut être activée.

### Configurer la 2FA

1. Se connecter à Anton
2. Ouvrir **Profil** → **Sécurité**
3. Saisir son propre mot de passe et cliquer sur **Activer** — les deux dans le
   même formulaire
4. Scanner le code QR avec l'application d'authentification. Si cela n'est pas
   possible, la clé figure en dessous sous forme de texte et peut être saisie à
   la main
5. **Conserver les codes de récupération** — ils sont le moyen de revenir si le
   téléphone est perdu
6. Saisir un code de l'application sous **Vérifier le code**. Anton indique s'il
   correspond; rien n'est modifié

À partir de là, Anton demande ce code à six chiffres après le mot de passe lors
de la connexion.

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
