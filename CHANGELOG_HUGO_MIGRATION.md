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
