---
name: learning-note
description: Turn Kush's own notes on a paper, essay, talk, video, podcast, report or book into a Learning Note on blogsbykush.com (content/posts/<slug>.md, /learning-notes/). Use when Kush says "learning note", "write up my notes on <source>", or gives notes plus a source link. Assembles his words into the template; never writes his takeaway for him; no LinkedIn copy.
---

# Learning Note

**First read `.claude/BLOG_WRITING_RULES.md`.** Its rules win over this file.

The template and publishing checklist come from Kush's plan, Sahayak `content/LEARNING-NOTES-PLAN.md`.
The file skeleton is `archetypes/learning-note.md`.

## Input
- **Required:** Kush's notes: bullets, rough paragraphs or a voice-note transcript. Usually 100–400 words.
- **Required:** the source, as a link, or a title Kush confirms.
- **Optional:** a research file (e.g. Digital-Dhaba `research/<date>/<slug>.md`) for metadata and reading links
  only, and the Digital Dhaba issue the source came from.

## Steps
1. **Read the input.** Map Kush's material to the five sections:

   | Section | Comes from | If missing |
   |---|---|---|
   | **TL;DR** (1 sentence: idea + why it matters to him) | his notes; may combine his own sentences | draft it from his words in other sections, mark `<!-- CHECK: TL;DR assembled from your notes -->` |
   | **The source** (who, what, where, link) | link, his notes, research-file metadata | ask for the link |
   | **The idea, in my words** (3–4 sentences) | his notes **only** | ask |
   | **What I took from it** (the core) | his notes **only** | **stop and ask** (never draft) |
   | **What I'm still unsure about** (1–2 items) | his notes | ask; if he has none, ask him to name one limit |
   | **Further reading** (3–5 links) | his notes, then research-file sources he approves | ask which to keep |

2. **Ask once** for everything missing (rule 2). Wait for the answers.
3. **Check the facts you can.**
   - In "The idea, in my words", keep the source's hedges: if Kush wrote "proves" but his input or the
     source says "suggests", flag it with `<!-- CHECK: source says "suggests"? -->`. Don't silently change it.
   - Any number must appear in Kush's notes or the source text he gave.
   - If you can read the source (it's attached, or the network allows it), compare each claim with it and
     add a `CHECK` to anything that doesn't match. If you can't read it, say so in the report.
4. **Write the file.**
   - `hugo new --kind learning-note content/posts/<slug>.md`, then fill it.
   - Title = **Kush's angle**, not the source's title. If his notes don't give an angle, propose 2 options
     made from his own sentences, then ask.
   - Front matter: `source`, `source_url`, `source_type` (`paper | essay | talk | video | podcast | report | book`).
   - Keep the footer line exactly: *Part of my [Learning Notes](/learning-notes/). Found via
     [Digital Dhaba](/tech-digest/).* If the source didn't come via Digital Dhaba, drop the second sentence.
   - Delete the archetype's checklist comment once you've reported it (step 5).
   - Length: 300–500 words. If it's longer, say what could be cut; don't cut his words yourself.
5. **Before handing back** (rules section 4): check the links, build, then report with the plan's checklist:
   - [ ] Every claim in "The idea, in my words" checked against the original, not just the research file
   - [ ] Every "Further reading" link opened and relevant
   - [ ] Nothing in "What I took from it" is made up
   - [ ] The title is his angle, not the source's title
   - [ ] Claude's help described plainly if mentioned
