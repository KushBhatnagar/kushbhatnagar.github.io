# Hugo Migration Changelog

Tracks every change made while migrating **blogsbykush.com** from Jekyll (Minimal Mistakes) to Hugo (PaperMod).

- **Branch**: built on `hugo-migration`; live on `main` since 2026-10-04 (`hugo-migration` kept as a frozen snapshot)
- **Theme**: PaperMod
- **Hugo**: Extended v0.163.3 (started on v0.140.0)
- **Key decision**: URLs preserved as `/:categories/:title/` (matches Jekyll `_config.yml:174`) to avoid SEO loss.

Format: `HH:MM [Phase N] change — detail`

---

## 2026-07-04

### Phase 0 — Setup
- Created git branch `hugo-migration` off `main` (Jekyll untouched).
- Installed Hugo Extended (later upgraded to v0.163.3, see Phase 4).
- Created this changelog.

### Phase 1 — Scaffold
- Added PaperMod as a git submodule at `themes/PaperMod`.
- Added Hugo artifacts (`/public/`, `/resources/_gen/`, `.hugo_build.lock`, `hugo_stats.json`) to `.gitignore`.
- Wrote `hugo.toml`: title/description/keywords/author, social icons (twitter, github, linkedin, medium, email, rss), Google site-verification tag, dark-mode toggle, TOC, reading time, breadcrumbs, code-copy; nav menu with URLs matching the live site (`/about/`, `/ml-made-easy/`, `/mlops-playground/`, `/my-bookshelf-chronicles/`, `/tags/`, `/year-archive/`, `/search/`); tags + categories taxonomies; home/RSS/JSON outputs (JSON drives search); goldmark `unsafe=true` for raw HTML in posts.

