# Research notes — plan (decided 2026-10-23, not built yet)

A fifth kind of page on the blog: selected research explainers from the Digital-Dhaba repo
(`research/YYYY-MM-DD/<slug>.md`, written by Claude with the `/explain-story` skill after Kush's discussion and
refinement), turned into blog pages. **Nothing is built yet.** This file records what was decided and what's still open,
so a later session can build it.

## Decided (Kush, 2026-10-23)

| Topic | Decision |
|---|---|
| Name | **Research notes** |
| Goal | A mix: search traffic, and more value for Digital Dhaba readers (a deeper reference behind a story) |
| Which notes | **Kush picks** individual notes from `research/`. Not all of them, never automatic |
| Email | Published Research notes go in the **Sunday letter** (like Concept Breakdown, Build Log, Learning Notes) |
| How they're made | A **separate skill** (like `/breakdown-post`, `/build-log-entry`, `/learning-note`) that reads a research MD and converts it into a blog page |
| Not this | No links to the MD files in GitHub (Digital-Dhaba is private; making it public would expose prompts/config, and readers would land on GitHub, not the blog) |
| When | Later. Recorded today, built in a future session |

## Proposed in the 2026-10-23 discussion (confirm when building)

From Claude's review of the 18 notes (all read for structure, 3 in full). Kush didn't object; confirm each one when the
skill is built.

1. **Label every page:** "Researched and written with Claude, read and checked by Kush", plus the research date and the
   original story. Research notes are **not** in Kush's voice; they sit beside Tech Digest (already "Claude-curated"),
   not inside Learning Notes, Build Log or Concept Breakdown.
2. **Strip before publishing:** "Good angles for a post" (Kush's private prompt list). Consider dropping or dating
   "What to watch next" (goes stale within weeks).
3. **Date it visibly:** "Researched on <date>; details may have changed since." News explainers age fast.
4. **Kush reads each one before publishing,** with extra care on claims about named companies or people (lawsuits,
   security incidents, criminal cases). The notes attribute claims carefully, but on the blog they're under Kush's name.
5. **Anthropic/Claude stories** (written by Claude, about Anthropic): add a one-line disclosure, or skip them.
6. **Pace:** a few at a time, not a batch. AdSense site review is pending, and a burst of long AI-written pages can read
   as "scaled / low-value content".
7. **Link both ways:** `/tech-digest/` and the matching Digital Dhaba issue → "Read the research note"; the research
   note → the issue it came from.
8. **Update `.claude/BLOG_WRITING_RULES.md`:** research prose may appear **only** in Research notes (labelled), never in
   Kush's own posts. Today rule 1 says research files are reference only.

## Open questions for the build session

- URL and category: `/research-notes/<slug>/` with category `research-notes`? Nav menu entry, and where on the homepage
  (if anywhere)?
- Indexed by search engines (yes, given the search-traffic goal?) and AdSense on these pages (yes/no)?
- Also link from the Thursday Digital Dhaba email, or only the Sunday letter?
- How Kush marks a pick: run the skill with a path (`/research-note research/2026-10-22/<slug>.md`), or a
  `publish: true` flag in the note?
- Keep the note's sources list as-is (yes, likely) and the "Key terms" section (likely yes: good for search and readers)?
- Front matter: `source`, `source_url`, `researched` date, link to the Digital Dhaba issue.
- Sunday letter: `scripts/kit_weekly_roundup.py` / `/posts.json` must include the new category (check when building).

## Candidates on 2026-10-23

The 18 notes in Digital-Dhaba `research/` (2026-09-27 → 2026-10-22). Kush picks. Notes whose sources were partly
"seen only through summaries" (most 2026-10-08 and 2026-10-17 ones) need a closer check before publishing.
