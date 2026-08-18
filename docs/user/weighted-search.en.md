# Weighted search

The weighted search improves the search results in list views by sorting hits according to their relevance. The better a search term matches a record, the higher up it appears in the result list.

## Areas of application

The weighted search is available for:

- **Actors**
- **Places**
- **Keywords**

## How it works

The system rates hits according to various criteria:

| Type of hit | Rating |
|------------|-----------|
| **Exact match** | Highest relevance (3×) |
| **Hit at the beginning of a word** | High relevance (2×) |
| **Hit contains the search term** | Base relevance (1×) |

**Example**: when searching for "Müller":

1. An actor named "Müller" (exact) is displayed at the very top
2. Followed by "Müller-Weber" (begins with)
3. Then "Anna Müller" (contains)

In addition, different fields are weighted differently. The name of an actor, for example, counts for more than a hit in the description.

## Activation

### In the list view

1. Open the desired list view (actors, for example)
2. Enter a search term in the filter field
3. Below the search field, the checkbox **"Sort by relevance"** appears
4. Tick the checkbox to sort the results by relevance

!!! note "Note"
    The checkbox only appears when a search is active.

### As a default in the user settings

The weighted search can be set as a personal default:

1. Click on the profile (top right)
2. Choose **Profile / Account**
3. Go to **Settings**
4. Under **"Weighted search"**, choose one of the options:
   - **Default**: uses the archive's global setting
   - **On**: weighted search is always activated
   - **Off**: weighted search is always deactivated

!!! tip "Tip"
    With the "Default" option, the setting configured for the archive is adopted automatically. Future adjustments by the administration then take effect as well.

## Tips

- The weighted search is particularly useful with **common names** or **general terms**
- When searching for **exact reference codes** or **IDs**, the normal sorting is often more helpful
- The setting can be switched per search at any time via the checkbox
