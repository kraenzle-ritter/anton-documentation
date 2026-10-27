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
6. Saisir un code de l'application sous **Vérifier le code**. S'il correspond, Anton le confirme en vert à côté du champ, et la carte porte la mention **Activée**. La vérification ne modifie rien

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

### Réinitialiser la 2FA

Si une personne a perdu l'appareil portant son second facteur, l'administration le réinitialise ; un compte superutilisateur, seul un superutilisateur. Auparavant, l'admin s'assure que la demande vient bien de cette personne (en personne, par téléphone ou par e-mail depuis l'adresse du compte).

1. Dans la section Admin, aller sur **Utilisateur·trice·s**, trouver la personne et cliquer sur **Réinitialiser la 2FA** (dans la ligne du tableau ou sous **Éditer**).
2. Sous **Motif**, noter comment la personne a été reconnue, p. ex. « e-mail de l'adresse du compte, 23.10. ». Pour un compte superutilisateur, c'est obligatoire.
3. **Supprimer aussi les passkeys** est coché : l'appareil perdu en porte généralement une. Ne décocher que s'il ne manque que l'application d'authentification.
4. Confirmer **Réinitialiser la 2FA**.

Toutes les sessions de la personne sont alors fermées, y compris sur l'appareil perdu. Elle reçoit un e-mail à l'adresse du compte indiquant qui a réinitialisé et quand. À sa prochaine connexion, elle configure à nouveau le second facteur. L'opération figure avec le motif dans le journal de sécurité.

## Dépannage

| Problème | Solution |
|---------|--------|
| `401 Unauthorized` | Vérifier le jeton ; l'en-tête est-il correctement formaté ? |
| `403 Forbidden` | Vérifier les droits de la personne |
| `Invalid key supplied` | Jeton d'API manquant ou non valide |
| Le code 2FA n'est pas accepté | Synchroniser l'heure de l'appareil |
