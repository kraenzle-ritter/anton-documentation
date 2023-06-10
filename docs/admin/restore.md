# Restore from Backup

Restoring from a backup may become necessary for various reasons. The database can be restored with the command 'anton:restore':

```bash
php artisan anton:restore -vv --file db_backup-besenval.sql.gz --env besenval
```

The database dump must be located in the `db_backup` folder in the customers-dir.

To delete any media that may no longer exist in the database after restoring from the backup:

```bash
php artisan anton:check-media -vv --levels 3 --delete-from-system --env besenval
```

If media-files are missing, they must be copied back from the external backup.
