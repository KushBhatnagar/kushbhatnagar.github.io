---
name: build-log-entry
description: Turn Kush's notes about something he built (a decision, a mistake, a number, a surprise, a milestone) into a Build Log entry on blogsbykush.com (content/posts/<slug>.md, /build-log/). Use when Kush says "build log", "write up what I built/decided", or gives build notes for Digital Dhaba, photoclean, plugin2prompt, Sahayak or another project. Assembles his words into the template; real numbers only; no LinkedIn copy.
---

# Build Log entry

**First read `.claude/BLOG_WRITING_RULES.md`.** Its rules win over this file.

The template and rules of thumb come from Kush's plan, Sahayak `content/BUILD-IN-PUBLIC-PLAN.md`.
The file skeleton is `archetypes/build-log.md`.

## Input
- **Required:** Kush's notes on **one** decision, problem or milestone: bullets, rough paragraphs or a
  voice-note transcript.
- **Required:** the project name and its status (`idea | building | shipped | paused`).
- **Optional:** screenshots or a diagram (save them next to the post, see step 4), a repo link, a commit or
  log excerpt, or the real numbers (before/after, cost, time).

## Steps
1. **One entry = one thing.** If the notes cover several decisions or a whole project history, propose
   splitting them into separate entries and ask which one to write first.
2. **Map Kush's material to the template:**

   | Section | Comes from | If missing |
   |---|---|---|
   | **TL;DR** (what happened + what he learned) | his notes | assemble from his sentences, mark `<!-- CHECK -->` |
   | **The problem** (2–3 concrete sentences) | his notes | can be one line if obvious; otherwise ask |
   | **What I built / decided** (for a decision: the option he did NOT pick) | his notes | ask; for a decision, ask what he rejected |
   | **The one thing** (the core: decision + why, mistake + cost, a number, or a surprise) | his notes **only** | **stop and ask** (never draft). Rule from his plan: no "one thing" = the entry isn't ready |
   | **What's still broken / next** (1–3 bullets) | his notes | ask; may be skipped only for a final `shipped` entry |

3. **Numbers:** every number must appear in his input or in a log or output he pasted. Never estimate.
   If a sentence needs a number he didn't give, ask, or rewrite the sentence without it (and tell him).
4. **Write the file.**
   - `hugo new --kind build-log content/posts/<slug>.md`, then fill it, including `project:` and `status:`.
   - **Title for search:** "<Project>: <the one thing, as a plain statement>", e.g. "photoclean: how I made
     sure an AI-built tool could never delete my photos".
   - **Images:** to include screenshots, make the post a page bundle: `content/posts/<slug>/index.md`,
     with the images in the same folder (`hugo new --kind build-log content/posts/<slug>/index.md`). Use
     descriptive alt text and the `![alt](file.png)` markdown.
   - **Footer:** keep *Part of my [Build Log](/build-log/).* An optional one-line call to action (try it /
     repo / subscribe) only if Kush gives one. His plan: the Digital Dhaba entry is the only one that pushes
     the newsletter.
   - Length: 400–700 words. If it's longer, suggest cuts; don't cut his words yourself.
   - Delete the archetype's rules comment.
5. **Before handing back** (rules section 4): check the links, build, then report with the rules of thumb:
   - [ ] Written the same day as the build or decision (ask if unsure; it affects `date`)
   - [ ] Real numbers only, all from his input
   - [ ] AI help named plainly ("Claude wrote the first version; I…")
   - [ ] Title chosen for search
   - [ ] Gaps stated honestly in "What's still broken / next"
