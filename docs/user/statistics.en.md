# Statistics

The statistics evaluate the holdings and their use. They are reachable from the
admin page.

!!! note "For the administration only"
    The statistics require the `admin` role. They are not accessible with the
    `editor` role.

## The tabs

**Overview** counts what the archive contains: records, fonds, actors, places,
keywords, media and user accounts. Added to this are the storage space occupied
and the agreed quota — the tab therefore also answers the question of how full
the archive is.

**New objects** shows the growth, broken down by year and by user account.

**Loans and orders** lists the [orders](cart.md) per year, the [loans](loans.md)
per year with a comparison of items lent out and returned, and the orders per
year and fonds — with a link to the fonds concerned. This is the only evaluation
of the orders that Anton keeps.

**Search** shows the search queries: as a chart, the queries per month over the last twelve months and how many of them had hits; as a table, the last 30 days per type of search with the number of queries, the hits and the success rate; and as a summary, all stored queries with total, hits and success rate. A low success rate is an indication that users are not finding what they are looking for. Queries are counted only while the setting `log_search_queries` is on; it is off by default, because the table grows without a time limit.

**Fonds** lists, for each fonds, the reference code, title, number of entries,
extent in linear metres and number of media.

**Actors**, **places** and **keywords** each have their own tab with the same
structure: the total number, how many of them are linked to
[authority data](authorities.md), and the distribution across the providers —
GND, Wikidata and so on. These three tabs therefore show how far the
synchronisation of authority data has progressed.
