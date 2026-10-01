# Site Refresh Plan — "Learn. Build. Explain."

Follow-on to the Jekyll → Hugo migration (see `CHANGELOG_HUGO_MIGRATION.md`).
Work happens on a feature branch and is merged into `hugo-migration` via PR; `hugo-migration`
goes live when merged into `main`.

## ▶ STATUS — where we left off (updated 2026-10-01)

**Phases 0–3 are built and merged into `hugo-migration` (PRs #1, #3). Nothing is live yet:**
`main` / blogsbykush.com is still the old Jekyll site. Go-live = PR #2 (`hugo-migration` → `main`).
Kush previewed everything locally and wants **a few more changes before go-live** (not yet specified).

| Area | State |
|---|---|
| Phase 0 — migration hygiene | ✅ Done |
| Phase 1 — structure, homepage, brand | ✅ Done, reviewed by Kush |
| Phase 2 — Concept Breakdown system | ✅ Done (lean format). Pilot *How LLMs Think* is still `draft: true` |
| Phase 3 — Tech Digest (Digital Dhaba) | ✅ Done. Auto-publish **verified**: Digital-Dhaba workflow pushed issue 2026-09-30 to `hugo-migration` |
| Phase 4 — Subscribers / newsletter | 📝 Decisions made 2026-10-01 (Kit Free, separate emails, re-permission, Actions→Kit API). Build plan proposed, **awaiting Kush's approval** |
| Go-live | ⏳ Waiting on Kush's extra changes, then the go-live checklist below |

**Open items for the next session**
1. Ask Kush for the "few more changes" he wants before go-live; do them on a branch → PR into `hugo-migration`.
2. *How LLMs Think*: Kush to verify transcript wording, then set `draft: false` (decide if it ships at launch).
3. PR #2's description is outdated (mentions "ML Made Easy", wrongly says images moved to `/images/`) —
   rewrite it if Kush agrees (it's his PR).
4. Phase 4: get Kush's approval/answers on the build plan (Phase 4 section), then build 4a/4b; Kush does 4c.

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
| Newsletter provider (2026-10-01) | **Kit (ConvertKit), Free Plan**, replacing Mailchimp. "Built with Kit" footer badge accepted |
| Email model (2026-10-01) | Separate emails: **one email per new blog post** (automatic) + **full Digital Dhaba HTML every Saturday** (automatic) |
| Mailchimp list (2026-10-01) | **Re-permission, not import**: one final Mailchimp email → Kit form with double opt-in; only confirmers join. Audit script optional |
| Sending mechanism (2026-10-01) | **GitHub Actions → Kit API v4** (not Kit RSS-to-email). Per-post: on deploy, posts-only detection (excludes Tech Digest). Digest: extra step in Digital-Dhaba `publish-to-blog.yml` |
| Signup source tracking | Separate Kit forms per source (auto-tag-by-form is paid); compare form subscriber counts |
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
- ~~Newsletter provider choice~~ → decided 2026-10-01: Kit Free (see Phase 4).
- ~~Subscriber cleanup~~ → replaced by re-permission (Phase 4); audit script optional.

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

## Phase 4 — Subscribers & email (Kit)  📝 PLANNED 2026-10-01, awaiting Kush's approval of the build plan

### Kit Free Plan facts (confirmed with Kit's support bot, 2026-10-01)
- Up to 10,000 subscribers, unlimited broadcasts, no monthly send limit.
- **API v4** available on Free. "Create a broadcast" accepts full HTML `content`, `email_template_id`,
  subscriber filters, and immediate or scheduled send.
  Docs: https://developers.kit.com/api-reference/broadcasts/create-a-broadcast
- Templates can't be bypassed: create **one minimal custom HTML template** (content + Kit's required footer)
  and pass its `email_template_id` (omitted → account default template; "Starting Point" templates unsupported).
- **Double opt-in** on by default for Kit Forms / Landing Pages (Settings → Confirmation Email; keep
  "Auto-confirm" unchecked).
- **Verified Sending Domain** on Free (Kit gives CNAMEs for SPF/DKIM); custom From address is a separate step.
  Warm up: clean list, engaged subscribers first, ramp gradually, Google Postmaster Tools.
  Docs: https://help.kit.com/en/articles/2502558-verify-your-domain-to-optimize-your-deliverability
- "Built with Kit" footer badge can't be removed on Free (accepted).
- Tags exist on Free, but **auto-tag by form is paid** → one Kit form per signup source instead.
- Free plan overview: https://help.kit.com/en/articles/16627071-the-kit-free-plan

### Proposed build plan (see "Phase 4 plan" in the 2026-10-01 session; build only after approval)
**4a: Blog repo (PR into `hugo-migration`, ships with go-live)**
- [ ] `newsletter_form.html` → plain HTML form posting to Kit's form endpoint (keeps current styling,
      no Kit JS); form ID chosen per placement (`source`: blog / linkedin / mailchimp), IDs in `hugo.toml`
      `params.kit`. Honeypot field kept; double opt-in does the real bot filtering.
