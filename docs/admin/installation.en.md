# Installation

Every `customer` has an identifier, the `customer-slug`. In what follows, "besenval" is used as an example customer slug.

## Setting up a new customer

Setting up a new `customer` requires command-line access.

### Creating config.php in bootstrap/

If the environment does not correspond to the subdomain, a `config.php` file has to be created that defines an array `$slugArray`. This maps the URL of the Anton installation to a `customer`:

```php
$slugArray = ['besenval.anton' => 'besenval'];
```

Here the `key` consists of the subdomain and domain, and the `value` contains the `customer-slug`, that is, the suffix of the `.env` file — in this case `.env.besenval`.


### Adapting the environment (.env)

The environment variables are stored in `.env.besenval` in the root directory of the Anton installation. Further variables are then stored in the database in the settings.

#### General environment variables

Example Besenval: 

```
APP_ENV=besenval
APP_URL=http://besenval.anton.ch
APP_DEBUG=false
DEBUGBAR_ENABLED=false
APP_KEY=AppKey
APP_LOG_LEVEL=debug
EMAIL_EXCEPTION_ENABLED=true
SNEAKER_SILENT=true
```

#### Database credentials
```
DB_HOST=127.0.0.1
DB_DATABASE=datenbankname
DB_USERNAME=username
DB_PASSWORD=passwort
```

### Drivers

```
CACHE_DRIVER=file
SESSION_DRIVER=database
QUEUE_DRIVER=database
```

!!! note "Important"
    Important: for the first commands, the cache driver in `.env.besenval` has to be set to file:

    ```
    CACHE_DRIVER=file
    ```

    After the basic installation (that is, after the database migration), this value should be changed to 'database'.

#### Email

```
MAIL_DRIVER
MAIL_HOST
MAIL_PORT
MAIL_USERNAME
MAIL_PASSWORD
MAIL_FROM
MAIL_NAME
```

Testing email dispatch is straightforward:
```bash
php artisan anton:doctor --all --env kr --mail 'kraenzle@k-r.ch'
```

#### Customers path
The variable `CUSTOMER_PATH` can also be set (it has to contain an absolute path). If `CUSTOMER_PATH` is not set, a `customers` folder is created in the Anton folder and used.


#### Geolocation 

To enable geolocation of places with Geonames and map display from Google Maps, the following variables have to be set:

```
GOOGLE_API_KEY
GEONAMES_USERNAME
```


## Creating the MySQL database

Log in as root:

```sql
mysql -u root -p
```

Create an empty MySQL database anton_"slug".

```sql
CREATE DATABASE anton_besenval;
```

Create a dedicated DB user:

```sql
CREATE USER 'anton_besenval'@'localhost' IDENTIFIED BY 'user_password';
```

Replace `user_password` with the password.

Grant all rights to this user:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'anton_besenval'@'localhost';
GRANT RELOAD, PROCESS ON *.* to 'anton_besenval'@'localhost';
```

## Basic installation

```bash
php artisan anton:install -vv --env=besenval
```

The necessary `migrations` now run and the database is supplied with the base data.

The cache in `.env.besenval` can now be set to 'database'.

## Creating the data directory

The customer data is stored in `customers/slug`, that is, `customers/besenval`. The directory including the necessary subdirectories can easily be created with `anton:customdir`:

```bash
php artisan anton:customdir -vv --create --env=besenval
```

Now make the directory writable as `root`:

```
chmod -R 775 customers/besenval
```

## Copying the logo

If no logo is available, the Anton logo can be copied:

```bash
php artisan anton:install --logo -vv --env=besenval
```

## Integrating Matomo

Log in to Matomo at [http://matomo.anton.ch/](http://matomo.anton.ch/). Under "All websites", add a new website.

Set up a user in Matomo with the appropriate permission.

In the Anton settings, fill in `analytics_id` with the Matomo ID and copy the `analytics_auth_token` from Matomo.

## Configure Supervisor

As `root`, open the configuration file `etc/supervisor/supervisor.conf` and set up a new `customer`.

```
[program:laravel-worker-besenval]
process_name=%(program_name)s_%(process_num)02d
command=%(ENV_SPRVS_PHP)s %(ENV_SPRVS_ANTON)s/artisan queue:work database --tries=3 --timeout=120 --env=besenval
autostart=true
autorestart=true
startretries=10
user=%(ENV_SPRVS_USER)s
numprocs=1
redirect_stderr=true
stdout_logfile=%(ENV_SPRVS_LOG)s/worker-besenval.log
```
Then create an `environment` file in the same directory and fill in the variables:

```
SPRVS_PHP=
SPRVS_LOG=
SPRVS_USER=
SPRVS_ANTON=
```

Then restart the supervisor as `root`:

```bash
supervisorctl stop
supervisorctl reread
supervisorctl update
supervisorctl restart
```
