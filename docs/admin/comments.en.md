# Comments

Comments are internal working notes on a unit of description — for everything
that belongs to the record but is not descriptive information: «The person in
the photograph is probably Hans Meier», «The dating is wrong», «Check the image
crop».

How they are used is described in [Comments](../user/comments.md) — this page
deals with the set-up.

## Comment or text field?

Both are text areas on the record, and they serve different purposes.

| | Text field | Comment |
|---|---|---|
| Part of the description | yes | no |
| Editable in the object form | yes | no, separate area |
| Author and date | no | yes |
| Status open/done | no | yes |
| In exports | depending on the field | **never** |
| Findable in full text | yes | no |

Rule of thumb: what someone outside is meant to learn about your archive is a
text field. What your staff record among themselves or still have to work
through is a comment.

## Switching on

Comments are switched off as long as you do nothing. After an update, nothing
changes in your archive.

There is **one single setting** for this. Under *Administration → Settings*:

| Setting | Values | Default |
|---|---|---|
| `comments_min_role` | empty, `user`, `user_intern`, `loan_admin`, `editor`, `admin` | **empty** |

**Empty means off.** No comment area, no work list, nothing to see. As soon as
you enter a role, comments are switched on — and the role entered is at the same
time the **lowest one allowed to write**.

An unknown value (a typo) counts as empty, that is, as switched off. Anton does
not guess in the more permissive direction here.

!!! note "The field is already in the form"
    On updating to v0.86, Anton creates the «Comments» field and places it at
    the end of your **internal detail form**. As long as the setting is empty it
    draws nothing — so you see nothing until you want to.

    Where the area sits remains up to you: in the [form editor](forms.md) it can
    be moved, added to further forms or removed entirely. Once you have moved or
    removed it, a later update no longer touches the placement.

## Who sees what

| Role | sees | writes | ticks off | work list |
|---|---|---|---|---|
| not logged in | – | – | – | – |
| `user` (external) | only their own | from the minimum role | – | – |
| `user_intern`, `loan_admin`, `editor` | all | from the minimum role | yes | yes |
| `admin` | all | yes | yes | yes |

Everyone may change and delete their own comments; only the administration may
do so for those of others.

!!! important "The default allows external contributions"
    With `comments_min_role = user`, any **logged-in** person may leave a note —
    the «that is my grandfather in this photograph» case. Such people see
    exclusively their own contributions, never those of your team, and cannot
    tick anything off.

    If you do not want that, set the minimum role to `user_intern`. Comments
    then remain entirely among your staff.

    Visitors who are not logged in cannot comment or see comments under any
    circumstances.

## Protection against misuse

Because external persons can write as well, the following applies:

* **Plain text.** No Markdown, no HTML — unlike in text fields.
* **At most 5000 characters** per comment.
* **At most 20 comments per account and hour.**
* In the work list, every entry shows the **role** of the person who wrote it,
  so an external contribution is recognisable at once.

No approval step is needed: external contributions are invisible to other
external persons anyway. The administration can delete any comment.

## Where comments do not appear

* In **no export** — not in EAD, EAD3, TEI, Dublin Core, RDF or DIP. The only
  exception is the SQL dump, which by definition is a complete backup of the
  database. See [export matrix](export-matrix.md).
* In **no public view**.
* **Not in the full text** of the record. You find comments via the work list,
  not via the normal search — otherwise working notes would mix in with the hits
  of your research.

## What comments cannot do

No replies to comments, no assignment to particular people, no notifications.
There is open and done, nothing more — that covers working through them without
imposing a workflow.
