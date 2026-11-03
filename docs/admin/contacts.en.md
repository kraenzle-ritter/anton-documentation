# Contact persons

Under **Administration › Users and loans › Contact persons** the archive records who answers for what. Whatever costs money or concerns the keeping of the files holds only once one of these people has confirmed it by mail.

## Functions

| Function | Confirms with the capability | Receives |
|---|---|---|
| Overall responsibility | Contract and contacts | Order confirmations, notices about the contract |
| Digital preservation | Change digital preservation | Monthly format report, findings of the integrity check |
| Billing | – | Usage statement |
| Technical | – | Maintenance and update notices |

Each function takes several people, as an **account** of this installation or as an **address without an account** (with a name). Only accounts holding the function's capability can confirm; the page shows for each person whether they can. Addresses without an account receive the notices.

All admins see the page. Accounts holding **Contract and contacts** name and remove people (see [User administration](users.md#capabilities)). Every change is recorded in the security log and mailed to everyone named for the function, to the person added or removed and to Kränzle & Ritter.

## Confirmation by mail

1. Anton sends the request to each person of the function who can confirm, with a link of their own. The mail gives the wording in question.
2. The link leads to the page in Anton; it is valid for 14 days. **Opening it confirms nothing**: mail programs open links themselves to check them.
3. The answer is the button on the page, given signed in with the account the link was made out to. One answer is enough; the request is closed then.
4. The answer is mailed to everyone named for the function and to Kränzle & Ritter.

At the bottom of the page «Contact persons» the requests are listed with their status (open, confirmed, declined, expired) and who answered when. The wording is kept as it was shown.

A superuser of Kränzle & Ritter cannot confirm for the archive unless named as a contact person.

!!! note "No requests yet"
    Since v0.118.0 the contact persons can be named. Anton asks for confirmations only with the bookings and the preservation mandate, which follow.
