# Media gallery

The media gallery shows the images of an archive as a tiled grid — a visual
entry point alongside the [search](search.md). It is located at `/gallery`.

!!! note "Not linked everywhere"
    Anton does not add the gallery to the navigation itself. Whether it appears
    in the menu is decided by each archive; otherwise it is only reachable via
    the address.

## Two variants

| Variant | Filter |
|---|---|
| Classic gallery | A filter row above the grid; which fields it contains is configurable per archive |
| Gallery V2 | A sidebar with facets and **hit counts** per fonds, keyword and media type, plus a year range |

V2 requires a Typesense search engine and is being introduced step by step;
which variant an archive uses is a setting. The tiles and the enlarged view are
identical in both.

## What appears in the gallery

An image only appears if **all** conditions are met:

- It is not marked as «do not show in gallery». This marking takes effect for
  **everyone**, including logged-in editors.
- It is not marked as a blocked medium.
- For outsiders additionally: the unit of description is not blocked, its status
  is not «draft», and the [protection period](access.md) has expired.

Internally logged-in users therefore see more than the public — but the marking
«do not show in gallery» overrides every role.

In addition, it can be restricted per archive which fonds the gallery shows at
all — separately for internal and public use.

## Removing images from the gallery

The marking is set in the media administration under **Admin → Media**. It is
the right approach for images that are catalogued but not fit for the shop
window — versos, misexposures, technical shots.

For images that may not be shown for legal reasons, the
[protection period](access.md) or blocking the medium is the right means
instead: the gallery marking is a display decision, not an access restriction.
