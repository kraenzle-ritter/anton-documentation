## Lending objects

### Lending out objects
In order to see loans on an object and to be able to mark an object as lent out, the loan field (id: 47) has to be part of the form in use.

After clicking the plus, a loan to a user can be entered. In doing so, that user is linked to the object. The day of the loan is entered as well. Further information can be recorded in a comment (purpose of the loan, expected return date).

### Return of objects
Only on return is the «to» date filled in. This completes the loan.

### List of open loans
In the admin area there is a list of open loans (`/loans`), that is, of loans that have no return date. From there it is possible to jump to the users, in order to record a user's loans as returned, for example, or to the objects lent out.

### Display for individual users
For individual users (`/users/{user_id}`), the loans are displayed in a table.

### On which levels a loan is possible
The `level_of_description_ids_for_loans` setting determines the levels of
description on which the loan module is offered. What is lent is a physical
unit, not a level of arrangement — without this restriction a whole fonds, or
the archive itself, could be «lent», which marked every subordinate entry as on
loan.

An **empty** value means: every level. That is the state of existing
installations, and it stays that way until somebody enters a value. New
installations are given file and item (`[5, 6]`). An archive that regularly
lends whole fonds adds the `3`.

A record that already carries loans keeps its module whatever this setting says
— hiding it would not undo the loan, only make it unreachable.

### Roles
Loans can be managed by `editor`, `admin` and `loan_admin`.

<!-- 
Currently not yet possible: setting loan periods; that would probably require changing the data model for loans.
-->
