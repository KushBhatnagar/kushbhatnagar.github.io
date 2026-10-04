---
name: breakdown-post
description: Write the body, SEO fields and slide alt text for a Concept Breakdown comic post on blogsbykush.com from Kush's comic PDF and conversation text. Use after scripts/new_breakdown.py has created the page bundle (content/posts/<slug>/ with slide-*.webp), or when Kush asks to write up / backfill a Concept Breakdown post. No LinkedIn copy (Sahayak writes LinkedIn posts).
---

# Concept Breakdown post writer

Turns a comic (slides + conversation text) into a complete, SEO-friendly post, in Kush's voice.

**First read `.claude/BLOG_WRITING_RULES.md`.** Its rules win over this file (note the exception there for
"The concept in plain words"). No LinkedIn copy: Sahayak writes the LinkedIn posts.

**Input:** Kush's comic **PDF** and **conversation text**. If the page bundle doesn't exist yet, create it:
`python3 scripts/new_breakdown.py <Comic.pdf> --title "<Title>" --transcript <conversation.txt>`. That gives a
bundle path such as `content/posts/how-llms-think/`. If no bundle or PDF is given, pick the newest bundle whose
`index.md` still has `draft: true` and empty sections. Optional: Kush's own notes on the concept.

## 1. Gather the source

1. Read `index.md` (title, slug, date).
2. **Conversation text:** if `transcript.txt` exists in the bundle, it is the source of truth for what
   the characters say. Use its wording.
3. **Read every slide image** (`slide-01.webp` …) with the Read tool, even when transcript.txt exists.
   You need them to map lines to slides, write alt text, and catch anything the text is missing.
   With no transcript.txt, transcribe the speech bubbles from the slides, and add
   `<!-- CHECK: transcribed from slides -->` at the top of the transcript section.

## 2. Who it's for and how it should sound

- **Readers:** PM aspirants, product managers, and non-technical people working in tech. Assume they're smart,
  but not engineers.
- **Voice (Kush):** warm, simple, conversational; short sentences; everyday Indian analogies (chai,
  cricket, antakshari, Swiggy, family functions) when they help; no hype, no buzzword soup, no "delve".
  Explain any term the first time it appears.
- **Accuracy beats flourish.** Don't add technical claims the comic doesn't support unless they're
  standard and correct. If you're unsure about something, keep it and add `<!-- CHECK: ... -->` for Kush.

## 3. Write the body (lean: comic + one short section)

Kush wants these pages lean: **the comic and the concept in plain words, nothing else.** Don't add
"Why this matters", takeaways, FAQ, related links or a table of contents (`ShowToc: false` stays in the
front matter).

The body is exactly:

```markdown
{{< carousel >}}

{{< transcript >}}
**Slide 1: <short scene title>**

**Teacher:** Remember playing Antakshari at family functions? …  
**Student:** Ha, yes! …
{{< /transcript >}}

## The concept in plain words

<120–170 words>
```

### Transcript (collapsed by default, "Read this comic as text")
Readers don't see it unless they open it, but Google and screen readers read every line. This is where
the page gets most of its indexable text, so include all of the dialogue.
- Group lines by slide, with a short scene title for each slide.
- Speaker labels: `Teacher`, `Student` (`Student 2` when a different student speaks in the same scene).
  Use names only once the cast has names.
- Fix typos and punctuation only; don't reword what the characters say.
- End each line with two trailing spaces so lines within a slide stay separate.
- Include text in captions or boxes (e.g. a "Takeaway" box) as `**Takeaway:** …`.
- If you transcribed from the slides, put `<!-- CHECK: transcript read from the slides -->` on the line
  above `{{< transcript >}}`.

### `## The concept in plain words` (120–170 words, 3–4 short paragraphs)
1. Define the concept in one plain sentence. Bold the key term the first time it appears.
2. Explain how it works using the comic's analogy.
3. Add one line on where the analogy stops working, or one practical point, when that helps.
4. Don't add new technical claims beyond the comic unless they're standard and correct.

## 4. Front matter

- `summary`: a teaser of 140 characters or fewer, shown on list pages.
- `description`: 140–160 characters for search results. Include the main keyword naturally.
- `tags`: 3–5 lowercase tags. Reuse existing ones (`machine learning`, `generative ai`,
  `classroom conversation`, …) before inventing new ones.
- `slide_alt`: one string per slide, in order, 125 characters or fewer. Say what the slide shows and its
  key line (e.g. `"Teacher asks students to remember playing Antakshari at family functions"`).
- Leave `draft: true`. Kush reviews the post and publishes it himself.

## 5. Verify

- Run `hugo --quiet --buildDrafts -d /tmp/bd-check` (Hugo may be at `~/bin/hugo`). It must build
  without errors.
- Check that `/tmp/bd-check/concept-breakdown/<slug>/index.html` contains the carousel, the `<details class="transcript">`
  block and the plain-words section, and has no table of contents.
- Report back to Kush with: any `CHECK` comments, and a reminder to set `draft: false`.
