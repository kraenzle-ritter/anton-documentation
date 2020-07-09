# Configuration

## .env File


## Settings
We go here through the most important `settings` which only can be set by the superuser.

### abo and maximum_storage 

`abo should contain "basic", "standard" or "pro".

`maximum_storage` should contain the disk space in GB. It is used by the command `anton:check-disk-space`.

## searchfields and search_fields_extern

If you want to configure the searchfields for the advanced search you can fill this setting with a json object. You can find the full json here: `/admin/searchfields`. 
