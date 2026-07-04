# blogsbykush.com - Migration Plan from Jekyll to Modern Framework

> **Generated**: April 6, 2026
> **Current Stack**: Jekyll 4.3.2 + Minimal Mistakes 4.24.0 + GitHub Pages
> **Domain**: blogsbykush.com
> **Total Posts**: 29 (across 3 categories: ml-made-easy, mlops, bookshelf)

---

## Table of Contents

1. [Framework Comparison & Recommendation](#1-framework-comparison--recommendation)
2. [Hugo Migration Plan](#2-hugo-migration-plan)
3. [Astro Migration Plan](#3-astro-migration-plan)
4. [Pre-Migration Cleanup (Common to Both)](#4-pre-migration-cleanup-common-to-both)
5. [Post-Migration Checklist](#5-post-migration-checklist)
6. [URL Redirect Map](#6-url-redirect-map)

---

## 1. Framework Comparison & Recommendation

### Options Evaluated

| Factor | Jekyll (stay) | Hugo | Astro | Next.js | 11ty |
|--------|:---:|:---:|:---:|:---:|:---:|
| **Learning curve** | None | Low | Medium | High | Low |
| **Migration effort** | 1-2 days | 3-5 days | 5-7 days | 2-3 weeks | 3-4 days |
| **Build speed** | Slow | Fastest | Fast | Medium | Fast |
| **Theme quality** | Dated | Excellent | Good | DIY | Limited |
| **Image optimization** | Manual | Plugin | Built-in | Built-in | Plugin |
| **Dark mode** | Theme-dependent | Most themes | Most themes | DIY | DIY |
| **Interactive content** | No | No | Yes (islands) | Yes (full React) | No |
| **Future-proofing** | Low | High | Highest | High | Medium |
| **Complexity** | Low | Low | Medium | High | Low |
| **GitHub Pages (native)** | Yes | Via Actions | Via Actions | Via Actions | Via Actions |

### Option 1: Stay with Jekyll, Modernize the Theme

- **What changes**: Replace Minimal Mistakes with a modern theme (e.g., Chirpy, Just the Docs, or a custom theme). Clean up the forked files.
- **Learning curve**: Lowest - you already know the system. Just theme swapping + cleanup.
- **Migration effort**: ~1-2 days. Zero content changes needed.
- **Hosting**: GitHub Pages natively (no change).
- **Drawbacks**: Jekyll is effectively in maintenance mode. Ruby ecosystem is shrinking. Build times are slow. No component model. You're polishing old furniture.
- **Best if**: You want minimal effort and just need it to look better.

### Option 2: Hugo

- **What it is**: Go-based static site generator. Extremely fast builds.
- **Learning curve**: Low-Medium. Hugo's templating language (Go templates) is more cryptic than Liquid but the structure is similar to Jekyll: content in `content/`, templates in `layouts/`, config in `hugo.toml`. Markdown + front matter ports over almost 1:1.
- **Migration effort**: ~3-5 days. Front matter is compatible. Folder structure changes slightly (`_posts/` → `content/posts/`). Date-prefixed filenames work natively.
- **Themes**: Rich ecosystem - PaperMod, Blowfish, Congo are all modern, fast, dark-mode-ready. Much more polished than Minimal Mistakes.
- **Hosting**: GitHub Pages, Netlify, Cloudflare Pages, Vercel. All free tier.
- **Key advantage**: Builds in milliseconds (vs. Jekyll's seconds/minutes). Single binary, no Ruby dependency hell.
- **Drawbacks**: Go template syntax is ugly (`{{ .Params.title }}`). Less intuitive than Liquid when you need custom logic. Shortcodes replace includes.
- **Best if**: You want a straightforward upgrade that feels familiar but is faster and more modern.

### Option 3: Astro

- **What it is**: Modern JS-based static site framework. "Islands architecture" - ships zero JavaScript by default, adds interactivity only where needed.
- **Learning curve**: Medium. Requires basic knowledge of: Node.js/npm, `.astro` file syntax (HTML-like components), and optionally JSX if you add React/Vue components. Learnable in a weekend.
- **Migration effort**: ~5-7 days. Markdown + front matter works natively via content collections. You define a schema for your front matter (type-safe). Layouts become `.astro` components.
- **Themes**: Growing ecosystem - AstroPaper, Astro-Starter-Blog. Or build your own with Tailwind CSS quickly.
- **Hosting**: Vercel, Netlify, Cloudflare Pages (all free). GitHub Pages with a build action.
- **Key advantages**: Content collections with type-safe schemas. Image optimization built-in (`<Image>` component auto-generates WebP/AVIF + responsive sizes). MDX support. Component-based architecture.
- **Drawbacks**: Node.js toolchain (npm/pnpm). More files/folders than Jekyll. Overkill if you just want to write Markdown and forget about it.
- **Best if**: You want a future-proof platform that can grow with you (add interactive ML demos, code playgrounds, etc.)

### Option 4: Next.js (App Router)

- **What it is**: React-based full-stack framework by Vercel.
- **Learning curve**: High. Requires React, JSX, Node.js, understanding of App Router.
- **Migration effort**: ~2-3 weeks if new to React.
- **Key advantages**: Most flexible option. Can add dynamic features.
- **Drawbacks**: Massive overkill for a blog. React hydration adds unnecessary JS to every page. Complex build pipeline.
- **Best if**: You want to build a full web app, not just a blog. Or you already know React.

### Option 5: Eleventy (11ty)

- **What it is**: Node.js based static site generator. Spiritual successor to Jekyll in the JS world.
- **Learning curve**: Low. Supports Liquid templates natively (same as Jekyll!).
- **Migration effort**: ~3-4 days. Liquid templates mostly work as-is.
- **Drawbacks**: Smaller theme ecosystem than Hugo. Less "batteries included".
- **Best if**: You want the closest thing to Jekyll but in a healthier ecosystem.

### Final Recommendation

> **Primary: Hugo + PaperMod/Blowfish theme** — Markdown files migrate with near-zero changes. PaperMod gives you dark mode, search, archives, tags, TOC, and a beautiful design out of the box. Single binary install, no Ruby/Node dependencies. Builds in under 100ms. Lowest meaningful upgrade from Jekyll.
>
> **Secondary: Astro** — Choose this only if you're excited about learning a modern JS framework and want to eventually add interactive elements (embedded Python notebooks, live model demos, code playgrounds in ML Made Easy series).
>
> **Avoid Next.js** unless you're planning to build a full product, not a blog.

---

## 2. Hugo Migration Plan

### 2.1 Prerequisites

```bash
# Install Hugo (Windows - using winget)
winget install Hugo.Hugo.Extended

# Or using Chocolatey
choco install hugo-extended

# Or using Scoop
scoop install hugo-extended

# Verify installation
hugo version
```

> **Important**: Install the **extended** version (needed for SCSS/SASS processing).

### 2.2 Project Structure Mapping

```
JEKYLL (current)                    HUGO (target)
================================    ================================
_config.yml                    →    hugo.toml
_posts/                        →    content/posts/
_pages/about.md                →    content/about.md
_pages/ml-made-easy.md         →    content/ml-made-easy/_index.md
_pages/mlops-playground.md     →    content/mlops/_index.md
_pages/my-bookshelf-chronicles →    content/bookshelf/_index.md
_pages/tags.md                 →    (auto-generated by Hugo)
_pages/year-archive.md         →    (auto-generated by Hugo)
_layouts/                      →    layouts/ (mostly provided by theme)
_includes/                     →    layouts/partials/
_sass/                         →    assets/scss/ (if custom)
assets/images/                 →    static/images/
assets/cv/                     →    static/cv/
index.md                       →    content/_index.md
CNAME                          →    static/CNAME
```

### 2.3 Step-by-Step Migration

#### Step 1: Create new Hugo site (Day 1)

```bash
# Create a new Hugo site in a separate directory
hugo new site blogsbykush-hugo
cd blogsbykush-hugo

# Initialize Git
git init

# Add PaperMod theme as a Git submodule
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

#### Step 2: Configure hugo.toml (Day 1)

Create `hugo.toml` with settings mapped from your current `_config.yml`:

```toml
baseURL = "https://blogsbykush.com/"
languageCode = "en-us"
title = "Blogs by Kush"
theme = "PaperMod"
paginate = 5

# SEO
enableRobotsTXT = true
buildDrafts = false
buildFuture = false
buildExpired = false

[params]
  env = "production"
  title = "Blogs by Kush"
  description = "Simplifying the complexities of MLOps, AWS, Machine Learning, and a lot more"
  keywords = ["Machine Learning", "MLOps", "AWS", "Blog"]
  author = "Kush Bhatnagar"
  images = ["/images/logo-kb-2-air.png"]
  defaultTheme = "auto"  # dark mode toggle: auto/dark/light
  disableThemeToggle = false
  ShowReadingTime = true
  ShowShareButtons = true
  ShowPostNavLinks = true
  ShowBreadCrumbs = true
  ShowCodeCopyButtons = true
  ShowWordCount = false
  ShowRssButtonInSectionTermList = true
  UseHugoToc = true
  disableSpecial1stPost = false
  disableScrollToTop = false
  comments = true
  hidemeta = false
  hideSummary = false
  showtoc = true

  [params.homeInfoParams]
    Title = "Hi, I'm Kush 👋"
    Content = """
I'm just another **nerdy**, **curious**, **lifelong learner** who believes in the power of simplicity.
I write about Machine Learning, MLOps, AWS, and books that inspire me.
"""

  [[params.socialIcons]]
    name = "twitter"
    url = "https://twitter.com/bhatnagarkush"
  [[params.socialIcons]]
    name = "github"
    url = "https://github.com/KushBhatnagar"
  [[params.socialIcons]]
    name = "linkedin"
    url = "https://www.linkedin.com/in/kushbhatnagar/"
  [[params.socialIcons]]
    name = "medium"
    url = "https://medium.com/@kushbhatnagar86"
  [[params.socialIcons]]
    name = "email"
    url = "mailto:kushbhatnagar86@gmail.com"

  [params.analytics]
    [params.analytics.google]
      SiteVerificationTag = "BKwv8d9RamS8UFYapYrQ8ppq348YsIXUDc9E2bWdaYM"

  [params.cover]
    hidden = false
    hiddenInList = false
    hiddenInSingle = false

  [params.profileMode]
    enabled = false
    title = "Kush Bhatnagar"
    subtitle = "Simplifying the complexities of MLOps, AWS, Machine Learning, and a lot more"
    imageUrl = "/images/kush-toon.jpg"
    imageTitle = "Kush Bhatnagar"

# Top navigation menu
[[menu.main]]
  identifier = "about"
  name = "About"
  url = "/about/"
  weight = 10
[[menu.main]]
  identifier = "ml-made-easy"
  name = "ML Made Easy"
  url = "/categories/ml-made-easy/"
  weight = 20
[[menu.main]]
  identifier = "mlops"
  name = "MLOps Playground"
  url = "/categories/mlops/"
  weight = 30
[[menu.main]]
  identifier = "bookshelf"
  name = "Bookshelf Chronicles"
  url = "/categories/bookshelf/"
  weight = 40
[[menu.main]]
  identifier = "tags"
  name = "Tags"
  url = "/tags/"
  weight = 50
[[menu.main]]
  identifier = "archives"
  name = "Archives"
  url = "/archives/"
  weight = 60
[[menu.main]]
  identifier = "search"
  name = "Search"
  url = "/search/"
  weight = 70

[outputs]
  home = ["HTML", "RSS", "JSON"]  # JSON needed for search

# Markdown rendering
[markup]
  [markup.highlight]
    codeFences = true
    guessSyntax = true
    lineNos = false
    style = "monokai"
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true  # needed for raw HTML in your markdown posts
```

#### Step 3: Migrate Content (Day 2)

**3a. Migrate blog posts**

Each post needs these front matter adjustments:

Jekyll front matter (current):
```yaml
---
title: What is Machine Learning
layout: single
categories: ml-made-easy
tag:
- machine learning
- classroom conversation
excerpt: "..."
seo_title: "What is Machine Learning"
seo_description: "..."
---
```

Hugo front matter (target):
```yaml
---
title: "What is Machine Learning"
date: 2023-06-09
categories: ["ml-made-easy"]
tags: ["machine learning", "classroom conversation"]
summary: "..."
description: "..."
cover:
  image: "/images/ml-made-easy/WhatIsMachineLearning.png"
  alt: "What is Machine Learning"
ShowToc: true
---
```

**Key changes:**
- `layout: single` → remove (theme handles it)
- `tag:` → `tags:` (must be plural, must be a list `["tag1", "tag2"]`)
- `categories: ml-made-easy` → `categories: ["ml-made-easy"]`
- `excerpt:` → `summary:` (PaperMod uses `summary`)
- `seo_title:` → can be dropped (Hugo uses `title` for SEO)
- `seo_description:` → `description:`
- Add `date:` field (extracted from filename)
- `toc: true` → `ShowToc: true`

**3b. Fix image references in post content**

Jekyll syntax:
```markdown
![WhatIsMachineLearning]({{ site.url }}{{ site.baseurl }}/assets/images/ml-made-easy/WhatIsMachineLearning.png){: .align-center}
```

Hugo syntax:
```markdown
![WhatIsMachineLearning](/images/ml-made-easy/WhatIsMachineLearning.png)
```

Or using Hugo figure shortcode for centering:
```
{{</* figure src="/images/ml-made-easy/WhatIsMachineLearning.png" align="center" alt="What is Machine Learning" */>}}
```

**3c. File rename mapping** (fix spaces and typos):

| Current Filename | Target Filename |
|-----------------|-----------------|
| `2023-07-05-what-is-deeplearning-and neuralnetwork.md` | `what-is-deeplearning-and-neuralnetwork.md` |
| `2024-06-09-what-is-feature-engineering .md` | `what-is-feature-engineering.md` |
| `2024-06-17- why-dvc-not-best-choice-with-awslambda-for-dataversioning.md` | `why-dvc-not-best-choice-with-awslambda-for-dataversioning.md` |
| `2023-10-29- what-is-the-most-effective-way-to-learn-ml.md` | `what-is-the-most-effective-way-to-learn-ml.md` |
| `2023-05-14-data-lekage.md` | `data-leakage.md` (fix typo) |

> In Hugo, remove date prefix from filenames — put the date in front matter instead.

**3d. Automated migration script (PowerShell)**

```powershell
# Run from the Jekyll project root
$jekyllPosts = Get-ChildItem -Path "./_posts" -Filter "*.md"
$hugoPostsDir = "../blogsbykush-hugo/content/posts"
New-Item -ItemType Directory -Force -Path $hugoPostsDir

foreach ($post in $jekyllPosts) {
    # Extract date and slug from filename
    if ($post.Name -match '^(\d{4}-\d{2}-\d{2})-?\s*(.+)\.md$') {
        $date = $Matches[1]
        $slug = $Matches[2].Trim() -replace '\s+', '-'
        $newName = "$slug.md"

        $content = Get-Content $post.FullName -Raw

        # Replace Jekyll image syntax with Hugo syntax
        $content = $content -replace '\!\[([^\]]*)\]\(\{\{ site\.url \}\}\{\{ site\.baseurl \}\}/assets/images/([^\)]+)\)\{[^\}]*\}', '![$1](/images/$2)'
        $content = $content -replace '\!\[([^\]]*)\]\(\{\{ site\.url \}\}\{\{ site\.baseurl \}\}/assets/images/([^\)]+)\)', '![$1](/images/$2)'
        $content = $content -replace '<img src\s*=\s*"/assets/images/([^"]+)">', '![$1](/images/$1)'

        # Replace tag: with tags: in front matter
        $content = $content -replace '(?m)^tag:', 'tags:'

        # Replace layout: single with nothing
        $content = $content -replace '(?m)^layout\s*:\s*single\s*$', ''

        # Add date to front matter (after title line)
        if ($content -match '(?m)^title:') {
            $content = $content -replace '(?m)^(title:\s*.+)$', "`$1`ndate: $date"
        }

        Set-Content -Path (Join-Path $hugoPostsDir $newName) -Value $content
        Write-Host "Migrated: $($post.Name) -> $newName"
    }
}
```

#### Step 4: Copy Static Assets (Day 2)

```bash
# Copy images
cp -r assets/images/* ../blogsbykush-hugo/static/images/

# Copy CV
cp -r assets/cv/* ../blogsbykush-hugo/static/cv/

# Copy CNAME for GitHub Pages
cp CNAME ../blogsbykush-hugo/static/CNAME
```

#### Step 5: Create special pages (Day 3)

**Archives page** — `content/archives.md`:
```yaml
---
title: "Archives"
layout: "archives"
url: "/archives/"
summary: "All posts by year"
---
```

**Search page** — `content/search.md`:
```yaml
---
title: "Search"
layout: "search"
url: "/search/"
summary: "Search all posts"
placeholder: "Search blogsbykush..."
---
```

**About page** — `content/about.md`:
```yaml
---
title: "Behind the Scenes"
url: "/about/"
summary: "About Kush Bhatnagar"
---

(Copy your existing about page content here, updating image paths)
```

#### Step 6: Add Integrations (Day 3-4)

**6a. Google Analytics (gtag)**

Create `layouts/partials/extend_head.html`:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QWTLYBWXCL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-QWTLYBWXCL');
</script>
```

**6b. Disqus Comments**

Create `layouts/partials/comments.html`:
```html
<div id="disqus_thread"></div>
<script>
    var disqus_config = function () {
        this.page.url = "{{ .Permalink }}";
        this.page.identifier = "{{ .RelPermalink }}";
    };
    (function() {
        var d = document, s = d.createElement('script');
        s.src = 'https://blogsbykush.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
</script>
```

**6c. Mailchimp Newsletter**

Create `layouts/partials/newsletter.html`:
```html
<div class="newsletter-signup" style="max-width: 550px; margin: 2rem auto; padding: 1.5rem; border: 1px solid var(--border); border-radius: 8px;">
  <h3>Be the first to hear about new posts</h3>
  <form action="https://blogsbykush.us21.list-manage.com/subscribe/post?u=c937565c206ad87a847339f0f&amp;id=e0273fdf87&amp;f_id=0054aae1f0" method="post" target="_blank">
    <input type="email" name="EMAIL" placeholder="Your email address" required style="width: 70%; padding: 0.5rem;">
    <input type="submit" value="Subscribe" style="padding: 0.5rem 1rem;">
    <div style="position: absolute; left: -5000px;" aria-hidden="true">
      <input type="text" name="b_c937565c206ad87a847339f0f_e0273fdf87" tabindex="-1" value="">
    </div>
  </form>
</div>
```

Then include it in `layouts/_default/single.html` (override theme's single layout):
```html
{{ define "main" }}
{{ partial "single.html" . }}
{{ partial "newsletter.html" . }}
{{ partial "comments.html" . }}
{{ end }}
```

**6d. Google AdSense (conditional)**

Create `layouts/partials/adsense.html`:
```html
{{ if and (eq hugo.Environment "production") (.Site.Params.adsense) }}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4896166132316701" crossorigin="anonymous"></script>
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-4896166132316701" data-ad-slot="5967806966" data-ad-format="auto" data-full-width-responsive="true"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
{{ end }}
```

Add to `hugo.toml`:
```toml
[params]
  adsense = true
```

#### Step 7: GitHub Actions Deployment (Day 4)

Create `.github/workflows/hugo.yml`:
```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.140.0
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb
          sudo dpkg -i ${{ runner.temp }}/hugo.deb
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5
      - name: Build with Hugo
        env:
          HUGO_CACHEDIR: ${{ runner.temp }}/hugo_cache
          HUGO_ENVIRONMENT: production
        run: |
          hugo --gc --minify --baseURL "${{ steps.pages.outputs.base_url }}/"
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

#### Step 8: Test Locally (Day 4-5)

```bash
cd blogsbykush-hugo
hugo server -D
# Open http://localhost:1313
```

Verify:
- [ ] All 29 posts render correctly
- [ ] Images load on all posts
- [ ] Categories pages work (ml-made-easy, mlops, bookshelf)
- [ ] Tags page shows all tags
- [ ] Archives page lists all posts by year
- [ ] Search works
- [ ] Dark mode toggle works
- [ ] Mobile responsive layout
- [ ] Disqus comments load
- [ ] Mailchimp form works
- [ ] About page with images
- [ ] RSS feed at /index.xml
- [ ] 404 page

### 2.4 Hugo Final Directory Structure

```
blogsbykush-hugo/
├── hugo.toml
├── static/
│   ├── CNAME
│   ├── images/
│   │   ├── kush-toon.jpg
│   │   ├── logo-kb-2-air.png
│   │   ├── ml-made-easy/
│   │   │   ├── WhatIsMachineLearning.png
│   │   │   ├── WhatIsModel.png
│   │   │   └── ...
│   │   └── ...
│   └── cv/
│       └── KushBhatnagar_Resume.pdf
├── content/
│   ├── _index.md              (homepage)
│   ├── about.md
│   ├── archives.md
│   ├── search.md
│   └── posts/
│       ├── what-is-machine-learning.md
│       ├── what-is-model.md
│       ├── overfitting-and-underfitting.md
│       ├── atomic-habits-bookshelf.md
│       ├── sagemaker-empowering-your-ml-lifecycle.md
│       └── ... (29 posts total)
├── layouts/
│   └── partials/
│       ├── extend_head.html   (analytics)
│       ├── comments.html      (disqus)
│       ├── newsletter.html    (mailchimp)
│       └── adsense.html       (conditional ads)
├── themes/
│   └── PaperMod/              (git submodule)
└── .github/
    └── workflows/
        └── hugo.yml           (auto-deploy)
```

---

## 3. Astro Migration Plan

### 3.1 Prerequisites

```bash
# Requires Node.js 18+ (check with: node --version)
# Install Node.js from https://nodejs.org/ if not installed

# Verify
node --version   # should be >= 18.x
npm --version    # should be >= 9.x
```

### 3.2 Project Structure Mapping

```
JEKYLL (current)                    ASTRO (target)
================================    ================================
_config.yml                    →    astro.config.mjs + src/consts.ts
_posts/                        →    src/content/posts/
_pages/about.md                →    src/pages/about.astro
_pages/ml-made-easy.md         →    src/pages/ml-made-easy.astro
_pages/mlops-playground.md     →    src/pages/mlops.astro
_pages/my-bookshelf-chronicles →    src/pages/bookshelf.astro
_pages/tags.md                 →    src/pages/tags/index.astro
_pages/year-archive.md         →    src/pages/archives.astro
_layouts/single.html           →    src/layouts/PostLayout.astro
_layouts/default.html          →    src/layouts/BaseLayout.astro
_includes/                     →    src/components/
_sass/                         →    Tailwind CSS (or global CSS)
assets/images/                 →    public/images/ or src/assets/images/
assets/cv/                     →    public/cv/
index.md                       →    src/pages/index.astro
CNAME                          →    public/CNAME
```

### 3.3 Step-by-Step Migration

#### Step 1: Scaffold Astro Project (Day 1)

```bash
# Create new Astro project
npm create astro@latest blogsbykush-astro

# Choose: Empty project
# Choose: Yes to TypeScript (recommended: strict)
# Choose: Yes to install dependencies

cd blogsbykush-astro

# Add integrations
npx astro add tailwind    # Tailwind CSS for styling
npx astro add sitemap     # Auto-generate sitemap
npx astro add mdx         # MDX support (optional, for interactive posts)
```

#### Step 2: Configure Astro (Day 1)

**`astro.config.mjs`**:
```javascript
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://blogsbykush.com',
  integrations: [tailwind(), sitemap(), mdx()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
  },
});
```

**`src/consts.ts`** (site-wide constants, replaces _config.yml):
```typescript
export const SITE_TITLE = "Blogs by Kush";
export const SITE_DESCRIPTION = "Simplifying the complexities of MLOps, AWS, Machine Learning, and a lot more";
export const SITE_AUTHOR = "Kush Bhatnagar";
export const SOCIAL_LINKS = {
  twitter: "https://twitter.com/bhatnagarkush",
  github: "https://github.com/KushBhatnagar",
  linkedin: "https://www.linkedin.com/in/kushbhatnagar/",
  medium: "https://medium.com/@kushbhatnagar86",
  email: "mailto:kushbhatnagar86@gmail.com",
};
export const GA_ID = "G-QWTLYBWXCL";
export const DISQUS_SHORTNAME = "blogsbykush";
```

#### Step 3: Define Content Schema (Day 1)

**`src/content.config.ts`** (type-safe content):
```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    categories: z.enum(["ml-made-easy", "mlops", "bookshelf"]).optional(),
    tags: z.array(z.string()).optional().default([]),
    excerpt: z.string().optional(),
    description: z.string().optional(),
    draft: z.boolean().optional().default(false),
    toc: z.boolean().optional().default(false),
    cover: z.string().optional(),
  }),
});

export const collections = { posts };
```

> This schema validates every post at build time. If a post has an invalid category or missing title, the build fails with a clear error. This catches bugs that Jekyll silently ignores.

#### Step 4: Create Base Layouts (Day 2)

**`src/layouts/BaseLayout.astro`**:
```astro
---
import { SITE_TITLE, GA_ID } from '../consts';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
}

const { title, description } = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <title>{title} - {SITE_TITLE}</title>
    <link rel="icon" type="image/png" href="/images/logo-kb-2-air.png" />
    <link rel="sitemap" href="/sitemap-index.xml" />

    <!-- Google Analytics -->
    <script async src={`https://www.googletagmanager.com/gtag/js?id=${GA_ID}`}></script>
    <script define:vars={{ GA_ID }}>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', GA_ID);
    </script>
  </head>
  <body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 min-h-screen flex flex-col">
    <Header />
    <main class="flex-1 max-w-4xl mx-auto px-4 py-8 w-full">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

**`src/layouts/PostLayout.astro`**:
```astro
---
import BaseLayout from './BaseLayout.astro';
import Newsletter from '../components/Newsletter.astro';
import Comments from '../components/Comments.astro';
import TagList from '../components/TagList.astro';
import FormattedDate from '../components/FormattedDate.astro';

const { title, date, categories, tags, excerpt, description } = Astro.props;
---

<BaseLayout title={title} description={description || excerpt}>
  <article class="prose dark:prose-invert max-w-none">
    <header class="mb-8">
      <h1 class="text-3xl font-bold mb-2">{title}</h1>
      <div class="text-gray-500 dark:text-gray-400 flex gap-4 items-center">
        <FormattedDate date={date} />
        {categories && <span class="bg-blue-100 dark:bg-blue-900 px-2 py-1 rounded text-sm">{categories}</span>}
      </div>
      {tags && tags.length > 0 && <TagList tags={tags} />}
    </header>

    <slot />

    <Newsletter />
    <Comments />
  </article>
</BaseLayout>
```

#### Step 5: Create Components (Day 2-3)

**`src/components/Header.astro`**:
```astro
---
import { SITE_TITLE } from '../consts';
import ThemeToggle from './ThemeToggle.astro';

const navLinks = [
  { href: '/about/', label: 'About' },
  { href: '/ml-made-easy/', label: 'ML Made Easy' },
  { href: '/mlops/', label: 'MLOps Playground' },
  { href: '/bookshelf/', label: 'Bookshelf' },
  { href: '/tags/', label: 'Tags' },
  { href: '/archives/', label: 'Archives' },
];
---

<header class="border-b border-gray-200 dark:border-gray-700">
  <nav class="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
    <a href="/" class="font-bold text-xl">{SITE_TITLE}</a>
    <div class="flex items-center gap-4">
      {navLinks.map(link => (
        <a href={link.href} class="hover:text-blue-600 dark:hover:text-blue-400 hidden md:inline">
          {link.label}
        </a>
      ))}
      <ThemeToggle />
    </div>
  </nav>
</header>
```

**`src/components/Newsletter.astro`**:
```astro
<div class="my-8 p-6 border border-gray-200 dark:border-gray-700 rounded-lg">
  <h3 class="text-lg font-semibold mb-4">Be the first to hear about new posts</h3>
  <form
    action="https://blogsbykush.us21.list-manage.com/subscribe/post?u=c937565c206ad87a847339f0f&amp;id=e0273fdf87&amp;f_id=0054aae1f0"
    method="post"
    target="_blank"
    class="flex gap-2"
  >
    <input
      type="email"
      name="EMAIL"
      placeholder="Your email address"
      required
      class="flex-1 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded bg-white dark:bg-gray-800"
    />
    <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
      Subscribe
    </button>
    <div style="position: absolute; left: -5000px;" aria-hidden="true">
      <input type="text" name="b_c937565c206ad87a847339f0f_e0273fdf87" tabindex="-1" value="" />
    </div>
  </form>
</div>
```

**`src/components/Comments.astro`**:
```astro
---
import { DISQUS_SHORTNAME } from '../consts';
const url = Astro.url.href;
const identifier = Astro.url.pathname;
---

<div id="disqus_thread" class="mt-8"></div>
<script define:vars={{ DISQUS_SHORTNAME, url, identifier }}>
  var disqus_config = function () {
    this.page.url = url;
    this.page.identifier = identifier;
  };
  (function () {
    var d = document, s = d.createElement('script');
    s.src = 'https://' + DISQUS_SHORTNAME + '.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
  })();
</script>
```

**`src/components/ThemeToggle.astro`**:
```astro
<button id="theme-toggle" class="p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700" aria-label="Toggle theme">
  <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20">
    <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
  </svg>
  <svg class="w-5 h-5 block dark:hidden" fill="currentColor" viewBox="0 0 20 20">
    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
  </svg>
</button>

<script>
  const toggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  toggle?.addEventListener('click', () => {
    html.classList.toggle('dark');
    localStorage.setItem('theme', html.classList.contains('dark') ? 'dark' : 'light');
  });

  // Set initial theme
  if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    html.classList.add('dark');
  }
</script>
```

#### Step 6: Create Pages (Day 3)

**`src/pages/index.astro`** (homepage):
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import FormattedDate from '../components/FormattedDate.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('posts'))
  .filter(post => !post.data.draft)
  .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
---

<BaseLayout title="Home" description="Simplifying the complexities of MLOps, AWS, Machine Learning, and a lot more">
  <section class="mb-12 text-center">
    <img src="/images/kush-toon.jpg" alt="Kush Bhatnagar" class="w-32 h-32 rounded-full mx-auto mb-4" />
    <h1 class="text-3xl font-bold mb-2">Hi, I'm Kush</h1>
    <p class="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
      I'm just another <strong>nerdy</strong>, <strong>curious</strong>, <strong>lifelong learner</strong>
      who believes in the power of simplicity. I write about Machine Learning, MLOps, AWS, and books.
    </p>
  </section>

  <section>
    <h2 class="text-2xl font-bold mb-6">Recent Posts</h2>
    <ul class="space-y-6">
      {posts.map(post => (
        <li class="border-b border-gray-200 dark:border-gray-700 pb-4">
          <a href={`/posts/${post.id}/`} class="group">
            <h3 class="text-xl font-semibold group-hover:text-blue-600 dark:group-hover:text-blue-400">
              {post.data.title}
            </h3>
            <div class="text-sm text-gray-500 mt-1">
              <FormattedDate date={post.data.date} />
              {post.data.categories && <span class="ml-2 bg-gray-100 dark:bg-gray-800 px-2 py-0.5 rounded">{post.data.categories}</span>}
            </div>
            {post.data.excerpt && <p class="text-gray-600 dark:text-gray-400 mt-2 line-clamp-2">{post.data.excerpt}</p>}
          </a>
        </li>
      ))}
    </ul>
  </section>
</BaseLayout>
```

**`src/pages/posts/[id].astro`** (single post):
```astro
---
import { getCollection, render } from 'astro:content';
import PostLayout from '../../layouts/PostLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('posts');
  return posts.map(post => ({
    params: { id: post.id },
    props: post,
  }));
}

const post = Astro.props;
const { Content } = await render(post);
---

<PostLayout {...post.data}>
  <Content />
</PostLayout>
```

**`src/pages/ml-made-easy.astro`** (category page):
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import FormattedDate from '../components/FormattedDate.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('posts'))
  .filter(post => post.data.categories === 'ml-made-easy')
  .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
---

<BaseLayout title="ML Made Easy" description="Breaking down ML concepts through comics and conversations">
  <h1 class="text-3xl font-bold mb-4">ML Made Easy!!</h1>
  <p class="mb-8 text-gray-600 dark:text-gray-400">
    Breaking down key Machine Learning concepts in a fun and engaging way, through comics and conversations.
  </p>
  <ul class="space-y-4">
    {posts.map(post => (
      <li>
        <a href={`/posts/${post.id}/`} class="hover:text-blue-600">
          <FormattedDate date={post.data.date} /> — {post.data.title}
        </a>
      </li>
    ))}
  </ul>
</BaseLayout>
```

> Create similarly for `/mlops/` and `/bookshelf/` pages.

**`src/pages/tags/index.astro`**:
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const allPosts = await getCollection('posts');
const tags = [...new Set(allPosts.flatMap(post => post.data.tags || []))].sort();
---

<BaseLayout title="Tags">
  <h1 class="text-3xl font-bold mb-8">Tags</h1>
  <div class="flex flex-wrap gap-3">
    {tags.map(tag => (
      <a href={`/tags/${tag}/`} class="bg-gray-100 dark:bg-gray-800 px-3 py-1 rounded-full hover:bg-blue-100 dark:hover:bg-blue-900">
        {tag}
      </a>
    ))}
  </div>
</BaseLayout>
```

**`src/pages/tags/[tag].astro`** (dynamic tag pages):
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import FormattedDate from '../../components/FormattedDate.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const allPosts = await getCollection('posts');
  const tags = [...new Set(allPosts.flatMap(post => post.data.tags || []))];
  return tags.map(tag => ({
    params: { tag },
    props: {
      posts: allPosts
        .filter(post => post.data.tags?.includes(tag))
        .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf()),
    },
  }));
}

const { tag } = Astro.params;
const { posts } = Astro.props;
---

<BaseLayout title={`Tag: ${tag}`}>
  <h1 class="text-3xl font-bold mb-8">Posts tagged: {tag}</h1>
  <ul class="space-y-4">
    {posts.map(post => (
      <li>
        <a href={`/posts/${post.id}/`} class="hover:text-blue-600">
          <FormattedDate date={post.data.date} /> — {post.data.title}
        </a>
      </li>
    ))}
  </ul>
</BaseLayout>
```

#### Step 7: Migrate Content (Day 3-4)

**Front matter changes** (same concept as Hugo):

Jekyll → Astro:
```yaml
# BEFORE (Jekyll)
---
title: What is Machine Learning
layout: single
categories: ml-made-easy
tag:
- machine learning
- classroom conversation
excerpt: "..."
seo_title: "What is Machine Learning"
seo_description: "..."
---

# AFTER (Astro)
---
title: "What is Machine Learning"
date: 2023-06-09
categories: "ml-made-easy"
tags: ["machine learning", "classroom conversation"]
excerpt: "..."
description: "..."
---
```

**Image reference changes:**

Jekyll → Astro:
```markdown
# BEFORE
![WhatIsMachineLearning]({{ site.url }}{{ site.baseurl }}/assets/images/ml-made-easy/WhatIsMachineLearning.png){: .align-center}

# AFTER
![WhatIsMachineLearning](/images/ml-made-easy/WhatIsMachineLearning.png)
```

**Automated migration script (PowerShell):**

```powershell
# Run from the Jekyll project root
$jekyllPosts = Get-ChildItem -Path "./_posts" -Filter "*.md"
$astroPostsDir = "../blogsbykush-astro/src/content/posts"
New-Item -ItemType Directory -Force -Path $astroPostsDir

foreach ($post in $jekyllPosts) {
    if ($post.Name -match '^(\d{4}-\d{2}-\d{2})-?\s*(.+)\.md$') {
        $date = $Matches[1]
        $slug = $Matches[2].Trim() -replace '\s+', '-'
        $newName = "$slug.md"

        $content = Get-Content $post.FullName -Raw

        # Replace Jekyll image syntax
        $content = $content -replace '\!\[([^\]]*)\]\(\{\{ site\.url \}\}\{\{ site\.baseurl \}\}/assets/images/([^\)]+)\)\{[^\}]*\}', '![$1](/images/$2)'
        $content = $content -replace '\!\[([^\]]*)\]\(\{\{ site\.url \}\}\{\{ site\.baseurl \}\}/assets/images/([^\)]+)\)', '![$1](/images/$2)'
        $content = $content -replace '<img src\s*=\s*"/assets/images/([^"]+)"[^>]*>', '![$1](/images/$1)'

        # Fix tag: → tags: (singular to plural)
        $content = $content -replace '(?m)^tag:', 'tags:'

        # Remove layout: single
        $content = $content -replace '(?m)^layout\s*:\s*single\s*\n', ''

        # Remove seo_title (Astro uses title)
        $content = $content -replace '(?m)^seo_title:\s*"[^"]*"\s*\n', ''

        # Rename seo_description to description
        $content = $content -replace '(?m)^seo_description:', 'description:'

        # Add date to front matter
        if ($content -match '(?m)^title:') {
            $content = $content -replace '(?m)^(title:\s*.+)$', "`$1`ndate: $date"
        }

        # Remove Jekyll-specific Liquid tags like {: .notice--info}
        $content = $content -replace '\{:\s*\.notice--\w+\s*\}', ''

        Set-Content -Path (Join-Path $astroPostsDir $newName) -Value $content
        Write-Host "Migrated: $($post.Name) -> $newName"
    }
}
```

#### Step 8: Copy Static Assets (Day 4)

```bash
# Copy images to public/
cp -r assets/images/* ../blogsbykush-astro/public/images/

# Copy CV
cp -r assets/cv/* ../blogsbykush-astro/public/cv/

# Copy CNAME
cp CNAME ../blogsbykush-astro/public/CNAME
```

#### Step 9: Tailwind Config for Dark Mode (Day 4)

**`tailwind.config.mjs`**:
```javascript
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
```

Install typography plugin:
```bash
npm install @tailwindcss/typography
```

#### Step 10: GitHub Actions Deployment (Day 5)

Create `.github/workflows/astro.yml`:
```yaml
name: Deploy Astro site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: npm
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

#### Step 11: Test Locally (Day 5-7)

```bash
cd blogsbykush-astro
npm run dev
# Open http://localhost:4321
```

Verify same checklist as Hugo (see section 2.3, Step 8).

### 3.4 Astro Final Directory Structure

```
blogsbykush-astro/
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
├── tsconfig.json
├── public/
│   ├── CNAME
│   ├── images/
│   │   ├── kush-toon.jpg
│   │   ├── logo-kb-2-air.png
│   │   ├── ml-made-easy/
│   │   │   ├── WhatIsMachineLearning.png
│   │   │   └── ...
│   │   └── ...
│   └── cv/
│       └── KushBhatnagar_Resume.pdf
├── src/
│   ├── consts.ts
│   ├── content.config.ts
│   ├── styles/
│   │   └── global.css
│   ├── content/
│   │   └── posts/
│   │       ├── what-is-machine-learning.md
│   │       ├── what-is-model.md
│   │       ├── atomic-habits-bookshelf.md
│   │       └── ... (29 posts total)
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   └── PostLayout.astro
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── Newsletter.astro
│   │   ├── Comments.astro
│   │   ├── ThemeToggle.astro
│   │   ├── TagList.astro
│   │   └── FormattedDate.astro
│   └── pages/
│       ├── index.astro
│       ├── about.astro
│       ├── ml-made-easy.astro
│       ├── mlops.astro
│       ├── bookshelf.astro
│       ├── archives.astro
│       ├── 404.astro
│       ├── posts/
│       │   └── [id].astro
│       └── tags/
│           ├── index.astro
│           └── [tag].astro
└── .github/
    └── workflows/
        └── astro.yml
```

---

## 4. Pre-Migration Cleanup (Common to Both)

Before migrating to either Hugo or Astro, fix these issues in your content files:

### 4.1 Fix Filenames with Spaces

| Current | Fixed |
|---------|-------|
| `2023-07-05-what-is-deeplearning-and neuralnetwork.md` | `what-is-deeplearning-and-neuralnetwork.md` |
| `2024-06-09-what-is-feature-engineering .md` | `what-is-feature-engineering.md` |
| `2024-06-17- why-dvc-not-best-choice-with-awslambda-for-dataversioning.md` | `why-dvc-not-best-choice-with-awslambda-for-dataversioning.md` |
| `2023-10-29- what-is-the-most-effective-way-to-learn-ml.md` | `what-is-the-most-effective-way-to-learn-ml.md` |

### 4.2 Fix Typos in Content

| Current | Fixed |
|---------|-------|
| `tag:` (singular in 18 posts) | `tags:` (must be plural) |
| `clasroom conversation` | `classroom conversation` |
| `data-lekage` / "Data Lekage" | `data-leakage` / "Data Leakage" |

### 4.3 Fix `tag:` vs `tags:` Inconsistency

Posts using `tag:` (singular) — must be `tags:` (plural):
- what-is-model.md
- overfitting-and-underfitting.md
- class-imbalance.md
- evaluation-metrics.md
- data-leakage.md
- what-is-machine-learning.md
- type-of-machine-learning.md
- what-is-deeplearning-and-neuralnetwork.md
- what-is-transferlearning.md
- what-is-recommender-system.md
- what-is-nlp.md
- what-is-cv.md
- what-is-cross-validation.md
- what-is-gradient-descent.md
- what-is-hyperparameters.md
- what-is-feature-engineering.md
- what-is-regularization.md
- what-is-bias-and-variance.md
- statistics-in-ml.md
- what-is-clustering.md

### 4.4 Remove Jekyll-specific Syntax from Markdown

| Pattern | Replacement |
|---------|-------------|
| `{{ site.url }}{{ site.baseurl }}/assets/images/` | `/images/` |
| `{: .align-center}` | Remove (use CSS/shortcode instead) |
| `{: .notice--info}` | Use blockquote or callout component |
| `{: .notice--warning}` | Use blockquote or callout component |
| `{% for post in site.categories.X %}...{% endfor %}` | Replace with framework-specific listing |

### 4.5 Optimize Images

Your `assets/images/` contains raw PNGs. Before migration:

```bash
# Install image optimization tool
npm install -g sharp-cli

# Convert PNGs to WebP (keeps originals)
# Do this for the ml-made-easy comics especially
```

Or handle this at the framework level (Astro has built-in `<Image>` optimization).

---

## 5. Post-Migration Checklist

### 5.1 SEO Continuity

- [ ] All existing URLs either work OR have 301 redirects
- [ ] `sitemap.xml` is generated and submitted to Google Search Console
- [ ] `robots.txt` exists and is correct
- [ ] Google Search Console re-verified
- [ ] Google Analytics tracking confirmed
- [ ] RSS feed URL maintained or redirected
- [ ] Open Graph / Twitter Card meta tags on all pages
- [ ] Canonical URLs set correctly

### 5.2 Functional Verification

- [ ] All 29 posts render correctly
- [ ] All images load (especially ml-made-easy comics)
- [ ] Code blocks render with syntax highlighting
- [ ] Disqus comments load and show historical comments
- [ ] Mailchimp subscription form works
- [ ] Search functionality works
- [ ] Dark mode toggle works
- [ ] Mobile responsive design verified
- [ ] 404 page works
- [ ] CNAME file present (custom domain)
- [ ] About page with CV download link works

### 5.3 Performance Targets

| Metric | Jekyll Current (est.) | Hugo Target | Astro Target |
|--------|:---:|:---:|:---:|
| Build time | 5-10s | <100ms | <2s |
| Lighthouse Performance | ~70 | 95+ | 95+ |
| First Contentful Paint | ~2.5s | <1s | <1s |
| Total JS shipped | ~150KB | <50KB | <30KB |

### 5.4 DNS / GitHub Pages

1. In your GitHub repo settings, go to **Pages**
2. Change source from "Deploy from branch" to **"GitHub Actions"**
3. Verify CNAME is in `static/` (Hugo) or `public/` (Astro)
4. SSL certificate should auto-renew

---

## 6. URL Redirect Map

Your current Jekyll URLs follow the pattern `/:categories/:title/`. Ensure the new framework produces the same URLs, or set up redirects.

| Current URL | Hugo URL | Astro URL | Action Needed |
|-------------|----------|-----------|---------------|
| `/ml-made-easy/what-is-machine-learning/` | `/posts/what-is-machine-learning/` | `/posts/what-is-machine-learning/` | **Redirect needed** |
| `/mlops/sagemaker-empowering-your-ml-lifecycle/` | `/posts/sagemaker-empowering-your-ml-lifecycle/` | `/posts/sagemaker-empowering-your-ml-lifecycle/` | **Redirect needed** |
| `/bookshelf/atomic-habits-bookshelf/` | `/posts/atomic-habits-bookshelf/` | `/posts/atomic-habits-bookshelf/` | **Redirect needed** |

**Option A**: Configure URL format to match Jekyll's category-based pattern (more complex).

**Hugo** - In `hugo.toml`:
```toml
[permalinks]
  posts = "/:categories/:slug/"
```

**Astro** - Rename `[id].astro` route to use `/:category/:slug` pattern, or create redirect aliases.

**Option B**: Use a `_redirects` file (Netlify) or redirect rules for GitHub Pages.

> **Recommendation**: Option A is cleaner. Match the existing URL structure to avoid SEO penalty.

---

## Timeline Summary

| Day | Hugo | Astro |
|-----|------|-------|
| **Day 1** | Install Hugo, set up project, configure `hugo.toml`, add theme | Scaffold Astro, configure, define content schema |
| **Day 2** | Run migration script, copy assets, fix front matter | Create base layouts and components |
| **Day 3** | Create special pages, test content rendering | Create all pages, run migration script |
| **Day 4** | Add integrations (analytics, comments, newsletter), CI/CD | Copy assets, add integrations, Tailwind setup |
| **Day 5** | Testing, fix issues, deploy | CI/CD setup, testing, fix issues |
| **Day 6** | - | Final testing, deploy |
| **Day 7** | - | Buffer for edge cases |

---

## Decision Matrix: Which One to Pick?

| Question | If YES → | If NO → |
|----------|----------|---------|
| Do you want the fastest migration with least friction? | **Hugo** | - |
| Do you want to learn a modern JS ecosystem? | **Astro** | **Hugo** |
| Will you add interactive ML demos in the future? | **Astro** | **Hugo** |
| Do you want zero JS shipped to readers? | **Hugo** | - |
| Do you prefer a single binary with no dependencies? | **Hugo** | - |
| Do you want type-safe content validation? | **Astro** | - |
| Do you plan to eventually build a portfolio/project showcase? | **Astro** | **Hugo** |

> **Bottom line**: Hugo for a pure blog upgrade. Astro if you're building a platform.
