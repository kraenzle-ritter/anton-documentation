# Normdaten-Abgleich (`resources:sync`)

Anton hält die Verknüpfungen zu externen Normdaten (GND, Wikidata,
Metagrid …) als **lokale Kopie** in der `resources`-Tabelle. Damit neu
verfügbare Links dort ankommen, muss regelmässig abgeglichen werden. Die
nutzerseitige Sicht auf das Thema beschreibt [Normdaten](../user/authorities.md).

## Kommando

```bash
php artisan resources:sync --env={slug}
```

Ein Lauf führt der Reihe nach drei Schritte aus:

1. **Provider-Namen normalisieren** – veraltete Provider-Bezeichnungen werden
   auf die kanonische Form gebracht (siehe [Normalisierung](#normalisierung)).
2. **Duplikate prüfen** – Ressourcen mit identischer URL werden gemeldet (und
   auf Wunsch entfernt, siehe `--delete-duplicates`).
3. **Entitäten abgleichen** – alle Akteur:innen, Orte und Schlagwörter, die
   bereits eine Ressource eines der Sync-Provider besitzen, werden erneut beim
   jeweiligen Provider abgefragt und um neu verfügbare Links ergänzt.

Am Ende wird eine Zusammenfassung ausgegeben (verarbeitete/aktualisierte
Entitäten, neue Ressourcen, Fehler, bereinigte Duplikate).

### Optionen

| Option | Wirkung |
|---|---|
| `--env={slug}` | Ziel-Installation (Environment-Slug), wie bei allen `--env`-Kommandos. |
| `--dry-run` | Nichts schreiben, nur simulieren und berichten. |
| `--limit={n}` | Nur die ersten *n* Entitäten je Modell verarbeiten (zum Testen). |
| `--delete-duplicates` | Gefundene URL-Duplikate tatsächlich löschen (ohne Flag nur melden). |
| `--mail={adresse}` | Zusammenfassung per E-Mail senden (mehrere Adressen kommasepariert). |

## Konfiguration

### Welche Provider

Beim **interaktiven Verknüpfen** im Bearbeitungsformular steht die volle Liste
der in `config/resources.php` (Schlüssel `providers`) definierten Provider zur
Verfügung – u. a. GND, Wikidata, Metagrid, GeoNames, ortsnamen.ch, Idiotikon,
diverse Wikipedia-Sprachen sowie zahlreiche Nachschlagewerke und Partnerarchive.
Jede Provider-Definition legt `api-type`, `base_url`, die `target_url` des
gespeicherten Links und – wo zutreffend – die `wikidata_property` fest;
Anton-basierte Partnerarchive (z. B. Georg Fischer, Gosteli, KBA) benötigen
zusätzlich einen `api_token` aus der `.env`.

Der **periodische Abgleich** `resources:sync` fragt jedoch nur die drei
Provider erneut ab, für die eine Live-Nachführung sinnvoll ist – in dieser
Reihenfolge:

1. `metagrid`
2. `gnd`
3. `wikidata`

Abgeglichen werden die Modelle **Actor**, **Place** und **Keyword**. Eine
Entität wird nur berührt, wenn sie bereits mindestens eine Ressource eines
dieser Provider besitzt – der Abgleich ergänzt vorhandene Verknüpfungen, er
legt keine völlig neuen an.

!!! note "Neue Provider aufnehmen"
    Zusätzliche Provider (oder geänderte Basis-URLs/Tokens) sind eine
    Code-/Konfigurationssache im `config/resources.php` und werden mit einem
    Deploy ausgerollt, nicht über `/settings`. Ob ein Provider auch in den
    periodischen Abgleich aufgenommen wird, ist im Kommando selbst festgelegt.

### Filter

Der Abgleich übergibt beim Nachführen den Wert des Settings
`resources_filter` an den Provider (leer, falls nicht gesetzt). Damit lassen
sich Treffer installationsweit einschränken.

### Normalisierung

Der `rename`-Abschnitt in `config/resources.php` bildet veraltete oder
uneinheitliche Provider-Slugs auf die kanonische Form ab (z. B. `loc` →
`lcnaf`, `wikipedia` → `wikipedia-de`, `sudoc` → `idref`). Jeder Sync-Lauf
wendet diese Zuordnung zuerst an, damit der Bestand konsistent bleibt.

## Cronjob einrichten

Auf den produktiven Servern ist der Laravel-Scheduler (`schedule:run`)
**nicht** installiert. Der Abgleich wird stattdessen **pro Installation als
eigener Crontab-Eintrag** eingerichtet – auf den k&r-Servern über
**anton-ansible** provisioniert, nicht in `app/Console/Kernel.php`.

Ein Eintrag ruft das Kommando direkt mit dem Environment-Slug auf, z. B. für
einen nächtlichen Lauf:

```cron
# Normdaten-Abgleich für die Installation "besenval", täglich 02:30
30 2 * * *  cd /var/www/anton && php artisan resources:sync --env=besenval --delete-duplicates --mail=admin@example.org >> storage/logs/resources-sync.log 2>&1
```

- **Pro Environment ein eigener Eintrag** – der Slug bestimmt die
  Zielinstallation.
- Die **Frequenz** ist pro Installation frei wählbar (üblich: nächtlich); wegen
  der Rate-Limits gegenüber den externen APIs läuft ein grosser Bestand nicht
  im Sekundenbereich durch.
- `--delete-duplicates` und `--mail=` sind optional, im geplanten Betrieb aber
  üblich, um den Bestand sauber zu halten und über das Ergebnis informiert zu
  werden.

!!! note "Metagrid-Partnerschaft"
    Damit die **eigenen** Akteur:innen bei Metagrid erscheinen, muss die
    Institution als Partner bei [Metagrid](https://metagrid.ch/) angemeldet
    sein. Der Abgleich betrifft nur den lokalen Bestand – er ersetzt die
    Partnerschaft nicht. Details siehe [Normdaten](../user/authorities.md).
