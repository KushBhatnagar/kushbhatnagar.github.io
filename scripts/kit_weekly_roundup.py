#!/usr/bin/env python3
"""
The weekly letter: one Kit email with everything published on the blog in the week that just ended,
Sunday to Saturday (Concept Breakdowns, Build Log, Learning Notes, …). Digital Dhaba issues are NOT included; they
go out separately on Thursdays (scripts/kit_send_digest.py).

    python3 scripts/kit_weekly_roundup.py            # run by .github/workflows/weekly-roundup.yml

Reads the LIVE https://blogsbykush.com/posts.json (blog posts only, no Tech Digest issues) and picks
posts dated in the 7 days BEFORE today (today = the letter's Sunday, IST; today's own posts go in next
week's letter). No new posts → no email. The letter is booked in Kit for 09:00 IST today (Kit sends on
time even when GitHub starts the run hours late; it did on 2026-10-11), or sent right away if that time
has passed. A re-run on the same day produces the same subject and is skipped as a duplicate.

Note: a post is picked by its front-matter `date`. When you publish a post that sat in draft for a
while, set `date` to the publishing day, or it may fall outside the 7-day window.

Kit settings come from env vars (see scripts/kit_api.py): dry run unless KIT_SEND=true, test mode while
KIT_TEST_TAG_ID is set. Also: SITE_URL (default https://blogsbykush.com), ROUNDUP_DAYS (default 7).
"""
import datetime, html, json, os, sys, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
import kit_api  # noqa: E402

SITE = os.environ.get("SITE_URL", "https://blogsbykush.com").rstrip("/")
DAYS = int(os.environ.get("ROUNDUP_DAYS", "7"))
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
SEND_TIME = os.environ.get("ROUNDUP_SEND_TIME", "09:00")  # IST, on the letter's day
LABELS = {
    "concept-breakdown": "Concept Breakdown",
    "build-log": "Build Log",
    "learning-notes": "Learning Note",
}


def label(p):
    for c in p.get("categories", []):
        if c in LABELS:
            return LABELS[c]
    return "New post"


def card(p):
    e = html.escape
    url = p["url"] + "?utm_source=kit&utm_medium=email&utm_campaign=weekly"
    img = (f'<tr><td style="padding:0 20px"><a href="{e(url)}"><img src="{e(p["image"])}" alt="" width="560" '
           f'style="display:block;width:100%;max-width:560px;height:auto;border:0;border-radius:8px"></a></td></tr>'
           if p.get("image") and "og-default" not in p["image"] else "")
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;background:#ffffff;border:1px solid #eeeeee;border-radius:10px;margin:0 0 18px">
<tr><td style="padding:22px 20px 6px;font-family:Helvetica,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#b8660b">{e(label(p))}</td></tr>
<tr><td style="padding:0 20px 14px;font-family:Helvetica,Arial,sans-serif;font-size:21px;line-height:1.3;font-weight:700;color:#131313"><a href="{e(url)}" style="color:#131313;text-decoration:none">{e(p["title"])}</a></td></tr>
{img}
<tr><td style="padding:14px 20px 4px;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:1.55;color:#333333">{e(p.get("summary", ""))}</td></tr>
<tr><td style="padding:12px 20px 24px"><a href="{e(url)}" style="display:inline-block;background:#f4a33a;color:#131313;font-family:Helvetica,Arial,sans-serif;font-size:15px;font-weight:700;text-decoration:none;padding:11px 20px;border-radius:999px">Read it &rarr;</a></td></tr>
</table>"""


def email_html(posts, week_label):
    intro = "Here's what I published on the blog this week."
    cards = "\n".join(card(p) for p in posts)
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#fbf8f1">
<tr><td align="center" style="padding:28px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px">
<tr><td style="padding:0 4px 4px;font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#11a8cc">Blogs by Kush · {html.escape(week_label)}</td></tr>
<tr><td style="padding:0 4px 18px;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:1.5;color:#333333">{intro}</td></tr>
</table>
{cards}
<p style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#6c6c6c;margin:8px 0 0">Learn. Build. Explain. &middot; <a href="{SITE}/" style="color:#0a7a96">blogsbykush.com</a></p>
</td></tr></table>"""


def pick(posts, today):
    """Posts dated in the DAYS days before today (Sunday's letter: the previous Sunday to Saturday).
    Today's posts are left for next week, so the run can happen early on Sunday without missing any."""
    start, end = today - datetime.timedelta(days=DAYS), today - datetime.timedelta(days=1)
    return [p for p in posts if start <= datetime.date.fromisoformat(p["date"]) <= end]


def send_slot(now):
    """Today at SEND_TIME (IST), or None (= send right away) if that has passed."""
    hh, mm = (int(x) for x in SEND_TIME.split(":"))
    slot = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
    return slot if slot > now else None


def main():
    with urllib.request.urlopen(SITE + "/posts.json", timeout=30) as r:
        posts = json.load(r)["posts"]
    now = datetime.datetime.now(IST)
    today = now.date()
    week = pick(posts, today)
    if not week:
        print(f"No posts dated in the {DAYS} days before {today}; no weekly letter this week.")
        return
    week.sort(key=lambda p: p["date"])
    week_label = "Week of " + today.strftime("%-d %b %Y")
    # Plain subject, like the digest's (Kush, 2026-10-04); the post titles go in the preview text.
    subject = f"Blogs by Kush — week of {today.strftime('%-d %b %Y')}"
    print(f"{len(week)} post(s): " + ", ".join(p["url"] for p in week))
    kit_api.create_broadcast(
        subject=subject[:150], content=email_html(week, week_label),
        preview_text="; ".join(p["title"] for p in week)[:150],
        description=f"Weekly letter, {week_label}", send_at=send_slot(now))


if __name__ == "__main__":
    main()
