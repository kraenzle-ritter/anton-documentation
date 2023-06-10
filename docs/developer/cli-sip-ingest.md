## Comand line SIP Import (for Tests)

For the Setup of the SIP Import cf. also [Sip Import](/users/sip-ingest.md)

```bash 
php artisan anton:import --env slug --from-sip --no-validation --create-actors -vv path/to/sip --import
```

### Revert a SIP Import or Confirm Import

Before a SIP Import Anton backups the database, so if anything goes wrong you can come back to the status before the Import. The backup name is stored in the SIP-Entry (in the accession archives) and the `Status of description` is set to draft.

This will restore the database from the last/actual backup and sync the media with the database (namely delete media wich are not registered in the database):

```bash
php artisan anton:sip-import --env puenktchen --id 123 -vv --revert
```

This will set the `Status of description` in the SIP-Entry to "final":

```bash
php artisan anton:sip-import --env puenktchen --id 123 -vv --confirm
```
