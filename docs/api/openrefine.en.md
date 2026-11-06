# Matching names with OpenRefine

Anton offers a matching service for actors following the [Reconciliation API](https://reconciliation-api.github.io/specs/latest/). It lets you assign names from a table in [OpenRefine](https://openrefine.org/) to an archive's records.

## Setting up

1. In OpenRefine, in the column with the names, choose **Reconcile → Start reconciling**.
2. Choose **Add Standard Service** and enter the address of the archive:

    ```
    https://<archive>/api/actors/reconcile.json
    ```

3. Choose a type such as **Person** or **Körperschaft**, or match without a type, and press **Start Reconciling**.

Only the actors of this archive are searched. A public archive needs no sign-in; if it is not public, the service answers 401.

## Result

For each row Anton proposes records with a score from 0 to 100. Only an unambiguous, exact top hit is matched automatically; all other rows are decided in OpenRefine. The name of a proposal leads to the record's page.

## Limits

- At most 50 queries per request and 25 hits per query, 5 if not specified.
- The service covers actors only, not places and keywords.
- It compares the name only: other columns such as life dates or a GND number are not used.
- Fetching data from Anton into the table (Data Extension) and suggestions while typing (Suggest) do not exist.

## Querying directly

```bash
curl -X POST https://<archive>/api/actors/reconcile \
  --data-urlencode 'queries={"q0":{"query":"Muster, Anna","type":"person","limit":3}}'
```
