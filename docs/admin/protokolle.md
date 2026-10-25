# Protokolle

Anton hält fest, wer was am Bestand getan hat (Bestandsprotokoll) und wer sich angemeldet hat oder abgewiesen wurde (Sicherheitsprotokoll). Die Durchsicht dieser Protokolle liegt beim Archiv. Festgehalten wird sie als **Durchsicht**: wer, wann, welcher Zeitraum (anton#670, anton#739; NDSA Co-4.1).

## Die Seite

Unter **Admin › Protokolle** stehen das Bestandsprotokoll, das Sicherheitsprotokoll, die Formatprüfung und die Durchsichten. Die Formatprüfung sehen alle Admins; die übrigen Reiter Superuser und, wo k & r sie freigeschaltet hat, die Admins des Archivs.

Unter jedem Protokoll lässt sich der gefilterte Zeitraum als durchgesehen festhalten, mit einer Bemerkung.

## Der Monat im Bericht

Archive, die den Monatsbericht erhalten, können darin die Protokolle des Vormonats bekommen:

- Anmeldungen (Anzahl, Konten), Fehlversuche und Sperren
- Konten neu, gelöscht oder mit neuer Rolle, auch gesperrte
- Löschungen von Datensätzen und Medien und Downloads von Mastern, je Person
- verweigerte Zugriffe angemeldeter Konten
- die Auffälligkeiten der täglichen Protokollprüfung, über den ganzen Monat

**Zu bestätigen** ist ein Monat mit einer Auffälligkeit, einer Kontoänderung, Löschungen oder Downloads von Mastern. Anmeldungen allein zählen nicht.

- Dann enthält der Bericht den Link **«Durchsicht bestätigen»**. Jede Empfänger:in erhält einen eigenen Link, gültig 45 Tage und nur für diesen Zeitraum und dieses Archiv. Erst der Knopf auf der geöffneten Seite hält die Durchsicht fest, das Öffnen allein nicht; Mailfilter öffnen Links, um sie zu prüfen. Festgehalten wird die Adresse und, wenn ihr genau ein Konto gehört, das Konto. Jede Empfänger:in bestätigt einmal.
- Nach der Anmeldung geht dasselbe unter **Admin › Protokolle**: Solange der Vormonat offen ist, steht dort ein Hinweis. Unter **Durchsichten** stehen die Zusammenfassung, Links in beide Protokolle und der Knopf **«Durchsicht bestätigen»**.
- War nichts zu bestätigen, sagt der Bericht das, und Anton trägt den Monat selbst ein, als **automatisch**. So bleibt die Reihe der Durchsichten lückenlos. Ein solcher Eintrag gilt nie als Durchsicht durch eine Person.

Die Liste der Durchsichten zeigt bei jedem Eintrag, wie er entstand: in Anton, per Link oder automatisch.

## Wann durchsehen

Einmal im Monat, wenn der Bericht da ist. Beim Durchsehen lohnt der Blick auf Konten, die niemand kennt, auf neue Admin-Rechte, auf Löschungen und Downloads in ungewohnter Menge und auf Konten mit vielen verweigerten Zugriffen. Was auffällt, gehört in die Bemerkung und an k & r.

## Auf der Kommandozeile

```bash
php artisan anton:doctor --logs --env=<slug>                       # Vormonat
php artisan anton:doctor --logs --month=2026-09 --env=<slug>       # ein bestimmter Monat
php artisan anton:doctor --logs --only-if-actionable --mail=<adresse> --env=<slug>
```

`--only-if-actionable` schickt den Bericht nur, wenn der Monat zu bestätigen ist oder eine Prüfung einen Fehler meldet. `anton:review-logs` ([Console Commands](console-commands.md)) prüft täglich und meldet sich nur bei Auffälligkeiten.
