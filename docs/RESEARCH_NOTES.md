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
| Theme fit | Under **Learn**, beside Tech Digest: Tech Digest is the quick weekly stop, a Research note is the long sit-down on one story. Both Claude-written and curated by Kush. **Not** under Explain (Explain = Kush's own words: Concept Breakdown, Learning Notes). A Research note can lead to a Learning Note or comic in his words. Motto "Learn. Build. Explain." unchanged |
| Homepage | Keep the 4 section cards (2×2); extend the Tech Digest card text, e.g. "…every Thursday, plus Research notes on the biggest stories." No 5th card |
| Top menu | No menu item at first; reach it from the Tech Digest page and each issue. Add a menu item later only if traffic justifies it |

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

## Pages to update when building (decided 2026-10-23)

| Where | Change |
|---|---|
| `hugo.toml` homepage pillars | Tech Digest card text gains "plus Research notes on the biggest stories" (wording at build time). Still 4 cards |
| `hugo.toml` menu | No change at first |
| `content/about.md` "How this blog works" | Learn bullet: "Tech Digest, plus Research notes: deeper dives into one story, researched with Claude". Diagram Learn box: "Tech Digest · Research notes" |
| `content/subscribe.md` | Body + meta description: the Sunday letter also includes Research notes |
| `content/tech-digest/_index.md` | One line + link: "Some stories get a full Research note →" |
| `hugo.toml` site description | Optional: add "research notes" |
| New `content/research-notes.md` | Landing page at `/research-notes/`, `layout: category-landing` like Learning Notes |
| Behind the scenes | `scripts/kit_weekly_roundup.py` (new category in the Sunday letter), `CLAUDE.md` positioning line + layout, `.claude/BLOG_WRITING_RULES.md`, `docs/NEWSLETTER.md`, new skill under `.claude/skills/` |

## Open questions for the build session

- URL and category: `/research-notes/<slug>/` with category `research-notes`? (Menu and homepage: decided above.)
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
