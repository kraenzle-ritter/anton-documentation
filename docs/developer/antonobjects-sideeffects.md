How do methods of AntonObject affect other Objects
==================================================

delete()
--------

- update Dates of all Ancestors (if date extends minmax of parent)
- no Update of fulltext index
- no Update of private Attribute
- not Update of real_depth
- not Update of path

children are not affected

create()
--------

- update Dates of all Ancestors (if date is set an extends minmax of parent)
- update of fulltext index for actual object
- no update of private Attribute
- set real_depth of Object
- set path of Object

no children are not affected

update()
--------

- update Dates of all Ancestors (if date extends minmax of parent)
- update of fulltext index for actual object
- update of fulltext for descendants (if title has changed)
- update of private Attribute for descendants (if private has changed)
- no update of real_depth
- no update of path

children might be affected

move()
------

- update Dates of old and new Ancestors (if date extends minmax of parent)
- update of fulltext index for actual object and descendants
- no update of private Attribute (can be inconsistant)
- update of real_depth of actual object and descendants
- update of path of actual object and descendants
