---
title: Relationship Audit
summary: Working list of candidate declared relationships across the current Structured Thought Wiki.
slug: relationship-audit
permalink: /design-journals/relationship-audit/
type: design-journal
status: review
workflow: created
updated: 2026-08-23
tags:
  - design-journal
  - structured-thought
  - relationships
aliases: []
---

# Relationship Audit

This is the working list of candidate declared relationships across Structured Thought.

It is an editorial audit, not an implementation. No relationship on this page should be added to canonical YAML until it has been reviewed and approved.

The rules governing links, direction and declared relationships are defined in [[Relationships]].

## Composition

1. [[People, Money and Things]] → `composed-of` → [[People]]
2. [[People, Money and Things]] → `composed-of` → [[Money]]
3. [[People, Money and Things]] → `composed-of` → [[Things]]

4. [[People, Process THEN Technology]] → `composed-of` → [[People]]
5. [[People, Process THEN Technology]] → `composed-of` → [[Process]]
6. [[People, Process THEN Technology]] → `composed-of` → [[Technology]]

7. [[Mavens, Connectors and Communicators]] → `composed-of` → [[Mavens]]
8. [[Mavens, Connectors and Communicators]] → `composed-of` → [[Connector]]
9. [[Mavens, Connectors and Communicators]] → `composed-of` → [[Communicator]]

10. [[Creative, Clever, Consistent and Complete]] → `composed-of` → [[Creative]]
11. [[Creative, Clever, Consistent and Complete]] → `composed-of` → [[Clever]]
12. [[Creative, Clever, Consistent and Complete]] → `composed-of` → [[Consistent]]
13. [[Creative, Clever, Consistent and Complete]] → `composed-of` → [[Complete]]

14. [[Producer Efficient Supply Chain]] → `composed-of` → [[Producer]]
15. [[Producer Efficient Supply Chain]] → `composed-of` → [[Efficient]]
16. [[Producer Efficient Supply Chain]] → `composed-of` → [[Supply]]

17. [[Customer Effective Demand Network]] → `composed-of` → [[Customer]]
18. [[Customer Effective Demand Network]] → `composed-of` → [[Effective]]
19. [[Customer Effective Demand Network]] → `composed-of` → [[Demand]]
20. [[Customer Effective Demand Network]] → `composed-of` → [[Network]]

21. [[TAM / SAM / SOM]] → `composed-of` → [[Total Addressable Market]]

## Conceptual Relationships

22. [[People, Process THEN Technology]] → `informs` → [[People First]]

23. [[Producer Efficient Supply Chain]] → `evolves-towards` → [[Customer Effective Demand Network]]

24. [[Systems of Record]] → `complements` → [[Systems of Engagement]]

25. [[The Age of Reason]] → `evolves-towards` → [[The Age of Experience]]

26. [[DIKIWI]] → `extends` → [[DIKW]]

## The Business Equation

27. [[The Business Equation]] → `incorporates` → [[People, Money and Things]]

28. [[The Business Equation]] → `incorporates` → [[Producer Efficient Supply Chain]]

29. [[The Business Equation]] → `incorporates` → [[Customer Effective Demand Network]]

30. [[The Business Equation]] → `incorporates` → [[Systems of Record]]

31. [[The Business Equation]] → `incorporates` → [[Systems of Engagement]]

32. [[The Business Equation]] → `connects` → [[The Age of Reason]]

33. [[The Business Equation]] → `connects` → [[The Age of Experience]]

## Other Architectural Candidates

34. [[Structured Thought]] → `organises` → [[The Business Equation]]

35. [[Engagement Profile]] → `applies-to` → [[Work]]

36. [[Systems of Engagement]] → `supports` → [[Engagement Profile]]

## Items Requiring Particular Review

### The Business Equation and the Ages

Relationships 32 and 33 are meaningful, but `connects` is too imprecise to approve as a relationship type. The relationship needs a better verb before either is wired.

### Structured Thought and The Business Equation

Relationship 34 may simply describe membership within Structured Thought rather than a meaningful knowledge relationship. It should survive only if `organises` expresses something we genuinely want to preserve.

### Engagement Profile

Relationships 35 and 36 need to be tested against the canonical Engagement Profile material before approval.

## Explicitly Rejected During Review

The following candidates have already been considered and rejected:

- `People First → governs → People, Process THEN Technology`
- `Wardley Maps → draws-on → Pace Layers`

They are recorded here to prevent them being accidentally reintroduced during later automated or editorial passes.

## Status

**36 candidate relationships remain. None has yet been wired into canonical page YAML.**
