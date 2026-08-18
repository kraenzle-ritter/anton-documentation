# Getting started

Anton is a web-based archival database. It follows ISAD(G) and represents
holdings as a tree — from the collection through fonds and series down to the
individual document. Media, [actors](actors.md), [places](places.md) and
[keywords](keywords.md) can be recorded for every
[unit of description](objects.md).

This documentation describes working with Anton from the perspective of
cataloguing. For installation and configuration, see the admin section.

## The interface

The navigation is at the top. Its content is configurable per archive; as a rule
it contains:

- the **entry point into the archival arrangement**. Each archive decides what it
  is called — «catalogue», «archive plan» or the name of the archive itself.
- **Admin** — despite the name, this is the collective page for all logged-in
  users. The page itself is headed **Administration** and leads via cards to
  **entities** (actors, places, keywords, locations), **users**, **info**,
  **import / export** and **settings**. Which cards appear depends on the role.
- **Help** — the in-application help; it shows the fields, value lists and
  cataloguing rules of **this** archive
- the **search** at the top right

!!! note "Labels may differ"
    Almost every label can be configured per archive — menu entries as well as
    field names. This documentation uses the designations of the standard form;
    in a given archive they may differ. Where the differences are particularly
    liable to cause confusion, this is noted on the spot.

## Roles

What someone sees and may do depends on their role. Anton keeps the role names
untranslated; they appear exactly like this in the user administration:

| Role | May |
|---|---|
| (not logged in) | Search the public catalogue — provided the archive makes it available |
| `user` | The same, logged in; own profile, notifications |
| `user_intern` | In addition, see blocked content and locations, borrow items and download original media |
| `loan_admin` | In addition, manage loans |
| `editor` | Catalogue: create, modify, move and delete records (including locations); import; media |
| `admin` | Settings, forms, user accounts, export, statistics |
| `blocked` | Nothing — access is barred |

Each role includes the rights of the preceding one.

Anyone cataloguing needs at least `editor`. The buttons for creating, moving and
deleting only appear with this permission — if they are missing, the role is the
reason.

!!! note "Superusers"
    Beyond `admin` there are superusers for interventions such as field types,
    value lists and protection periods. This is not a role in the user
    administration but a separately maintained list of accounts.

## Logging in

Logging in is done with a username and password. Depending on the archive,
[two-factor authentication](2FA.md) and [passkeys](passkey.md) are also
available.

## Where to read on

The entry point into everyday work is [units of description](objects.md); how
the tree is structured and how records can be re-hung is described under
[Archival arrangement and moving records](hierarchy.md). Why a given form looks
different from the examples here is explained in
[Forms and fields](forms.md).
