# Connecting AI assistants (MCP)

An AI assistant such as Claude or ChatGPT can research an archive's public
catalogue directly: survey the holdings, search, read records, move through the
hierarchy and quote from the full texts of digitised documents. The connection
uses the **Model Context Protocol (MCP)**, an open standard supported by the
common assistants.

The assistant then answers from the catalogue rather than from what it picked
up in training — with the reference code and a link for every record it relies
on.

!!! note "Only where the archive has switched it on"
    The interface is enabled per archive and is available only for archives
    with a public catalogue. If the address answers «Not Found», it is not in
    operation there.

## What the assistant sees

Exactly what is visible in the browser without logging in: descriptions with
status «Final» that are not [blocked](access.md). Documents and their full text
only once the protection period has expired. Private actors, internal text
fields and blocked media are left out.

There is no login, and none is needed — even with an Anton account, the
interface shows only the public view.

!!! warning "What the assistant reads, its provider reads too"
    Everything the interface returns goes to the assistant's provider
    (Anthropic, OpenAI, Microsoft …). It is public data only — but worth
    knowing.

## Address

```
https://<archive address>/api/mcp
```

For example `https://archive.example.ch/api/mcp`.

## Setting up

### Claude (claude.ai and Claude Desktop)

**Settings → Connectors → Add custom connector**, give it a name (the archive's
name, say) and enter the address. No authentication needs to be configured.
Whether custom connectors are available depends on the plan.

### Claude Code

```bash
claude mcp add --transport http archive https://archive.example.ch/api/mcp
```

### ChatGPT, Microsoft Copilot and others

Any assistant that can connect to a remote MCP server over «Streamable HTTP»
without authentication will work. Where the setting lives differs by product
and plan; the provider's instructions are authoritative.

## What the assistant can do with it

| Tool | Purpose |
|---|---|
| `holdings_overview` | What does the archive hold? Archives, record groups and fonds with reference code, title and date |
| `search_records` | Search the descriptions — titles, text fields, actors, places, keywords |
| `search_media_texts` | Search the full texts of digitised documents; returns passages around each hit |
| `read_record` | One record with all public fields, linked authority data and documents; the full text page by page |
| `navigate_tree` | Parent and child records, neighbours |
| `lookup_authority` | Actors, places and keywords with authority references (GND, Wikidata …) and their linked records |

The assistant picks the tools itself. Just ask:

- «What does the archive contain?»
- «What did the Maurmer Post report about the founding of FC Maur? Quote the passages.»
- «Which records concern the building of the school house, and where are they in the holdings?»

## Limits

- **Search terms shorter than three letters** are poorly indexed. Have
  abbreviations searched as a phrase together with a longer word.
- **Text recognition (OCR) is not error-free.** If a word finds nothing, a
  prefix with `*` or a different spelling often helps.
- **Read only.** Ordering, editing or creating is not possible through the
  interface.
- **Number of requests:** 60 per minute per address. A research question
  usually needs a few dozen.

The assistant's answers remain its own. What counts is the linked record — when
in doubt, check there.
