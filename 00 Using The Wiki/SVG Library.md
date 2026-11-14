---
title: SVG Library
summary: Every SVG graphic the Studio uses, shown in one place with the file name for each.
slug: svg-library
permalink: /svg-library
type: foundation
status: review
workflow: crafted
updated: 2026-11-14
tags: []
---

**Format:** Scalable vector graphics (SVG)

**Master copies:** The `_Assets/SVGs/` folder in the Studio vault

**How they are managed:**

- **Live** - `_Assets/SVGs/`, one flat folder. Names never carry a version number and never change, so links never break. Nobody edits a live file directly.
- **Workshop** - `_Assets/SVGs/_in-process/`. To change a diagram, copy it here as `name-v1.svg` and iterate (`-v2`, `-v3`). Version numbers live only here.
- **Promote** - when it is ready, copy the final version over the live file, keeping the live name. Every page picks it up.
- **Archive** - before promoting, copy the old live file to `_Assets/SVGs/_archive/` as `name-pre-YYYY-MM-DD.svg`. Git also keeps the history of every live file.
- **With or without the logo** - a diagram that carries the PHI⑊PIN logo has two live files: `name.svg` without the logo, which documents use, and `name-logo.svg` with it.

## Structured Thought

### The PHI⑊PIN architecture

How PHI⑊PIN goes to business, from the people-first foundation (PHI) and identity (PIN), through elements and engagement, to domains, products, applications, services and the value customers see.

![[architecture-philpin.svg|560]]

File: `architecture-philpin.svg`

### The Business Equation

Every business is an equation: people, money and things go into the business, and value comes out. The picture shows where the weight has moved. Rust is the old world, bottom left: systems of record and producer efficient supply chains (PESC). Blue is the new, top right: systems of engagement and customer effective demand networks (CEDN), with the market now in charge. Market, Organisation, Production and Commerce sit around the core; the diagonal runs rust to blue. Drawn on the golden rectangle, to match the architecture. See [[Business Equation]].

![[business-equation.svg|560]]

File: `business-equation.svg` (without the logo, for documents)

Also: `business-equation-logo.svg` (with the logo) and `business-equation-original.svg` (the earlier blue picture, kept as a reference).

### PESC and CEDN

PESC, how value gets made, mirrored by CEDN, who value is for: Producer and Customer, Efficient and Effective, Supply and Demand, Chain and Network. See [[PESC]] and [[CEDN]].

![[pesc-cedn-mirror.svg|560]]

File: `pesc-cedn-mirror.svg`

### The eight Domains

The eight Domains arranged around the individual and the organisation, each in its accent colour. See [[Eight Domains Map]] and [[Domains Index|the Domains]].

![[domains-eight.svg|560]]

File: `domains-eight.svg`

### Domains applied

The eight Domains as a wheel, with the deliverable types inside it and value at the centre. The interactive version is on philpin.com; here it appears as a still.

![[domains-applied.svg|560]]

File: `domains-applied.svg`

### Deliverable types

The deliverable types a Domain can take: Advisory, Consulting, Enablement, Injection, Licence and Product. See [[Deliverable Types]].

![[domains-deliverable-types.svg|560]]

File: `domains-deliverable-types.svg`

## People First

### The People First Framework

Purpose sets the direction, two frames hold everything, five flows keep five states true, and performance is what comes out. See [[People First Framework]].

![[framework-people-first.svg|560]]

File: `framework-people-first.svg`

## Stages of understanding

The six stages of [[DIKIWI]], drawn as static images. Interactive versions of the six are on philpin.com.

![[dikiwi-1-data.svg|110]] ![[dikiwi-2-information.svg|110]] ![[dikiwi-3-knowledge.svg|110]] ![[dikiwi-4-insight.svg|110]] ![[dikiwi-5-wisdom.svg|110]] ![[dikiwi-6-impact.svg|110]]

| Stage | What it shows | File |
| --- | --- | --- |
| Data | Scattered, unconnected, raw | `dikiwi-1-data.svg` |
| Information | Connected, grouped, beginning to relate | `dikiwi-2-information.svg` |
| Knowledge | Pocketed, structured, beginning to bridge | `dikiwi-3-knowledge.svg` |
| Insight | Signal found, one path complete, others trailing off | `dikiwi-4-insight.svg` |
| Wisdom | Converging, synthesising, one complete picture | `dikiwi-5-wisdom.svg` |
| Impact | Resonant, rippling, everything changes | `dikiwi-6-impact.svg` |

## Personal Dashboard

### The Personal Dashboard

An individual lens that works across any app, drawing on Pulse, Community, Intelligence and Library modules, a shared database and third-party services.

![[domains-personal-dashboard.svg|560]]

File: `domains-personal-dashboard.svg`

### Across ecosystems

One Personal Dashboard connecting to several ecosystems at once, each seen through the same individual lens.

![[domains-personal-integrated-dashboard.svg|560]]

File: `domains-personal-integrated-dashboard.svg`

## Identity

![[identity-cameron-seven-laws.svg|340]] ![[identity-mayo-seven-dimensions.svg|340]]

**Cameron's Seven Laws of Identity** (left) - user control and consent, minimal disclosure, justifiable parties, directed identity, pluralism of technology, human integration and a consistent experience. See [[Identity]]. File: `identity-cameron-seven-laws.svg`

**The seven dimensions of identity** (right) - where it happens (three environments), what is being done (three transaction categories), who is involved (two and three parties), who is proven (entities authenticated), how they prove it (credentials, a two-step process), how much confidence (levels of assurance) and how much is shared (levels of disclosure). File: `identity-mayo-seven-dimensions.svg`

## Software

### Software As A Sandwich

SAAS, a framework that sets scope of concern (personal, contained, scalable) against decision authority (vibe, tension, structure) to name nine software postures, from The Sketch to The Cathedral. Original idea by Andrew Mayfield; graphic inspired by the "define a sandwich" meme.

![[framework-software-as-a-sandwich.svg|560]]

File: `framework-software-as-a-sandwich.svg`

## Brand

### The PHI⑊PIN logotype

The mark itself, in six formats built to one set of rules. See [[Style Guide]] for the rules and when to use each, and [[About The Logo]] for the story.

### Wide

One line. Headers, mastheads, footers.

![[philpin-logo-wide.svg|560]]

File: `philpin-logo-wide.svg`

### Square

App icons, favicons, social profiles.

![[philpin-logo-square.svg|200]]

File: `philpin-logo-square.svg`

### Circle

Avatars and round crops.

![[philpin-logo-circle.svg|200]]

File: `philpin-logo-circle.svg`

### φ badge

The golden rectangle, 1.618 : 1. Cards, slides, screens.

![[philpin-logo-phi.svg|324]]

File: `philpin-logo-phi.svg`

### A-series

The A paper shape, 1.414 : 1, landscape and portrait. Anything printed on A4 or A5.

![[philpin-logo-a-series.svg|283]]

File: `philpin-logo-a-series.svg`

![[philpin-logo-a-series-portrait.svg|200]]

File: `philpin-logo-a-series-portrait.svg`
