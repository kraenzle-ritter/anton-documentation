# Authority data (GND, Wikidata, Metagrid …)

Actors, places and keywords can be linked to entries in external authority
databases and reference works – to the
[Integrated Authority File (GND)](https://gnd.network/), to
[Wikidata](https://www.wikidata.org/) or to [Metagrid](https://metagrid.ch/),
for example. Metagrid plays a special role here: it is not a single reference
work but a **linking service** that brings together entries on the same person
across many Swiss research and memory institutions (e.g. Historical Dictionary
of Switzerland, Dodis, Swiss Social Archives, Swiss Economic Archives).

## How links come about

When editing an actor, a place or a keyword, the providers can be searched for
matching entries and the correct hit saved as a resource. Anton then stores a
link in a dedicated `resources` table – the link subsequently belongs to the
record.

!!! note "Local copy"
    Anton holds the external links as a **local copy** and displays them from
    there. When an actor is opened, Metagrid, GND or Wikidata are not queried
    live on every page view. This makes the display fast and independent of the
    availability of the external services – but it also means that newly added
    external links only appear after a **synchronisation**.

## Synchronisation

Newly added external links only appear in Anton after a **synchronisation** with
the providers. In production installations, this synchronisation runs
**automatically and repeatedly** as a scheduled job; the frequency is
configurable per installation. Manual intervention for each new link is not
necessary – new links appear by themselves, at the latest on the next scheduled
run.

!!! info "For the administration"
    The underlying `resources:sync` command and scheduled operation are described
    under [Authority data synchronisation](../admin/authorities.md).

## Two directions

For the interplay with a linking service such as Metagrid, it is worth keeping
two directions apart. They are independent of one another.

### Anton as a source: making new actors known

When a new actor is recorded in Anton, it is up to the linking service and the
partners involved to take up this entry and – where appropriate – link back to
Anton. Whether and how often a partner (the Historical Dictionary of
Switzerland, for example) updates its links is determined by the partner or the
linking service, not by Anton.

Anton's contribution to this direction is twofold:

- the **link** between the actor and the entry in the linking service, and
- making the person data available via the [Anton API](../api/index.md) so that
  partners can collect it periodically (page by page, filtered by entity type).

!!! warning "Prerequisite: partnership with Metagrid"
    This direction – making one's own actors visible to the linking service –
    works **only** if the institution has previously **registered as a partner
    with Metagrid**. Without this partnership, the persons recorded in Anton are
    not taken up by Metagrid and no back-links arise there either. Registration
    takes place directly with [Metagrid](https://metagrid.ch/) and is
    independent of the technical synchronisation in Anton.

!!! tip "In practice"
    An entry published *before* the corresponding actor existed in Anton
    initially contains no back-link to Anton – the target record did not yet
    exist at the time. Whether such legacy entries are updated retrospectively
    depends on the update rhythm of the respective partner. Questions about
    synchronisation frequency or back-links should therefore be addressed to the
    linking service or the partner.

### Anton as a consumer: adopting new links

When new partner institutions join the linking service, additional linking
options arise for existing actors. These new links appear in Anton **after the
next synchronisation** – that is, through the scheduled run described above. No
manual procedure per link is required; the recurring synchronisation pulls in the
newly available links automatically.

## In summary

- External links are stored locally and displayed from there.
- A scheduled, recurring synchronisation keeps the local stock up to date and
  adopts newly available links on its own.
- How quickly **other** institutions take up a new Anton actor is determined by
  those institutions or the linking service – not by Anton.
- For one's own actors to appear in Metagrid at all, the institution must be
  **registered as a partner with Metagrid**.
