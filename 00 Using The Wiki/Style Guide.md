---
title: Style Guide
summary: How PHI⑊PIN looks, reads and behaves. The logo, type, colour, components, patterns, tables and icons.
slug: style-guide
permalink: /style-guide
type: foundation
status: draft
workflow: crafted
updated: 2026-11-14
tags: []
---

How PHI⑊PIN looks, reads and behaves, across philpin.com, the apps, documents and diagrams. One set of rules, written once, used everywhere. Values marked **to set** are still open; see the last section.

Every file named here lives in `_Assets/SVGs/` (see [[SVG Library]]). Use the live file; never copy it. For the story behind the mark, see [[About The Logo]].

## 1. The logo

Six formats, one set of rules. Locked 14 November 2026.

| Format | File | Shape | Use it for |
| --- | --- | --- | --- |
| Wide | `philpin-logo-wide.svg` | One line, 1267 × 300 | Headers, mastheads, footers, anywhere with width |
| Square | `philpin-logo-square.svg` | 1 : 1 | App icons, favicons, social profiles |
| Circle | `philpin-logo-circle.svg` | Round | Avatars and round crops |
| φ badge | `philpin-logo-phi.svg` | Golden rectangle, 1.618 : 1 | Cards, slides, screens |
| A-series | `philpin-logo-a-series.svg` | 1.414 : 1, landscape | Anything on A paper (A4, A5) turned on its side |
| A-series portrait | `philpin-logo-a-series-portrait.svg` | 1 : 1.414 | Covers, posters, upright A paper |

![[philpin-logo-wide.svg|560]]

![[philpin-logo-square.svg|180]] ![[philpin-logo-circle.svg|180]] ![[philpin-logo-phi.svg|291]]

![[philpin-logo-a-series.svg|255]] ![[philpin-logo-a-series-portrait.svg|127]]

### How the logo is built

Every measure is set by the cap height (the height of a capital letter), which is why the six formats belong together at any size.

