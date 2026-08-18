# Cart

The cart — labelled **order basket** in the interface — allows users to collect
units and send an order or enquiry from them by email to the archive. It is an
ordering aid, not a loan management system; [loans](loans.md) are handled
separately.

!!! note "Not in every archive"
    The order basket has to be enabled for the archive. The setting cannot be
    changed in the admin area but is set when the installation is created; with
    Anton as a Service, k & r is responsible for it.

## Procedure

1. In the detail view of a unit of description, click the **shopping cart
   icon**. It is on the right above the record and carries no label.
2. The **order basket** entry appears in the navigation — and only now: as long
   as the basket is empty, it does not exist in the menu.
3. Under **order basket** are the collected units. Individual ones can be
   removed, and the whole basket can be emptied.
4. Fill in the form above and click **Send**.

!!! warning "Only files and items"
    The button only appears at the **file** and **item** levels. Fonds and
    series cannot be ordered — for those, an enquiry to the archive is required.

## The form

By default the following have to be given: **name**, **email**, the **date of
the planned visit** and a **message**; the **institution** is optional. The
fields can be adapted per archive.

The order goes as an email to the archive. The ordering person is entered as the
reply address and receives a copy.

## What the archive does with it

The order arrives in the archive's **email inbox** — that is where it is
processed. Anton has **no order management**: there is no list of open orders, no
status, no detail view. The only thing evaluated is the number, under
[statistics](statistics.md) → «loans and orders».

!!! danger "Check the recipient address"
    If no recipient address is stored for the archive, a hard-coded default
    address at k & r takes effect — the order then does not reach the archive.
    When putting the order basket into operation it is therefore essential to
    check that the address is set, and to verify with a test order that it
    arrives.

## The basket does not last forever

The contents are held in the session. After logging out, or when the session
expires, they are gone — order baskets cannot be built up over several days.
