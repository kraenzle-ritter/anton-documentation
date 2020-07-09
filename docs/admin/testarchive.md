# Testinstallation: Kränzle & Ritter Firmenarchiv

Unter [https://kr.anton.ch](https://kr.anton.ch) gibt es eine Testinstallation. Diese dient als Spielwiese. Die Daten der Testinstallation werden täglich zurückgesetzt.

## Wiederherstellen des Testarchivs

Das Testarchiv wird täglich mit ``anton:reset`` per cronjob wiederhergestellt.

```bash
1 2 * * * cd /usr/local/prj/anton; \
/usr/bin/php7.3 /usr/local/prj/anton/artisan anton:reset --env="kr" \
--dump="/usr/local/prj/anton/customers/kr/reset_db/reset.sql.gz" \
--assets="/usr/local/prj/anton/customers/kr/reset_assets" \
--mail >/dev/null
```

## Änderungen dauerhaft speichern

Um Änderungen dauerhaft zu speichern, ist deshalb ein Backup aus dem Datenbank-Dump `customers/kr/reset_db/reset.sql.gz` zu machen:

```bash
php artisan anton:backup --file "customers/kr/reset_db/reset.sql.gz" --env kr
```

Nun wird bei der nächsten Wiederherstellung das neue Backup verwendet.
