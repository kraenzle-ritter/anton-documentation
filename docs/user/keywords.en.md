# Keywords

Keywords describe units of description by subject — for things, events,
techniques, works. Persons and organisations, by contrast, belong with the
[actors](actors.md), geographical information with the [places](places.md).

They are found under **Admin → Keywords**; they are linked in the object form in
the **keywords (subjects)** field.

!!! note "No hierarchy"
    Keywords stand side by side. Anton maintains no thesaurus: there are no
    broader and narrower terms and no cross-references between keywords. The
    **type** merely groups them.

## Types

The types can be defined freely per archive and differ considerably between
archives. Common ones are event, object, unit of measurement/currency,
collection/work of art, procedure/process/technique, book/manuscript/publication
and other/miscellaneous; archives with special holdings maintain considerably
more — for raw materials and geology, buildings, flora and fauna or military
technology, for example. Authoritative is the value list of one's own archive,
which can be consulted under **Help → Value lists**.

## Recording

The form contains type, label, other name forms, variants, abbreviations,
description, sources and comment.

Whether the label can be recorded **multilingually** depends on the
`translate_keywords` setting. If it is switched off, there is only one input
field in the archive's main language.

Anton recognises existing keywords by their normalised label and reuses them
instead of creating duplicates.

Keywords can also be created **directly from the object form**: next to the
selection list in the **keywords** field there is a **+** which opens a window
with the same creation form. After creation the new keyword is selected — the
unit of description itself still has to be saved afterwards.

## Authority data

Like actors and places, keywords can be linked to
[authority data](authorities.md) — to Wikidata or the GND, for example.

!!! warning "Not available in every archive"
    The authority data column only appears on the keyword if providers are
    configured for the archive. If the setting is missing, there is no way to
    link a keyword — whereas actors and places can still be linked.

## Where a keyword is used

Under «appears in», the detail page shows all units of description that carry
the keyword.

## Deleting

A keyword can only be deleted as long as it is entered on **no unit of
description**. Otherwise Anton refuses deletion and reports the reason. Which
units are affected is shown by «appears in» on the detail page; the assignments
have to be removed there first.
