# Passkeys 

## Que sont les passkeys ?

Les passkeys sont une alternative moderne et sûre au mot de passe traditionnel. Au lieu de devoir retenir un mot de passe, vous utilisez :

- l'**empreinte digitale** (Touch ID)
- la **reconnaissance faciale** (Face ID)
- le **code PIN ou le verrouillage d'écran** de votre appareil
- une **clé de sécurité matérielle** (p. ex. YubiKey)

Les passkeys sont plus sûrs que les mots de passe, car ils ne peuvent être ni volés, ni devinés, ni dérobés par des attaques de hameçonnage.

## Conditions préalables

- Votre service d'archives doit avoir activé la fonction passkey
- Un navigateur récent (Chrome, Safari, Firefox, Edge)
- Un appareil doté d'une authentification biométrique ou d'une clé de sécurité

## Configurer un passkey

1. **Connectez-vous avec votre mot de passe** (comme d'habitude)
2. **Ouvrez votre profil** via le menu utilisateur
3. **Rendez-vous sur «&nbsp;Sécurité&nbsp;» ou «&nbsp;Passkeys&nbsp;»**
4. **Cliquez sur «&nbsp;Ajouter un passkey&nbsp;»**
5. **Suivez les instructions de votre navigateur ou de votre appareil** :
   - Confirmez avec l'empreinte digitale, Face ID ou le code PIN
   - Le passkey est enregistré automatiquement sur votre appareil
6. **Attribuez un nom** au passkey (p. ex. «&nbsp;MacBook bureau&nbsp;», «&nbsp;iPhone&nbsp;»)

> **Conseil :** vous pouvez configurer plusieurs passkeys pour différents appareils.

## Se connecter avec un passkey

1. **Ouvrez la page de connexion** d'Anton
2. **Cliquez sur «&nbsp;Se connecter avec un passkey&nbsp;»**
3. **Confirmez avec votre empreinte digitale, Face ID ou votre code PIN**
4. Vous êtes connecté·e – sans mot de passe !

## Gérer les passkeys

Dans votre profil, vous pouvez :

- **consulter tous les passkeys enregistrés**
- **renommer des passkeys** (pour une meilleure vue d'ensemble)
- **supprimer des passkeys** (p. ex. en cas de perte d'un appareil)

## Questions fréquentes

### Puis-je continuer à utiliser mon mot de passe ?
Oui, les passkeys constituent une possibilité de connexion supplémentaire. Votre mot de passe continue de fonctionner.

### Que se passe-t-il en cas de perte de l'appareil ?
Connectez-vous avec votre mot de passe et supprimez dans votre profil le passkey de l'appareil perdu.

### Le passkey fonctionne-t-il sur d'autres appareils ?
Selon le système (iCloud, Google Password Manager, Windows Hello), les passkeys peuvent être synchronisés entre appareils. Les clés de sécurité sont liées à l'appareil physique.

### L'authentification à deux facteurs est-elle encore nécessaire ?
Les passkeys sont considérés comme très sûrs et peuvent remplacer l'authentification à deux facteurs – cela dépend des réglages de votre service d'archives.

## Les avantages en un coup d'œil

| Mot de passe | Passkey |
|----------|---------|
| Peut être oublié | Toujours avec vous sur votre appareil |
| Peut être volé | Protégé par cryptographie |
| Risque de hameçonnage | Immunisé contre le hameçonnage |
| Règles complexes | Utilisation simple |


## Contexte technique

Les passkeys reposent sur le standard WebAuthn (FIDO2). Lors de l'enregistrement, une paire de clés cryptographiques est créée :
- La **clé privée** reste en sécurité sur votre appareil
- La **clé publique** est enregistrée dans Anton

Lors de la connexion, votre appareil prouve qu'il possède la clé privée – sans jamais la transmettre.

*État : février 2026*
