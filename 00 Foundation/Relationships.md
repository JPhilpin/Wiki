---
title: Relationships
summary: Rules for linking and declaring meaningful relationships between elements of Structured Thought.
slug: relationships
permalink: /foundation/relationships/
type: architecture
status: review
workflow: crafted
updated: 2026-08-23
tags:
  - architecture
  - structured-thought
  - relationships
aliases: []
---

# Relationships

Structured Thought is not simply a collection of pages. Its value also lies in the relationships between ideas, terms and structures.

A link and a relationship are not the same thing.

## Navigational Links

A `[[Wiki link]]` helps a reader move to another canonical page when doing so improves understanding.

For example:

`[[People]], [[Money]] and [[Things]]`

These links are useful because each term has a canonical meaning elsewhere in the Wiki. They do not, by themselves, make a formal claim about the relationship between the pages.

Not every occurrence of a defined word should become a link. Links should help the reader, not decorate the prose.

## Declared Relationships

A declared relationship makes an explicit claim about how two elements of Structured Thought connect.

For example:

`People, Process THEN Technology → informs → People First`

`DIKIWI → extends → DIKW`

`Producer Efficient Supply Chain → evolves-towards → Customer Effective Demand Network`

A declared relationship should normally be one-way.

The fact that one page relates to another does not imply that the reverse relationship is also true. Reciprocal relationships should be declared only when the reverse claim is independently meaningful.

## Direction

Relationships are written as:

**Subject → relationship → object**

The subject comes first because it is the thing we are making a claim about. The object comes last because it is the thing affected, incorporated, extended, informed or otherwise related to.

The order is therefore not a judgement about which idea is more important.

For example:

`DIKIWI → extends → DIKW`

DIKW came first historically, but DIKIWI is the subject of the claim. We are saying that DIKIWI extends DIKW.

Likewise:

`The Business Equation → incorporates → People, Money and Things`

The Business Equation is the thing being described. People, Money and Things is something it incorporates.

## The Rule

**Every link should have a reason to exist. Every declared relationship should make a claim worth preserving.**

Relationships should not be generated simply because two pages share vocabulary.

## YAML

Declared relationships should be stored as structured metadata so that the Wiki can render, query and map them independently of the prose.

```yaml
relationships:
  - target: People First
    type: informs
  - target: People
    type: composed-of
```

The prose may also express an important relationship naturally. YAML records the relationship as part of the knowledge architecture.

## Relationship Vocabulary

The vocabulary should remain small and grow only when a distinction is useful.

Initial relationship types include:

- `composed-of` — identifies constituent elements.
- `informs` — contributes understanding to another idea or principle.
- `extends` — deliberately develops an existing idea or model.
- `evolves-towards` — describes a directional transition.
- `complements` — identifies elements that perform different but mutually useful roles.
- `incorporates` — identifies an element used within a larger construct.
- `supports` — provides useful structure or capability to another element.
- `applies-to` — identifies a domain or context in which something is used.

This vocabulary should remain provisional until tested across the Wiki. A new relationship type should be added only when the existing vocabulary cannot express an important distinction clearly.

## Rendering

Navigational links should remain ordinary inline Wiki links.

Declared relationships should render differently, for example in a Relationships panel or other distinct treatment. Their structured YAML should allow future backlinks, relationship views and knowledge maps without changing the underlying pages.

## Editorial Test

Before adding a declared relationship, ask:

1. Is the connection meaningful rather than merely lexical?
2. Can the relationship be expressed with a precise verb?
3. Is the direction correct?
4. Would removing the relationship lose useful knowledge?
5. Does an existing relationship type already express it?
6. Is the reverse relationship independently true, or are we merely assuming symmetry?

If the relationship survives those tests, it is probably worth declaring.
