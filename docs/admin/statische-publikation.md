# Statische Publikation & Round-Trip

Anton kennt zwei **self-contained** Export-Pakete, die einen ganzen
(Teil-)Bestand samt Medien in *eine* ZIP-Datei packen — ohne dass zur
Anzeige oder Wiederherstellung eine laufende Anton-Instanz nötig ist:

- **A+ Static Bundle** — der CIDOC-CRM/RiC-O-Graph + Medien-Derivate,
  **öffentlich-sicher** und offline-hostbar. Gedacht als *Publikation*.
- **Nativer Round-Trip** — das Anton-eigene Format + Master-Medien,
  **verlustfrei und wieder importierbar**. Gedacht als *Backup / Umzug*.

Leitidee: **Anton ist der Editor, das Paket ist die Auslieferung.** Kleine
Archive können damit ihren Bestand pflegen und das Ergebnis kostenlos als
statische Website (z. B. GitHub Pages) veröffentlichen — ohne Server,
ohne Datenbank, ohne laufende Kosten.

!!! info "Kurz: welches Paket wofür?"
    - **Öffentlich zeigen / an Portale liefern** → **A+ Static Bundle**
      (Privates ist herausgefiltert, Standards-konform).
    - **Sichern / auf eine andere Anton-Instanz umziehen** → **Nativer
      Round-Trip** (verlustfrei, enthält aber private Daten → *nicht*
      öffentlich hosten).

---

## A+ Static Bundle (CIDOC CRM + RiC-O)

Ein ZIP mit dem serialisierten A+-Graphen als `data.jsonld` an der Wurzel,
den kopierten Medien-Derivaten (`thumb`/`web`) unter `media/{id}/…` und
einem `manifest.json` mit einer Transparenz-Übersicht. Die Medien-Verweise
im Graphen sind **bundle-relative Pfade** (`media/123/web.jpg`), damit das
Paket überall rendert — von der Festplatte, von GitHub Pages, aus einem
Unterverzeichnis.

```
bundle.zip
├── data.jsonld          ← CIDOC/RiC-O-Graph (JSON-LD)
├── manifest.json        ← Format, Medien-Anzahl, Transparenz-Summary
└── media/{id}/…         ← thumb/web-Derivate
```

**Erzeugen:**

```bash
# CLI — schreibt <identifier>-bundle.zip nach storage/rdf/
php artisan anton:export-rdf --env=<slug> --root=<id> --profile=a-plus-bundle
```

Oder in der UI unter **Daten-Export → RDF**, Spalte *„A+ Bundle
(statisch)"*. Das fertige ZIP erscheint in der Dateiliste zum Download.

**Öffentlich-sicher:** Es gilt derselbe Datenschutz-Filter wie beim
RDF-Export — private Objekte, `private_media` und private Notiztypen
(`internal_note`, `archivists_notes`, `comment`) werden weggelassen. Das
`manifest.json` zählt transparent, wie viel gefiltert wurde und welche
Konversionen fehlten, damit man das Paket vor dem Publizieren prüfen kann.

Details zum A+-Graphen selbst: siehe
[RDF-Export](download-rdf.md).

---

## Nativer Round-Trip (anton-import-format)

Ein ZIP mit dem Bestand als **`anton-import-format`-Dokument**
(`metadata.json`) plus den **Master-Mediendateien**. Es ist die
verlustfreie Gegenstück zum (bewusst verlustbehafteten) CIDOC-Paket: was
Anton hier exportiert, kann Anton **wieder einlesen**.

```
paket.zip
├── metadata.json        ← anton-import-format v0.4 (JSON)
└── media/{id}/…         ← Master-Dateien (Originale)
```

**Erzeugen und Wiederherstellen:**

```bash
# Export eines Teilbaums
php artisan anton:export-native --env=<slug> --root=<id> --out=/pfad/paket.zip

# Wieder einlesen (in dieselbe oder eine andere Anton-Instanz)
php artisan anton:import-native /pfad/paket.zip --env=<zielslug>

# Bestehende Datensätze überschreiben statt überspringen
php artisan anton:import-native /pfad/paket.zip --env=<zielslug> --update
```

**Was es verlustfrei trägt:** Objekte (inkl. `uuid`, `formset_id`, alle
Sprach-Varianten von Titel/Label), Hierarchie (über die Eltern-`uuid`),
Events, Deskriptoren, **Notizen aller Datensätze** (auch private,
Biografien), termselect-Werte und die Medien-Identität. Es wendet **keinen
Datenschutz-Filter** an — es ist ein Backup, keine Publikation.

**Identität über `uuid` (portabel).** Objekte *und* Normdaten
(Actor/Place/Keyword) tragen eine stabile, instanz-unabhängige `uuid`. Beim
Re-Import wird darüber wieder verankert:

- unbekannte `uuid` → neuer Datensatz,
- bekannte `uuid` → übersprungen (mit `--update` aktualisiert),
- gleiche `uuid` in zwei Beständen → *ein* Datensatz (keine Dubletten).

Dadurch funktioniert der Round-Trip auch **zwischen verschiedenen
Anton-Instanzen**: ein Bestand aus Instanz A landet in Instanz B unter
seinen Original-`uuid`s; ein späterer erneuter Import aktualisiert dieselben
Datensätze statt sie zu duplizieren.

