# Word Findbücher

Die Möglichkeit, Findbücher zu einzelnen Beständen herunterzuladen, können in das Formular (default, internal, detail) eingebaut werden: `module_word_download`. Der Download wird aber nur für die Verzeichnungsstufen angezeigt die im Setting `level_of_description_ids_for_word_download` angegeben sind. Für Bestände: `[3]`

Um das Logo einzubinden, ist im `customers/{slug}/img` Ordner das Logo als `word_logo.png` abzuspeichern.

Ausserdem kann in der Einstellungen der Footer (`word_footer`) sowie der Header `word_header` angepasst werden.

## Eigener Word-Export

Für einen eigenen Word-Export braucht es im Verzeichnis `Controller\Word` eine Klasse, die den Download organisiert, zum Beispiel `ArchivdatenWordEdxport`. Die Klasse muss nach dem Muster `${template}WordEdxport` benannt sein; im Beispiel lautet das Template also «Archivdaten».

Die Export-Klasse muss eine Methode besitzen, die eine ganze Zahl entgegennimmt und eine `Symfony\Component\HttpFoundation\Response` zurückgibt:

```php
public function run($id) : Response
```

Ist die Klasse fertig, wird das `ModuleWordDownload` über die Oberfläche in das Standard-Objektformular aufgenommen.

Anschliessend lässt sich festlegen, für welche Verzeichnungsstufen der Download angeboten wird: Dazu kommt ein Array mit den Ids der Verzeichnungsstufen in die Einstellung `level_of_description_ids_for_word_download`, und in die Einstellung `word_export_template` das Template (Gross- und Kleinschreibung beachten) — im Beispiel «Archivdaten».
