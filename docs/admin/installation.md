# Installation

Für jeden `customer` gibt es eine Kennung, `customer-slug`. Im folgenden wird als Beipiel "besenval" als customer-slug verwendet.

## Einen neuen customer einrichten

Um einen neuen `customer` einzurichten benötigt man den Zugang über die Kommandozeile.

###  config.php in bootstrap/ anlegen

Falls die Umgebung nicht der subdomain entspricht, muss man ein `config.php` File anlegen, das ein Array definiert:

```php
$slugArray = ['besenval.anton' => 'besenval'];
```

Der `key` besteht aus Subdomain und Domain (verbunden durch einen Punkt), der `value` enthält den `customer-slug` bzw. die Erweiterung des `.env` files.


### Umgebung anpassen

Die App beziehungsweise subdomain soll "besenval" heissen. Folgende Zeilen im `.env` File müssen angepasst werden:

```
APP_ENV=besenval
APP_URL=http://besenval.anton.test
DB_HOST=127.0.0.1
DB_DATABASE=anton_besenval
DB_USERNAME=username
DB_PASSWORD=passwort
```

Die `.env` Datei speichern unter `.env.besenval`.


!!! note "Wichtig"
    Wichtig: Für die ersten Commands muss der Cache-Driver in `.env.besenval` auf file gestellt sein:

    ```
    CACHE_DRIVER=file
    ```

    Nach der migration kann dieser Wert zu 'database' geändert werden.


## Mysql-Datenbank erstellen

Als root anmelden:

```sql
mysql -u root -p
```

Eine leere mysql-db anton_"slug" erstellen.

```sql
CREATE DATABASE anton_besenval;
```

Einen eigenen DB-User erstellen:

```sql
CREATE USER 'anton_besenval'@'localhost' IDENTIFIED BY 'user_password';
```

Ersetze `user_password` durch das Passwort.

Alle Rechte für diese user einrichten:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'anton_besenval'@'localhost';
```

## Grundinstallation

```bash
php artisan anton:install -vv --env=besenval
```

Es laufen nun die nötigen `migrations` und die Datenbank wird mit den Grunddaten versorgt.

Nun kann im `.env.besenval` der Cache auf 'database' gesetzt werden.

## Datenverzeichnis erstellen

In `custumers/slug` bzw. `customers/besenval` werden die Kundendaten gespeichert. Das Verzeichnis inklusive der nötigen Unterverzeichnisse kann einfach mit `anton:customdir` erstellt werden:

```bash
php artisan anton:customdir -vv --create --env=besenval
```

## Logo kopieren

Falls kein Logo zur Verfügung steht, kann das Antonlogo kopiert werden:

```bash
php artisan anton:install --logo -vv --env=besenval
```

## Matomo einbinden

Auf Matomo einloggen [http://matomo.anton.ch/](http://matomo.anton.ch/). Unter "Websites Verwalten" eine neue Website hinzufügen.

In den Anton Settings `analytics_id` mit der Motomo ID ausfüllen.

## Configure Supervisor

Als `root` die Konfigurationsdatei `etc/supervisor/supervisor.conf` öffnen und einen neuen `customer` einrichten.

```
[program:laravel-worker-besenval]
process_name=%(program_name)s_%(process_num)02d
command=/usr/bin/php7.3 {{ path to anton dir }}artisan queue:work database --tries=3 --timeout=300 --env=besenval
autostart=true
autorestart=true
start retries=10
user={{ user who runs anton }}
numprocs=1
redirect_stderr=true
stdout_logfile={{ path to log }} 
``

