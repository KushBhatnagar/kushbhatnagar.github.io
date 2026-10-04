---
title: "Digital Dhaba: how I built an AI-written tech newsletter that can't make up news"
date: 2026-10-04
draft: true
ShowToc: false
categories: ["build-log"]
tags: ["generative ai", "automation", "newsletter"]
url: /build-log/digital-dhaba-ai-newsletter-that-cannot-make-up-news/
summary: "A weekly tech digest where code picks the stories, Claude only writes from them, and every item links to its source."
description: "How I built Digital Dhaba, a weekly AI and tech newsletter: code gathers and ranks stories, Claude writes only from them, and every item links to its source."
project: Digital Dhaba
status: shipped
---

**TL;DR:** Digital Dhaba is a one-page weekly newsletter: code gathers and ranks the week's stories, Claude writes the digest only from those stories, and every item links to the original source, so you can check it in one click.
<!-- CHECK: TL;DR assembled from your notes and your LinkedIn draft -->

## The problem

Tech and AI news never stops, and it is spread across dozens of sites, newsletters and forums. Most people can't follow it all, and much of it is written for specialists.

## What I built

Tech Digest is a one-page weekly newsletter, published under the name Digital Dhaba, that tells a non-specialist what mattered this week in tech, AI and LLMs. Every item links to the original source. Each issue has:

- **Top Stories:** the 5 most important stories of the week.
- **Topic sections:** the rest of the news, grouped by subject.
- **Quick Hits:** 5–8 one-line stories worth knowing.
- **Try This:** one practical AI tip.
- **Worth Your Weekend:** 2–3 essays, talks, papers or books worth slowing down for.

### How one issue gets built

One script, `run_digest.sh`, runs four steps in order:

1. **Gather:** `fetch.py` pulls the week's stories from Hacker News, research paper sites, tech news sites and other newsletters. It removes duplicates, sorts stories into sections and ranks them by how much attention they got.
   <!-- CHECK: your notes were cut off after "from H…"; I used the source list from your LinkedIn draft -->
2. **Write:** Claude gets those stories plus the instructions and writes the digest as Markdown.
   <!-- CHECK: notes cut off at "plus the instru…" -->
3. **Convert:** a Node script turns the Markdown into structured data (`digest.json`).
4. **Design:** another Node script renders that into an email-safe HTML page (`newsletter.html`).

All three files land in `issues/YYYY-MM-DD/`.

### Decisions I took

- **Claude writes with no tools and no web access.** It can only use the stories it was handed, so it can't invent news.
- **Ranking is done by code, not by AI.** The same input always gives the same ranking, and only the writing step costs tokens.
  <!-- CHECK: notes cut off at "The same inpu…" -->
- **Weekend picks come from a hand-checked shelf** (`weekend_picks.yaml`), with summaries verified in advance.
- **Tips come fresh from The Neuron's last 7 days,** with `tips.yaml` (now 9 tips) as the fallback when there is no good fresh one.
- **Nothing repeats.** The script reads past issues to see what has already run, so there is no history file to maintain.
  <!-- CHECK: notes cut off at "reads past issues to …" -->
- **Test issues don't count.** `no_repeat_since: 2026-10-08` means picks used before launch can run again for real readers.
- **A GitHub Action runs it,** not a laptop or a cloud machine I have to keep switched on, and it runs the exact same script every week.
  <!-- CHECK: notes cut off at "or a cloud … yours switched on" -->
- **Cost is about $0.93 per issue** at API prices; on my Claude subscription it counts against plan usage instead.

### How it gets published

1. Every Thursday, GitHub starts a fresh temporary machine and runs `run_digest.sh` (`weekly-digest.yml`).
2. If the digest comes out empty or broken, the run fails and nothing is published.
   <!-- CHECK: notes cut off at "the run…ed" -->
3. Otherwise it commits the new issue folder to the Digital Dhaba repo.
4. It then starts the second workflow, `publish-to-blog.yml`, which copies the issue into my blog repo so it appears on blogsbykush.com.

## The one thing

The rule I care most about: it only writes from what it collected. Nothing from the model's memory, nothing made up to fill space. Every item links back, so you can check it yourself in one click. An AI-written newsletter is only useful if you can verify it. That link is the whole trust model.
<!-- CHECK: taken word for word from your LinkedIn draft; confirm, or send your own "one thing" -->

Read the [latest issue](/tech-digest/), or get it every Thursday: [subscribe](/subscribe/).

---
*Part of my [Build Log](/build-log/).*
