---
title: Studio Constitution
summary: The rules that govern how the Studio is built - stewardship, structure, permalinks, slugs, classification and provenance.
slug: studio-constitution
permalink: /studio-constitution
type: foundation
status: active
workflow: crafted
updated: '2026-09-28'
version: '0.8'
tags:
- studio
- governance
- stewardship
---

## Purpose

STUDIO is the working environment in which Structured Thought is captured, tested, connected and developed into durable knowledge. It is published live: what is here is the current state of that work, not a finished result.

## Operating distinction

Studio contains the current body of work. Posterity records the conversations, decisions and changes through which that body of work emerged. They run in parallel and serve different purposes.

## Paper workflow

A Paper develops through working material in `Scratch` and becomes an active narrative in `Papers`. Every Paper opens with its Executive Overview and Key Takeaways where appropriate. These are sections of the Paper, not separate artefacts.

## Structural rule

Only top-level folders are numbered. Numbers reveal order without turning the whole vault into a brittle hierarchy.

## Stewardship rule

No substantive change is silent. Earlier thinking is preserved where it remains useful, and current canonical wording has one clear home.

## Permalink rule

Every publishable page carries an explicit `permalink:` in its frontmatter. A page's URL is never derived from its folder path. This is what lets a page move - between sections, into a new folder, even into a newly created section - without breaking a single inbound link. Folders organise the vault for people; permalinks are the actual, load-bearing address.

The shape is `/[section]/[slug]` for a content page and `/[section]` for a section index. One level only: the `01 Structured Thought` parent and the numeric folder prefixes are dropped. No trailing slash. The section stays in the path because it gives a namespace - without it, a Paper named Models and the Models section would claim the same address.

`slug:` is authored by hand. `permalink:` is derived from it and must never disagree with it. Any slug that changes keeps its old form as an alias.

## Slug rule

Lowercase throughout. Spaces and slashes become hyphens. Apostrophes are dropped without leaving a hyphen behind. An ampersand becomes `and`, though a title is better written without one.

No leading article: The Business Equation is addressed as `business-equation`. This applies to page names as well as slugs.

Initials are dropped rather than made into their own segment, so E. Jerome McCarthy is `jerome-mccarthy`. The title keeps the initial where the person's name carries it.

Numerals stay numerals and are never spelled out. A name built from a numeral and letters runs together rather than hyphenating - `4es`, `4ps`, `5ds`, `3ts`. These are names, not phrases, and the alternatives are worse: `4-es` reads as broken, `four-es` contradicts the rule above.

## Models describe, frameworks operate

A model is something you see through. It describes how things fit together, and there is nothing in it to fill in.

A framework is something you do to something else. It has stages, elements or slots, and it produces an output.

Where a page could be either, the test is whether a reader has anything to complete. If not, it is a model.

## Borrowed, bent, built

Every model and framework declares where the idea came from, in an `origin:` field carrying exactly one of three values, with a `source:` field naming the originator beside it.

**Borrowed** means the idea is someone else's, unchanged. **Bent** means it is someone else's, altered. **Built** means it is ours.

The test is what the original author would say on reading the page. Borrowed: that is mine. Bent: that is mine, but that is not what I said. Built: nothing, because there is nothing to recognise.

Origin belongs to the idea, not to the page. Framing it, commenting on it and wiring it into the Glossary do not bend anything; changing what the thing is does. Being provoked by something is not bending it either - the Four Es answer the Four Ps and share nothing with them, so they are built.

A bent page links to the borrowed page it came from. Where that parent does not exist, either it is written or the page was never bent. The exception is a bend that keeps the original name, where there is no second page to make.

`source:` is required for borrowed and bent, and empty for built. Borrowed or bent without a source is an unverifiable claim.

Provenance is a property, not a place. A borrowed model is filed as a model, and References holds sources - people, books, podcasts, organisations - not ideas sorted by where they came from.

## Families

A page that belongs to a curated set declares it in a `family:` field. CEDN, PESC, the numeral sets. The field renders as a **Family:** row on the page and groups every member together on the families list.

Membership is a field, not a tag. The set already has a page of its own, so a tag named after it would create a second thing answering the same question - the same reason a tag never duplicates a section. The field links to the set's page; a tag would only gesture at it.

Every family has a Glossary entry, because that is where the field's link resolves to. A set with no definition is not yet a family.

## Index, never contents

A section's listing page is its index. The word is used in filenames, slugs, headings and the scripts that generate them. "Contents" is not used anywhere.

## Status tells the truth

A page is `stub` until there is thinking on it. A title and a link is a stub, whatever else it resembles. A page describing itself as active while its body is empty is the frontmatter making a claim the page cannot support, and the stewardship rule above applies to that as much as to anything else.

## Tags never duplicate a section

A tag is not permitted to share its name with a section, or with a `type:` value already in use (Concept, Paper, Principle, Model, Framework, Pattern, Domain, Deliverable, Reference). Sections are the structural axis - where a page lives. Tags are the cross-cutting axis - traits that run sideways across sections, such as `author`, `testimonial`, `collaborator`. A tag with a section's name creates two different pages both claiming to answer the same question (`/tagged/domains` versus `/domains`), with nothing to tell a reader which one they want. Where a page genuinely relates to a section conceptually, that relationship belongs in a `[[wikilink]]` in the body, not in a tag.
