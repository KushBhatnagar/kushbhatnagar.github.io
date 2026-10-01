#!/usr/bin/env python3
"""
Email newly published blog posts to Kit subscribers (one broadcast per post).

Two steps, run by .github/workflows/hugo.yml:

  1. plan   (build job, BEFORE deploy)
     python3 scripts/kit_notify_posts.py plan public/posts.json new-posts.json
     Fetches the LIVE https://blogsbykush.com/posts.json and writes the posts that are in the new
     build but not live yet. Safety guards:
       - live posts.json missing (e.g. the go-live deploy from Jekyll) → nothing is sent, just logged
       - only posts dated within the last 14 days
       - more than 3 new posts in one deploy → nothing is sent (looks like a bulk change, not a post)

  2. send   (notify job, AFTER deploy, so links and images work)
     python3 scripts/kit_notify_posts.py send new-posts.json

Kit settings come from env vars (see scripts/kit_api.py): dry run unless KIT_SEND=true,
test mode while KIT_TEST_TAG_ID is set.
"""
import datetime, html, json, os, sys, urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
import kit_api  # noqa: E402

SITE = os.environ.get("SITE_URL", "https://blogsbykush.com").rstrip("/")
MAX_AGE_DAYS = 14
MAX_NEW = 3


def load_live():
    try:
        with urllib.request.urlopen(SITE + "/posts.json", timeout=30) as r:
            return json.load(r)["posts"]
    except (urllib.error.URLError, ValueError, KeyError) as e:
        print(f"Live posts.json not available ({e}); treating this deploy as the baseline. Nothing to send.")
        return None


def plan(new_path, out_path):
    new = json.load(open(new_path, encoding="utf-8"))["posts"]
    live = load_live()
    picked = []
    if live is not None:
        live_urls = {p["url"] for p in live}
        cutoff = datetime.date.today() - datetime.timedelta(days=MAX_AGE_DAYS)
        fresh = [p for p in new if p["url"] not in live_urls]
        picked = [p for p in fresh if datetime.date.fromisoformat(p["date"]) >= cutoff]
        for p in fresh:
            if p not in picked:
                print(f"Not emailing (older than {MAX_AGE_DAYS} days): {p['url']}")
        if len(picked) > MAX_NEW:
            print(f"{len(picked)} new posts in one deploy (> {MAX_NEW}): looks like a bulk change, sending none.")
            picked = []
    json.dump({"posts": picked}, open(out_path, "w", encoding="utf-8"), indent=2)
    print(f"Planned {len(picked)} post email(s): " + ", ".join(p["url"] for p in picked))


def email_html(p):
    e = html.escape
    url = p["url"] + "?utm_source=kit&utm_medium=email&utm_campaign=new-post"
    img = (f'<a href="{e(url)}"><img src="{e(p["image"])}" alt="" width="560" '
           f'style="display:block;width:100%;max-width:560px;height:auto;border:0;border-radius:8px"></a>'
           if p.get("image") else "")
    label = "New Concept Breakdown" if "concept-breakdown" in p.get("categories", []) else "New on Blogs by Kush"
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#fbf8f1">
<tr><td align="center" style="padding:28px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;background:#ffffff;border:1px solid #eeeeee;border-radius:10px">
<tr><td style="padding:24px 20px 8px;font-family:Helvetica,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#b8660b">{e(label)}</td></tr>
<tr><td style="padding:0 20px 14px;font-family:Helvetica,Arial,sans-serif;font-size:24px;line-height:1.25;font-weight:700;color:#131313">{e(p["title"])}</td></tr>
<tr><td style="padding:0 20px">{img}</td></tr>
<tr><td style="padding:16px 20px 4px;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:1.55;color:#333333">{e(p.get("summary", ""))}</td></tr>
<tr><td style="padding:16px 20px 28px"><a href="{e(url)}" style="display:inline-block;background:#f4a33a;color:#131313;font-family:Helvetica,Arial,sans-serif;font-size:16px;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:999px">Read it on Blogs by Kush &rarr;</a></td></tr>
</table>
<p style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#6c6c6c;margin:16px 0 0">Learn. Build. Explain. &middot; <a href="{SITE}/" style="color:#0a7a96">blogsbykush.com</a></p>
</td></tr></table>"""


def send(plan_path):
    posts = json.load(open(plan_path, encoding="utf-8"))["posts"]
    if not posts:
        print("No new posts to email.")
        return
    for p in posts:
        kit_api.create_broadcast(subject=p["title"], content=email_html(p),
                                 preview_text=p.get("summary", "")[:150],
                                 description=f"New post: {p['url']}")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "plan":
        plan(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3 and sys.argv[1] == "send":
        send(sys.argv[2])
    else:
        sys.exit(__doc__)
