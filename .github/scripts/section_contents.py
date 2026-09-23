import os, re, sys
ROOT = "."
S = [
 ("00 Foundation","Foundation","foundation","The rules, relationships and background that govern how the Studio is built.","title"),
 ("01 Structured Thought/00 Glossary","Glossary","glossary","The working vocabulary of Structured Thought: short definitions of the terms used across the Studio.","letters"),
 ("01 Structured Thought/01 Concepts","Concepts","concepts","The core ideas that Structured Thought is built on.","title"),
 ("01 Structured Thought/02 Papers","Papers","papers","The paper series, in reading order. Each paper builds on the ones before it.","file"),
 ("01 Structured Thought/03 Principles","Principles","principles","The commitments that shape how the work is done.","title"),
 ("01 Structured Thought/04 Models","Models","models","Models for seeing how things fit together, some original and some borrowed.","title"),
 ("01 Structured Thought/05 Frameworks","Frameworks","frameworks","Frameworks that turn the ideas into something usable.","title"),
 ("01 Structured Thought/07 Patterns","Patterns","patterns","Recurring shapes worth recognising when they appear.","title"),
 ("01 Structured Thought/08 Domains","Domains","domains","The eight Domains, where the thinking meets an area of practice.","title"),
 ("01 Structured Thought/09 Design Journals","Design Journals","design-journals","Working notes on how parts of the Studio were designed and why.","title"),
 ("02 References","References","references","The people, books and outside sources the thinking draws on.","title"),
]
def fm(path):
    t=open(path,encoding="utf-8").read()
    m=re.match(r"^---\s*\n(.*?)\n---",t,re.S)
    d={}
    if m:
        for line in m.group(1).splitlines():
            mm=re.match(r"^(title|summary|kind):\s*(.*)$",line)
            if mm: d[mm.group(1)]=mm.group(2).strip().strip('"').strip("'")
    return d
def clean(s): return re.sub(r"^\d{3}\s+","",s).strip()
out=[]
for folder,name,slug,intro,order in S:
    fname=f"{name} - Contents.md"
    target=os.path.join(folder,fname)
    items=[]
    for dp,_,fs in os.walk(folder):
        for f in fs:
            if not f.endswith(".md") or f==fname: continue
            p=os.path.join(dp,f); d=fm(p); base=f[:-3]
            title=clean(d.get("title") or base)
            items.append((base,title,d.get("summary",""),d.get("kind","")))
    if order=="file": items.sort(key=lambda x:x[0].lower())
    else: items.sort(key=lambda x:x[1].lower())
    link=lambda b,t: f"[[{b}]]" if b==t else f"[[{b}|{t}]]"
    body=[f"{intro}",""]
    if order=="letters":
        acr=[x for x in items if x[3]=="acronym"]
        if acr:
            body+=["","## Acronyms",""]+[f"- **{link(x[0],x[1])}** - {x[2]}" if x[2] else f"- **{link(x[0],x[1])}**" for x in acr]
            items=[x for x in items if x[3]!="acronym"]
        cur=None
        for b,t,s,*_ in items:
            L=t[:1].upper()
            if not L.isalpha(): L="#"
            if L!=cur:
                body+=["",f"## {L}",""]; cur=L
            body.append(f"- {link(b,t)}")
    else:
        body.append(f"{len(items)} {'page' if len(items)==1 else 'pages'}.")
        body.append("")
        for b,t,s,*_ in items:
            body.append(f"- **{link(b,t)}**" + (f" - {s}" if s else ""))
    doc=f"""---
title: {name}
summary: Contents of the {name} section.
slug: {slug}
permalink: /{slug}
type: section
status: active
tags: []
---

""" + "\n".join(body).strip()+"\n"
    open(target,"w",encoding="utf-8").write(doc)
    out.append(f"{len(items):4d}  {target}")
print("\n".join(out))
