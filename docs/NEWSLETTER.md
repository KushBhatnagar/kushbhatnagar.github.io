# Newsletter (Kit) — setup and how it works

Subscribers live in **Kit (Free Plan)**. Subscribers get **at most two emails a week**, both automatic:

| Email | When | Sent by |
|---|---|---|
| **Digital Dhaba** (the full newsletter) | **Thursday 07:00 IST**, after the issue is published early Thursday | Digital-Dhaba workflow → `scripts/kit_send_digest.py` |
| **Weekly letter**: every post from the last 7 days (Concept Breakdown, Build Log, Learning Notes) with image, summary and "Read it" button | **Sunday 09:00 IST**, only if something was published | `.github/workflows/weekly-roundup.yml` → `scripts/kit_weekly_roundup.py` |

There are no per-post emails. The weekly letter picks posts by their front-matter `date`, so when a draft
finally goes live, set `date` to the publishing day.

Signups: every signup box on the site (`layouts/_partials/newsletter_form.html`) posts to **one Kit form**,
ID in `hugo.toml` → `params.kit.form` (`10000596`).

The form uses **double opt-in**: nobody is added until they click the confirmation email, which also
keeps bots and fake addresses out.

## Safety switches (GitHub repository *variables*, no code changes)

| Variable | Effect |
|---|---|
| `KIT_ROUNDUP_ENABLED` (blog repo) / `KIT_DIGEST_ENABLED` (Digital-Dhaba) | `true` turns that email on. Unset = the step doesn't run |
| `KIT_SEND` | `true` = really create broadcasts. Anything else = **dry run** (the workflow log shows the email it would send) |
| `KIT_TEST_TAG_ID` | Optional. While set, emails go **only to subscribers with that tag** (just you) and subjects start with `[TEST]`. Delete it to send to everyone |
| `KIT_EMAIL_TEMPLATE_ID` | Optional custom template (`docs/kit/email-template.html`); Kit's default is used if unset |
| `KIT_FROM_EMAIL` | Optional sender, e.g. `kush@blogsbykush.com` (must be verified in Kit) |

Built-in guards: duplicate subjects are skipped (safe to re-run); no new posts → no weekly letter; the digest
waits for its hero image to be live before an immediate send. The weekly letter can also be run by hand:
Actions → "Weekly letter (Kit)" → Run workflow.

---

## One-time setup (Kush)

### Done (2026-10-04)
- Kit account (Free), postal address, unsubscribe survey.
- Sending address `kush@blogsbykush.com`; domain `blogsbykush.com` verified (SPF/DKIM CNAMEs + `_dmarc` TXT).
- One inline form (ID `10000596`) with the confirmation email (double opt-in) on; wired into the site.
- v4 API key saved as secret `KIT_API_KEY` in both repos (old v3 key/secret replaced); variable
  `KIT_FROM_EMAIL` = `kush@blogsbykush.com` in both repos.

### Done after go-live (2026-10-04)
- Digital-Dhaba workflow copied with the Kit email step (`BLOG_BRANCH: main`); `KIT_DIGEST_ENABLED` and
  `KIT_SEND` = `true`; inbox test sent (`send_now`). First scheduled send: Thursday 2026-10-08.
- Weekly letter switches (`KIT_ROUNDUP_ENABLED`, `KIT_SEND`) on in the blog repo; first letter sent by hand.
- Kush subscribed; audited Mailchimp list uploaded with tag `from-mailchimp`.

### Still to do
1. **Close Mailchimp** (download a final full export first and keep it on your machine). Optional afterwards:
   remove the legacy Mailchimp fallback form (`newsletter_form.html`, `hugo.toml` comment), which only shows
   if `params.kit.form` is emptied.

Optional later: Google Postmaster Tools for blogsbykush.com; a custom email template (`KIT_EMAIL_TEMPLATE_ID`).

---

## Moving the Mailchimp list (done 2026-10-04; kept as the record of how)

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
4. **Close Mailchimp** (safe now: the live site's forms all post to Kit). Before closing, download a final
   full export and keep it on your machine as the record of who signed up and when.
