# Keywords

Keywords describe units of description by subject — for things, events,
techniques, works. Persons and organisations, by contrast, belong with the
[actors](actors.md), geographical information with the [places](places.md).

They are found under **Admin → Keywords**; they are linked in the object form in
the **keywords (subjects)** field.

!!! note "Hierarchy only on request"
    By default keywords stand side by side; the **type** merely groups them. Broader and narrower terms and «see also» can be switched on per archive, see [Broader and narrower terms](#broader-and-narrower-terms).

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

## Broader and narrower terms

With the setting `keyword_relations` switched on under **Admin → Settings**, every keyword carries **broader terms**, **narrower terms** and **see also**. Switched off, the default, everything stays as it was.

In the keyword's form the terms are picked in three fields, as in the object form. A narrower term can be entered from either end; Anton stores the relation once and shows it on both sides.

A keyword may have **several broader terms**. One of them is the **primary** one: the keyword sits under it in the **path** shown at the top of the detail page, for instance «Writing › Letter». The first broader term becomes the primary one; where there are several, it is chosen in the form under **Primary**.

Anton allows no circle: a keyword cannot sit under one of its own narrower terms, nor be related to itself. The form then comes back with a message and saves nothing.

The **Term tree** button on the keyword list and beside the path of a keyword shows broader and narrower terms as a tree. It loads as you go, like the archive plan, and opens the way to the keyword you start from. A keyword with several broader terms opens only under its primary term; under the others it appears as a reference, such as «letter (see writing)».

Deleting a keyword removes its relations. Merging two keywords hands the relations of the one that goes to the one that stays.

## Authority data

Like actors and places, keywords can be linked to
[authority data](authorities.md) — to Wikidata or the GND, for example.

!!! warning "Not available in every archive"
    The authority data column only appears on the keyword if providers are
    configured for the archive. If the setting is missing, there is no way to
    link a keyword — whereas actors and places can still be linked.

## Downloading as a thesaurus

With broader and narrower terms switched on, signed-in staff find the button **Download SKOS** on the keyword list and **Subtree as SKOS** on every keyword. The file holds all keywords, or the keyword with everything below it, as Turtle, RDF/XML or N-Triples: labels in every language, other names, broader and narrower terms, «see also» and the linked authority data. Every keyword appears under its lasting address. The [export matrix](../admin/export-matrix.md) lists what exactly goes out.

## Where a keyword is used

Under «appears in», the detail page shows all units of description that carry
the keyword.

If the keyword has narrower terms, the switch **Including narrower terms** adds their units of description to the list. The same switch appears in the search beside the chosen filters as soon as you filter by a keyword.

## Deleting

A keyword can only be deleted as long as it is entered on **no unit of
description**. Otherwise Anton refuses deletion and reports the reason. Which
units are affected is shown by «appears in» on the detail page; the assignments
have to be removed there first.