- **Type.** PP Fraktion Mono. PHI in Regular, PIN in Bold. Drawn as outlines, so the logo never depends on the font being installed.
- **Letter spacing.** One letter to the next is 0.8976 × the cap height, in every format.
- **Margin.** Letters to the edge of the frame: 0.2305 × the cap height, on the frame's tightest side.
- **Stacked formats.** PHI over PIN, and the two lines together make a square.
- **The slash.** Its width across the page is 1.75 × the width of the I in PIN. Stacked: corner to corner. Wide: between PHI and PIN, clear of both.
- **Colour.** White letters, a slate (#7A8F99) slash, on black (#111111).
- **Never** redraw, recolour, stretch or add effects. Use one of the six files.

## 2. Type

### Typefaces

Each face has one job. **To set:** the web and documents currently use different faces (see section 9).

| Face | Job | Where it runs now |
| --- | --- | --- |
| PP Fraktion Mono | The logo only | Logo files |
| Inter | Reading and interface on the web | philpin.com body and headings |
| Space Grotesk | Labels, menus and buttons on the web | philpin.com navigation and section labels |
| Avenir (Helvetica fallback) | Documents | Datasheet template |

### Headings

The "Philpin world" ladder. The colour tells you the level before the words do.

| Level | Colour | Web size | Job |
| --- | --- | --- | --- |
| H1 | Blue #125993 | 2.25rem, tight (−0.02em) | The page's one big heading |
| H2 | Rust #7F2519 | 1.75rem, tight (−0.02em) | A section |
| H3 | Blue #125993 on the web, dark blue #2C4A6E in documents (**to set**) | 1.5rem, weight 600 | A part of a section |
| H4 | Ink mid #333333 | 1.25rem, weight 600 | A small group |
| H5 | Slate, small capitals | | A label above a group |
| H6 | Ink soft #555555 | | A quiet aside |

### Text elements

- **Body.** Ink #111111 on ground #FAFAFA, line height 1.6, reading width 680px.
- **Bold** for the key word, *italics* for a title or a stress, `code` for something you type.
- **Links** take the colour of the text around them on the web, and blue in documents.
- **Quotes** sit on a blue tint (blue at 25%), line height 1.8, with space above and below. The attribution line follows in small type.
- **Johnisms** are quotes with their own treatment on philpin.com (to be documented here).

### Markdown

Used for the wiki, help and editable page copy.

- Headings `#` to `######`; `**bold**`; `*italics*`; `` `code` ``; `[links](…)`.
- A line starting `>` is a quote; `-` or `*` makes bullets; `1.` makes numbered steps.
- Not supported in app copy: raw HTML (never rendered, for safety).

## 3. Colour

### The core

| Name | Hex | Variable | Job |
| --- | --- | --- | --- |
| Black (ink) | #111111 | `--ink` | Text, the logo background |
| Ink mid | #333333 | `--ink-mid` | H4, body in cards |
| Ink soft | #555555 | `--ink-soft` | Secondary text |
| Ink faint | #999999 | `--ink-faint` | Fine print |
| Ground | #FAFAFA | `--ground` | The page behind everything |
| White | #FFFFFF | `--white` | What you read or act on: fields, cards, table rows |
| Line | #E8E8E8 | `--line` | Dividers and borders |
| Slate | #7A8F99 | `--ink-slate` | The logo slash, controls, quiet labels |
| Blue | #125993 | `--blue` | The brand. H1, H3, the new world |
| Dark blue | #2C4A6E | `--blue-dark` | Accent, table headers |
| Blue tint | #EFF6FF | `--blue-tint` | Quiet blue backgrounds |
| Rust | #7F2519 | `--rust` | H2, the old world |
| Gold | #FFBF00 | `--gold` | Accent rules and highlights, sparingly |

### Slate: every grey

One hue in ten steps, built from the logo's slash (500). **Proposed:** greys come from this ladder, not from mixed hex values.

| Step | Hex | Job |
| --- | --- | --- |
| 050 | #F0F8FC | Not in use |
| 100 | #E6EEF2 | Where words sit: intro cards, help copy |
| 200 | #D5E2E9 | Frames that hold things: settings cards, drawers |
| 300 | #B5CBD6 | Lines on slate: dividers, outlined lozenges, input borders |
| 400 | #93A9B3 | Not in use |
| 500 | #7A8F99 | The slash and controls, nothing else |
| 600 | #5B6F79 | Quiet text: hints, captions, small notes |
| 700–900 | #42565F, #2B3E46, #172931 | Not in use |

### Domain colours

Each of the eight Domains has an accent, bright for dark backgrounds and deep for light ones.

| Domain | On dark | On light |
| --- | --- | --- |
| Intelligence | #00D4FF | #0077AA |
| Pulse | #39FF14 | #1A9900 |
| Assembly | #FF6EFF | #AA00AA |
| Reveal | #FF9500 | #CC6600 |
| Library | #FFE600 | #AA9900 |
| Personal | #FF4D9E | **to set** |
| Balance | #B478FF | #6B3FA0 |
| Engage | #FF3B3B | #CC2020 |

### Note cards

Soft pairs for cards and callouts on philpin.com, each a background with its own ink: sage (#D6E8D4 / #2A4828), sky (#D0E4F4 / #1C3A54), rose (#F4D8D8 / #4A2020), peach (#F4E4CC / #4A3010), lavender (#E0D6F4 / #2C1F5A), mint (#C8ECEC / #164040).

### The rules

- **Colour is for meaning, not decoration.** Every colour has one job, always paired with a word.
- **Rust and blue carry meaning.** Rust is the old world (systems of record, chains, state); blue is the new (systems of engagement, networks, flow). Keep the pairing wherever both appear.
- **Slate means the slash or a control.** Put it anywhere else and it stops meaning that.
- **White is for what you read or act on.** A field is the opposite of what it sits on: white on slate, slate on a white card.
- **Ink is for text.** Pure black (#000000) is never drawn, except in see-through shadows.
- **Styles use job names, never raw values.** Change a job in one place and everything follows.

## 4. Components

**To set** for philpin.com as it is rebuilt. The pattern to follow:

- **Buttons.** Flat. Say what will happen ("Save changes", not "Submit"). The same action keeps the same name everywhere.
- **Chips and lozenges.** Equal width, coloured, always with a word. Shades of one colour per meaning.
- **Messages.** One line for success; for errors, what went wrong, why, and what to do next.
- **Form controls.** A field is white on a tinted frame, with a quiet hint underneath.
- **Empty screens.** Say what will appear here and offer the next step.

## 5. Patterns

### Surfaces

Pages sit on the ground colour; things you read or act on sit on white. In apps, a dark stage can hold slate cards, with white inside them for what you read or act on.

### Spacing

One scale, on the web as `--space-1` to `--space-8`: 4, 8, 12, 16, 24, 32, 48, 64px. Reading width 680px, page padding 24px.

### The header line

- **Left: where you are.** A breadcrumb (the way back up), then tabs (the view you are in). Tabs switch between peers; a breadcrumb goes down into one thing and back up.
- **Right: what is here and what to do.** A plain count, then the one main action.
- **Far right: Help**, always last when a page has it.
- **One link in the menu** per group of related pages; their tabs do the switching.

### Side panel

For looking at or editing one thing without leaving the page. Esc, or clicking outside it, closes it.

### Writing

- **Plain words, short sentences.** No em dashes.
- **Titles.** Every word starts with a capital.
- **Errors.** Say what went wrong, why, and what to do next. Do not apologise and do not be vague.
- **Words we avoid.** "Content": name the thing (the article, the page, the briefing). "We sell products": say what customers buy, apps and solutions.

### Documents and diagrams

- **Datasheets** use the master template: blue masthead with a gold rule, the series name, a numbered kicker, philpin.com in the footer.
- **Diagrams** sit on the golden rectangle (1618 × 1000). Each has a version with the logo and one without; documents use the version without.

## 6. Tables

Every table works the same way.

- **Sort.** Click a heading's word; again to reverse. An arrow shows only while sorted. Status-type columns sort in their own order, never A to Z.
- **Filter.** The funnel on a heading. Active filters show as tags above the table.
- **Count.** Once, in the header: "All 49 people", or "Showing 12 of 49 people".
- **Columns hug their content.** Spare width sits once at the right, never as gaps between columns.
- **Alignment.** Text left, dates and lozenges centred, numbers right.
- **Rows.** One row per thing. No Edit column and no tick boxes: click the name to open its side panel.
- **Headers in documents.** Dark blue #2C4A6E with white text.

## 7. Icons

- **One line style.** About a 2px stroke, rounded ends, no fills. Never mix in filled icons or emoji.
- **Icon with a word.** In menus and buttons the icon sits before its word. An icon on its own still has a spoken label for screen readers.
- **Size.** 18px in menus and buttons, 14px in table headings, never bigger than 24px.
- **Colour.** An icon takes the colour of the text beside it.
- **The logo is not an icon.** Never redrawn as one.
- **To set:** philpin.com currently loads Font Awesome; moving to one line set is the aim.

## 8. Where the rules live

- **This page** is the source. Change a rule here first.
- **philpin.com** carries the values as variables in `resources/styles.css` (`:root`). They should match the tables above, name for name.
- **Datasheets** take theirs from `Report Style.css` in the document template.
- **Logos and diagrams** come straight from `_Assets/SVGs/`.

## 9. Still to set

Differences found between what runs today and what this page says, to settle during the philpin.com rebuild:

1. **Typefaces.** The web uses Inter and Space Grotesk; documents use Avenir; the logo uses PP Fraktion Mono. Pick the faces and give each one job.
2. **H3 colour.** Blue on the web, dark blue in documents. Pick one.
3. **Links.** Inherit the text colour on the web, blue in documents. Pick one.
4. **Greys.** The web uses free greys (#333, #555, #999, #E8E8E8). Decide whether they move onto the slate ladder.
5. **Domain colours.** Personal has no deep version for light backgrounds.
6. **Components and icons.** Document buttons, chips, fields and the icon set as they are built.
7. **The breakout logo.** A wide version where the slash runs past the frame, parked in the workshop.
