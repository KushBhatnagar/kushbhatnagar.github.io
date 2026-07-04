# CLAUDE.md — blogsbykush.com

Context for Claude Code sessions on this repo.

## What this repo is

The source for **https://blogsbykush.com** (GitHub Pages repo `kushbhatnagar.github.io`), a
personal blog by Kush Bhatnagar about Machine Learning, MLOps, AWS, and books.
**29 posts** across 3 series: `ml-made-easy` (comic/conversation explainers), `mlops`, `bookshelf`.

## Current state: mid-migration Jekyll → Hugo

The site is being migrated from **Jekyll (Minimal Mistakes)** to **Hugo (PaperMod)**.

- **`main` branch** = the live Jekyll site (untouched during migration).
- **`hugo-migration` branch** = the new Hugo site (do work here). ← *active branch*
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
   - Example of a deliberately frozen typo: `content/posts/data-leakage.md` has clean filename +
     fixed title, but `url: /ml-made-easy/data-lekage/` (the indexed URL keeps the typo).
2. **Assets stay under `/assets/...`.** Images live in `static/assets/images/`, CV in
   `static/assets/cv/` — preserving indexed URLs like `/assets/cv/KushBhatnagar_Resume.pdf`.
   Posts reference images as `/assets/images/...` (raw `<img>` tags and markdown both work;
   goldmark `unsafe = true` is enabled).
3. **Post front matter** (Hugo/PaperMod): `title`, `date`, `categories: ["..."]`, `tags: [...]`,
   `summary` (list blurb), `description` (SEO meta), `url` (frozen). No Jekyll `layout:`/`seo_*`.

## Layout of the Hugo site

```
hugo.toml                         # config: menus, socials, taxonomies, params
content/
  posts/*.md                      # the 29 blog posts (section "posts")
  about.md terms.md               # standalone pages
  year-archive.md archive.md      # PaperMod `archives` layout
  search.md                       # PaperMod `search` layout (fuse.js; needs JSON output)
  ml-made-easy.md                 # category landing pages at their custom URLs,
  mlops-playground.md             #   backed by layouts/category-landing.html
  my-bookshelf-chronicles.md
layouts/
  category-landing.html           # custom: lists posts of one category (date-desc)
  _partials/
    extend_head.html              # GA gtag (G-QWTLYBWXCL) + AdSense (prod only)
    comments.html                 # Disqus (shortname: blogsbykush) — posts only
    extend_post_content.html      # Mailchimp newsletter — posts only
assets/css/extended/custom.css    # newsletter, category-list, blockquote, image styling
static/assets/{images,cv}/        # migrated assets (URLs preserved)
static/{favicon*,CNAME,...}       # favicons, PWA icons, CNAME=blogsbykush.com
.github/workflows/hugo.yml        # deploy to GitHub Pages via Actions (prod build)
_migration/migrate_posts.py       # one-off Jekyll→Hugo post converter (kept for audit)
```

## External integrations (IDs)

- Google Analytics (gtag): `G-QWTLYBWXCL`
- Google AdSense: `ca-pub-4896166132316701`
- Disqus shortname: `blogsbykush`
- Mailchimp: `blogsbykush.us21.list-manage.com` (u=`c937565c206ad87a847339f0f`, id=`e0273fdf87`)

## Remaining steps to finish the migration

1. Final visual review via `hugo server`.
2. GitHub repo **Settings → Pages** → switch source to **GitHub Actions** (before merging).
3. Merge `hugo-migration` → `main` to trigger deploy.
4. Delete the old Jekyll files (`_config.yml`, `_posts/`, `_pages/`, `_layouts/`, `_includes/`,
   `_sass/`, `_data/`, `Gemfile*`, `index.md`, `feed.xml`, `archive.html`) and `_migration/`.
5. Confirm Disqus threads still resolve (identifiers use `RelPermalink`, matching old paths).

## Preferences observed

- Wants to **know what will change before execution** and keep a running changelog
  (`CHANGELOG_HUGO_MIGRATION.md`) of what changed and when.
- Values simplicity and low maintenance — this is why PaperMod (pure Hugo, no Node/Tailwind
  build) was chosen over Blowfish/Congo/Stack.
