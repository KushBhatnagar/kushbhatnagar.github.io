# CLAUDE.md — blogsbykush.com

Context for Claude Code sessions on this repo.

## What this repo is

The source for **https://blogsbykush.com** (GitHub Pages repo `kushbhatnagar.github.io`), a
personal blog by Kush Bhatnagar about AI, ML and product (older MLOps/AWS/book posts stay live).
Positioning: **"Learn. Build. Explain."**. Kush is a Technical PM (17+ yrs, 5+ on AI/GenAI and cloud)
writing for PMs, PM aspirants and non-technical folks in tech. Sections follow the loop:
**Tech Digest** (learn, weekly, Claude-curated) + **Learning Notes** (learn, Kush's own notes on sources),
**Build Log** (build in public), **Concept Breakdown** (explain, comics; formerly "ML Made Easy").
Learning Notes and Build Log entries start from `archetypes/` (templates from Sahayak `content/*-PLAN.md`). Older series `mlops` and `bookshelf` stay live but are off the nav.
Roadmap and checklist: **`PLAN_SITE_REFRESH.md`**.

## ▶ Start here (new session)

Read **`PLAN_SITE_REFRESH.md` → "STATUS — where we left off"** first: current state and open items.
Update that STATUS section (and the changelog) at the end of every session.
Snapshot (2026-10-05): **LIVE** on Hugo since 2026-10-04 (PR #2). Both emails work (first Digital Dhaba test and
first Sunday letter sent). Published: How LLMs Think, first Learning Note, first Build Log entry (Digital Dhaba).
Homepage shows 2 breakdown cards (PR #11) and 2 recent posts (`recentPosts`, 2026-10-06). Launch cleanup finished 2026-10-05: Jekyll files removed (PR #14),
old branches deleted, Mailchimp closed, Search Console sitemap + indexing requested. Open: watch the first automatic
emails (Thu 2026-10-08, Sun 2026-10-11).
Also read **"Kush's rules"** below before writing anything for the site.

## Current state: live on Hugo (since 2026-10-04)

- **`main`** = the live site. GitHub Pages builds from **GitHub Actions** (`.github/workflows/hugo.yml`) on every push
  to `main`. Work goes on a feature branch → PR into `main` → merge = deploy (~2 min).
- **`hugo-migration`** = the old staging branch, fully merged; deleted 2026-10-05 (Kush). PRs #1–#9 hold the history.
- The Jekyll files (`_config.yml`, `_posts/`, `_pages/`, layouts, Gemfile, root favicons, the Jekyll copies in root
  `assets/images|cv|js`) were removed on 2026-10-05; find them in git history if ever needed. Root `assets/` now holds
  only Hugo's `css/extended/`. Live files are in `static/`.
- Full record of every change: **`CHANGELOG_HUGO_MIGRATION.md`**. Original migration analysis:
  `git show 8c40350:MIGRATION_PLAN.md`.

## Hugo setup

- **Theme:** PaperMod (git submodule at `themes/PaperMod`). It uses Hugo's new template system
  (`layouts/_partials/`, flat `layouts/`), which requires **Hugo Extended ≥ 0.146**.
- **Hugo binary:** Extended **0.163.3** (CI pins the same version). Cloud sessions start without it: download
  `hugo_extended_0.163.3_linux-amd64.tar.gz` from the gohugoio/hugo GitHub release into `~/bin` (or the scratchpad)
  and run with `export PATH="$HOME/bin:$PATH"`.
- **Config:** `hugo.toml`.

### Build & preview

```bash
export PATH="$HOME/bin:$PATH"
hugo server                         # dev preview at http://localhost:1313
HUGO_ENVIRONMENT=production hugo --gc --minify   # production build → public/
```

> The **dev server intentionally excludes** Google Analytics, AdSense, and Disqus — those are
> gated to `hugo.Environment == "production"`. They only appear in the CI/production build.

## Critical conventions — do not break these

1. **URLs are frozen to the live sitemap for SEO.** Every post/page sets an explicit `url:` in
   front matter matching the exact current live URL (verified against blogsbykush.com/sitemap.xml).
   When adding/renaming content, preserve existing URLs; use Hugo `aliases` for any change.
   - Post URLs follow `/:category/:slug/`; the 5 old uncategorized posts sit at root `/:slug/`.
   - Concept Breakdown posts moved from `/ml-made-easy/<slug>/` to `/concept-breakdown/<slug>/`: each
     keeps `aliases: [old url]` (redirect page) and `disqus_identifier: old url` (keeps comment threads).
     Never remove those two fields.
2. **Assets stay under `/assets/...`.** Images live in `static/assets/images/`, CV in
   `static/assets/cv/` — preserving indexed URLs like `/assets/cv/KushBhatnagar_Resume.pdf`.
   Posts reference images as `/assets/images/...` (raw `<img>` tags and markdown both work;
   goldmark `unsafe = true` is enabled).
3. **Post front matter** (Hugo/PaperMod): `title`, `date`, `categories: ["..."]`, `tags: [...]`,
   `summary` (list blurb), `description` (SEO meta), `url` (frozen). No Jekyll `layout:`/`seo_*`.

## Adding a Concept Breakdown (comic) post

1. `python3 scripts/new_breakdown.py Comic.pdf --title "How LLMs Think" [--transcript convo.txt]`
   → page bundle `content/posts/<slug>/` (4:5 WebP slides, clean PDF, cover.jpg, `draft: true`).
2. Run the **`/breakdown-post`** skill (`.claude/skills/breakdown-post/SKILL.md`) → collapsed transcript
   (`transcript` shortcode), "The concept in plain words", SEO fields, slide alt text.
   **Keep these pages lean** (Kush's call): comic + plain-words section only, no TOC/FAQ/extra sections.
3. Kush reviews, sets `draft: false`. (`transcript.txt` is in `ignoreFiles`, never published.)

## Writing skills (Kush, 2026-10-03)

Three skills, one per post type, all bound by **`.claude/BLOG_WRITING_RULES.md`**:
`/breakdown-post` (comic PDF + conversation), `/learning-note` (Kush's notes + source link),
`/build-log-entry` (Kush's build notes). They **assemble Kush's words into the template**; they never write
his takeaway / "one thing", never invent numbers, treat Claude-written research files as reference only,
leave `draft: true`, and run `scripts/check_links.py` + a build. **No LinkedIn copy anywhere**: LinkedIn
posts are generated in Sahayak from the finished post.

## Tech Digest (Digital Dhaba) issues

Generated in the private repo `KushBhatnagar/Digital-Dhaba`; a GitHub Action there runs
`scripts/add_digest.py issues/<date>` and pushes to this repo (auto-publish). Each issue is a bundle in
`content/tech-digest/<date>/` (`newsletter.txt` = issue HTML byte-for-byte, `digest.json`, `hero.*`,
generated `index.md` with `build.publishResources: false`). `layouts/tech-digest/single.html` serves
the HTML standalone with site bar / SEO / GA / fixed placeholders; `list.html` is the archive.
Never edit `newsletter.txt` by hand; re-import instead. Setup and flow: `docs/TECH_DIGEST.md`.

## Newsletter (Kit) — Phase 4

Kit Free Plan replaces Mailchimp. Signup forms: `layouts/_partials/newsletter_form.html` (one Kit form, ID `10000596` in
`hugo.toml` → `params.kit.form`; empty → no signup box). **Only two emails** (Kush, 2026-10-03), via Kit API v4 from GitHub Actions, never Kit RSS:
1. **Digital Dhaba**, Thursday 07:00 IST → Digital-Dhaba workflow (`scripts/kit_send_digest.py`).
2. **Weekly letter**, Sunday 09:00 IST → `.github/workflows/weekly-roundup.yml` (`scripts/kit_weekly_roundup.py`):
   every post dated in the last 7 days (Concept Breakdown, Build Log, Learning Notes) in one email; none → no email.
No per-post emails. Switches are repo variables (`KIT_ROUNDUP_ENABLED`, `KIT_DIGEST_ENABLED`, `KIT_SEND`,
`KIT_TEST_TAG_ID` = test mode). Setup: `docs/NEWSLETTER.md`. Mailchimp list: audited with
a one-off script (removed 2026-10-05; in git history), the real ~15 uploaded to Kit by Kush; Mailchimp closed 2026-10-05.

## Layout of the Hugo site

```
hugo.toml                         # config: menus, homepage copy (homeInfoParams), socials, params
content/
  posts/*.md                      # older posts (section "posts")
  posts/<slug>/index.md           # page bundles: comic posts with slide-*.webp, <slug>.pdf, cover.jpg
  concept-breakdown.md            # category landings at custom URLs, backed by
  build-log.md learning-notes.md  #   layouts/category-landing.html (grid: true → thumbnail cards)
  tech-digest/_index.md           # Tech Digest archive (layouts/tech-digest/list.html)
  tech-digest/<date>/             # one bundle per Digital Dhaba issue (layouts/tech-digest/single.html)
  mlops-playground.md my-bookshelf-chronicles.md   # live, off-nav
  subscribe.md                    # /subscribe/ — the link shared on LinkedIn
  about.md terms.md year-archive.md archive.md search.md
layouts/
  category-landing.html           # custom: lists/grids posts of one category, empty state
  _shortcodes/carousel.html       # LinkedIn-style slide carousel (bundle slide-* resources)
  _shortcodes/transcript.html     # collapsed "Read this comic as text" block (SEO + accessibility)
  _shortcodes/subscribe.html      # newsletter form inside content
  _partials/
    home_info.html                # homepage intro, CTAs, pillars, latest breakdown cards
    post_card.html thumbnail.html # thumbnail cards (WebP via Hugo image processing)
    newsletter_form.html          # ONLY place with newsletter-provider markup (Kit forms per source)
    extend_head.html              # Fredoka font, GA gtag + AdSense loader (prod only)
    extend_post_content.html      # AdSense unit (prod) + newsletter — posts only
    comments.html                 # Disqus — posts only; honours disqus_identifier
assets/css/extended/custom.css    # brand layer (colours from the comics), cards, carousel
static/assets/{images,cv}/        # assets (URLs preserved); mounted into assets/ for thumbnails
static/ads.txt                    # AdSense authorised seller
scripts/new_breakdown.py          # PDF → Concept Breakdown page bundle
scripts/add_digest.py             # Digital Dhaba issue folder → content/tech-digest/<date>/
scripts/kit_api.py                # Kit API v4 client (stdlib): dry run / test mode / dedupe
scripts/kit_send_digest.py        # Digital Dhaba email, Thursday 07:00 IST
scripts/kit_weekly_roundup.py     # Sunday weekly letter: all posts from the last 7 days
.github/workflows/weekly-roundup.yml  # cron for the weekly letter (Sun 09:00 IST)
layouts/home.postsjson.json       # /posts.json (posts only, no Tech Digest), read by the weekly letter
archetypes/learning-note.md build-log.md  # `hugo new --kind learning-note content/posts/<slug>.md`
docs/NEWSLETTER.md                # Kit setup, switches, moving the audited Mailchimp list
docs/kit/email-template.html      # minimal Kit email template
docs/TECH_DIGEST.md               # Tech Digest pipeline + one-time setup
docs/tech-digest/publish-to-blog.yml  # workflow to copy into Digital-Dhaba
.claude/BLOG_WRITING_RULES.md      # shared rules for the three writing skills
.claude/skills/breakdown-post/    # Concept Breakdown body (comic PDF + conversation)
.claude/skills/learning-note/     # Learning Note from Kush's notes + source
.claude/skills/build-log-entry/   # Build Log entry from Kush's build notes
scripts/check_links.py            # link checker used by the skills
.github/workflows/hugo.yml        # deploy to GitHub Pages via Actions (prod build)
_migration/*.py                   # one-off Jekyll→Hugo converters (kept for audit; their Jekyll inputs are gone)
```

## External integrations (IDs)

- Google Analytics (gtag): `G-QWTLYBWXCL`
- Google AdSense: `ca-pub-4896166132316701`, ad unit slot `5967806966`
- Disqus shortname: `blogsbykush`
- Kit (newsletter, Phase 4): form ID in `hugo.toml` `params.kit.form`; API key = secret `KIT_API_KEY` in both repos
- Mailchimp (closed 2026-10-05; fallback form removed from code): `blogsbykush.us21.list-manage.com` (u=`c937565c206ad87a847339f0f`, id=`e0273fdf87`)

## Publishing a post (Kush's checklist)

In the post's `.md` file, front matter at the top:
- `draft: true` → `draft: false` (or delete the line) when it's ready.
- `date: YYYY-MM-DD` = **the day you publish** (not the day you started). The Sunday letter emails every post dated in
  the last 7 days; an old date means it's never emailed. The writing skills set this; re-set it if a draft waited.
- Commit on a branch → PR into `main` → merge. Live in ~2 minutes; in the next Sunday letter automatically.

## Brand

Palette from the comics: blue `#11a8cc` (links use darker `#0a7a96`), orange `#f4a33a`, cream `#fff6d1`,
ink `#131313`. Headings/logo in **Fredoka**. Default social preview: `static/assets/images/og-default.png`.

## Kush's rules (decided, don't re-ask)

Content and brand:
- Don't name his employer (HP) anywhere on the site. Say "an enterprise AI platform".
- Don't mention consulting or "open to roles". Don't reveal Sahayak or other unreleased projects: keep projects
  generic ("building AI products"). MLOps/AWS are past skills; the focus is AI + product management.
- Old career: "software engineer", never "software tester"; keep it subtle, focus on product.
- Socials shown: X (icon only), GitHub, LinkedIn, Medium, email, RSS. No Facebook/Reddit/Telegram/WhatsApp. No CV link.
- About page: no repeated intro line under the heading (`hideDescription`), no share bar.
- Concept Breakdown pages stay lean (comic + plain words only).

Email (Kit):
- Subjects plain, no prefixes: Digital Dhaba subject = issue title, preview = issue dek.
  Sunday letter subject = "Blogs by Kush — week of <d Mon yyyy>".
- Signups: every site signup box POSTs straight to Kit form `10000596` (Kush's inline form; its settings such as
  double opt-in and confirmation email apply). **No welcome email or sequence** (Kush, 2026-10-05: keep it light);
  the confirmation email (edited by Kush in Kit) does the welcoming. Kit's JS embed (`cfe26ba09f`) is **not** used.
  The Kit **API v4** key is used only by GitHub Actions to create/send the two broadcasts.
- Link to share on LinkedIn: `https://blogsbykush.com/subscribe/`; for Digital Dhaba posts, the latest issue page.
- Secrets: API keys only as repo secrets, never in chat or git. Subscriber data never in git (run audits locally).

Git:
- Ask Kush before deleting any branch. Merged `claude/*` session branches: delete after merge (Kush, 2026-10-05). Never push straight to `main`: branch → PR → merge.

## LinkedIn tracking (Google Analytics, UTM tags)

Nothing to set up in GA or on the site: GA reads the tags from the link automatically.
Share links on LinkedIn with tags added:

    https://blogsbykush.com/<page>/?utm_source=linkedin&utm_medium=social&utm_campaign=<post-name>

- `utm_source=linkedin`, `utm_medium=social`: always the same, lowercase.
- `utm_campaign`: one name per LinkedIn post, lowercase with hyphens (e.g. `site-launch`, `how-llms-think`).
- Optional `utm_content=post` or `utm_content=comment` to compare link placement.
- Before posting: run the tagged link through linkedin.com/post-inspector (refreshes the preview), and
  check GA → Reports → Realtime shows `linkedin / social` (open the link with no ad blocker).
- Results (after 24–48 h): GA → Reports → Acquisition → Traffic acquisition → switch the first column to
  "Session source / medium" (LinkedIn traffic) or "Session campaign" (per post). Pages read:
  Engagement → Pages and screens, filter Session source = linkedin.
- Signups aren't in GA (the form posts to Kit): compare Kit → Subscribers with GA visits for the same day.

## Resuming in a new chat

New sessions load this file automatically. Start with: *"Read CLAUDE.md and the STATUS in PLAN_SITE_REFRESH.md,
then <task>."* Full history of what changed and why: `CHANGELOG_HUGO_MIGRATION.md`. Older chat transcripts are not
needed; if something isn't in these three files, it wasn't decided.

## Preferences observed

- Wants to **know what will change before execution** and keep a running changelog
  (`CHANGELOG_HUGO_MIGRATION.md`) of what changed and when.
- Wants everything **automated after initial setup** (newsletter, Tech Digest publishing).
- Values simplicity and low maintenance — this is why PaperMod (pure Hugo, no Node/Tailwind
  build) was chosen over Blowfish/Congo/Stack.
