# Newsletter (Kit) — setup and how it works

Subscribers live in **Kit (Free Plan)**. Subscribers get **at most two emails a week**, both automatic:

| Email | When | Sent by |
|---|---|---|
| **Digital Dhaba** (the full newsletter) | **Thursday 07:00 IST**, after the issue is published early Thursday | Digital-Dhaba workflow → `scripts/kit_send_digest.py` |
| **Weekly letter**: every post from the last 7 days (Concept Breakdown, Build Log, Learning Notes) with image, summary and "Read it" button | **Sunday 09:00 IST**, only if something was published | `.github/workflows/weekly-roundup.yml` → `scripts/kit_weekly_roundup.py` |

There are no per-post emails. The weekly letter picks posts by their front-matter `date`, so when a draft
finally goes live, set `date` to the publishing day.

Signups come from the site's forms (all in `layouts/_partials/newsletter_form.html`), one Kit form per source
so you can compare where subscribers come from:

| Kit form | Used on | `hugo.toml` key |
|---|---|---|
| **Blog** | end of every post, Build Log, Tech Digest | `params.kit.forms.blog` |
| **LinkedIn** | `/subscribe/` (the link you share on LinkedIn) | `params.kit.forms.linkedin` |

Every form uses **double opt-in**: nobody is added until they click the confirmation email, which also
keeps bots and fake addresses out.

## Safety switches (GitHub repository *variables*, no code changes)

| Variable | Effect |
|---|---|
| `KIT_ROUNDUP_ENABLED` (blog repo) / `KIT_DIGEST_ENABLED` (Digital-Dhaba) | `true` turns that email on. Unset = the step doesn't run |
| `KIT_SEND` | `true` = really create broadcasts. Anything else = **dry run** (the workflow log shows the email it would send) |
| `KIT_TEST_TAG_ID` | While set, emails go **only to subscribers with that tag** (just you) and subjects start with `[TEST]`. Delete it to send to everyone |
| `KIT_EMAIL_TEMPLATE_ID` | The minimal template below |
| `KIT_FROM_EMAIL` | Optional sender, e.g. `kush@blogsbykush.com` (must be verified in Kit) |

Built-in guards: duplicate subjects are skipped (safe to re-run); no new posts → no weekly letter; the digest
waits for its hero image to be live before an immediate send. The weekly letter's schedule only runs from
`main`, so it starts after go-live (or run it by hand: Actions → "Weekly letter (Kit)" → Run workflow).

---

## One-time setup (Kush)

### 1. Kit account and settings
1. Sign up at kit.com (Free plan).
2. **Settings → General / Account**: your name and **postal address** (Kit puts it in every email footer;
   a PO box or virtual mailbox address is fine).
3. **Settings → Email → Confirmation email** (double opt-in): keep **Auto-confirm unchecked**. Confirmation line:
   *"Confirm to get Digital Dhaba every Thursday, plus a short Sunday letter with my new posts."*

### 2. Sending domain and From address
1. Kit → **Settings → Email → Sending domain** (wording may differ) → add `blogsbykush.com`.
2. Kit shows a few **CNAME** records. Add them at the company where blogsbykush.com's DNS is managed
   (your domain registrar or DNS host). Wait for Kit to show "Verified" (minutes to a few hours).
3. Also add a **DMARC** record (Gmail/Yahoo expect one for newsletters):
   `TXT` record, name `_dmarc`, value `v=DMARC1; p=none; rua=mailto:kush@blogsbykush.com`
4. Set the From address to `kush@blogsbykush.com` (a separate step in Kit after the domain is verified).
   Make sure that address can actually receive mail (replies go there).
5. Optional but recommended: add the domain to **Google Postmaster Tools** to watch spam rates.

### 3. Email template
Kit → **Send → Email Templates → New template** → choose the HTML/code option → paste
`docs/kit/email-template.html` → save. Open it again and copy the **template ID** from the URL.

### 4. Forms
Create two forms (Kit → **Grow → Landing Pages & Forms → Create new → Form**, any style): **Blog** and
**LinkedIn**. For each, open it → **Embed** → copy the number from the embed code
(the form ID), then put the IDs into `hugo.toml`:
```toml
[params.kit.forms]
  blog = "1234567"
  linkedin = "2345678"
```
(Or send the IDs to Claude.) In each form's settings, set the **success redirect** to
`https://blogsbykush.com/` or leave Kit's default "check your email" page.

