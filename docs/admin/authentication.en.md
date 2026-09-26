# Authentication

## Passwords

However it is set (profile, user management, «forgot password»,
`anton:add-user`, `anton:upwd`), a new password must

- be at least **8 characters** long,
- be at most **72 bytes** long; accented letters count twice, the hashing
  cannot store more,
- contain more than words belonging to Anton or the archive: «Archiv2026!»,
  «Anton-Ritter» and the archive's name or slug are refused,
- not be known from a **data breach**.

The last check asks *Have I Been Pwned*. Only the first five characters of the
hash leave the machine, never the password. If the service cannot be reached,
the password is accepted. Installations without internet access switch the
check off in the `.env` file:

```
PASSWORD_CHECK_BREACHED=false
```

Existing passwords stay valid; the rule applies from the next change on.

## Two-factor authentication

### Activate

Two-factor authentication can be enabled with an entry in the `.env` file:

```
2FA=1
```

In the settings (`two-factor-auth-role`) a role can be set for which 2FA is obligatory. If, for example, editor is specified, 2FA is mandatory for editor and admin.

The check is therefore **hierarchical**, and that is where it is easy to get
wrong: `user_intern` obliges not that one role but user_intern, loan_admin,
editor and admin — four of them. An empty value, or `none`, switches the
requirement off.

!!! warning "Without `2FA=1` the setting has no effect"
    The environment has the last word. If two-factor authentication is not
    enabled there, Anton does not register the enrolment routes at all — a role
    obliged to enrol could not, and sign-in would go round in circles. Anton
    therefore does not require it where it cannot be set up.

A code is valid for up to 90 seconds: the current 30-second step and one on
either side, so that a phone whose clock is slightly off does not fail.

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

## Service accounts {#dienstkonten}

The account `anton` exists on every installation. It holds the API token of
scripts and is meant for no person. Anton therefore **does not let it sign in
in the browser**: neither with a password nor with a passkey, and a session it
still holds ends on its next request. Refused attempts are in the security log.
The **API token** and the command line keep working.

Which accounts are service accounts is set by `AUTH_SERVICE_ACCOUNTS` in the
`.env` (comma separated, default `anton`, empty for none, for example on a demo
installation that signs in as `anton`).
