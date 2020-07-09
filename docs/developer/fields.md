# Fields

## display

Shows information. Standard field for `detail` forms.

- required: `label`, `name`  
    
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
