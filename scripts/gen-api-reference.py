#!/usr/bin/env python3
"""
Erzeugt die API-Referenz von Lotte (docs/lotte/api.md und api.en.md) aus der
OpenAPI-Beschreibung `openapi.yaml` im Lotte-Repo (Standardpfad ../lotte) und
legt eine Kopie der Datei neben die Seite (docs/lotte/openapi.yaml), zum
Herunterladen.

Die Beschreibung lebt bei Lotte: ein Test dort (OpenApiCoversRoutesTest)
schlägt an, wenn sie und die Routen auseinanderlaufen. Dieser Generator hält
den Block zwischen den Markern der Seite aktuell — die Prosa darüber bleibt
Handarbeit.

Aufruf (aus dem anton-documentation-Repo):
    python3 scripts/gen-api-reference.py           # Seite und Kopie schreiben
    python3 scripts/gen-api-reference.py --check    # nur prüfen, Exit 1 bei Drift

YAML liest der Generator nicht selbst (die Doku hat keinen YAML-Parser in
requirements.txt): Er lässt PHP im DDEV von Lotte die Datei in JSON umsetzen,
mit der YAML-Erweiterung, die das DDEV-Image mitbringt. Ohne DDEV fällt
--check auf eine Strukturprüfung zurück und vergleicht nur die Kopie mit der
Datei im Lotte-Repo, falls es daneben liegt. Dokumentiert wird, was in Lotte
committet ist: Ist `openapi.yaml` dort geändert, gilt der Stand von HEAD.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
PAGE = DOCS / "docs" / "lotte" / "api.md"
COPY = DOCS / "docs" / "lotte" / "openapi.yaml"
LOTTE = DOCS.parent / "lotte"
SPEC = "openapi.yaml"

BEGIN = "<!-- BEGIN generated api reference -->"
END = "<!-- END generated api reference -->"
METHODS = ("get", "put", "post", "delete", "patch", "head", "options", "trace")

# Die Beschreibungen kommen aus openapi.yaml und sind englisch; uebersetzt
# werden nur die Beschriftungen des Blocks.
LABELS = {
    "de": {
        "version": "Version", "download": "OpenAPI-Beschreibung herunterladen",
        "access": "Zugang", "no_key": "ohne Schlüssel",
        "any_key": "Schlüssel, keine besondere Befugnis", "key_with": "Schlüssel mit Befugnis",
        "or": "oder", "parameters": "Parameter", "name": "Name", "in": "Ort",
        "required": "Pflicht", "description": "Beschreibung", "yes": "ja", "no": "nein",
        "request": "Anfrage", "field": "Feld", "type": "Typ", "responses": "Antworten",
        "status": "Status", "headers": "Kopfzeilen", "values": "Werte",
        "default": "Vorgabe", "schemas": "Datenstrukturen", "array_of": "Liste von",
        "body": "Inhalt",
        "where": {"path": "Pfad", "query": "Abfrage", "header": "Kopfzeile"},
    },
    "en": {
        "version": "Version", "download": "Download the OpenAPI description",
        "access": "Access", "no_key": "no key",
        "any_key": "key, no particular ability", "key_with": "key with ability",
        "or": "or", "parameters": "Parameters", "name": "Name", "in": "In",
        "required": "Required", "description": "Description", "yes": "yes", "no": "no",
        "request": "Request", "field": "Field", "type": "Type", "responses": "Responses",
        "status": "Status", "headers": "Headers", "values": "Values",
        "default": "Default", "schemas": "Data structures", "array_of": "list of",
        "body": "Body",
        "where": {"path": "path", "query": "query", "header": "header"},
    },
}


def pages() -> list[tuple[Path, str]]:
    found = [(PAGE, "de")]
    for path in sorted(PAGE.parent.glob("api.*.md")):
        locale = path.suffixes[-2].lstrip(".")
        if locale in LABELS:
            found.append((path, locale))
    return found


def committed_spec() -> str | None:
    """Der Text von openapi.yaml, wie er in Lotte committet ist; None, wenn
    das Repo fehlt. Eine geänderte Arbeitskopie wird gemeldet und übergangen."""
    path = LOTTE / SPEC
    if not path.is_file():
        return None
    try:
        status = subprocess.run(
            ["git", "-C", str(LOTTE), "status", "--porcelain", "--", SPEC],
            capture_output=True, text=True, check=True, timeout=30,
        ).stdout.strip()
        if status:
            print(f"Lotte: {SPEC} ist nicht committet — es gilt der Stand von HEAD.",
                  file=sys.stderr)
            return subprocess.run(
                ["git", "-C", str(LOTTE), "show", f"HEAD:{SPEC}"],
                capture_output=True, text=True, check=True, timeout=30,
            ).stdout
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    return path.read_text()


def parse(text: str) -> dict | None:
    """YAML -> dict über PHP im DDEV von Lotte; None, wenn es nicht erreichbar ist."""
    code = ("echo json_encode(yaml_parse(stream_get_contents(STDIN)), "
            "JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);")
    try:
        out = subprocess.run(
            ["ddev", "exec", "php", "-r", code], input=text,
            cwd=LOTTE, capture_output=True, text=True, check=True, timeout=120,
        ).stdout
        spec = json.loads(out)
    except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError):
        return None
    return spec if isinstance(spec, dict) and "paths" in spec else None


def cell(text) -> str:
    return " ".join(str(text or "").split()).replace("|", "\\|")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def ref_name(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


def resolve(spec: dict, node: dict) -> dict:
    """Ein $ref auf components aufgelöst, sonst der Knoten selbst."""
    seen = 0
    while isinstance(node, dict) and "$ref" in node and seen < 10:
        target = spec
        for part in node["$ref"].lstrip("#/").split("/"):
            target = target.get(part, {}) if isinstance(target, dict) else {}
        node, seen = target, seen + 1
    return node if isinstance(node, dict) else {}


def type_of(schema: dict, t: dict) -> str:
    """Der Typ eines Schemas als kurzer Text, mit Link auf benannte Strukturen."""
    if not isinstance(schema, dict):
        return ""
    if "$ref" in schema:
        name = ref_name(schema["$ref"])
        return f"[{name}](#schema-{slug(name)})"
    for key in ("oneOf", "anyOf"):
        if key in schema:
            return " \\| ".join(type_of(s, t) for s in schema[key])
    if "const" in schema:
        return f"`{schema['const']}`"
    kind = schema.get("type", "")
    kinds = kind if isinstance(kind, list) else [kind]
    parts = []
    for k in kinds:
        if k == "array":
            parts.append(f"{t['array_of']} {type_of(schema.get('items', {}), t)}".strip())
        elif k:
            parts.append(k)
    text = " \\| ".join(parts) or "object"
    if schema.get("format"):
        text += f" ({schema['format']})"
    return text


def notes(schema: dict, t: dict) -> str:
    """Beschreibung, Werte und Vorgabe eines Schemas in einer Zelle."""
    out = [cell(schema.get("description", ""))]
    if schema.get("enum"):
        out.append(f"{t['values']}: " + ", ".join(f"`{v}`" for v in schema["enum"]))
    if "default" in schema:
        out.append(f"{t['default']}: `{json.dumps(schema['default']) if not isinstance(schema['default'], str) else schema['default']}`")
    if schema.get("pattern"):
        out.append(f"`{cell(schema['pattern'])}`")
    return " · ".join(p for p in out if p)


def access(operation: dict, t: dict) -> str:
    security = operation.get("security")
    if not security:
        return t["no_key"]
    options = []
    for requirement in security:
        scopes = next(iter(requirement.values()), []) if requirement else []
        options.append(t["any_key"] if not scopes else
                       f"{t['key_with']} " + " + ".join(f"`{s}`" for s in scopes))
    return f" {t['or']} ".join(options)


def field_rows(spec: dict, schema: dict, t: dict, with_required: bool = True) -> list[str]:
    """Die Felder eines Objekt-Schemas, eine Ebene tiefer auch die Felder von
    Unterobjekten und von Listen aus Objekten. Ohne `with_required` fehlt die
    Spalte «Pflicht» (Antworten: dort steht jedes Feld)."""
    schema = resolve(spec, schema)

    def row(name: str, prop: dict, required: set) -> str:
        flag = f" {t['yes'] if name.rsplit('.', 1)[-1].removeprefix('[]') in required else t['no']} |" if with_required else ""
        return f"| `{name}` | {type_of(prop, t)} |{flag} {notes(prop, t)} |"

    rows = []
    for name, prop in (schema.get("properties") or {}).items():
        rows.append(row(name, prop, set(schema.get("required", []))))
        items = prop.get("items", {}) if prop.get("type") == "array" else {}
        if isinstance(items, dict) and "properties" in items:
            for sub, sub_prop in items["properties"].items():
                rows.append(row(f"{name}[].{sub}", sub_prop, set(items.get("required", []))))
        if prop.get("type") == "object" and "properties" in prop:
            for sub, sub_prop in prop["properties"].items():
                rows.append(row(f"{name}.{sub}", sub_prop, set(prop.get("required", []))))
    return rows


def field_head(t: dict, with_required: bool = True) -> list[str]:
    if with_required:
        return [f"| {t['field']} | {t['type']} | {t['required']} | {t['description']} |",
                "|---|---|---|---|"]
    return [f"| {t['field']} | {t['type']} | {t['description']} |", "|---|---|---|"]


def build_operation(spec: dict, path: str, method: str, item: dict, op: dict, t: dict) -> list[str]:
    anchor = "op-" + slug(op.get("operationId") or f"{method} {path}")
    lines = [f"\n#### `{method.upper()} {path}` {{#{anchor}}}\n"]
    if op.get("summary"):
        lines.append(f"**{cell(op['summary'])}.** " + cell(op.get("description", "")))
    else:
        lines.append(cell(op.get("description", "")))
    lines += ["", f"{t['access']}: {access(op, t)}"]

    params = [resolve(spec, p) for p in (item.get("parameters", []) + op.get("parameters", []))]
    if params:
        lines += ["", f"**{t['parameters']}**", "",
                  f"| {t['name']} | {t['in']} | {t['required']} | {t['type']} | {t['description']} |",
                  "|---|---|---|---|---|"]
        for p in params:
            where = t["where"].get(p.get("in", ""), p.get("in", ""))
            lines.append(f"| `{p.get('name')}` | {where} | "
                         f"{t['yes'] if p.get('required') else t['no']} | "
                         f"{type_of(p.get('schema', {}), t)} | "
                         f"{' · '.join(x for x in (cell(p.get('description', '')), notes(p.get('schema', {}), t)) if x)} |")

    body = op.get("requestBody")
    if body:
        body = resolve(spec, body)
        for media, content in (body.get("content") or {}).items():
            schema = content.get("schema", {})
            lines += ["", f"**{t['request']}** (`{media}`): {type_of(schema, t)}"]
            described = cell(resolve(spec, schema).get("description", ""))
            if described:
                lines += ["", described]
            rows = field_rows(spec, schema, t) if "$ref" not in schema else []
            if rows:
                lines += ["", *field_head(t), *rows]

    responses = op.get("responses") or {}
    if responses:
        lines += ["", f"**{t['responses']}**", "",
                  f"| {t['status']} | {t['description']} | {t['body']} |", "|---|---|---|"]
        for status in sorted(responses, key=str):
            r = resolve(spec, responses[status])
            text = cell(r.get("description", ""))
            headers = list((r.get("headers") or {}).keys())
            if headers:
                text += f" · {t['headers']}: " + ", ".join(f"`{h}`" for h in headers)
            bodies = []
            for media, content in (r.get("content") or {}).items():
                kind = type_of(content.get("schema", {}), t)
                bodies.append(f"`{media}`" + (f" {kind}" if kind and "json" in media else ""))
            lines.append(f"| {status} | {text} | {'<br>'.join(bodies)} |")
    return lines


def build_block(spec: dict, locale: str) -> str:
    t = LABELS.get(locale, LABELS["de"])
    info = spec.get("info", {})
    lines = [BEGIN, "",
             f"{t['version']} `{info.get('version', '')}` · [{t['download']}](openapi.yaml)"]

    tags = [tag["name"] for tag in spec.get("tags", [])]
    tag_text = {tag["name"]: tag.get("description", "") for tag in spec.get("tags", [])}
    by_tag: dict[str, list] = {name: [] for name in tags}
    for path, item in spec.get("paths", {}).items():
        for method in METHODS:
            if method in item:
                op = item[method]
                tag = (op.get("tags") or ["other"])[0]
                by_tag.setdefault(tag, []).append((path, method, item, op))

    for tag, ops in by_tag.items():
        if not ops:
            continue
        lines += ["", f"### {tag} {{#tag-{slug(tag)}}}", ""]
        if tag_text.get(tag):
            lines.append(cell(tag_text[tag]))
        for path, method, item, op in ops:
            lines += build_operation(spec, path, method, item, op, t)

    schemas = (spec.get("components") or {}).get("schemas") or {}
    lines += ["", f"### {t['schemas']} {{#schemas}}"]
    for name, schema in schemas.items():
        lines += ["", f"#### {name} {{#schema-{slug(name)}}}", ""]
        described = cell(schema.get("description", ""))
        if schema.get("properties"):
            if described:
                lines += [described, ""]
            with_required = "required" in schema
            lines += [*field_head(t, with_required), *field_rows(spec, schema, t, with_required)]
        else:
            lines.append(" · ".join(x for x in (type_of(schema, t), notes(schema, t)) if x))
    lines.append(END)
    return "\n".join(lines) + "\n"


def structure_ok(text: str) -> bool:
    m = re.search(re.escape(BEGIN) + r"(.*?)" + re.escape(END), text, flags=re.S)
    if not m:
        print(f"Marker {BEGIN} / {END} fehlen.", file=sys.stderr)
        return False
    ops = [ln for ln in m.group(1).splitlines() if ln.startswith("#### `")]
    if len(ops) < 10:
        print(f"Generierter Block wirkt beschädigt: nur {len(ops)} Operationen.", file=sys.stderr)
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Lotte's API reference from openapi.yaml.")
    parser.add_argument("--check", action="store_true", help="only check, exit 1 on drift")
    args = parser.parse_args()

    targets = pages()
    for path, _ in targets:
        if not path.is_file() or BEGIN not in path.read_text() or END not in path.read_text():
            print(f"Marker {BEGIN} / {END} fehlen in {path}", file=sys.stderr)
            return 2

    text = committed_spec()
    spec = parse(text) if text is not None else None

    if spec is None:
        if args.check:
            ok = all(structure_ok(p.read_text()) for p, _ in targets)
            same = text is None or (COPY.is_file() and COPY.read_text() == text)
            if not same:
                print(f"Kopie {COPY.name} weicht von Lottes {SPEC} ab.")
            print(f"Lotte: Struktur {'ok' if ok else 'fehlerhaft'} in {len(targets)} "
                  "Sprachfassung(en) (DDEV von Lotte nicht erreichbar — volle "
                  "Drift-Prüfung braucht es).")
            return 0 if ok and same else 1
        print("Lotte nicht erreichbar (Repo oder DDEV?) — nichts zu tun.", file=sys.stderr)
        return 2

    stale, written = [], []
    if not COPY.is_file() or COPY.read_text() != text:
        if args.check:
            stale.append(COPY)
        else:
            COPY.write_text(text)
            written.append(COPY)
    for path, locale in targets:
        old = path.read_text()
        block = build_block(spec, locale)
        new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block.rstrip("\n"),
                     old, flags=re.S)
        if new == old:
            continue
        if args.check:
            stale.append(path)
        else:
            path.write_text(new)
            written.append(path)

    if args.check:
        if stale:
            print("API-Referenz ist veraltet (" + ", ".join(p.name for p in stale) +
                  ") — `python3 scripts/gen-api-reference.py` ausführen.")
            return 1
        print(f"API-Referenz ist aktuell ({len(targets)} Sprachfassung(en)).")
        return 0
    print("API-Referenz aktualisiert: " + ", ".join(str(p) for p in written)
          if written else "Keine Änderung nötig.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
