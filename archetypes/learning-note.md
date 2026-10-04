---
# hugo new --kind learning-note content/posts/<slug>.md   (template: Sahayak content/LEARNING-NOTES-PLAN.md)
title: "<Your angle as a plain statement, not the source's title>"
date: {{ .Date | time.Format "2006-01-02" }}
draft: true
ShowToc: false
categories: ["learning-notes"]
tags: []
url: /learning-notes/{{ .File.ContentBaseName }}/
summary: ""        # one line for list pages
description: ""    # ~150 characters for search results
source: "<Source title>"
source_url: <link to the original>
source_type: <paper | essay | talk | video | podcast | report | book>
---

**TL;DR:** <one sentence: the idea + why it matters to me>

## The source

<One line: who made it, what it is, where it's from. Link to it.>

## The idea, in my words

<3–4 sentences. Only claims checked against the original. Keep the source's hedges.>

## What I took from it

<Your angle: how it connects to your work, another source, or something you believed before.>

## What I'm still unsure about

<1–2 honest open questions or limits.>

## Further reading

- [<Title>](<link>): <why it's worth it>

---
*Part of my [Learning Notes](/learning-notes/). Found via [Digital Dhaba](/tech-digest/).*

<!-- Checklist before draft: false
- Every claim in "The idea, in my words" checked against the original, not just the research MD
- Every "Further reading" link opened and relevant
- Nothing in "What I took from it" is made up
- The title is your angle, not the source's title
- Claude's help described plainly if mentioned -->
