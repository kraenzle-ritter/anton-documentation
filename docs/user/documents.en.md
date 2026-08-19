# Documents

The «Documents» module provides a separate route to selected PDFs — annual
reports or publications, for example, that an archive wants to offer
specifically for reading. It is a shop window alongside the [search](search.md),
not another way into the archival arrangement.

The overview is located at `/documents` and can be linked to from the archive's
own website. The documents appear there arranged in groups, each group with a
short explanatory text.

!!! note "Set-up required"
    The module only shows anything if it has been set up — see
    [Setting up documents](../admin/documents.md). Without configuration,
    calling it up leads back to the home page.

## What the cataloguing has to provide

In the module, **one document corresponds to one unit of description**. Anyone
wishing to use it therefore catalogues the PDFs individually and not collectively
in one file.

## The viewer {#der-viewer}

When a document is opened, the content of the **form and content** field appears
on the left, the PDF on the right.

A table of contents can simply be written into the text field as a list:

```markdown
Contents:
- First chapter (p. 5)
- Second chapter (p. 17)
```

### When the page numbers do not match

The printed page numbers frequently differ from the PDF pages — a report with a
title page and a preface may begin its page 5 on PDF page 17. So that the jump
nevertheless lands in the right place, the PDF page can be added as a comment
after the entry:

```markdown
Contents:
- First chapter (p. 5) <!-- 17 -->
- Second chapter (p. 17) <!-- 29 -->
```

The printed page number continues to be displayed; the jump goes to the PDF page
in the comment. For readers, the comment remains invisible.
