# Fields

All fields must have a name.

## Attributes

### `@name`

Rules: `string`

Description: There must be an attribute or an accessor in the model which returns the name of the model. 

### `@type` 

Rules: `nullable|string|in:display,...`

Default: Display

Description: Contains a field type like textarea, input ...


### `@label`

Rules: `nullable|string` 

Description: Contains a key from `resources/lang/messages.php`. 

`@labelCssClass` 

Rules: `nullable|string` 

Default: `col-md-2`

Description: Contains a CSS class für the label.

`@fieldCssClass`

Rules: `nullable|string` 

Default: `col-md-10`

Description: Contains a CSS class für the field div.


## display

Shows information. Standard field for `detail` and `detail_intern` forms.

- required: `name`, `label` 
    
!!! note
    `name` must correspond to an attribute or accessor of the model

## module_actors

Displays actors as descriptors.

- uses: `$model->actors->links()`
- required: `label`

## module_event

Displays an antonevents of the same type. 

- uses: 
    - `$model->hasChrildren()`
    - `$model->creationDateLabel`
    - `model->antonevents`
- required: 
    - (string) `eventtype` ("creation"), 
    - `label`
    - `modus`
- restricted to: `antonobjects` (other entities dont have children)

## module_keywords

Displays keywords as descriptors.

- uses: `$model->keywords->links()`
- required: `label`

## module_permalink

Shows a permanent link with endpoint and id (eg. "/actors/3")
 
- uses: `$endpoint`, `$model->id`
- required: `label`

## module_places

Displays places as descriptors.

- uses: `$model->places->links()`
- required: `label`

## section

Separates and titles information areas.

- required: `label`  
- options: `with_save_button`

## textarea
