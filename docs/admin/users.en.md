# User administration

User accounts are managed on the admin page under **Users**. Creating, changing
and deleting requires the `admin` role.

## Roles

Anton keeps the roles **untranslated** — in the selection list they appear
exactly like this:

| Role | May |
|---|---|
| `blocked` | Nothing; access is barred |
| `user` | See the catalogue like the public, plus profile and notifications |
| `user_intern` | In addition, blocked content, locations (view only), loans, original media |
| `loan_admin` | In addition, manage loans |
| `editor` | Catalogue: create, change, move, delete (including locations); import; media |
| `admin` | Settings, forms, user accounts, export, statistics |

Each role includes the rights of the one below it.

!!! tip "Block accounts rather than delete them"
    `blocked` is the right approach for accounts that are no longer used. When
    an account is deleted, the references are lost — the description control
    then shows a name without an account.

## Superusers

Beyond `admin` there are superusers for system-related interventions: field
types, value lists, [protection periods](protection-periods.md), descriptors,
logs and the merging of places.

**Superuser is not a role** and cannot be assigned in the user administration.
What counts is a separately maintained list of usernames; it permanently
contains the k & r accounts and can be extended via a setting.

## Releasing individual areas

An account with the `user` role can be granted access to particular branches —
for researchers who may work on a blocked holding without seeing everything.

To do so, the IDs of the units of description are entered in the **released
IDs** field as a comma-separated list. An ID always stands for the **entire
branch** below it — the unit itself and all subordinate ones.

## API tokens

For access via the [API](../api/authentication.md), a token can be generated per
account. It receives the rights of the account; a token for read access
therefore belongs to an account with a correspondingly restricted role, not to
an administration account.

## Login procedures

Besides username and password, [two-factor
authentication](../user/2FA.md) and [passkeys](../user/passkey.md) are available
depending on the installation — see [Authentication](authentication.md).
