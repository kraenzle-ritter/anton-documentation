# Installation

Für jeden `customer` gibt es eine Kennung, `customer-slug`. Im folgenden wird als Beispiel "besenval" als customer-slug verwendet.

## Einen neuen customer einrichten

Um einen neuen `customer` einzurichten benötigt man den Zugang über die Kommandozeile.

###  config.php in bootstrap/ anlegen

Falls die Umgebung nicht der subdomain entspricht, muss man ein `config.php` File anlegen, das ein Array `$slugArray` definiert. Dieses ordnet die URL der Anton-Installation einem den `customer` zu: 

```php
$slugArray = ['besenval.anton' => 'besenval'];
```

Der `key` besteht aus hier Subdomain und Domain, der `value` enthält den `customer-slug` bzw. das suffix des `.env` files, das in diesem Fall `.env.besenval` heisst.


### Umgebung anpassen (.env)

Die Umgebungsvariablen werden im `.env.besenval` im root Verzeichnis der Anton-Installation gespeichert. Weitere Variablen sind dann in der Datenbank in den Settings gespeichert.

#### Allgemeine Umgebungsvariablen

Beispiel Besenval: 

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

#### Datenbank Credentials
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

!!! note "Wichtig"
    Wichtig: Für die ersten Commands muss der Cache-Driver in `.env.besenval` auf file gestellt sein:

    ```
    CACHE_DRIVER=file
    ```

    Nach der Grundinstallation (bzw. der database migration) sollte dieser Wert zu 'database' geändert werden.

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

Es ist einfach, den Email Versand zu testen:
```bash
php artisan anton:doctor --all --env kr --mail 'kraenzle@k-r.ch'
```

#### Customers Path
Ausserdem kann die Variable `CUSTOMER_PATH` gesetzt werden (sie muss einen absoluten Pfad enthalten). Ist der `CUSTOMER_PATH` nicht gesetzt wird im Anton Ordner ein `customers` Ordner angelegt und verwendet.


#### Geolokalisierung 

Um Geolokalisierung der Orte mit Geonames und Kartendarstellungen von Google Maps zu ermöglichen, müssen folgende Variablen gesetzt sein:

```
GOOGLE_API_KEY
GEONAMES_USERNAME
```


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
GRANT RELOAD, PROCESS ON *.* to 'anton_besenval'@'localhost';
```

## Grundinstallation

```bash
php artisan anton:install -vv --env=besenval
```

Es laufen nun die nötigen `migrations` und die Datenbank wird mit den Grunddaten versorgt.

Nun kann im `.env.besenval` der Cache auf 'database' gesetzt werden.

## Datenverzeichnis erstellen

In `customers/slug` bzw. `customers/besenval` werden die Kundendaten gespeichert. Das Verzeichnis inklusive der nötigen Unterverzeichnisse kann einfach mit `anton:customdir` erstellt werden:

```bash
php artisan anton:customdir -vv --create --env=besenval
```

Nun als `root` das Verzeichnis schreibbar machen:

```
chmod -R 775 customers/besenval
```

## Logo kopieren

Falls kein Logo zur Verfügung steht, kann das Antonlogo kopiert werden:

```bash
php artisan anton:install --logo -vv --env=besenval
```

## Matomo einbinden

Der Befehl [`matomo`](console-commands.md#matomo) richtet alles drei ein — die
Website in Matomo, einen Benutzer mit Leserecht auf genau diese Website, und
einen Token dafür — und trägt `analytics_id` und `analytics_auth_token` in die
Einstellungen des Mandanten ein:

```bash
php artisan matomo --env=<slug>
php artisan matomo --env=<slug> --show-sites   # nur nachsehen, was Matomo kennt
```

Vorausgesetzt sind `APP_URL`, `MATOMO_ADMIN_AUTH_TOKEN` und `MATOMO_EMAIL` in
der `.env` des Mandanten. `MATOMO_URL` ist optional und steht standardmässig auf
`https://matomo.anton.ch`; `analytics.anton.ch` ist dieselbe Installation unter
einem zweiten Namen.

Jeder Mandant bekommt einen **eigenen** Token mit Leserecht auf seine eigene
Website. Ein gemeinsamer Hauptschlüssel wäre bequemer und ist bewusst nicht
vorgesehen: Ein Matomo-Token mit Superuser-Rechten löscht über
`SitesManager.deleteSite` eine Website samt ihrer ganzen Auswertungshistorie,
ohne nach einem Passwort zu fragen.

Von Hand geht es weiterhin: in Matomo einloggen, unter «Alle Websites» eine
Website anlegen, einen Benutzer mit Leserecht darauf einrichten, und
`analytics_id` und `analytics_auth_token` in den Anton-Einstellungen eintragen.

### Was die Statistikseite zeigt

Die Seite «Anton Analytics» holt die Zahlen serverseitig von Matomo und stellt
sie selbst dar: Besuche, verschiedene Besucher:innen, Seitenaufrufe,
Verweildauer, Absprungrate, die zehn meistgesehenen Seiten, die Herkunft der
Besucher:innen und die Suchbegriffe. Zwischen Tag, Woche, Monat und Jahr lässt
sich oben wechseln.

Der Token verlässt den Server dabei nicht. Bis Version 0.93.0 war Matomos
eigenes Auswertungsfenster eingebettet, und dessen Adresse trug den Token — er
stand damit im Quelltext der Seite, in der Verlaufsliste des Browsers und im
Zugriffsprotokoll von Matomo.

Ist für einen Mandanten keine `analytics_id` oder kein Token hinterlegt, sagt
die Seite das. Sie zeigte in diesem Fall früher stillschweigend nichts.

## Configure Supervisor

Als `root` die Konfigurationsdatei `etc/supervisor/supervisor.conf` öffnen und einen neuen `customer` einrichten.

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
Im selben Verzeichnis dann ein File environment anlegen und die Variablen befüllen:

```
SPRVS_PHP=
SPRVS_LOG=
SPRVS_USER=
SPRVS_ANTON=
```

Dann den supervisor als `root` neu starten:

```bash
supervisorctl stop
supervisorctl reread
supervisorctl update
supervisorctl restart
```
