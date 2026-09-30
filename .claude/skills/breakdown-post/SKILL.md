---
name: breakdown-post
description: Write the body, SEO fields, slide alt text and LinkedIn copy for a Concept Breakdown comic post on blogsbykush.com. Use after scripts/new_breakdown.py has created the page bundle (content/posts/<slug>/ with slide-*.webp), or when Kush asks to write up / backfill a Concept Breakdown post.
---

# Concept Breakdown post writer

Turns a comic (slides + conversation text) into a complete, SEO-friendly post, in Kush's voice.

**Input:** a page bundle path, e.g. `content/posts/how-llms-think/`. If none is given, pick the newest
bundle whose `index.md` still has `draft: true` and empty sections.

## 1. Gather the source

1. Read `index.md` (title, slug, date).
2. **Conversation text:** if `transcript.txt` exists in the bundle, it is the source of truth for what
   the characters say. Use its wording.
3. **Read every slide image** (`slide-01.webp` …) with the Read tool, even when transcript.txt exists.
   You need them to map lines to slides, write alt text, and catch anything the text is missing.
   With no transcript.txt, transcribe the speech bubbles from the slides, and add
   `<!-- CHECK: transcribed from slides -->` at the top of the transcript section.
4. List the existing Concept Breakdowns (`grep -l 'concept-breakdown' content/posts/*.md content/posts/*/index.md`)
   and read their titles and `url:` values. You'll link 2–3 related ones.

## 2. Who it's for and how it should sound

- **Readers:** PM aspirants, product managers, and non-technical people working in tech. Assume they're smart,
  but not engineers.
- **Voice (Kush):** warm, simple, conversational; short sentences; everyday Indian analogies (chai,
  cricket, antakshari, Swiggy, family functions) when they help; no hype, no buzzword soup, no "delve".
  Explain any term the first time it appears.
- **Accuracy beats flourish.** Don't add technical claims the comic doesn't support unless they're
  standard and correct. If you're unsure about something, keep it and add `<!-- CHECK: ... -->` for Kush.

## 3. Write the body (target 500–800 words, excluding the transcript)

Keep `{{< carousel >}}` as the first line of the body. Fill the skeleton headings:

### `## What's happening in this comic`
The transcript, grouped by slide, so it reads cleanly and Google can index the dialogue:

```markdown
**Slide 1: <short scene title>**

**Teacher:** Remember playing Antakshari at family functions? …
**Student:** Ha, yes! …
```
- Speaker labels: `Teacher`, `Student` (use `Student 2` when two different students speak in one
  scene). Use names only once the cast has names.
- Fix typos and punctuation only; don't reword what the characters say.
- End each line with two trailing spaces, or put a blank line between lines, so they don't merge
  into one paragraph.
- Include text in captions or boxes (e.g. a "Takeaway" box) as `**Takeaway:** …`.

### `## The concept in plain words` (150–250 words)
Define the concept in one plain sentence, then build on the comic's analogy: where it fits, and where
it breaks down. Include one concrete, real-world example. Bold the key term the first time it appears.

### `## Why this matters for PMs` (100–180 words)
Why a product person should care, with 3–4 bullets, each a concrete implication for how they build,
scope, test or talk about products. (For example, for LLMs: why outputs vary, why prompts and context
matter, why "hallucination" happens, what that means for evals and UX.)

### `## Key takeaways`
Exactly 3 bullets, one line each.

### `## FAQ`
2–3 questions that people actually type into Google (e.g. "Do LLMs think before they answer?"). Each
question is an `###` heading; each answer is 40–80 plain words.

Finish with a related-reading line:

```markdown
**Related breakdowns:** [Title A](/concept-breakdown/a/) · [Title B](/concept-breakdown/b/)
```

## 4. Front matter

- `summary`: a teaser of 140 characters or fewer, shown on list pages.
- `description`: 140–160 characters for search results. Include the main keyword naturally.
- `tags`: 3–5 lowercase tags. Reuse existing ones (`machine learning`, `generative ai`,
  `classroom conversation`, …) before inventing new ones.
- `slide_alt`: one string per slide, in order, 125 characters or fewer. Say what the slide shows and its
  key line (e.g. `"Teacher asks students to remember playing Antakshari at family functions"`).
- Leave `draft: true`. Kush reviews the post and publishes it himself.

## 5. LinkedIn copy

Write `linkedin.txt` in the bundle (it isn't published; nothing on the site links to it):

```
POST
<hook line: a question or surprising claim, max 12 words>

<3–5 short lines: the idea in plain words, one line per thought>

<one line inviting comments, e.g. "What analogy made LLMs click for you?">

#ProductManagement #GenAI #<topic> (3–5 hashtags)

FIRST COMMENT
Full breakdown, transcript and PDF: https://blogsbykush.com/concept-breakdown/<slug>/
Get one of these in your inbox every week: https://blogsbykush.com/subscribe/
```

LinkedIn shows posts with links in the body to fewer people, so links go only in the first comment.

## 6. Verify

- Run `hugo --quiet --buildDrafts -d /tmp/bd-check` (Hugo may be at `~/bin/hugo`). It must build
  without errors.
- Check that `/tmp/bd-check/concept-breakdown/<slug>/index.html` contains the transcript and the carousel.
- Report back to Kush with: the word count, any `CHECK` comments, and a reminder to set `draft: false`.
