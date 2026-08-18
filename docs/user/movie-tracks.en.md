# Cataloguing film content

For video and audio media, the content can be catalogued along the time axis:
instead of a description of the whole film, a **table of contents** is created
from entries with time markers — comparable to chapters.

!!! note "Not in every form"
    The table of contents is a form component and has to be provided for in the
    [form set](forms.md). On units of description without video it hides itself
    automatically.

## Recording

The video player sits above the table. The workflow is deliberately designed for
following along during playback:

1. Play the video and pause at the desired point.
2. The **+** button places a new entry **at the current playback position**.
3. Type the description directly into the cell. It is saved as soon as the field
   is left.

Also available: the **pin** icon sets the time marker of an existing entry to the
current playback position, the **✕** removes it, and the **handle** on the left
allows the entries to be reordered with the mouse.

!!! warning "Every change takes effect immediately"
    The table of contents has no save button — every entry is saved immediately.
    Deleting an entry happens without a confirmation query and cannot be undone.

Recording requires the `editor` role.

## In the detail view

There the table of contents appears as a list with description and time.
**Clicking an entry jumps to that point in the video** and plays it — the table
of contents thus becomes a means of navigating the film. The same list is
available in the [media gallery](gallery.md).
