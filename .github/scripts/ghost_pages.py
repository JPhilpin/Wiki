#!/usr/bin/env python3
"""Ghost pages: links to pages that do not exist yet.

Scans the vault (excluding Candidates, Templates and this page) for [[wikilinks]] whose
target matches no file name, title or alias. Writes "Ghost Pages.md" at the vault root,
split into:
  Wanted - links that name a page (capitalised or multi-word): pages the wiki is asking for
  Ideas  - single lowercase words linked in passing: candidates for glossary entries
Ghost names are written as plain text on purpose: a wikilink to a missing page would
create an empty note when clicked in Obsidian.
Run from the vault root:  python3 .github/scripts/ghost_pages.py
"""
import os, re, collections, datetime
OUT = "Ghost Pages.md"
SKIP = ("05 Candidates", "04 Templates", ".git", ".github")
names, aliases, files = set(), {}, []  # names = real files/titles; aliases = alias -> page (for near-miss hints only)
for dp, _, fs in os.walk("."):
    rel = os.path.relpath(dp, ".")
    for f in fs:
        p = os.path.normpath(os.path.join(rel, f))
        names.add(os.path.splitext(f)[0].lower())
        if not f.endswith(".md"): continue
        t = open(p, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---", t, re.S)
        if m:
            fm = m.group(1)
            tm = re.search(r"^title:\s*(.*)$", fm, re.M)
            if tm: names.add(tm.group(1).strip().strip("\"'").lower())
            page = os.path.splitext(f)[0]
            am = re.search(r"^aliases:\s*\n((?:\s*-.*\n?)+)", fm, re.M)
            if am:
                for a in re.findall(r"^\s*-\s*(.+)$", am.group(1), re.M): aliases[a.strip().strip("\"'").lower()] = page
        if not p.startswith(SKIP) and f != OUT: files.append((p, t))
def near_miss(t):
    """Existing page a broken link probably meant: an alias, or a singular/plural form."""
    if t in aliases: return aliases[t]
    for cand in (t[:-3] + "y" if t.endswith("ies") else None, t[:-2] if t.endswith("es") else None, t[:-1] if t.endswith("s") else None, t + "s"):
        if cand and cand in names: return cand
    return None
ghosts, fixes = collections.defaultdict(set), collections.defaultdict(set)
for p, t in files:
    body = re.sub(r"```.*?```", "", t, flags=re.S)
    body = re.sub(r"`[^`\n]*`", "", body)
    for link in re.findall(r"(?<!!)\[\[([^\]|#^]+)", body):
        target = link.strip()
        key = target.split("/")[-1].lower()
        if target and key not in names:
            src = os.path.splitext(os.path.basename(p))[0]
            hit = near_miss(key)
            (fixes if hit else ghosts)[(target, hit) if hit else target].add(src)
def is_idea(n): return " " not in n and n == n.lower()
def section(items):
    out = []
    for n, refs in sorted(items, key=lambda kv: (-len(kv[1]), kv[0].lower())):
        links = ", ".join(f"[[{r}|{re.sub(r'^\d{3}\s+', '', r)}]]" if re.match(r'^\d{3}\s', r) else f"[[{r}]]" for r in sorted(refs))
        out.append(f"- **{n}** ({len(refs)}) - linked from {links}")
    return "\n".join(out) if out else "None right now."
wanted = [(k, v) for k, v in ghosts.items() if not is_idea(k)]
ideas  = [(k, v) for k, v in ghosts.items() if is_idea(k)]
doc = f"""---
title: Ghost Pages
summary: Pages the Studio links to that do not exist yet - the ideas and pages it is asking for.
slug: ghost-pages
permalink: /ghost-pages
type: section
status: active
tags:
  - studio
---

<nav class="studio-listnav"><a href="/entries-list-alphabetical">Entries A to Z</a><a href="/entries-list-most-recent">Recent changes</a><a href="/tags-list-alphabetical">Tags A to Z</a><a href="/types-list">Types A to Z</a><a href="/ghost-pages" class="is-current">Ghost pages</a></nav>

Pages that other pages link to, but that have not been written yet. {len(wanted)} wanted and {len(ideas)} ideas, most-linked first. Generated from the vault on {datetime.date.today():%-d %B %Y}.

## Wanted

Pages the Studio clearly means to have.

{section(wanted)}

## Ideas

Single terms linked in passing. Each could grow into a glossary entry.

{section(ideas)}
"""
open(OUT, "w", encoding="utf-8").write(doc)
print(f"{OUT}: {len(wanted)} wanted, {len(ideas)} ideas")
for (t, hit), refs in sorted(fixes.items()):
    print(f"NEAR-MISS  [[{t}]] probably means '{hit}'  <- {', '.join(sorted(refs))}")

# Safety net: images outside _Assets get published by Blot as empty posts (they show in lists
# with the "My apologies" placeholder). Keep every image under _Assets/ (underscore = ignored by Blot).
IMG=(".png",".jpg",".jpeg",".gif",".svg",".webp")
for dp, _, fs in os.walk("."):
    rel=os.path.relpath(dp,".")
    if rel.startswith(("_", ".git")) or "/_" in rel: continue
    for f in fs:
        if f.lower().endswith(IMG): print(f"STRAY IMAGE (move under _Assets/): {os.path.normpath(os.path.join(rel,f))}")
