# Logs

Anton records who did what to the holdings (holdings log) and who signed in or was turned away (security log). Looking through these logs is the archive's task. It is recorded as a **review**: who, when, which period (anton#670, anton#739; NDSA Co-4.1).

## The page

**Admin › Logs** holds the holdings log, the security log, the format validation and the reviews. All admins see the format validation; the other tabs are for superusers and, where k & r has enabled them, the archive's admins.

Below each log, the filtered period can be recorded as reviewed, with a note.

## The month in the report

Archives that receive the monthly report can have the previous month's logs in it:

- sign-ins (count, accounts), failed attempts and lockouts
- accounts created, deleted or with a new role, blocked ones included
- deletions of records and media and master downloads, by person
- refused access of signed-in accounts
- the findings of the daily log check, over the whole month

A month **must be acknowledged** when it has a finding, an account change, deletions or master downloads. Sign-ins alone do not count.

- Then the report contains the link **«Acknowledge review»**. Each recipient gets a link of their own, valid for 45 days and only for this period and this archive. Only the button on the opened page records the review, not opening it; mail filters open links to check them. The address is recorded and, if exactly one account has it, the account. Each recipient acknowledges once.
- After signing in, the same works under **Admin › Logs**: while the previous month is open, a notice says so. Under **Reviews** are the summary, links into both logs and the button **«Acknowledge review»**.
- If there was nothing to acknowledge, the report says so and Anton enters the month itself, as **automatic**. That keeps the series of reviews without gaps. Such an entry never counts as a review by a person.

The list of reviews shows for each entry how it came about: in Anton, by link or automatic.

## When to review

Once a month, when the report arrives. Worth a look: accounts nobody knows, new admin rights, deletions and downloads in unusual numbers, and accounts with many refusals. Whatever stands out belongs in the note and to k & r.

## On the command line

```bash
php artisan anton:doctor --logs --env=<slug>                       # previous month
php artisan anton:doctor --logs --month=2026-09 --env=<slug>       # a given month
php artisan anton:doctor --logs --only-if-actionable --mail=<address> --env=<slug>
```

`--only-if-actionable` sends the report only when the month must be acknowledged or a check reports an error. `anton:review-logs` ([console commands](console-commands.md)) checks daily and writes only when something stands out.
