# Markdown

In Anton, the texts in the text fields can be formatted using the markup language [Markdown](https://en.wikipedia.org/wiki/Markdown). Markdown is simple and quick to learn. The text data also stays relatively clean, because only very few additional characters and conventions are needed to enable the formatting.

[ [Detailed information](https://www.markdownguide.org/basic-syntax/) ]


The most important formatting options in Anton:

### New lines, new paragraphs

New lines are produced with two spaces at the end of a line.

New paragraphs by means of an empty line.

### Headings

Headings can be created with `#` at the beginning of a line, where one `#` followed by a space marks a first-level heading, two `##` followed by a space a second-level heading, and so on:

```markdown
# Heading level 1
## Heading level 2
```
Produces:
<div class="myframe">
<h1>Heading level 1</h1>
<h2>Heading level 2</h2>
</div>

### Lists

Lists can be created with `-` or `*` at the beginning of a line, or, if numbered, with `1.`, `2.` followed by a space. Sub-items are also possible and are then indented.

```markdown
- Greek philosophers
    - Aristotle
    - Plato
- Roman philosophers
    - Cicero
```

### External links

The text to be linked is placed in square brackets. The target of the link follows in round brackets.

```markdown
[This text will be linked](https://link_target.ch)
```

### References within Anton

References within Anton work like links. The respective relative URL is given as the target:

```markdown
[Anton](/actors/2)
```

The reference then leads to the actor with ID 2. Units of description can be
linked in much the same way; the target is then `/objects/123`.

### Reference codes are linked automatically

As a rule, reference codes do not have to be linked by hand at all: if a
reference code is mentioned in a text field, Anton recognises it in the
**detail view** and turns it into a link to the search. In the edit view the
text remains untouched so that it stays editable.

!!! note "Not in every archive"
    Recognition relies on a search pattern that is stored per archive. If none
    is configured, reference codes in the text remain unlinked.

### Emphasis

For emphasis, `*italic*` (*italic*) or `**` (**bold**) or `***` (***bold and italic***) can be used.
