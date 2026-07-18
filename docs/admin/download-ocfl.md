# OCFL Download

Anton kann Bestände zusätzlich zu DIP/BagIt im [Oxford Common File Layout
(OCFL) v1.1](https://ocfl.io/1.1/spec/) exportieren. OCFL ist eine
Storage-Spezifikation für die Langzeitarchivierung: versioniert,
prüfsummen-gesichert, Content-Adressing, self-describing. Mehrere
Schweizer Langzeitarchive — namentlich UB Basel und das DLZA — erwarten
OCFL für die Übergabe.

Verfügbar seit **v0.66.0**.

## Zwei Modi

| Modus | Knopf in der Detail-Ansicht | Inhalt |
|---|---|---|
| **Einzel-Objekt** | "OCFL" | Ein OCFL Object Root mit den Medien dieses Datensatzes |
| **Subtree (Bestand)** | "OCFL (Bestand)" | Ein OCFL Storage Root (HashedNTupleStorageLayout) mit je einem Object pro Descendant |

Beide Modi liefern ein ZIP zum sofortigen Download. Pro OCFL-Version (v1)
enthält jedes Objekt:

- `data/content/<datei>` — die Original-Mediendateien
- `metadata/ead.xml` — vollständige EAD-Beschreibung
- `metadata/dc/<datei>.xml` — DublinCore pro Medium
- `metadata/anton-import.json` — Round-Trip-Payload im Anton-Import-Format

Die Object-ID ist `urn:anton:{tenant}-objects-{id}` (entspricht dem
`full_id` des AntonObjects, mit URN-Präfix).

## Sichtbarkeit der Knöpfe konfigurieren

Wie bei DIP/Word gehören die OCFL-Knöpfe ins Modul `module_word_download`
der Detail-internal-Form. Die Sichtbarkeit pro Verzeichnungsstufe steuern
zwei Settings:

| Setting | Default | Empfohlen |
|---|---|---|
| `level_of_description_ids_for_ocfl_download` | leer | `[3, 4, 5, 6]` (Fonds, Series, File, Item) |
| `level_of_description_ids_for_ocfl_subtree_download` | leer | `[3]` (nur Fonds) |

Die Standard-Defaults sind **bewusst leer** — OCFL ist nur für Archive
sinnvoll, bei denen die empfangende Stelle das Format erwartet. Aktivieren über
`/settings` oder via Tinker.

## Adressfeld in der OCFL-Inventory

Jede OCFL-Version trägt im `inventory.json` einen `user.address`-Eintrag
zur Provenienz. Anton füllt ihn mit dem Tenant-Setting
`repository_email` (als `mailto:` URI), Fallback ist eine stabile URN
`urn:anton:tenant:{slug}`. Damit landen keine personenbezogenen
E-Mail-Adressen im Archivpaket, aber das empfangende Archiv hat einen
Kontaktpunkt.

## Validierung

Jeder Export läuft durch den offiziellen OCFL-Validator des
[`ottosmops/ocfl`](https://packagist.org/packages/ottosmops/ocfl)-Pakets
und validiert alle 55/12/13 OCFL-Fixtures der Spec.

Eine externe Validierung ist über das CLI möglich:

```bash
# OCFL-Object validieren
ddev exec vendor/bin/ocfl validate <pfad-im-container>

# Storage-Root listen
ddev exec vendor/bin/ocfl list <pfad-im-container>

# Object-Inhalt anzeigen
ddev exec vendor/bin/ocfl info <pfad-im-container>
```

Exit-Codes: `0` valid, `1` invalid, `2` Usage-Fehler, `3` Runtime-Fehler.

## Wann OCFL, wann DIP?

| Empfangende Stelle | Format |
|---|---|
| Klassisches Endarchiv erwartet BagIt-Container | **DIP** |
| Langzeitarchiv mit OCFL-Anforderung (UB Basel §7, DLZA) | **OCFL** |
| Forschungs-Repositorium, das OCFL versteht | **OCFL** |
| Lokale Übergabe mit Word-Findbuch | **DIP** |

Beide laufen additiv — DIP bleibt vollständig erhalten.

## Routen

- `GET /objects/ocfl/{id}` — Einzel-Objekt-Export (ZIP)
- `GET /objects/ocfl-subtree/{id}` — Subtree-Export (ZIP)

Beide hinter `admin`-Middleware. Keine Web-Form, direkter Download.
