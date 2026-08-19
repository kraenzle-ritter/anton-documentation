# Setting up documents

The [documents](../user/documents.md) module is configured via the setting
`documents-navigation` (ID 261). It contains a JSON object describing the groups
of the overview page. Without a valid entry, `/documents` redirects to the home
page and reports this to logged-in users.

## Structure

Every key of the object is a group and becomes the slug in the URL
(`/documents/geschäftsberichte`). Per group:

| Field | Meaning |
|---|---|
| `title` | Heading of the group, per language |
| `comment` | Explanatory text below the heading, per language |
| `parent_id` | ID of the unit of description below which all documents of the group are located |
| `regex` | currently without function, set to `null` |

## Example

```json
{
    "geschäftsberichte": {
        "title": {
            "de": "Geschäftsberichte",
            "en": "Annual Reports"
        },
        "comment": {
            "de": "Deutscher Kommentar",
            "en": "English Comment"
        },
        "parent_id": 9367,
        "regex": null
    },
    "publikationen": {
        "title": {
            "de": "Publikationen",
            "en": "Publications"
        },
        "comment": {
            "de": "Kommentar",
            "en": ""
        },
        "parent_id": 12319,
        "regex": null
    }
}
```

## Cataloguing

The module assumes that **each document corresponds to its own unit of
description**. All units below the respective `parent_id` appear in the group.

The text that the viewer displays to the left of the PDF comes from the **form
and content** field. How to build a jumping table of contents from it — even
with diverging page numbers — is described under
[Documents](../user/documents.md#der-viewer).

## Linking

The overview is reachable at `/documents` and can be linked to from the
archive's own website.
