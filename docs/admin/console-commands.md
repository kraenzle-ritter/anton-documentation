# Commands

## Grundsätzliches

Antons Kommandos sind [Laravel-Kommandos](https://laravel.com/docs/7.x/artisan) und werden über `artisan` aufgerufen.

Die meisten Kommandos erwarten die Angabe einer Umgebung, d.h. eines `customers-slug`.

``` bash
php artisan anton:command --env=besenval
```

Die Anton-Kommandos verwenden `Ottosmops\Consoleoutput\ConsoleOutputTrait`. Das bedeutet, dass Ausgaben nach `stdout` nur ausgegeben werden, wenn das verbosity-level erhöht wird.

Die Option `-v` gibt `info`-messages aus.

Mit der Option `-vv` werden auch `debug`-messages ausgegeben.

## anton:add-medium

```bash
php artisan anton:add-medium file.jpg --env="besenval" --id=123
```

Mit diesem Befehl kann ein Medium (Bild, Dokument) über die Kommandozeile einem Datensatz hinzugefügt werden. Das ist nützlich, wenn ein Bild zu gross für einen Upload mit dem Browser ist.

## anton:backup
Erstellt ein Backup der Datenbank. Ohne Angabe eines `--target-dir` wird das Backup im Customers Ordner (`db_backup`) gespeichert. Mit den Optionen `hourly`, `--weekly`, `--mothly`, `--yearly` werden die Dateinamen für rotierende Backups präpariert. Z.B.: `00_backup_besenval-daily-19.sql.gz`. Mit `--file` kann ein neuer Dateiname angegeben werden. 

vgl. anton:restore

## anton:check-disk-space

Das Kommando ist identisch mit `anton:doctor --disk`.

Überprüft die Speicherplatzbelegung eines `customers`.

``` bash
php artisan anton:check-disk-space --env="besenval" -vv
```

Das Kommando vergleicht die aktuelle Speicherplatzbelegung mit der erlaubten Speicherplatzbelegung, die in `setting('maximum_storage')` in GB gespeichert ist.

Wenn über 80% des Speicherplatzes belegt ist, wird eine Warung ausgegeben.

Wenn mehr Speicherplatz als erlaubt belegt ist, wird ein Fehler zurückgegeben.


## anton:check-terms

## anton:condense-history

## anton:count

## anton:count-jobs

## anton:customdir
vgl. Admin => Installation

## anton:doctor

Überprüft einige grundlegende Settings und kann evtl. Auskunft geben, ob etwas an der Installation nicht stimmt.

``` bash
php artisan anton:doctor --env="besenval" --all -vv
```

Optionen: 
```
    --all             check everything
    --binaries        check binaries
    --database        check if positions are not unique (within a parent)
    --disk            check disk usage
    --environment     check environment variables, setting etc.
    --jobs            check if supervisor is running
    --media           show problematic media
    --statistics      count rows in tables
    --mail[=MAIL]     email-adress
```

## media:check

Prüft die Konsistenz zwischen Anton-Datenbank, lokalem Filesystem, Inge und Dimag. Sechs Prüfebenen (1–6), einzeln oder kombiniert aufrufbar.

```bash
php artisan media:check --levels=1,5,6 --env=besenval -vv
```

Optionen:
```
    --levels=          Prüfebenen (1-6), kommasepariert
    --sip=             Nur Medien eines bestimmten SIP prüfen (AntonObject-ID)
    --fix-cloud-status Repariert cloud_status in DB (Level 5)
    --delete-local-masters  Löscht lokale Masterdateien nach Cloud-Verifikation (Level 5)
    --delete-from-system    Löscht Filesystem-Einträge ohne DB-Pendant (Level 3)
    --delete-from-inge      Löscht Waisen aus Inge/Dimag (Level 6)
    --year=            Startjahr für Dimag-Abfrage (Default: Jahr des ältesten Inge-Mediums)
```

Gibt am Ende eine Summary-Tabelle mit Counts und Status pro Level aus. Details siehe [Inge und Dimag](inge.md).

## storage:audit

Prüft lokale Masterdateien und SIP-Verzeichnisse. Bei Inge-Installationen sollten keine lokalen Masterfiles vorhanden sein.

```bash
php artisan storage:audit --env=besenval -vv
```

Optionen:
```
    --clean-sips       Entpackte SIP-Verzeichnisse löschen (ZIP-Archive bleiben)
    --clean-masters    Verifizierte lokale Masterfiles löschen (nur bei cloud=inge)
```

## notification:send

Erstellt eine System-Nachricht in einer oder allen Installationen. Siehe [Nachrichten](notifications.md) für Details.

```bash
# Einzelne Installation
php artisan notification:send --title="Wartung" --body="Details." --env=besenval

# Alle Installationen
php artisan notification:send --title="Update v0.54" --all

# Mehrsprachig
php artisan notification:send --title='{"de":"Update","fr":"Mise à jour"}' --all

# Adressaten einschränken
php artisan notification:send --title="Intern" --audience=editors --env=besenval
```

Optionen:
```
    --title=          Titel (Pflicht). String oder JSON
    --body=           Text (optional). String oder JSON
    --file=           Text aus Datei lesen
    --audience=       Adressaten: all, editors, admins (Default: all)
    --env=            Ziel-Installation
    --all             An alle Installationen senden
```

## sip:reconcile

Prüft den Sync-Status aller SIPs über Anton-DB, Inge und Dimag. Zeigt eine Summary-Tabelle pro SIP.

```bash
php artisan sip:reconcile --env=besenval -vv
```

Optionen:
```
    --sip=            Nur ein bestimmtes SIP prüfen (AntonObject-ID)
```

## anton:export

## anton:import

## anton:restore



## anton:update
