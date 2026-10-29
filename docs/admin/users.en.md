# User administration

User accounts are managed on the admin page under **Users**. Creating, changing
and deleting requires the `admin` role and the capability **Manage users and
capabilities**.

## Creating an account

A new account needs a username and an **e-mail address**. You do not set a
password: the person receives an e-mail with a link and chooses their own
password, so only they know it. The link is valid for **72 hours** and works
once.

If it has expired or the mail did not arrive, send the invitation again with
**Send invitation** on the account's page.

## Roles

Anton keeps the roles **untranslated** — in the selection list they appear
exactly like this:

| Role | May |
|---|---|
| `blocked` | Nothing; access is barred |
| `user` | See the catalogue like the public, plus profile and notifications |
| `user_intern` | In addition, blocked content, locations (view only), loans, original media |
| `editor` | Catalogue: create, change, move, delete (including locations); import; media |
| `admin` | Settings, forms, user accounts, export, statistics |

Each role includes the rights of the one below it. The former role
`loan_admin` is gone: such accounts are `user_intern` with the capability
**Manage loans**.

## Capabilities

Some tasks require a **capability** on top of the role, granted to one account
at a time. Not everyone with the `admin` role has to be allowed everything. A
right needs the minimum role **and** the capability.

| Capability | Allows | from role |
|---|---|---|
| Manage loans | Record, change and delete loans | `user_intern` |
| Change digital preservation | Change the format policy, the format list and image processing; start format identification again. All admins can view the pages. | `admin` |
| Manage users and capabilities | Create, change, delete and invite accounts, end their sessions, reset 2FA and grant capabilities | `admin` |
| Create API tokens for others | Create and revoke API tokens for other accounts | `admin` |
| Create own API tokens | Create and revoke one's own API tokens on the profile (tab **Security**) | `user` |

Capabilities are granted by superusers and by admins holding **Manage users and
capabilities**, on an account's edit page. Nobody can change their own
capabilities. Superusers hold all capabilities. Every change is recorded in the
security log.

At the changeover every admin received every capability and every editor
**Manage loans**, so nothing changed until an archive withdraws capabilities. New
accounts hold no capability until they are given one.

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

Within that branch the account sees everything `user_intern` sees: blocked
descriptions and drafts, media under protection period and blocked media, and
the internal detail view. Outside the branch it sees what guests see.

## API tokens

For access via the [API](../api/authentication.md), tokens can be generated per
account — for other accounts with the capability **Create API tokens for others**,
for one's own on the profile with **Create own API tokens** — each with a name and, if needed, an expiry date. A token is shown only
once, right after it was created; the detail page then lists name, last use and
expiry and lets you revoke single tokens. A token receives the rights of the
account; a token for read access therefore belongs to an account with a
correspondingly restricted role, not to an administration account.

## Login procedures

Besides username and password, [two-factor
authentication](../user/2FA.md) and [passkeys](../user/passkey.md) are available
depending on the installation — see [Authentication](authentication.md).
