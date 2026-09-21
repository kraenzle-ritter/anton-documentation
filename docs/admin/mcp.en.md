# AI assistants (MCP)

Anton offers its public catalogue as an **MCP server**: a user connects an AI
assistant (Claude, ChatGPT, Copilot …), which then researches the catalogue on
its own. The user's side is described in
[Connecting AI assistants](../user/mcp.md).

The direction is the reverse of [AI-assisted cataloguing](ai-cataloging.md):
Anton calls no language model, needs no key and incurs no model costs. The
assistant belongs to whoever connects it.

## Activation

The interface is **off by default**. Two settings must be set:

1. **`mcp_enabled`** — the switch for the interface. Editable by admins under
   **Settings**. The setting is created by `anton:update`; before that it does
   not appear in the list.
2. **`public_access`** — the catalogue must be accessible without login. If it
   is not, the interface stays closed even with `mcp_enabled` set: whoever sees
   nothing in the browser should not see more through an assistant.

While either is missing, `/api/mcp` answers 404.

The interface can be checked from the command line:

```bash
curl -s -X POST https://archive.example.ch/api/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

The answer lists six tools.

## What is returned

The interface is **anonymous** and shows the public view only — the same rule
as for guests in the browser, with no separate permission check alongside it:

- Descriptions with status «Final» (or no status) whose **blocked** field is not set.
  Withheld records leave no trace among child records or in counts.
- The fields of the **external detail form** — what the public detail page
  shows is what the interface returns.
- Documents and their full text only once the
  [protection period](protection-periods.md) has expired and the media are not
  blocked indefinitely.
- No private actors.

An account makes no difference: a logged-in staff member also sees only the
public view through the interface. Access to internal holdings through an
account is planned for a later stage.

!!! warning "Before switching it on"
    An assistant queries in minutes what would take a person weeks. What is
    public today only in theory — a forgotten draft set to «Final», a text field
    in the external form that was meant to be internal — will actually be read.
    Before switching on, it is worth looking at the public detail page of a few
    records and at the fields of the external detail form.

## Limiting requests

**60 requests per minute** are allowed per address; above that the interface
answers 429. A research question usually needs a few dozen calls. The value is
in `config/ratelimiting.php` under `mcp`; `0` removes the limit.

## Operating behind Anubis and the cookie gate

An MCP client sends single requests without a cookie and without a browser —
exactly the pattern Anubis and the cookie gate turn away. The path `/api/mcp`
must therefore be routed past both, as the OAI endpoint is. Otherwise the switch
is set and the interface is still unreachable.