### 5. Test tag
Kit → **Subscribers** → add yourself (confirm the email) → add a tag `test` to yourself. Copy the tag's
ID (open the tag → number in the URL).

### 6. API key and GitHub settings
1. Kit → **Settings → Developer** → create a **v4 API key**. Copy it (don't paste it anywhere else).
2. In **both** repos (blog `kushbhatnagar.github.io` and `Digital-Dhaba`): Settings → Secrets and variables →
   Actions:
   - **Secrets** tab → `KIT_API_KEY` = the key.
   - **Variables** tab → `KIT_EMAIL_TEMPLATE_ID` = template ID, `KIT_TEST_TAG_ID` = test tag ID,
     `KIT_FROM_EMAIL` = `kush@blogsbykush.com`.
3. Blog repo variable `KIT_ROUNDUP_ENABLED` = `true`; Digital-Dhaba variable `KIT_DIGEST_ENABLED` = `true`.
4. Copy the updated `docs/tech-digest/publish-to-blog.yml` into Digital-Dhaba
   (`.github/workflows/publish-to-blog.yml`), keeping your `BLOG_BRANCH` value.

### 7. Test (still safe: test mode + dry run)
1. Re-run the Digital-Dhaba workflow (Actions → Run workflow). The "Email the issue" step should log
   `DRY RUN (TEST (tag … only))` with the subject and send time.
2. Set variable `KIT_SEND` = `true` in Digital-Dhaba and re-run: a `[TEST]` broadcast appears in Kit →
   Broadcasts, scheduled for Thursday 07:00 IST. Open it in Kit and **send a preview to yourself** to check
   it in Gmail. Delete the scheduled test broadcast if you don't want it to go out.
3. Weekly letter: blog repo → Actions → "Weekly letter (Kit)" → Run workflow. With `KIT_SEND` unset it logs
   the email (dry run); with `KIT_SEND` = `true` and the test tag set, it sends a `[TEST]` letter to you
   (needs at least one post dated in the last 7 days on the live site).

### 8. Go fully live
Delete `KIT_TEST_TAG_ID` in both repos. From then on, emails go to all confirmed subscribers.

---

## Moving the Mailchimp list (direct upload of the audited list)

Decision (Kush, 2026-10-03): upload only the audited real subscribers to Kit, then close Mailchimp. No
re-permission email. The list is small (about 15 real people out of 267; the rest are bot signups), and these
people did sign up for this newsletter.

1. **Audit** (on your machine; the CSVs never go into git):
   `python3 scripts/audit_subscribers.py <mailchimp-export>.csv` → `keep.csv`, `review.csv`, `junk.csv`.
   - From `keep.csv`, remove your own and test addresses.
   - From `review.csv`, add only people you recognise. When in doubt, leave them out: Kit treats imported
     subscribers as confirmed, so a wrong address can't be filtered later.
   - Never upload or email anyone in `junk.csv` (bot-made or other people's real addresses).
2. **Upload to Kit** (after the Kit setup above; ideally right after go-live): Kit → **Subscribers → Import**
   (Add subscribers → import a CSV) → upload a CSV with the `email` column of your final list → add the tag
   `from-mailchimp`. (Menu names not verified from the Claude session; Kit's help covers CSV import.)
3. **Tell them once.** The first email they get (the next Digital Dhaba) should say in one line that the
   newsletter moved and they can unsubscribe with one click, e.g. at the top of the issue for the
   `from-mailchimp` tag, or a short one-off broadcast to that tag:
   > Blogs by Kush has a new home and a new format: Digital Dhaba every Thursday and a short Sunday letter
   > with what I published. You signed up on the old list; if this isn't for you anymore, unsubscribe below.
4. **Close Mailchimp only after go-live and after the Kit form IDs are in `hugo.toml`.** Until then the live
   Jekyll site's form and the Hugo fallback form still post to Mailchimp. Before closing, download a final
   full export and keep it on your machine as the record of who signed up and when.
