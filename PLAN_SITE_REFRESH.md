# Site Refresh Plan — "Learn. Build. Explain."

Follow-on to the Jekyll → Hugo migration (see `CHANGELOG_HUGO_MIGRATION.md`).
Work happens on a feature branch and is merged into `hugo-migration` via PR; `hugo-migration`
goes live when merged into `main`.

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
| Launch order | Phase 0–2 ship with the Hugo launch; Phases 3–4 follow on the live site |
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
- [ ] Kush reviews working copy (`hugo server`)

## Phase 2 — Concept Breakdown system
- [x] `scripts/new_breakdown.py` — PDF → slides → page bundle with pre-filled `index.md`
- [x] `carousel` shortcode (swipe, arrows, keyboard, counter, dots, lazy-load, PDF download)
- [x] `/breakdown-post` Claude Code skill — transcript, plain-words concept, "Why this matters for PMs",
      takeaways, FAQ, SEO fields, alt text, LinkedIn post + first comment
- [x] Pilot: *How LLMs Think* (transcript drafted from the comic — Kush to verify)
- [ ] Ideas backlog: series numbering + prev/next, FAQ structured data, backfill old 20 posts (~2/week)

## Parked (Kush, 2026-09-30)
- **Tech Digest publishing:** Kush runs the digest manually today; likely a GitHub Action in the newsletter repo
  later. Waiting on the issue HTML template (re-attach; first upload didn't arrive).
- **Newsletter provider choice:** revisit later (current lean: Buttondown for API sending; verify pricing).
- **Subscriber cleanup:** Kush will share the Mailchimp export later; ~268 subscribers, suspected mostly spam.

## Phase 3 — Tech Digest (needs a sample issue HTML)
- [ ] `static/tech-digest/<date>/index.html` (issue kept byte-for-byte) + metadata page per issue
- [ ] `scripts/add_digest.py issue.html` — copy, extract title/date/summary, inject slim site bar + GA + canonical
- [ ] `/tech-digest/` archive (issue cards), homepage card, own RSS feed
- [ ] Automation: newsletter repo's GitHub Action opens a PR here each week (optionally auto-merge)
- [ ] Same Action sends the issue via the newsletter provider's API

## Phase 4 — Subscribers
- [ ] Pick provider (shortlist: Kit, Buttondown) against "fully automated" + API sending of HTML issue
- [ ] Double opt-in + CAPTCHA (Turnstile or provider built-in); tag signups by source (LinkedIn/blog/digest)
- [ ] `scripts/audit_subscribers.py` — run locally on Mailchimp CSV export; flags junk (random local parts,
      no MX / disposable domains, burst signups, never-opened)
- [ ] Re-permission email to survivors; import only confirmed humans
- [ ] Swap `/subscribe/` + post footer form to new provider; retire Mailchimp

## Post-launch checks
- [ ] AdSense serving (site approved? `ads.txt` present? auto-ads enabled in AdSense console?)
- [ ] Disqus threads resolve on moved Concept Breakdown posts
- [ ] Search Console: submit new sitemap, watch redirected URLs get re-indexed