- [ ] `/subscribe/` uses the **LinkedIn** form; posts/Build Log/Tech Digest use the **Blog** form;
      `/subscribe/?from=mailchimp` (or a separate page) uses the **Mailchimp-move** form.
- [ ] Posts-only JSON output (`/posts.json`: url, title, summary, image, date, section) excluding `tech-digest`.
- [ ] `scripts/kit_notify_posts.py`: diff live `posts.json` (before deploy) vs new build → new posts →
      Kit broadcast per post (title, summary, image, "Read it" link). Guards: skip when live `posts.json`
      is missing (go-live deploy / first run), cap at 3 new posts per run, only posts dated in the last
      14 days, dry-run unless `KIT_SEND=true`.
- [ ] `hugo.yml`: `notify` job after `deploy` (needs `KIT_API_KEY`, `KIT_TEMPLATE_ID`), test mode
      (`KIT_TEST_TAG_ID` → send only to a "test" tag) until Kush flips it.
**4b: Digital-Dhaba workflow (file delivered for Kush to commit, as in Phase 3)**
- [ ] `scripts/kit_send_digest.py` (lives in the blog repo, run by the Digital-Dhaba workflow after
      publishing): newsletter.html → hero data-URI swapped for `https://blogsbykush.com/tech-digest/<date>/hero.jpg`,
      placeholders mapped (unsubscribe → Kit tag, view-in-browser → web issue URL, forward → mailto share),
      body extracted; **scheduled** for the next Saturday send time (immediate if that time has passed);
      skip if a broadcast with the same subject already exists (no duplicates on re-runs); test mode as above.
**4c: Kush (accounts, DNS, content)**
- [ ] Kit account; API key saved as `KIT_API_KEY` secret in **both** repos (never in chat)
- [ ] Sending domain blogsbykush.com verified (Kit CNAMEs + DMARC TXT); From `kush@blogsbykush.com`
- [ ] Minimal custom email template; 3 forms (Blog, LinkedIn, Mailchimp-move); a "test" tag with Kush only
- [ ] Postal address for Kit's footer; Saturday send time; confirmation-email line
- [ ] Mailchimp re-permission email (Claude drafts copy) → wait ~2 weeks → archive Mailchimp audience
- [ ] Google Postmaster Tools for blogsbykush.com

### To verify in Kit's docs during the build (docs sites blocked from the Claude cloud session)
- Kit merge-tag syntax for unsubscribe / subscriber preferences / web version inside broadcast `content`
  and which tags the custom template must contain.
- Form submission endpoint + field names for a plain HTML form (no JS embed).
- `send_at` format and `subscriber_filter` shape (tag filter) for test sends.

## Post-launch checks
- [ ] AdSense serving (site approved? `ads.txt` present? auto-ads enabled in AdSense console?)
- [ ] Disqus threads resolve on moved Concept Breakdown posts
- [ ] Search Console: submit new sitemap, watch redirected URLs get re-indexed
