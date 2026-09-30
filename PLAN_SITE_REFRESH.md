# Site Refresh Plan — "Learn. Build. Explain."

Follow-on to the Jekyll → Hugo migration (see `CHANGELOG_HUGO_MIGRATION.md`).
Work happens on a feature branch and is merged into `hugo-migration` via PR; `hugo-migration`
goes live when merged into `main`.

## ▶ STATUS — where we left off (updated 2026-09-30)

**Phases 0–3 are built and merged into `hugo-migration` (PRs #1, #3). Nothing is live yet:**
`main` / blogsbykush.com is still the old Jekyll site. Go-live = PR #2 (`hugo-migration` → `main`).
Kush previewed everything locally and wants **a few more changes before go-live** (not yet specified).

| Area | State |
|---|---|
| Phase 0 — migration hygiene | ✅ Done |
| Phase 1 — structure, homepage, brand | ✅ Done, reviewed by Kush |
| Phase 2 — Concept Breakdown system | ✅ Done (lean format). Pilot *How LLMs Think* is still `draft: true` |
| Phase 3 — Tech Digest (Digital Dhaba) | ✅ Done. Auto-publish **verified**: Digital-Dhaba workflow pushed issue 2026-09-30 to `hugo-migration` |
| Phase 4 — Subscribers / newsletter | ⏸ **Parked by Kush** — not started (see Phase 4 below) |
| Go-live | ⏳ Waiting on Kush's extra changes, then the go-live checklist below |

**Open items for the next session**
1. Ask Kush for the "few more changes" he wants before go-live; do them on a branch → PR into `hugo-migration`.
2. *How LLMs Think*: Kush to verify transcript wording, then set `draft: false` (decide if it ships at launch).
3. PR #2's description is outdated (mentions "ML Made Easy", wrongly says images moved to `/images/`) —
   rewrite it if Kush agrees (it's his PR).
4. Phase 4 when Kush un-parks it: provider choice + Mailchimp CSV export.

## Go-live checklist (in this order)
1. [ ] Kush's pre-launch changes merged into `hugo-migration`; local preview OK (`hugo server -D`)
2. [ ] Blog repo **Settings → Pages → Source → GitHub Actions** (must be BEFORE step 3)
3. [ ] Merge PR #2 (`hugo-migration` → `main`); watch Actions → "Deploy Hugo site to Pages" goes green
4. [ ] In Digital-Dhaba `.github/workflows/publish-to-blog.yml`: `BLOG_BRANCH: hugo-migration` → `main`
5. [ ] Post-launch checks (bottom of this file)
6. [ ] Delete old Jekyll files (`_config.yml`, `_posts/`, `_pages/`, `_layouts/`, `_includes/`, `_sass/`,
       `_data/`, `Gemfile*`, `index.md`, `feed.xml`, `archive.html`) in a follow-up PR

## Brand direction

- **Who:** Kush Bhatnagar — Technical Product Manager, 17+ years in tech, last 5+ on AI/GenAI
  platforms and cloud infrastructure.
- **Idea:** the blog is a learning system in public — *I learn, I build, then I explain.*
- **Readers:** PM aspirants and product managers, and non-technical folks working in technical domains.
- **Goal:** credibility now; possibly consulting later.
- **Site map follows the loop:**

  | Loop    | Section           | URL                   |
  |---------|-------------------|-----------------------|
  | Learn   | Tech Digest       | `/tech-digest/`       |
  | Build   | Build Log         | `/build-log/`         |
  | Explain | Concept Breakdown | `/concept-breakdown/` |

- **Palette (from the comics):** blue `#11a8cc`, orange `#f4a33a`, cream `#fff6d1`, ink `#131313`.
  Headings in *Fredoka* (matches the comic lettering).

## Decisions made

| Topic | Decision |
|---|---|
| Launch order | Phases 0–3 ship with the Hugo launch (plus Kush's extra changes); Phase 4 follows on the live site |
| ML Made Easy → Concept Breakdown | Posts move to `/concept-breakdown/<slug>/`; old URLs kept as redirects (`aliases`); Disqus threads pinned to old identifiers |
| Concept Breakdown scope | ML, GenAI, Cloud, Product Management, occasional life lessons |
| Nav | Concept Breakdown · Tech Digest · Build Log · Archive · Search · About (MLOps Playground, Bookshelf Chronicles, Tags removed from nav only — pages stay live) |
| Carousel | PDF → cropped 4:5 WebP slides + swipeable `carousel` shortcode + "Download PDF" |
| Transcript source | Kush's conversation text (source of truth); PDF read to map lines to slides and write alt text |
| Tech Digest | Self-contained HTML per issue, archived on site **and emailed** weekly |
| Newsletter | Move off Mailchimp; must be fully automated after setup; budget ≤ ~$12/mo |
| AdSense | Keep; verify it actually serves after launch |

## Phase 0 — Migration hygiene
- [x] Serve RSS at `/feed.xml` (same path as Jekyll; Feedburner/subscribers keep working)
- [x] Restore AdSense ad unit on posts + add `ads.txt`
- [x] Move ML Made Easy write-ups from `summary:` (list-only) into the post body; fix stray `n` in Statistics post
- [x] Untrack `.claude/settings.local.json`; refresh `README.md`

## Phase 1 — Structure, homepage, brand
- [x] Rename ML Made Easy → **Concept Breakdown** (landing, category, 20 post URLs + redirects)
- [x] New nav; add **Build Log** (empty state) and **Tech Digest** (placeholder) landings
- [x] `/subscribe/` page — the one link to share on LinkedIn (provider can change behind it)
- [x] Homepage: intro + proof line + CTAs, Learn/Build/Explain pillars, latest breakdown thumbnails
- [x] Brand layer: colours, heading font, comic thumbnail grid, default social-preview image
- [x] Kush reviewed working copy (`hugo server`)

## Phase 2 — Concept Breakdown system
- [x] `scripts/new_breakdown.py` — PDF → slides → page bundle with pre-filled `index.md`
- [x] `carousel` shortcode (swipe, arrows, keyboard, counter, dots, lazy-load, PDF download)
- [x] `/breakdown-post` Claude Code skill — collapsed transcript, plain-words concept, SEO fields, alt text,
      LinkedIn post + first comment
- [x] Lean format after Kush's review: comic + "concept in plain words" only; transcript collapsed
      ("Read this comic as text"); no TOC / PM section / takeaways / FAQ
- [x] Pilot: *How LLMs Think* — still `draft: true`; transcript read from slides, Kush to verify
- [ ] Ideas backlog: series numbering + prev/next, backfill transcripts for the old 20 posts (~2/week)

## Parked (Kush, 2026-09-30)
- **Newsletter provider choice:** revisit later (current lean: Buttondown for API sending of the HTML
  issue; Kit is the alternative; verify current pricing; budget ≤ ~$12/mo; must be fully automated).
- **Subscriber cleanup:** Kush will share the Mailchimp export later; ~268 subscribers, suspected mostly spam.
  The CSV contains personal data: the audit script should be run by Kush locally.

## Phase 3 — Tech Digest (Digital Dhaba)
Decisions (2026-09-30):
  - Source: private repo `KushBhatnagar/Digital-Dhaba`; `run_digest.sh` writes
    `issues/YYYY-MM-DD/{newsletter.html, digest.json, digest-*.md}` (self-contained HTML, hero embedded).
  - Naming: nav stays **"Tech Digest"**; page title **"Digital Dhaba · Tech Digest"**.
  - Publishing: **auto-publish**. A GitHub Action in Digital-Dhaba (on push to `issues/**`) copies the issue
    into this repo with a fine-grained token (repo is private, so the blog can't pull on its own).
  - The web copy fixes the `{{VIEW_IN_BROWSER_URL}}` / `{{FORWARD_URL}}` / `{{UNSUBSCRIBE_URL}}` placeholders;
    the site hosts the hero image for the email version; archive cards are built from `digest.json`.
  - Idea: `research/` explainers → "Deep Dive" blog posts linked from each digest.

- [x] Issue bundles `content/tech-digest/<date>/` via `scripts/add_digest.py` (HTML kept byte-for-byte)
- [x] Issue page: original design + site bar, canonical/SEO/social tags, GA, web-safe placeholder links
- [x] `/tech-digest/` archive (cards from `digest.json`), homepage "New Tech Digest" strip, section RSS
- [x] Issues on the site: 2026-09-27 (manual import), 2026-09-30 (auto-published)
- [x] Auto-publish workflow for Digital-Dhaba: `docs/tech-digest/publish-to-blog.yml` (+ `docs/TECH_DIGEST.md`)
- [x] Kush: created `BLOG_REPO_TOKEN`, added the workflow to Digital-Dhaba (`BLOG_BRANCH: hugo-migration`
      for now); first automatic publish worked (issue 2026-09-30, commit `9517175`)
- [ ] Emailing the issue from the same workflow → Phase 4 (provider choice parked)

## Phase 4 — Subscribers & emailing the digest  ⏸ PARKED (not started; Kush plans to start 2026-10-01)

**What Kush brings to kick off Phase 4**
1. Decision (or "help me decide"): **Buttondown** (recommended: Markdown/HTML-native, API sends the generated
   issue as-is) vs **Kit**; budget ≤ ~$12/mo. Kush checks current pricing on both sites.
2. A free account on the chosen provider (paid plan can wait until the first real send), plus its **API key**,
   saved as secret `NEWSLETTER_API_KEY` in Digital-Dhaba (never pasted in chat).
3. **Sender identity:** from-name (e.g. "Kush from Blogs by Kush") and from-address on blogsbykush.com, plus
   access to the domain's DNS (where blogsbykush.com is registered) to add SPF/DKIM records.
4. **Mailchimp export:** Audience → All contacts → Export as CSV (keep it local; the audit script runs on
   Kush's machine) and, if easy, the open/click activity report.
5. **Send schedule:** day/time for the weekly email (the digest signoff says Saturday).
6. Double opt-in wording: one line for the confirmation email, e.g. "Confirm to get Digital Dhaba every Saturday".

- [ ] Pick provider (shortlist: Kit, Buttondown) against "fully automated" + API sending of HTML issue
- [ ] Double opt-in + CAPTCHA (Turnstile or provider built-in); tag signups by source (LinkedIn/blog/digest)
- [ ] `scripts/audit_subscribers.py` — run locally on Mailchimp CSV export; flags junk (random local parts,
      no MX / disposable domains, burst signups, never-opened)
- [ ] Re-permission email to survivors; import only confirmed humans
- [ ] Swap `/subscribe/` + post footer form to new provider (only `layouts/_partials/newsletter_form.html`); retire Mailchimp
- [ ] Extend the Digital-Dhaba workflow to send each issue via the provider API (hero from `/tech-digest/<date>/hero.jpg`,
      provider merge tags for `{{VIEW_IN_BROWSER_URL}}` / `{{FORWARD_URL}}` / `{{UNSUBSCRIBE_URL}}`)

## Post-launch checks
- [ ] AdSense serving (site approved? `ads.txt` present? auto-ads enabled in AdSense console?)
- [ ] Disqus threads resolve on moved Concept Breakdown posts
- [ ] Search Console: submit new sitemap, watch redirected URLs get re-indexed
