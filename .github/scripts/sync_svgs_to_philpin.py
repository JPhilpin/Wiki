#!/usr/bin/env python3
"""Copy the wiki's SVGs to philpin.com, one way: wiki -> philpin.

The wiki vault (_Assets/SVGs/) is the master. philpin.com keeps its own copies at
resources/svgs/ so every philpin page keeps its existing paths. (The wiki blocks
<object>, <iframe> and <embed> from other sites, so the interactive
domains-applied.svg has to be served from philpin.com itself.)

Run from the vault root, after changing any SVG:

    python3 .github/scripts/sync_svgs_to_philpin.py            # dry run: shows what would happen
    python3 .github/scripts/sync_svgs_to_philpin.py --apply    # copies the files

Then upload the files it lists to SiteGround (public_html/resources/svgs/).

Safety rules:
- One way only. It never deletes anything, on either side.
- It skips any SVG that is not valid XML or is suspiciously small (the silent
  write corruption that left 1 to 7 byte files behind in August).
- If the philpin copy is NEWER than the wiki copy and differs, it does not
  overwrite it. Someone edited it on the philpin side. Use --force to override.
"""
import os, sys, glob, shutil
import xml.etree.ElementTree as ET

SRC = os.path.join("_Assets", "SVGs")
DEST = "/Users/johnphilpin/Documents/Claude/1-PROJECTS-LIVE-SITES/PHILPIN.COM/PHILPIN-DOT-COM/resources/svgs"
MIN_BYTES = 200

apply = "--apply" in sys.argv
force = "--force" in sys.argv

if not os.path.isdir(SRC):
    sys.exit("Run this from the vault root (the folder that contains _Assets/).")
if not os.path.isdir(DEST):
    sys.exit("Destination not found: " + DEST)

copied, unchanged, skipped, held = [], [], [], []
names = sorted(os.path.basename(p) for p in glob.glob(os.path.join(SRC, "*.svg")))
for n in names:
    s = os.path.join(SRC, n)
    d = os.path.join(DEST, n)
    size = os.path.getsize(s)
    if size < MIN_BYTES:
        skipped.append((n, "only %d bytes, looks corrupt" % size)); continue
    try:
        ET.parse(s)
    except ET.ParseError as e:
        skipped.append((n, "not valid XML: %s" % e)); continue
    if os.path.exists(d):
        if open(s, "rb").read() == open(d, "rb").read():
            unchanged.append(n); continue
        if os.path.getmtime(d) > os.path.getmtime(s) and not force:
            held.append((n, "philpin copy is newer and differs")); continue
    copied.append((n, "new" if not os.path.exists(d) else "updated"))
    if apply:
        shutil.copy2(s, d)

wiki = set(names)
only_philpin = sorted(os.path.basename(p) for p in glob.glob(os.path.join(DEST, "*.svg")) if os.path.basename(p) not in wiki)

print(("APPLIED" if apply else "DRY RUN (nothing copied; add --apply)") + "\n")
print("Copy (%d):" % len(copied));  [print("  %-8s %s" % (w, n)) for n, w in copied]
print("Unchanged (%d)" % len(unchanged))
if held:    print("\nHELD, not overwritten (%d):" % len(held));  [print("  %s  (%s)" % (n, w)) for n, w in held]
if skipped: print("\nSKIPPED (%d):" % len(skipped));            [print("  %s  (%s)" % (n, w)) for n, w in skipped]
if only_philpin: print("\nOn philpin only, left alone (%d): %s" % (len(only_philpin), ", ".join(only_philpin)))
if apply and copied:
    print("\nUpload to SiteGround, folder resources/svgs/ :")
    [print("  " + n) for n, _ in copied]
