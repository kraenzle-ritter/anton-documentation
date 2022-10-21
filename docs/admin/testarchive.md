# Testinstallation: Kränzle & Ritter Firmenarchiv

Unter [https://kr.anton.ch](https://kr.anton.ch) gibt es eine Testinstallation. Diese dient als Spielwiese. Die Daten der Testinstallation werden täglich zurückgesetzt.

## Wiederherstellen des Testarchivs

Das Testarchiv wird täglich mit `anton:reset` per cronjob wiederhergestellt.

```bash
1 2 * * * cd path_to_anton; \
php artisan anton:reset --env="kr" \
--dump="{path_to_anton-customers}/kr/reset_db/reset.sql.gz" \
--assets="{path_to_anton-customers}/kr/reset_assets" \
--mail >/dev/null
```

## Änderungen dauerhaft speichern

Um Änderungen dauerhaft zu speichern, ist deshalb ein Backup aus dem Datenbank-Dump `{path_to_anton-customers}/kr/reset_db/reset.sql.gz` zu machen:

```bash
php artisan anton:backup --file "customers/kr/reset_db/reset.sql.gz" --env kr
```

Nun wird bei der nächsten Wiederherstellung das neue Backup verwendet.
