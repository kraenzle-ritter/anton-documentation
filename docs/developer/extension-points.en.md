# Extension points

Archives have special requirements — their own reference code logic, a
particular Word finding aid, a format normalisation. Anton answers this with
**one consistent pattern** instead of forking the core per customer:

> Tenant-specific behaviour is hooked in by **naming a class via a setting** — or
> by having a customer-specific subclass. The core remains unchanged.

Anyone who internalises that sentence will find most extension seams on their
own. This page lists the most important ones.

## Reference code generation

The setting `identifier_generator` contains either one of the built-in modes
(`standard`, `recordgroup_as_base`, `id_identifier`, `manual_identifiers`) or the
**fully qualified class name** of a custom generator. Anton instantiates it and
calls `getNewIdentifier(...)`:

```php
$generator = setting('identifier_generator');
// e.g. 'Anton\Models\IdentifierGenerators\KaeNewIdentifier'
return (new $generator($this))->getNewIdentifier($level_of_description_id, …);
```

Custom generators are located under `app/Models/IdentifierGenerators/`
(`KaeNewIdentifier`, `StopNewIdentifier` as templates). This allows an archive to
pull the location into the reference code or to run an entirely custom scheme
without the standard generator knowing about it.

## Exporters

The export layer is built along this seam. Anyone extending it follows two rules
(see also `CLAUDE.md`, section *Exporter layout*):

- Builders, DTOs and format logic belong under
  `app/Services/Exporter/<Format>/`, **never** in an HTTP controller.
- A controller under `app/Http/Controllers/Exporter/` is only a route handler.

Two concrete extension patterns:

**TEI via a factory.** `custom_teiexporter` is a setting that names an exporter
class per entity (`actors`, `places`, `keywords` …). The `TeiExporterFactory`
resolves it and otherwise falls back to the standard exporters. This gives an
archive a special format (the Opera format of ZBZ, for example) without touching
the standard.

**Customer-specific subclasses.** Word finding aids exist as `AntonWordExport`
and variants derived from it (`CasparwolfWordExport`, `GosteliWordExport`,
`ArchivdatenWordExport`); the DIP has a ZH variant (`ZhCreateDip`). The pattern:
inherit from the standard, override what differs.

!!! important "Maintain the export matrix as well"
    Anyone adding an export format or changing what an existing one outputs
    updates the [export matrix](../admin/export-matrix.md) in the same step —
    archives decide on that basis what counts as a backup. The rule is also in
    `CLAUDE.md`.

## Media conversions

The standard conversions (`web`, `thumb`, `poster`) are in
`config/conversions.php`. For anything different, a **custom conversion script**
can be stored: `media:conversions --conversion-script=…` reads it from the
tenant's `scripts/` directory (`customers/{slug}/scripts/`). This allows an
archive to run a normalisation that the core does not know about.

## Forms and value lists

Not code but data — and yet the most important «extension» of all: fields, form
sets and value lists are created by an archive via the interface or via seeders.
Details under [The form system](forms.md). Seeders deliberately do not overwrite
existing configurations.

## Tenant assets

Beyond code and database, tenant-specific material is located under
`customers/{slug}/` — logo and favicons, the conversion scripts mentioned, paths
for import and reset. That is the place for everything that belongs to the
installation but not to the code.

## The limit

The price of this pattern: customer classes and named settings are scattered
across the tree. Before building a new special case as its own class, it is
worth asking whether it could not be expressed as **configuration** — a form
set, a value list, a setting. Configuration survives refactorings; a customer
class has to be dragged along.
