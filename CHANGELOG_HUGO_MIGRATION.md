# Hugo Migration Changelog

Tracks every change made while migrating **blogsbykush.com** from Jekyll (Minimal Mistakes) to Hugo (PaperMod).

- **Branch**: `hugo-migration` (Jekyll `main` stays intact until verified & merged)
- **Theme**: PaperMod
- **Hugo**: Extended v0.140.0
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

## Known deviations from the original MIGRATION_PLAN.md
- **URLs preserved** as `/:categories/:title/` (plan proposed `/posts/:slug/`) — frozen to the live sitemap for zero SEO loss.
- **Assets kept under `/assets/...`** (plan proposed `/images/...`) — avoids breaking indexed image/CV URLs.
- **Built in-repo on `hugo-migration` branch** (plan proposed a separate sibling dir).
- **Linux install + Hugo 0.163.3** (plan assumed Windows winget + 0.140.0).
- Migration script is **Python** (plan used PowerShell — not available on this Linux/WSL host).

## Remaining manual steps (not yet done)
1. Review the site locally: `~/bin/hugo server` → http://localhost:1313 (dev build excludes GA/AdSense/Disqus).
2. In GitHub repo **Settings → Pages**, switch source from "Deploy from branch" to **GitHub Actions** (required before merging to `main`).
3. Merge `hugo-migration` → `main` to trigger the deploy workflow.
4. Post-merge: remove the now-unused Jekyll files (`_config.yml`, `_posts/`, `_pages/`, `_layouts/`, `_includes/`, `_sass/`, `_data/`, `Gemfile*`, `index.md`, `feed.xml`, `archive.html`) and the `_migration/` helper.
5. Verify Disqus threads still map (identifiers use `RelPermalink`, matching old paths).
