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

### Roles
Loans can be managed by `editor`, `admin` and `loan_admin`.

<!-- 
Currently not yet possible: setting loan periods; that would probably require changing the data model for loans.
-->
