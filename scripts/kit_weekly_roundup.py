#!/usr/bin/env python3
"""
The weekly letter: one Kit email with everything published on the blog in the last 7 days
(Concept Breakdowns, Build Log, Learning Notes, …). Digital Dhaba issues are NOT included; they
go out separately on Thursdays (scripts/kit_send_digest.py).

    python3 scripts/kit_weekly_roundup.py            # run by .github/workflows/weekly-roundup.yml

Reads the LIVE https://blogsbykush.com/posts.json (blog posts only, no Tech Digest issues) and picks
posts whose `date` falls in the last 7 days. No new posts → no email. A re-run in the same week
produces the same subject and is skipped as a duplicate.

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
    start = today - datetime.timedelta(days=DAYS - 1)
    return [p for p in posts if start <= datetime.date.fromisoformat(p["date"]) <= today]


def main():
    with urllib.request.urlopen(SITE + "/posts.json", timeout=30) as r:
        posts = json.load(r)["posts"]
    today = datetime.datetime.now(IST).date()
    week = pick(posts, today)
    if not week:
        print(f"No posts dated in the last {DAYS} days; no weekly letter this week.")
        return
    week.sort(key=lambda p: p["date"])
    week_label = "Week of " + today.strftime("%-d %b %Y")
    lead = week[-1]["title"]
    more = f" (+{len(week) - 1} more)" if len(week) > 1 else ""
    subject = f"This week on Blogs by Kush: {lead}{more}"
    print(f"{len(week)} post(s): " + ", ".join(p["url"] for p in week))
    kit_api.create_broadcast(
        subject=subject[:150], content=email_html(week, week_label),
        preview_text="; ".join(p["title"] for p in week)[:150],
        description=f"Weekly letter, {week_label}")


if __name__ == "__main__":
    main()
