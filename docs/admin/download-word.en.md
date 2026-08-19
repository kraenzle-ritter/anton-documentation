# Word finding aids

The option to download finding aids for individual fonds can be built into the form (default, internal, detail): `module_word_download`. The download is, however, only displayed for the levels of description specified in the setting `level_of_description_ids_for_word_download`. For fonds: `[3]`

To include the logo, save it as `word_logo.png` in the `customers/{slug}/img` folder.

The footer (`word_footer`) and the header (`word_header`) can also be adapted in the settings.

## Custom Word export

For a Word export there must be a class in the `Controller\Word` directory which organises the download, for example `ArchivdatenWordEdxport`. The class has to be named like `${template}WordEdxport`. In the example, therefore, the template is «Archivdaten».

The export class must have one method which takes an integer as an argument and returns a `Symfony\Component\HttpFoundation\Response`:

```php
public function run($id) : Response
```

When the class is finished, you have to add the `ModuleWordDownload` to the default object form (via the GUI).

Then you can specify the levels of description that should offer the download, by adding an array of level-of-description IDs to the setting `level_of_description_ids_for_word_download`; and to the setting `word_export_template` you have to add the template (case-sensitive), in the example «Archivdaten».
