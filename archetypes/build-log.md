---
# hugo new --kind build-log content/posts/<slug>.md   (template: Sahayak content/BUILD-IN-PUBLIC-PLAN.md)
title: "<Project>: <the one thing, as a plain statement>"
date: {{ .Date | time.Format "2006-01-02" }}
draft: true
ShowToc: false
categories: ["build-log"]
tags: []
url: /build-log/{{ .File.ContentBaseName }}/
summary: ""        # one line for list pages
description: ""    # ~150 characters for search results
project: <Digital Dhaba | photoclean | plugin2prompt | Sahayak>
status: <idea | building | shipped | paused>
---

**TL;DR:** <one sentence: what happened and what I learned>

## The problem

<2–3 sentences. Whose problem, and why it matters. Make it concrete.>

## What I built / decided

<What exists now, or what I chose. For a decision, name the option I did NOT pick.>

## The one thing

<ONE of: a decision and why · a mistake and what it cost · a number (before/after) · a surprise.>

## What's still broken / next

- <1–3 honest bullets>

---
*Part of my [Build Log](/build-log/).*

<!-- Rules: write it the same day; real numbers only; name AI help plainly; title for search. -->
