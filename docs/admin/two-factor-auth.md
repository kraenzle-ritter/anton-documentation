# Two-Factor Authentication

## Activate

The two-factor authentication can be enabled with an enztry in the `.env` file:

```
2FA=1
```

In the settings (`two-factor-auth-role`) you can set a role for which the 2FA is obligatory. If for example editor is specified, a 2FA is mandatory for editor and admin.

## Registration

It is also possible via the `.env` file to allow user registration:

```
REGISTRATION=1
```

## Deactivate 2FA for a User

If a user has lost the two-factor secrets and has also no recovery code, it is possible to remove this from the user so that it is possible to start over with a fresh 2FA.
