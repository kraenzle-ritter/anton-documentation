# Language configuration in Anton

## Overview

Anton supports multilingual (DE, EN, FR and IT) content for various fields (title, text fields, keywords, etc.). This document describes the available settings and gives recommendations for the configuration.

## Kinds of language

Anton has two different concepts of "language":

1. **UI language** (`app.locale`): the language of the user interface (menus, labels, messages)
2. **Content languages** (`locales`): the languages in which archival data can be recorded

## System setting: `locales`

| Property | Value |
|------------|------|
| Type | Array |
| Scope | `localisation` |
| Example | `["de", "en", "fr"]` |

Defines which languages are available for translatable fields.

**Important:** the **first language in the array is the main language** and is used as a fallback when no value exists for another language.

**Translatable fields:**
- Title (AntonObject)
- Note fields
- Keywords (name, use_for)
- Places (description)

## User setting: `show_all_locales_in_edit_forms`

| Property | Value |
|------------|------|
| Type | Boolean |
| Default | `false` |
| Location | Profile → Settings → Editing |

**When activated (`true`):**
- In edit forms, **separate input fields for each configured language** are displayed
- Example: title (DE), title (EN), title (FR)

**When deactivated (`false`):**
- Only **one input field** is displayed (for the current UI language)
- Values already entered in other languages are shown for information but are not editable

## Language on import

An import has its own **content language**, independent of the language of the interface. It determines which language titles, text fields and newly created authority data are written in — and in which language Anton searches for existing actors and places.

Up to v0.86.x, the import followed the interface language; anyone who had set English created English titles with German text. Since **v0.87.0** the language is chosen deliberately and is visible before the run.

Translatable fields can also be addressed **per language** in the import — `title_de`, `title_fr`, `scopecontent_it`. Multilingual titles can thus be imported, and the update table of a multilingual archive goes out and comes back in without loss.

Both are described in detail under [Import → Content language of the import](import.md#content-language-of-the-import).

## Fallback behaviour

If no value exists for the current language:
1. Anton uses the value of the **first language** from `setting('locales')`
2. If nothing is there either: it searches the further configured languages

In the detail view, editors are shown which language the value comes from (e.g. "Title (DE)").

## Recommendation: one language per field

**Our recommendation is to store only one language per field** (`show_all_locales_in_edit_forms = false`).

### Reasons

1. **Consistency**: if titles are recorded in several languages, all translations have to be maintained. When the original changes, the translations are often not updated.

2. **Archival standards**: in archival practice, documents are normally described in their original language, not translated.

3. **Searchability**: the full-text search (`full_text` column) contains all language versions. That can lead to confusing hits.

4. **Maintenance effort**: multilingual data maintenance requires considerably more resources.

### When multilingualism makes sense

- Archives with an international audience (scholarly collections, for example)
- Holdings with documents in various languages, where the title is recorded in the original language
- Institutions with a legal obligation to be multilingual

## Configuration examples

### Monolingual archive 

```php
// Setting: locales
["de"]
```
```php
// UserSettings
show_all_locales_in_edit_forms: false
```

### Bilingual archive (DE/FR)

```php
// Setting: locales
["de", "fr"]
```
```php
// UserSettings (as required)
show_all_locales_in_edit_forms: false  // Recommended
```

### International archive

```php
// Setting: locales
["en", "de", "fr", "it"]
```
```php
// UserSettings (for translators)
show_all_locales_in_edit_forms: true
```
