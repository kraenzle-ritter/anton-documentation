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

## check-disk-space

Überprüft die Speicherplatzbelegung eines `customers`.

``` bash
php artisan anton:check-disk-space --env="besenval" -vv
```

Das Kommando vergleicht die aktuelle Speicherplatzbelegung mit der erlaubten Speicherplatzbelegung, die in `setting('maximum_storage')` in GB gespeichert ist.

Wenn über 80% des Speicherplatzes belegt ist, wird eine Warung ausgegeben.

Wenn mehr Speicherplatz als erlaubt belegt ist, wird ein Fehler zurückgegeben.

## check-media

Überprüft die Integrität (`md5sum`) sämtlicher Medien.

``` bash
php artisan anton:check-media --env="besenval"
```

Mit der Option `--files` kann man eine Liste der korrupten Dateien ausgeben.

## doctor

Überprüft einige grundlegende Settings und kann evtl. Auskunft geben, ob etwas an der Installation nicht stimmt.

``` bash
php artisan anton:doctor --env="besenval"
```
