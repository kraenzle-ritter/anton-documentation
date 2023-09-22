# Shrink Anton for a public installation

If Anton is also to manage highly sensitive data, it is a good idea to run Anton on a private network rather than on the Internet. To publish your data nevertheless, it is possible to synchronise Anton with an instance on the Internet in which private and blocked information has been deleted.

For this we use 3 Anton instances:

Private Network:

- __production__: your working environment with all data  
- __sync__: a non-visible installation to delete the sensitive data

Internet:

- __public__: a clone of the sync environment in the internet

## Process

1. Backup of production  
2. Restore database with data from production in sync  
3. Shrink the data  
4. Delete Media if not referenced in Sync; copy web-versions from production when needed  
5. Backup of sync  
6. Sync data from sync to public  
7. Restore public

For steps 1 to 4 there is the bash script `sync.sh`, which after the backup/restore starts the laravel script `anton:shrink-to-public` for step 3 and 4.

## Shrink to public

```php
php artisan anton:shrink-to-public --path-to-media {path} --env {sync}
```

Since we are running this command in the sync environment, we need to pass the path to the media directory of the production environment.

There is also an option `--days`. If set the command only copies media from production to sync if in the database the media has been updated during this period. If the syncronisation onve has been done that is an option to accelerate the cronjob.
