# Normdaten-Abgleich (`resources:sync`)

Anton hält die Verknüpfungen zu externen Normdaten (GND, Wikidata,
Metagrid …) als **lokale Kopie** in der `resources`-Tabelle. Damit neu
verfügbare Links dort ankommen, muss regelmässig abgeglichen werden. Die
nutzerseitige Sicht auf das Thema beschreibt [Normdaten](../user/authorities.md).

## Kommando

```bash
php artisan resources:sync --env={slug}
```

Der Lauf geht alle Entitäten durch, die bereits eine Ressource eines
Providers besitzen, fragt den jeweiligen Provider erneut ab und ergänzt neu
verfügbare Links. Zusätzlich bereinigt er doppelte Einträge und
vereinheitlicht die Provider-Bezeichnungen.

`{slug}` ist der Environment-Slug der jeweiligen Installation (wie bei den
übrigen `--env`-Kommandos).

## Geplanter Betrieb

In den produktiven Installationen läuft der Abgleich **automatisiert und
wiederkehrend** als geplanter Job (Scheduler). Die Frequenz ist pro
Installation konfigurierbar und wird bei Bedarf angepasst; ein manueller
Eingriff pro neuem Link ist nicht nötig. Neue Verknüpfungen erscheinen
spätestens beim nächsten geplanten Lauf.

Der manuelle Aufruf oben ist vor allem für Erstbefüllung, Tests oder einen
sofortigen Abgleich ausserhalb des Zeitplans gedacht.

!!! note "Metagrid-Partnerschaft"
    Damit die **eigenen** Akteur:innen bei Metagrid erscheinen, muss die
    Institution als Partner bei [Metagrid](https://metagrid.ch/) angemeldet
    sein. Der Abgleich betrifft nur den lokalen Bestand – er ersetzt die
    Partnerschaft nicht. Details siehe [Normdaten](../user/authorities.md).
