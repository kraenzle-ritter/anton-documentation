# Correspondences

The correspondence view groups letters into exchanges: it shows who corresponded
with whom, how many letters survive and over what period. From there, an
exchange can be browsed chronologically — going forward and back stays within
the same exchange.

The view is located at `/correspondences`. It is not linked in the navigation;
archives that use it add it to the menu themselves.

## An exchange comes about by itself

There is nothing to click and nothing to create. Anton derives the exchanges
**automatically from the [events](antonevents.md)**:

> If a unit of description carries a **creation date** event with actor A and a
> **reception** event with actor B, it counts as a letter from A to B.

The sending person is therefore recorded as the actor of the creation event, the
receiving person as the actor of the reception event. As soon as enough such
pairs exist, the exchange appears in the list. Conversely: anyone wishing to use
the view has to set both events consistently when cataloguing — a letter lacking
the reception event appears nowhere.

The level of description is irrelevant.

!!! note "Minimum number of letters"
    A pair of actors only appears above a minimum number of letters — five by
    default. Isolated letters are therefore left out. The threshold can be set
    per archive but cannot be changed in the admin area; with Anton as a
    Service, k & r is responsible for it.

## Who this is worthwhile for

The view is aimed at archives with letter holdings — personal papers,
collections of scholarly correspondence. It is present in every installation but
remains empty as long as cataloguing does not follow this pattern. For an archive
without letters it is of no use.
