# Shrink Anton for a public installation

If Anton is also to manage highly sensitive data, it is a good idea to run Anton on a private network rather than on the internet. To publish the data nevertheless, it is possible to synchronise Anton with an instance on the internet in which private and blocked information has been deleted.

For this we use 3 Anton instances:

Private network:

- __production__: the working environment with all data  
- __sync__: a non-visible installation for deleting the sensitive data

Internet:

- __public__: a clone of the sync environment on the internet

## Process

1. Backup of production  
2. Restore the database with data from production in sync  
3. Shrink the data  
4. Delete media if not referenced in sync; copy web versions from production when needed  
5. Backup of sync  
6. Sync data from sync to public  
7. Restore public

For steps 1 to 4 there is the bash script `sync.sh`, which after the backup/restore starts the Laravel command `anton:shrink-to-public` for steps 3 and 4.

## Shrink to public

```php
php artisan anton:shrink-to-public --path-to-media {path} --env {sync}
```

Since this command is run in the sync environment, the path to the media directory of the production environment has to be passed.

There is also an option `--days`. If set, the command only copies media from production to sync if the media has been updated in the database during this period. Once the synchronisation has been done, that is an option for speeding up the cron job.
