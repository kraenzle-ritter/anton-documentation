# Verkleinern für eine öffentliche Installation

Soll Anton auch hochsensible Daten verwalten, empfiehlt es sich, Anton in einem privaten Netz statt im Internet zu betreiben. Um die Daten dennoch zu veröffentlichen, lässt sich Anton mit einer Instanz im Internet abgleichen, in der private und gesperrte Informationen gelöscht sind.

Dafür verwenden wir drei Anton-Instanzen:

Privates Netz:

- __production__: die Arbeitsumgebung mit allen Daten  
- __sync__: eine nicht sichtbare Installation, in der die sensiblen Daten gelöscht werden

Internet:

- __public__: ein Klon der sync-Umgebung im Internet

## Ablauf

1. Sicherung von production  
2. Datenbank mit den Daten aus production in sync wiederherstellen  
3. Daten verkleinern  
4. Medien löschen, die in sync nicht referenziert sind; bei Bedarf Webversionen aus production kopieren  
5. Sicherung von sync  
6. Daten von sync nach public abgleichen  
7. public wiederherstellen

Für die Schritte 1 bis 4 gibt es das Bash-Skript `sync.sh`, das nach Sicherung und Wiederherstellung für die Schritte 3 und 4 den Laravel-Befehl `anton:shrink-to-public` startet.

## Shrink to public

```php
php artisan anton:shrink-to-public --path-to-media {path} --env {sync}
```

Da der Befehl in der sync-Umgebung läuft, ist der Pfad zum Medienverzeichnis der production-Umgebung zu übergeben.

Ausserdem gibt es die Option `--days`. Ist sie gesetzt, kopiert der Befehl Medien nur dann von production nach sync, wenn sie in der Datenbank innerhalb dieses Zeitraums aktualisiert wurden. Nach einem ersten vollständigen Abgleich beschleunigt das den Cronjob.