!!! warning "Enthält private Daten"
    Der native Export ist ein Backup und trägt bewusst **auch private
    Objekte, private Medien und interne Notizen**. Er ist **nicht** zum
    öffentlichen Hosten gedacht — dafür ist das A+ Static Bundle da.

Das zugrunde liegende Format ist als eigenes, versioniertes Paket
gepflegt: [`kraenzle-ritter/anton-import-format`](https://github.com/kraenzle-ritter/anton-import-format).
Dasselbe Format konsumiert auch der Excel-Import und die agate-SIP-Pipeline.

---

## Konkreter Vergleich: anton-format ↔ CIDOC

Beide Pakete beschreiben denselben Bestand und packen dieselben Medien —
aber mit gegensätzlichem Zweck. Das eine ist **Standard-Interop** (breit
konsumierbar, semantisch reich, verlustbehaftet), das andere ist
**Anton-native Treue** (verlustfrei, wieder-importierbar, einfach).

| | **anton-format** (nativer Round-Trip) | **CIDOC A+ Bundle** |
|---|---|---|
| **Zweck** | Backup · Restore · Umzug zwischen Anton-Instanzen | Publikation · Interop · statische Anzeige |
| **Basis** | `anton-import-format` v0.4 (JSON) | CIDOC CRM 7.1 + RiC-O 1.1 (JSON-LD) |
| **Standardisiert** | Nein (Anton-eigenes Schema) | Ja (internationale Ontologien) |
| **Verlustfrei** | **Ja** — `uuid`, `formset_id`, alle Locales, alle Notizen, termselect, Rohwerte | Nein — Discovery-Sicht; kein `formset_id`, keine Rohwerte |
| **Wieder importierbar** | **Ja** (`anton:import-native`, uuid-anchored) | Nein |
| **Privatsphäre** | Enthält Privates (Backup!) → **nicht öffentlich hosten** | Privates gefiltert → **für öffentliches Hosting gedacht** |
| **Struktur** | Flach & Anton-nah: `entries[]` mit `title`/`identifier`/`events`/`notes`/`files` | Graph aus CRM/RiC-Knoten & -Properties |
| **Rendern in einem JS-Viewer** | **Einfach** (direkt les-/mapbar) | **Aufwändiger** (Ontologie-Traversierung nötig) |
| **Medien** | Master-Dateien (Originale) | `thumb`/`web`-Derivate |
| **Portabilität** | `uuid`-Identität, auch cross-tenant | bundle-relative Locatoren, offline |
| **Zielgruppe** | Anton-Betreiber:innen | Aggregatoren (Europeana, Memobase) · eigener statischer Viewer |
| **Kommando** | `anton:export-native` / `anton:import-native` | `anton:export-rdf --profile=a-plus-bundle` |

**Die Kernaussage:** CIDOC ist die *standardisierte, öffentlich-sichere*
Sicht — ideal, um Daten an Portale zu geben oder standardkonform ins Netz
zu stellen, aber sein JSON-LD ist für einen selbstgebauten Viewer
aufwändiger zu verarbeiten. Das anton-format ist *einfach zu rendern und
verlustfrei*, trägt aber private Daten und ist kein anerkannter Standard.

---

## Vision: kleine Archive statisch & kostenlos publizieren

Der eigentliche Zweck dieser Pakete: **kleine Projekte sollen Anton als
Editor nutzen und ihren Bestand als statische Website veröffentlichen** —
ohne Server, ohne Datenbank, quasi kostenlos (GitHub Pages, Netlify, ein
USB-Stick).

Der geplante nächste Schritt ist eine **kleine, eigenständige statische
Viewer-Anwendung** (eigenes Projekt): ein reiner Browser-Client, der ein
exportiertes Paket lädt und den Bestand als navigierbare Website darstellt
— Baum, Detailseiten, Medien, Volltext-Suche client-seitig.

**Welches Format soll dieser Viewer konsumieren?** Die beiden Pakete oben
markieren die Enden eines Spektrums:

- **A+ Bundle (CIDOC)** — öffentlich-sicher und standardkonform, aber der
  Graph ist zum Rendern sperrig.
- **anton-format** — trivial zu rendern, aber es enthält private Daten und
  ist kein Standard.

Für einen *öffentlichen* Viewer will man beides zugleich: **einfach zu
rendern *und* datenschutz-gefiltert**. Das legt für das Viewer-Projekt einen
dritten, schlanken **Publikations-Export** nahe — flaches, gut lesbares JSON
wie das anton-format, aber mit demselben Datenschutz-Filter wie das A+
Bundle und nur Display-Derivaten (`thumb`/`web`). Er würde die Einfachheit
des nativen Builders mit dem Privacy-Filter der Publikation verbinden.

Bis dieser dedizierte Publikations-Export existiert, ist das **A+ Static
Bundle die richtige öffentliche Grundlage** — es ist bereits offline-hostbar
und privatsphäre-sicher; der Viewer müsste „nur" den JSON-LD-Graphen lesen.

!!! note "Status"
    A+ Static Bundle und nativer Round-Trip sind implementiert und getestet.
    Der dedizierte, schlanke Publikations-Export und die statische
    Viewer-Anwendung sind als **eigenes Folgeprojekt** vorgesehen.
