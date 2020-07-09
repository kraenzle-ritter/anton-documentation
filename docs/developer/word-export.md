# Word Export

For a Word Export there must be a Class in the `Controller\Word` directory, which organizes the download, for example `ArchivdatenWordEdxport`. The class must be named like `${template}WordEdxport`. So in the example the template is "Archivdaten". 

The export class must have one method which takes as an argument an integer and returns a `Symfony\Component\HttpFoundation\Response`:

```php
public function run($id) : Response
```

When the class is done you have to add the `ModuleWordDownload` to the default objectform (via the gui). 

Then you can specify the level_of_descriptions, which should offer the download by adding an array of level_of_description_ids to the setting `level_of_description_ids_for_word_download` and to the setting `word_export_template` you have to add the template (casesensitive), in the example "Archivdaten". 