### Phase 2 — Content migration (`_migration/migrate_posts.py`)
- Migrated all **29 posts** `_posts/*.md` → `content/posts/*.md`.
- **URLs frozen to the live sitemap** via an explicit `url:` in every post (verified 1:1 against https://blogsbykush.com/sitemap.xml). No SEO breakage.
- Cleaned filenames (typos/spaces) WITHOUT changing URLs, e.g. `2023-05-14-data-lekage.md` → `data-leakage.md` while `url:` stays `/ml-made-easy/data-lekage/`.
- Front matter: dropped `layout:`/`toc:`/`seo_title:`; `tag:`→`tags:`; `excerpt:`→`summary:`; `seo_description:`→`description:`; scalar `categories:` → list; added `date:` (from filename, skipped where already present) + `url:`.
- Body: stripped Jekyll Liquid `{{ site.url }}{{ site.baseurl }}` (kept `/assets/...` paths); removed kramdown attr blocks (`{: .align-center}` ×29, `{: .notice--* }` ×58 → now plain blockquotes).
- Fixed visible typos with word-boundary matching so image filenames stay intact: `clasroom`→`classroom` (20 posts), `Lekage`→`Leakage` (title/body only, NOT `DataLekage.png`).

### Phase 3 — Assets
- Copied `assets/images` → `static/assets/images` (96 files) and `assets/cv` → `static/assets/cv` — **preserving `/assets/...` URLs** (incl. indexed `/assets/cv/KushBhatnagar_Resume.pdf`).
- Copied favicons, PWA icons, `site.webmanifest`, `browserconfig.xml`, and `CNAME` to `static/`.

### Phase 4 — Pages
- Upgraded Hugo 0.140.0 → **0.163.3 extended** (latest PaperMod requires Hugo ≥ 0.146 new template system).
- `content/about.md` (`/about/`), `content/terms.md` (`/terms/`) — migrated; removed `{: .notice--info}`; CV link preserved.
- `content/year-archive.md` (`/year-archive/`) + `content/archive.md` (`/archive/`) — PaperMod `archives` layout.
- `content/search.md` (`/search/`) — PaperMod `search` layout (fuse.js).
- Category landing pages `content/ml-made-easy.md`, `content/mlops-playground.md`, `content/my-bookshelf-chronicles.md` at their original custom URLs, backed by new `layouts/category-landing.html` (lists posts of the category, date-desc).

### Phase 5 — Integrations
- `layouts/_partials/extend_head.html` — GA gtag (`G-QWTLYBWXCL`) + AdSense loader (`ca-pub-4896166132316701`), gated to `HUGO_ENVIRONMENT=production`.
- `layouts/_partials/comments.html` — Disqus (`blogsbykush`), rendered on blog posts only.
- `layouts/_partials/extend_post_content.html` — Mailchimp newsletter, blog posts only.
- `assets/css/extended/custom.css` — styling for newsletter, category lists, blockquotes (partial replacement for old notice callouts), centered post images.

### Phase 6 — CI/CD & verification
- Added `.github/workflows/hugo.yml` (Hugo 0.163.3 extended, `HUGO_ENVIRONMENT=production`, deploy to GitHub Pages via Actions).
- Production build passes: **73 pages, 108 static files**, sitemap + RSS + search index generated.
- Verified all 37 live sitemap URLs resolve in `public/`; landings list posts; search/tags/year-archive/404/robots all work; GA/Disqus/newsletter present on posts and absent on about/terms.

---

### Theme evaluation (post-build)
- Trialled Stack, Blowfish, and Congo live on separate ports alongside PaperMod, sharing the same
  content/URLs.
- **Decision: keep PaperMod.** It was already fully wired (GA/Disqus/Mailchimp/search/landings/CI),
  is pure Hugo with no Node/Tailwind build dependency, and is the most battle-tested blog theme.
  Blowfish/Congo need a Tailwind v4 build toolchain; Stack's card thumbnails would require adding
  `cover:` to all 29 posts.
- Removed the trial themes (`themes/stack`, `themes/blowfish`, `themes/congo`) and `_preview/`.
- Added **`CLAUDE.md`** so future Claude Code sessions load project context automatically.

### Homepage photo (2026-09-21)
- PaperMod's `homeInfoParams` mode is text-only (no avatar), so the author photo from the old
  Jekyll home was missing. (Post/about images were fine — they render wherever embedded; the
  homepage and category listings are just text-only by PaperMod design.)
- Kept the intro + recent-posts homepage and added a round avatar beside the intro:
  overrode `layouts/_partials/home_info.html`, added `imageUrl`/`imageTitle` to
  `homeInfoParams` in `hugo.toml` (`/assets/images/kush-toon.jpg`), and styled `.home-avatar` /
  `.home-info-flex` in `assets/css/extended/custom.css` (responsive: stacks on mobile).
- Decided **not** to add `cover:` thumbnails to post lists — kept clean text listings.

## 2026-09-30 — Site refresh, phases 0–2 (see `PLAN_SITE_REFRESH.md`)

### Phase 0 — Migration hygiene
- RSS output renamed to **`/feed.xml`** (the Jekyll path; `/index.xml` no longer produced). Social RSS icon updated.
- AdSense: restored the Jekyll site's ad unit (slot `5967806966`) at the end of posts (production only) —
  the Hugo build previously loaded only the script, so no ads rendered unless Auto ads was on.
  Added **`static/ads.txt`** (never existed on the Jekyll site either).
- Untracked `.claude/settings.local.json`; README rewritten for Hugo.

### Phase 1 — Structure, homepage, brand
- **ML Made Easy → Concept Breakdown** (`_migration/concept_breakdown.py`): 20 posts moved to
  `/concept-breakdown/<slug>/` (typo slug fixed: `data-lekage` → `data-leakage`), `aliases` redirect every old
  URL, `disqus_identifier` keeps comment threads, `images:` set for previews/thumbnails; write-ups that lived only
  in `summary:` (never shown on the post page) copied into bodies; summaries shortened to one-line teasers; stray
  `n` removed from Statistics post. `/ml-made-easy/` landing redirects to `/concept-breakdown/`.
- Nav: Concept Breakdown · Tech Digest · Build Log · Archive · Search · About (MLOps Playground, Bookshelf
  Chronicles, Tags off-nav; pages still live).
- New pages: `/build-log/` (empty state), `/tech-digest/` (placeholder), `/subscribe/`.
- Homepage rewritten: "Learn. Build. Explain." tagline, proof line, Subscribe/LinkedIn CTAs, three pillars,
  latest 4 Concept Breakdown cards, then recent posts.
- Brand layer: comic palette, Fredoka headings, pill buttons, thumbnail card grid (WebP thumbnails generated
  by Hugo via a module mount of `static/assets/images`), mobile nav wraps, default social image
  `og-default.png`. Newsletter form extracted to one partial (provider swap = one file).

### Phase 2 — Concept Breakdown system
- `scripts/new_breakdown.py`: PDF → cropped 1080×1350 WebP slides, clean PDF, 1200×630 cover, draft bundle.
- `carousel` shortcode: scroll-snap swipe, arrows, keyboard, counter, dots, lazy/srcset, Download PDF.
- `/breakdown-post` skill for transcript + SEO write-up + LinkedIn copy.
- Pilot post **How LLMs Think** (`draft: true`, transcript read from slides — to be verified by Kush).

### Phase 2 — review feedback (Kush)
- Concept Breakdown posts made lean: comic carousel + "The concept in plain words" only. Removed TOC,
  "Why this matters for PMs", takeaways, FAQ and related links.
- Transcript kept but collapsed via new `transcript` shortcode ("Read this comic as text"), so the page
  stays lean while search engines and screen readers get the dialogue.
- `scripts/new_breakdown.py` template and `/breakdown-post` skill updated to the lean format.

### Phase 3 — Tech Digest / Digital Dhaba (2026-09-30)
- `content/tech-digest.md` placeholder replaced by the `tech-digest` section (`_index.md`, title
  "Digital Dhaba · Tech Digest"; nav label stays "Tech Digest").
- `scripts/add_digest.py`: imports an issue folder from Digital-Dhaba into a page bundle (HTML stored as
  `newsletter.txt`, `digest.json`, extracted `hero.jpg`, generated `index.md` with top stories).
- `layouts/tech-digest/single.html`: standalone issue page, original design untouched; build-time site bar,
  SEO/Open Graph, GA (prod), `{{VIEW_IN_BROWSER_URL}}`/`{{UNSUBSCRIBE_URL}}` removed, `{{FORWARD_URL}}` → mailto.
- `layouts/tech-digest/list.html`: archive with latest-issue hero card; homepage "New Tech Digest" strip.
- First issue imported (2026-09-27). Auto-publish workflow for Digital-Dhaba in `docs/tech-digest/`.

### Status snapshot (2026-09-30, end of session)
- PRs #1 and #3 merged into `hugo-migration`; Digital-Dhaba auto-publish verified (issue 2026-09-30).
- Not live: go-live (PR #2) waits on Kush's extra pre-launch changes. Phase 4 parked.
- "Where we left off" now lives at the top of `PLAN_SITE_REFRESH.md`; CLAUDE.md points new sessions there.

## 2026-10-01 — Phase 4 kickoff (decisions only, nothing built yet)
- Provider: **Kit Free Plan** replaces Mailchimp ("Built with Kit" badge accepted).
- Email model: one automatic email per new blog post + the full Digital Dhaba HTML every Saturday.
- Mailchimp list: re-permission via one final Mailchimp email → Kit double opt-in form; no bulk import
  (imported contacts would count as confirmed). Subscriber audit script now optional.
- Sending: GitHub Actions → Kit API v4 (not RSS-to-email); per-post detection excludes Tech Digest;
  digest send added to the Digital-Dhaba workflow.
- Kit Free facts recorded in `PLAN_SITE_REFRESH.md` (API v4, custom template required, double opt-in,
  verified sending domain, no auto-tag-by-form → one form per source).
- Build plan proposed in `PLAN_SITE_REFRESH.md` → Phase 4; awaiting approval.

## 2026-10-01 — Phase 4 build (4a/4b)
- Forms: `newsletter_form.html` posts to Kit (one form per source: blog / linkedin / mailchimp; IDs in
  `hugo.toml` `params.kit.forms`, empty → legacy Mailchimp form). `/subscribe/` uses the LinkedIn form; new
  `/stay-subscribed/` (noindex, not in sitemap) for the Mailchimp re-permission email.
- `/posts.json` (posts only, no Tech Digest) via a `postsjson` output format.
- New-post emails: `scripts/kit_notify_posts.py` (plan before deploy by diffing live vs new `/posts.json`, send
  after deploy) + `notify` job in `hugo.yml`. Guards: no live `posts.json` → nothing sent (covers go-live),
  ≤3 per deploy, ≤14 days old.
- Digest emails: `scripts/kit_send_digest.py` (hero → hosted URL, placeholders → Kit tag / web URL / mailto,
  scheduled Sat 08:00 IST, dedupe by subject) + email step in `docs/tech-digest/publish-to-blog.yml`.
- `scripts/kit_api.py`: stdlib Kit API v4 client with dry run (`KIT_SEND`), test mode (`KIT_TEST_TAG_ID`).
- Docs: `docs/NEWSLETTER.md` (setup, switches, re-permission email), `docs/kit/email-template.html`.
- Tested against a mock Kit API; real Kit API details to confirm on Kush's first test send.

## 2026-10-03 — Learning Notes, two-email model, Thursday digest
- New **Learning Notes** section (`/learning-notes/`), separate from Build Log; in the menu, Archive moved to the
  footer (with Subscribe and Terms). Placeholder note "Training an AI for one skill quietly changes its other
  answers" (to be rewritten/verified by Kush). Archetypes for Learning Notes and Build Log entries.
- Email model changed to **two emails**: Digital Dhaba (Thursday 07:00 IST) + weekly letter (Sunday 09:00 IST,
  all posts from the last 7 days). Removed per-post emails (`kit_notify_posts.py`, `hugo.yml` notify job);
  added `scripts/kit_weekly_roundup.py` + `.github/workflows/weekly-roundup.yml`.
- Digest default send slot Saturday 08:00 → **Thursday 07:00 IST**; site copy and docs updated.
- Tech Digest page copy now says Claude curates the issue.
- `kit_api.py`: clear error when Kit can't be reached.

### 2026-10-03 — Writing skills
- New skills `/learning-note` and `/build-log-entry`; `/breakdown-post` now reads the same shared rules
  (`.claude/BLOG_WRITING_RULES.md`): assemble Kush's own words into the templates, never write the core
  takeaway, never invent numbers, research files only for metadata/links, `draft: true`, link check + build.
- LinkedIn copy removed from `/breakdown-post`; `content/posts/how-llms-think/linkedin.txt` deleted;
  `ignoreFiles` now only excludes `transcript.txt`. LinkedIn posts come from Sahayak.
- `scripts/check_links.py`: link checker that distinguishes broken links from unreachable ones.

### 2026-10-03 — Homepage, About page, photo, CV (brand review)
- Photo: `kush-toon.jpg` (ToonMe watermark, ghost artefact) → `static/assets/images/kush-avatar.jpg`, made from
  Kush's own `Kush.png` (white background swapped for light brand blue, square 400px). Used on homepage + About.
- Homepage (`hugo.toml`): proof line no longer claims "5+ years building AI/GenAI & cloud"; intro leads with
  "I lead an enterprise AI platform by day and build my own AI products after hours". Site description and
  keywords drop MLOps/AWS (past skills). Employer not named, no consulting / "open to roles" (Kush's call).
- `layouts/home.html` (copy of PaperMod `list.html`): "Recent posts" skips the 4 breakdowns already shown as cards.
- About page rewritten (`content/about.md`, URL unchanged): who, what I work on (resume facts, no employer),
  what I'm building (generic, no project names), how the blog works, the path, get in touch. One small
  learning-loop image instead of two large ones; share bar off.
- CV (`/assets/cv/KushBhatnagar_Resume.pdf`, URL unchanged): replaced the 2023 CV with Job-Hunting's
  master resume, re-rendered without the phone number (Job-Hunting repo untouched).
- Four old comic summaries: "in our latest classroom conversation." → "in a classroom comic.", missing spaces fixed.

- Kush's feedback on About: description no longer repeated under the title (`hideDescription: true`, handled in
  `extend_head.html`; meta description kept), "What I work on" is one paragraph, "The path here" removed (values
  line moved into "How this blog works"), CV link removed, X and Medium added to "Get in touch".
- Share buttons on posts: X and LinkedIn only (`ShareButtons` in `hugo.toml`).
- Social icon Twitter bird → X logo (`x.com/bhatnagarkush`); About "Get in touch" shows the same icon row
  via the new `{{< social-icons >}}` shortcode (`layouts/_shortcodes/social-icons.html`).

### 2026-10-03 — Mailchimp subscriber audit
- `scripts/audit_subscribers.py`: sorts a Mailchimp export into keep / review / junk (bot name fields,
  throwaway domains, the late-2024 onward bot wave); prints counts only. Kush's list: 267 → 19 / 15 / 233.
- `docs/NEWSLETTER.md`: re-permission email now goes only to the audited keep (+ approved review) segment.
- `.gitignore`: Mailchimp exports and audit output can't be committed.

- **Revised same day (Kush): direct upload instead of re-permission.** Kush uploads the audited real
  subscribers (~15) to Kit with tag `from-mailchimp`, then closes Mailchimp after go-live. Removed
  `/stay-subscribed/` and the `mailchimp` form slot; `docs/NEWSLETTER.md` rewritten for the upload.
- `docs/tech-digest/publish-to-blog.yml`: `BLOG_BRANCH` back to `hugo-migration` (the copy said `main`, which
  would have pushed issues to the live Jekyll site if copied before go-live).
- Merged `hugo-migration` (auto-published Tech Digest 2026-10-03) into the feature branch.

## 2026-10-04 — Kit connected
- Kush set up Kit: account, verified sending domain (SPF/DKIM/DMARC), `kush@blogsbykush.com`, one form with
  double opt-in, v4 API key as `KIT_API_KEY` secret in both repos.
- Site: one Kit form (`params.kit.form = "10000596"`) for every signup box; per-source forms removed
  (`newsletter_form.html`, `subscribe` shortcode, `/subscribe/`). No Mailchimp form left in the build.
- `docs/NEWSLETTER.md` setup cut to what's done + the remaining test steps; template and test tag optional.
- First real Kit run (Digital-Dhaba workflow, issue 2026-10-03): broadcast created and scheduled for Thu 07:00 IST.
  Kush's feedback: digest subject is now just "Digital Dhaba — <date>" and preview text just the issue's dek
  (no story names). Hero image is broken until go-live (hosted on blogsbykush.com).
- Tech Digest archive: removed issues 2026-09-27 and 2026-09-30 (Kush); the site starts with 2026-10-03.
  They stay in Digital-Dhaba; the workflow only republishes issues whose files change.
- Placeholder Learning Note set to `draft: true` for go-live (not Kush's words yet); Learning Notes shows its
  empty state until the first real note.
- Digest email: manual runs of the Digital-Dhaba workflow get a `send_now` tick box (`DIGEST_SEND_NOW`) to email
  right away instead of scheduling, for an inbox test while Kush is the only subscriber.

## 2026-10-04 — GO-LIVE
- Kush switched Pages → GitHub Actions; PR #6, #7 merged into `hugo-migration`; **PR #2 merged into `main`**
  (`4ef1146`); "Deploy Hugo site to Pages" build + deploy succeeded.
- Digital-Dhaba `publish-to-blog.yml`: `BLOG_BRANCH: main`.

## 2026-10-04 — After go-live
- Build Log landing: empty-state text no longer mentions the AI content tool (Sahayak stays unannounced).
- Published (Kush): *How LLMs Think* and the Learning Note (dates set to 2026-10-04 so the Sunday letter picks them up).
- First Build Log entry drafted with `/build-log-entry` from Kush's notes:
  `content/posts/digital-dhaba-ai-newsletter-that-cannot-make-up-news.md`; Kush confirmed the CHECK items → published.
- CLAUDE.md rewritten for the live state (branch workflow = PR into `main`; publishing checklist; cleanup list).
- Weekly letter subject now plain: "Blogs by Kush — week of <date>"; first letter sent by a manual run (Kush's choice).

## 2026-10-05
- Homepage: "Latest Concept Breakdowns" shows 2 cards instead of 4 (Kush: too much scrolling on mobile before
  "Recent posts"). Count is `homeInfoParams.breakdownCards` in `hugo.toml`, shared with the Recent-posts filter.
- Handoff docs for new chats: CLAUDE.md gets "Kush's rules" (brand, email, git decisions) and "Resuming in a new
  chat"; PLAN_SITE_REFRESH.md STATUS rewritten for the live site (stale pre-launch table and go-live checklist removed).
- CLAUDE.md: "LinkedIn tracking" section (UTM tag format, where to read results in GA).
- Docs tidy (Kush): `docs/tech-digest/publish-to-blog.yml` copy now says `BLOG_BRANCH: main` (matches the live
  Digital-Dhaba workflow); `docs/NEWSLETTER.md` and `docs/TECH_DIGEST.md` setup steps marked done (only "close
  Mailchimp" left); stale pre-go-live notes removed from PLAN and this changelog. Kush: keep branch
  `hugo-migration` (frozen snapshot, behind `main`); delete merged `claude/*` branches.

## Known deviations from the original MIGRATION_PLAN.md
- **URLs preserved** as `/:categories/:title/` (plan proposed `/posts/:slug/`) — frozen to the live sitemap for zero SEO loss.
- **Assets kept under `/assets/...`** (plan proposed `/images/...`) — avoids breaking indexed image/CV URLs.
- **Built in-repo on `hugo-migration` branch** (plan proposed a separate sibling dir).
- **Linux install + Hugo 0.163.3** (plan assumed Windows winget + 0.140.0).
- Migration script is **Python** (plan used PowerShell — not available on this Linux/WSL host).

## Go-live steps (all done 2026-10-04)
Review locally, switch Pages to GitHub Actions, merge into `main`. Still open: removing the Jekyll files and
`_migration/` (cleanup PR) and the Disqus check on moved posts; tracked in `PLAN_SITE_REFRESH.md` → STATUS.
