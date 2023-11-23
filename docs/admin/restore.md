# Backup and Restore from Backup

To backup the database just use the command

```bash
php artisan anton:backup --env besenval
```

```
Options:
  --file[=FILE]              Target file
  --target-dir[=TARGET-DIR]  Target directory for the backup
  --hourly                   Hourly Backup (filename: 00_backup_slug-hourly-23)
  --daily                    Daily Backup (filename: 00_backup_slug-daily-19)
  --weekly                   Weekly Backup (filename: 00_backup_slug-weekly-19)
  --monthly                  Monthly Backup (filename: 00_backup_slug-monthly-04)
  --yearly                   Yearly Backup (filename: 00_backup_slug-yearly-2019)
```

## Restore from Backup

Restoring from a backup may become necessary for various reasons. The database can be restored with the command 'anton:restore':

```bash
php artisan anton:restore --env besenval
```

```
Options:
  --list            Lists available anton-sql-dumps.
  --file[=FILE]     Source file.
  --drop            Erase all tables.
```
The database dump must be located in the `db_backup` folder in the customers-dir.

## Delete obsolete Media 
To delete any media that may no longer referenced in the database after restoring from the backup:

```bash
php artisan anton:check-media -vv --levels 3 --delete-from-system --env besenval
```

## Restore lost Media
If media-files are missing, they must be copied back from the external backup.
