# Tech Digest (Digital Dhaba) on blogsbykush.com

Weekly issues are generated in the private **Digital-Dhaba** repo (`run_digest.sh` →
`issues/YYYY-MM-DD/{newsletter.html, digest.json, …}`) and published on the blog automatically.

## How it works

```
Digital-Dhaba                                  blogsbykush.com (this repo)
─────────────                                  ───────────────────────────
run_digest.sh → issues/2026-09-27/   push      scripts/add_digest.py
  newsletter.html, digest.json  ───────────▶   content/tech-digest/2026-09-27/
                 (GitHub Action)                 index.md, newsletter.txt, digest.json, hero.jpg
                                                          │ push → deploy workflow
                                                          ▼
                                     /tech-digest/              archive (cards from digest.json)
                                     /tech-digest/2026-09-27/   the issue, exactly as designed
                                     /tech-digest/feed.xml      RSS
```

The issue page (`layouts/tech-digest/single.html`) serves the newsletter HTML unchanged, adding at
build time: a slim "← Blogs by Kush · All issues · Subscribe" bar, canonical/SEO/social tags (hero as
preview image), Google Analytics (production only), and web-safe versions of the email placeholders
(`{{VIEW_IN_BROWSER_URL}}` and `{{UNSUBSCRIBE_URL}}` links removed, `{{FORWARD_URL}}` → email-a-friend
link). The homepage shows a "New Tech Digest" strip for the latest issue.

## One-time setup (done 2026-09-30; kept for when the token expires or the repo moves)

1. **Create a token** that can push to the blog repo only.
   GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** →
   Generate new token:
   - Resource owner: `KushBhatnagar`
   - Repository access: **Only select repositories** → `kushbhatnagar.github.io`
   - Permissions → Repository permissions → **Contents: Read and write** (nothing else)
   - Expiration: up to 1 year; put a reminder in your calendar to renew it.
2. **Save it in Digital-Dhaba**: repo → Settings → Secrets and variables → Actions →
   New repository secret → name `BLOG_REPO_TOKEN`, value = the token.
3. **Add the workflow**: copy `docs/tech-digest/publish-to-blog.yml` from this repo to
   `.github/workflows/publish-to-blog.yml` in Digital-Dhaba, and commit (`BLOG_BRANCH: main`).
4. **Test**: Digital-Dhaba → Actions → "Publish issue to blogsbykush.com" → Run workflow
   (leave the issue blank to publish the latest).

## Emailing the issue (Kit)

The same workflow then runs `scripts/kit_send_digest.py`, which schedules the issue as a Kit broadcast for
**Thursday 07:00 IST** (or sends right away if run on Thursday after 07:00). It swaps the embedded hero for
`https://blogsbykush.com/tech-digest/<date>/hero.jpg` and maps the placeholders to Kit's unsubscribe tag,
the web issue URL and an email-a-friend link. Off until `KIT_DIGEST_ENABLED` is set; setup, test mode and
dry run: `docs/NEWSLETTER.md`.

## Weekly routine

Run `./run_digest.sh`, commit and push `issues/<date>/` to Digital-Dhaba. That's it: the Action
imports the issue, pushes to the blog, and the site redeploys within a couple of minutes.

## Manual import (fallback)

```bash
python3 scripts/add_digest.py ../Digital-Dhaba/issues/2026-09-27
```

Re-running for the same date overwrites that issue (use this to fix a published issue).
