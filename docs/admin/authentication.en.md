# Authentication

## Two-factor authentication

### Activate

Two-factor authentication can be enabled with an entry in the `.env` file:

```
2FA=1
```

In the settings (`two-factor-auth-role`) a role can be set for which 2FA is obligatory. If, for example, editor is specified, 2FA is mandatory for editor and admin.

### Deactivating 2FA for a user

If a user has lost their two-factor secret and has no recovery code either, it is possible to remove it from the user so that they can start over with a fresh 2FA.

## Registration

User registration can also be allowed via the `.env` file:

```
REGISTRATION=1
```

## Passkeys

To enable passkeys, simply set the setting `passkeys_enabled` to true. When using subdomains, set `WEBAUTHN_ID` in the `.env` file. For example:

```
WEBAUTHN_ID=kba.anton.ch
```
