# Zürcher Gemeinden (Dürnten, Lindau, Opfikon)

## Import nach Dimag funktioniert wird aber in Inge nicht finalisiert und nicht in der Inge DB gespeichert.

Dateien finalisieren (in Dimag mit Status 20 «Abgeschlossen» versehen, in Inge DB speichern)

Im Inge-Verzeichnis:
```bash
art inge:sync --archive opfikon --aid opfikon-media-445 -vv
```

Im Anton-Verzeichnis:
```bash
art media:check --env opfikon -vv --levels 5 --fix-cloud-status
```
