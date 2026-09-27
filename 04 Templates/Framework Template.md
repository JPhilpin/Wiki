---
title: Framework Template
summary: Template for a new Framework page - copy it, fill it in, delete the field notes.
slug: framework-template
permalink: /templates/framework-template
type: template
origin: 
source: 
family: 
status: stub
workflow: raw
updated: 
tags: []
aliases: []
---

## Working definition

One paragraph. What the framework does and what it produces when applied.

## Provenance

Borrowed, bent or built - and from whom. Delete this heading when origin is built and there is nothing to declare.

## The framework

The stages, elements or slots. What each one asks for. Where the sequence matters and where it loops.

## Applying it

What it takes as input. What comes out the other end. Where it breaks.

## Relationships

### Related

- [[Related Page]]

---

## Field notes

Delete this section when the page is written.

**Model or framework?** A model describes - you see through it. A framework operates - you do it to something. If there is nothing to fill in, it is a model.

**origin** - one of three, always set.

| Value | Test | Example |
|---|---|---|
| `borrowed` | The author reads it and says "that is mine" | Wardley Maps |
| `bent` | The author reads it and says "that is mine, but that is not what I said" | DIKIWI |
| `built` | The author has nothing to recognise | The Four Es |

Being provoked by something is not the same as bending it. The Four Es answer the Four Ps and share nothing with them, so they are built, not bent. Test the artefact, not the inspiration.

Bent is a property of the framework, not the page. Framing, commentary and wiring into the Glossary do not bend anything. Changing what the thing is does.

**A bent page must link to its borrowed parent.** If the parent does not exist, either write it or the page is not bent - it is built. The exception is a bend that keeps the original name, where there is no second page to make.

**source** - required for borrowed and bent. A `[[Person]]` link where one exists, otherwise the origin in plain words. Empty for built.

**family** - the curated set this page belongs to, where it belongs to one (`4C`, `CEDN`, `PESC`). Renders as a **Family:** row in the meta card and groups the page on `/families-list`. Leave empty when the page is not part of a set. The value must match a Glossary page, because the meta row links to `/glossary/<family>/`.

**status** - `stub` until there is thinking on the page. A title and a link is a stub, whatever else it looks like.

**workflow** - `raw` on creation, `crafted` once written and checked.

**slug and permalink** - `slug` is authored, `permalink` is derived. The shape is `/[section]/[slug]`, one level, no trailing slash. The two must never disagree. See the Studio Constitution for the full slug rules.
