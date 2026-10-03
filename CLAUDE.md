# CLAUDE.md — blogsbykush.com

Context for Claude Code sessions on this repo.

## What this repo is

The source for **https://blogsbykush.com** (GitHub Pages repo `kushbhatnagar.github.io`), a
personal blog by Kush Bhatnagar about Machine Learning, MLOps, AWS, and books.
Positioning: **"Learn. Build. Explain."**. Kush is a Technical PM (17+ yrs, 5+ on AI/GenAI and cloud)
writing for PMs, PM aspirants and non-technical folks in tech. Sections follow the loop:
**Tech Digest** (learn, weekly), **Build Log** (build in public), **Concept Breakdown** (explain, comics;
formerly "ML Made Easy"). Older series `mlops` and `bookshelf` stay live but are off the nav.
Roadmap and checklist: **`PLAN_SITE_REFRESH.md`**.

## ▶ Start here (new session)

Read **`PLAN_SITE_REFRESH.md` → "STATUS — where we left off"** first: it has the current state, open items
and the go-live checklist. Update that STATUS section (and the changelog) at the end of every session.
Snapshot (2026-09-30): Phases 0–3 merged into `hugo-migration`; **not live yet**; Phase 4 (newsletter
provider + subscriber cleanup) parked by Kush; Kush wants a few more changes before go-live (PR #2).

## Current state: mid-migration Jekyll → Hugo

The site is being migrated from **Jekyll (Minimal Mistakes)** to **Hugo (PaperMod)**.

- **`main` branch** = the live Jekyll site (untouched during migration).
- **`hugo-migration` branch** = the new Hugo site (staging). Feature work goes on branches merged into it via PR.
  Go-live = PR #2 (`hugo-migration` → `main`), after switching Pages to GitHub Actions.
- Both stacks currently coexist in the tree on `hugo-migration`; Jekyll's underscore dirs
  (`_config.yml`, `_posts/`, `_pages/`, `_layouts/`, `_includes/`, `_sass/`, `_data/`) are
  ignored by Hugo and will be deleted once the migration is verified and merged.
- Full step-by-step record of every change: **`CHANGELOG_HUGO_MIGRATION.md`**.
- Original migration analysis: **`MIGRATION_PLAN.md`** (deleted from working tree; recover with
  `git show 8c40350:MIGRATION_PLAN.md`).

## Hugo setup

- **Theme:** PaperMod (git submodule at `themes/PaperMod`). It uses Hugo's new template system
  (`layouts/_partials/`, flat `layouts/`), which requires **Hugo Extended ≥ 0.146**.
- **Hugo binary:** installed at `~/bin/hugo` (Extended **0.163.3**). Not on the default PATH —
  run with `export PATH="$HOME/bin:$PATH"` or call `~/bin/hugo` directly. CI pins the same version.
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
   (`transcript` shortcode), "The concept in plain words", SEO fields, slide alt text, `linkedin.txt`.
   **Keep these pages lean** (Kush's call): comic + plain-words section only, no TOC/FAQ/extra sections.
3. Kush reviews, sets `draft: false`. (`linkedin.txt` / `transcript.txt` are in `ignoreFiles`, never published.)

## Tech Digest (Digital Dhaba) issues

Generated in the private repo `KushBhatnagar/Digital-Dhaba`; a GitHub Action there runs
`scripts/add_digest.py issues/<date>` and pushes to this repo (auto-publish). Each issue is a bundle in
`content/tech-digest/<date>/` (`newsletter.txt` = issue HTML byte-for-byte, `digest.json`, `hero.*`,
generated `index.md` with `build.publishResources: false`). `layouts/tech-digest/single.html` serves
the HTML standalone with site bar / SEO / GA / fixed placeholders; `list.html` is the archive.
Never edit `newsletter.txt` by hand; re-import instead. Setup and flow: `docs/TECH_DIGEST.md`.

## Layout of the Hugo site

```
hugo.toml                         # config: menus, homepage copy (homeInfoParams), socials, params
content/
  posts/*.md                      # older posts (section "posts")
  posts/<slug>/index.md           # page bundles: comic posts with slide-*.webp, <slug>.pdf, cover.jpg
  concept-breakdown.md            # category landings at custom URLs, backed by
  build-log.md                    #   layouts/category-landing.html (grid: true → thumbnail cards)
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
    newsletter_form.html          # ONLY place with newsletter-provider markup
    extend_head.html              # Fredoka font, GA gtag + AdSense loader (prod only)
    extend_post_content.html      # AdSense unit (prod) + newsletter — posts only
    comments.html                 # Disqus — posts only; honours disqus_identifier
assets/css/extended/custom.css    # brand layer (colours from the comics), cards, carousel
static/assets/{images,cv}/        # assets (URLs preserved); mounted into assets/ for thumbnails
static/ads.txt                    # AdSense authorised seller
scripts/new_breakdown.py          # PDF → Concept Breakdown page bundle
scripts/add_digest.py             # Digital Dhaba issue folder → content/tech-digest/<date>/
docs/TECH_DIGEST.md               # Tech Digest pipeline + one-time setup
docs/tech-digest/publish-to-blog.yml  # workflow to copy into Digital-Dhaba
.claude/skills/breakdown-post/    # writes the post body + LinkedIn copy
.github/workflows/hugo.yml        # deploy to GitHub Pages via Actions (prod build)
_migration/*.py                   # one-off converters (kept for audit)
```

## External integrations (IDs)

- Google Analytics (gtag): `G-QWTLYBWXCL`
- Google AdSense: `ca-pub-4896166132316701`, ad unit slot `5967806966`
- Disqus shortname: `blogsbykush`
- Mailchimp: `blogsbykush.us21.list-manage.com` (u=`c937565c206ad87a847339f0f`, id=`e0273fdf87`)

## Remaining steps to finish the migration

See the **go-live checklist** in `PLAN_SITE_REFRESH.md` (Pages → GitHub Actions *before* merging PR #2,
switch the Digital-Dhaba workflow to `BLOG_BRANCH: main`, post-launch checks, then delete the Jekyll files).

## Brand

Palette from the comics: blue `#11a8cc` (links use darker `#0a7a96`), orange `#f4a33a`, cream `#fff6d1`,
ink `#131313`. Headings/logo in **Fredoka**. Default social preview: `static/assets/images/og-default.png`.

## Preferences observed

- Wants to **know what will change before execution** and keep a running changelog
  (`CHANGELOG_HUGO_MIGRATION.md`) of what changed and when.
- Wants everything **automated after initial setup** (newsletter, Tech Digest publishing).
- Values simplicity and low maintenance — this is why PaperMod (pure Hugo, no Node/Tailwind
  build) was chosen over Blowfish/Congo/Stack.
