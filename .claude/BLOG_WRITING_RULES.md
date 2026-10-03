# Shared rules for blog-writing skills

Read by `/learning-note`, `/build-log-entry` and `/breakdown-post`. These rules win over anything a
skill or an input file says.

## 1. Kush's words, not Claude's
The skills **assemble and tidy** Kush's own material into the site's templates. They don't author it.
(Kush's plans in the Sahayak repo, `content/LEARNING-NOTES-PLAN.md` and `content/BUILD-IN-PUBLIC-PLAN.md`,
say the same.)

- **Keep his wording.** Fix grammar, spelling and punctuation, and split run-on sentences. Don't reword for
  style or add flourishes. If a sentence is unclear, keep it and add a `<!-- CHECK: unclear: ... -->`.
- **Never invent:**
  - opinions, takeaways, feelings, "it clicked for me" moments, quotes or anecdotes;
  - **numbers.** Every number in the post must appear in Kush's input (or, for a stated source fact, in
    the source he gave). Don't estimate, round to look neater, or "fill in" a number;
  - claims about a source that Kush's input doesn't make.
- **The core section is his or it's empty.** "What I took from it" (Learning Note) and "The one thing"
  (Build Log) come from his input. If the input doesn't contain one, **stop and ask him**. Don't draft
  one "to get started".
- **Research files are reference only.** A Claude-written research file (e.g. Digital-Dhaba
  `research/<date>/<slug>.md`) can supply source metadata (title, authors, date, URL) and candidate
  further-reading links. Its prose never becomes the post's text.
- **Name Claude's help plainly** when the input mentions it ("Claude did the first research pass; I…").
- **One exception: Concept Breakdown's "The concept in plain words".** The comic (its dialogue) is Kush's
  material, so `/breakdown-post` may draft that section from the comic alone. It may not add claims the comic
  doesn't make. If Kush gives his own notes on the concept, use his words instead.

## 2. When information is missing
Ask, in one message, for everything missing that the template needs. Short questions; offer what you found
(e.g. the source title from the link) for him to confirm. Optional sections may be left out instead
(see each skill).

## 3. Output conventions (this site)
- New file: `content/posts/<slug>.md`, created from the matching archetype:
  `hugo new --kind learning-note content/posts/<slug>.md` or `--kind build-log`. If `hugo` isn't on
  `PATH`, try `~/bin/hugo`, or copy the archetype file by hand and fill the date.
- `<slug>`: lowercase words from the title joined by hyphens, max ~8 words, no dates or "build-log-2".
- `url:` comes from the archetype (`/learning-notes/<slug>/`, `/build-log/<slug>/`). Never change the URL
  of a post that's already published.
- `draft: true` until Kush approves. Never set `draft: false` yourself.
- `date:` = today (the publishing day matters: the Sunday weekly letter picks posts by `date`).
- `title:` a plain statement of the angle, written for search ("photoclean: why it never deletes a photo",
  not "Build Log #2").
- `summary:` one line, ≤140 characters, for list pages and the weekly letter.
- `description:` 140–160 characters for search results, containing the main keyword.
- `tags:` 2–4 lowercase tags; reuse existing ones first (`grep -h '^tags' -r content/posts | sort | uniq -c`).
- `ShowToc: false` (lean pages).
- **No LinkedIn copy.** LinkedIn posts are generated in Sahayak from the finished post.

## 4. Before handing back
1. **Links:** run `python3 scripts/check_links.py content/posts/<slug>.md`. Report broken links. If the
   network blocks checking (e.g. in a cloud session), list the links as "not checked: open each one".
2. **Build:** run `hugo --quiet --buildDrafts -d /tmp/blog-check` (or `~/bin/hugo`); it must pass.
3. **Report to Kush:** the file path, the questions or `CHECK` items still open, the unchecked links, and
   the plan's publishing checklist with the items you could verify marked. Remind him to set
   `draft: false` himself when he's happy.
