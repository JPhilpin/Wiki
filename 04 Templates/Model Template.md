---
title: ""
summary: ""
slug: 
permalink: /
type: model
origin: 
source: 
status: stub
workflow: raw
updated: 
tags: []
aliases: []
---

## Working definition

One paragraph. What the model describes and what it makes visible.

## Provenance

Borrowed, bent or built - and from whom. Delete this heading when origin is built and there is nothing to declare.

## The model

The substance. What the parts are, how they relate, what changes when you see through it.

## Relationships

### Related

- [[Related Page]]

---

## Field notes

Delete this section when the page is written.

**origin** - one of three, always set.

| Value | Test | Example |
|---|---|---|
| `borrowed` | The author reads it and says "that is mine" | DIKW |
| `bent` | The author reads it and says "that is mine, but that is not what I said" | DIKIWI |
| `built` | The author has nothing to recognise | The Four Es |

Bent is a property of the model, not the page. Framing, commentary and wiring into the Glossary do not bend anything. Changing what the thing is does.

**A bent page must link to its borrowed parent.** If the parent does not exist, either write it or the page is not bent - it is built. The exception is a bend that keeps the original name, where there is no second page to make.

**source** - required for borrowed and bent. A `[[Person]]` link where one exists, otherwise the origin in plain words. Empty for built.

**status** - `stub` until there is thinking on the page. A title and a link is a stub, whatever else it looks like.

**workflow** - `raw` on creation, `crafted` once written and checked.

**slug and permalink** - `slug` is authored, `permalink` is derived. Permalink is always `/` plus the slug, flat, with no section in the path. A page keeps its URL when it moves between sections. The two must never disagree.
