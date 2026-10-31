# Selection and bulk actions

Several units of description can be ticked in result lists and processed together. There are two actions for this: [moving](hierarchy.md), from the role `admin`, and the [bulk edit](#sammelbearbeitung), from the role `editor`.

!!! note "Only in some archives"
    Bulk actions have to be enabled. They are not a standard feature; the setting cannot be changed in the admin area, and with Anton as a Service, k & r is responsible for it. Anyone who does not need them can additionally switch them off in their own [profile](profile.md).

## First the action, then the selection

The order is the reverse of what one is used to and is the most common stumbling block:

1. **First** choose the action in the **actions** selection field: **move** or **edit**. Before that, nothing can be ticked; the boxes have no effect.
2. **Then** tick the units. The icon with the clipboard list above the result list — it shows the number of units selected — allows the current selection to be inspected at any time.
3. Carry out the action. **Clear** discards the selection.

!!! warning "Changing the action clears the selection"
    If the selection field is changed afterwards, the previous selection is discarded. The action therefore has to be determined before ticking.

## What can be selected together

For **moving**, only units that **could be siblings**. As soon as a file is ticked, a fonds can no longer be added — Anton prevents selections that could not be moved together. Anyone unable to tick a unit should therefore check the levels already selected. For **editing**, any units can be selected together.

If a move operation is already under way, the selection is locked until it has been completed or cancelled.

## Bulk edit {#sammelbearbeitung}

With the action **edit**, the button **Edit (number)** in the selection leads to the page **Bulk edit**. There a change applies to all selected units, at most 500 at a time.

| Change | What it does |
|---|---|
| **Set a value list** | set location, object type, status or level of detail of the description to a value or clear it; optionally **only where empty** |
| **Set a text field** | **replace** a text field in one language, fill it **only where empty**, or **append** a text (as a new paragraph) |
| **Keyword** | **add** or **remove** an existing keyword |
| **Search and replace** | replace a text in the title (all languages) or in a text field (all languages); optionally match case and whole words only |

Only the fields that occur in the archive's edit forms are offered. The search is literal, without wildcards or regular expressions. Reference code, level of description and protection period cannot be changed in bulk: the reference code because equal codes collide, level and protection period because they decide the place in the tree and the access to the units below as well.

A bulk edit runs like this:

1. **Preview**: Anton shows how many units change and the first 20 changes, before and after. The preview writes nothing.
2. **Run**: only after a preview of exactly these settings. Anyone who changes something afterwards needs a new preview.
3. The run happens in the background. First Anton takes a **backup of the database**; if it fails, nothing is changed. Then the units are changed one by one.
4. **Last runs** shows the status: waiting, running, done or failed, the number of changed units, errors and the name of the backup.

Every change stands in the unit's edit history and in the [holdings log](../admin/protokolle.md) like an edit in the form, with the name of the person who started the run. A run can be undone through the backup; the administration is responsible for that.

## Not the same as the order basket

The selection and the [order basket](cart.md) look similar and are nevertheless two separate lists that never influence one another. The selection serves editing, the order basket ordering. A selection cannot be transferred into the order basket.
