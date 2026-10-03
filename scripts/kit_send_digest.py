#!/usr/bin/env python3
"""
Email a Digital Dhaba issue to Kit subscribers, scheduled for Thursday morning.

    python3 scripts/kit_send_digest.py ../Digital-Dhaba/issues/2026-09-27

Run by the Digital-Dhaba workflow right after the issue is published to the blog
(docs/tech-digest/publish-to-blog.yml). It:
  1. takes newsletter.html and makes it email-ready:
       - the embedded (base64) hero image → the hosted copy https://blogsbykush.com/tech-digest/<date>/hero.jpg
         (Gmail/Outlook block embedded images)
       - {{UNSUBSCRIBE_URL}}     → Kit's unsubscribe merge tag (KIT_UNSUBSCRIBE_TAG)
       - {{VIEW_IN_BROWSER_URL}} → the issue's page on the blog
       - {{FORWARD_URL}}         → a mailto: "forward to a friend" link with the issue URL
       - keeps the <style> block and the <body> contents (Kit's template provides the outer HTML)
  2. schedules the broadcast for the next send slot (default Thursday 07:00 IST). The issue is published
     early on Thursday, so normally it goes out at 07:00; if the run happens on Thursday after 07:00, it
     sends in ~2 minutes, after checking the hero image is live.
  3. skips if a broadcast with the same subject already exists (safe to re-run).

Env: see scripts/kit_api.py (dry run unless KIT_SEND=true; test mode while KIT_TEST_TAG_ID is set), plus
    DIGEST_SEND_WEEKDAY  0=Mon … 3=Thu … 6=Sun (default 3)   DIGEST_SEND_TIME  HH:MM in IST (default 07:00)
    KIT_UNSUBSCRIBE_TAG  default "{{ unsubscribe_url }}"   SITE_URL  default https://blogsbykush.com
"""
import datetime, json, os, pathlib, re, sys, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
import kit_api  # noqa: E402

SITE = os.environ.get("SITE_URL", "https://blogsbykush.com").rstrip("/")
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def next_slot(now=None):
    """Next send slot (aware datetime). If we're past today's slot on the send day, send now."""
    now = now or datetime.datetime.now(IST)
    weekday = int(os.environ.get("DIGEST_SEND_WEEKDAY", "3"))
    hh, mm = (int(x) for x in os.environ.get("DIGEST_SEND_TIME", "07:00").split(":"))
    days = (weekday - now.weekday()) % 7
    slot = (now + datetime.timedelta(days=days)).replace(hour=hh, minute=mm, second=0, microsecond=0)
    if slot <= now:  # send day, after the send time
        return None
    return slot


def wait_until_live(url, minutes=15):
    deadline = time.time() + minutes * 60
    while True:
        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status == 200:
                    return True
        except urllib.error.URLError:
            pass
        if time.time() > deadline:
            return False
        print(f"Waiting for {url} to go live …")
        time.sleep(30)


def email_ready(html_text, date, title):
    issue_url = f"{SITE}/tech-digest/{date}/"
    hero_url = f"{SITE}/tech-digest/{date}/hero.jpg"
    unsub = os.environ.get("KIT_UNSUBSCRIBE_TAG", "{{ unsubscribe_url }}")
    forward = "mailto:?subject=" + urllib.parse.quote(title) + "&body=" + urllib.parse.quote(
        f"Thought you'd like this week's Digital Dhaba: {issue_url}")

    html_text = re.sub(r'src="data:image/[a-z]+;base64,[^"]+"', f'src="{hero_url}"', html_text, count=1)
    html_text = (html_text.replace("{{UNSUBSCRIBE_URL}}", unsub)
                          .replace("{{VIEW_IN_BROWSER_URL}}", issue_url)
                          .replace("{{FORWARD_URL}}", forward))
    styles = "".join(re.findall(r"<style[^>]*>.*?</style>", html_text, flags=re.S | re.I))
    body = re.search(r"<body[^>]*>(.*)</body>", html_text, flags=re.S | re.I)
    content = styles + (body.group(1) if body else html_text)
    leftovers = re.findall(r"\{\{[A-Z_]+\}\}", content)
    if leftovers:
        sys.exit(f"Unmapped placeholders in newsletter.html: {sorted(set(leftovers))}")
    return content, issue_url, hero_url


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    digest = json.loads((src / "digest.json").read_text(encoding="utf-8"))
    issue = digest["issue"]
    date = datetime.datetime.strptime(issue["date"], "%B %d, %Y").date().isoformat()
    name = issue.get("name", "Digital Dhaba")
    title = f"{name} — {issue['date']}"
    top = digest.get("topStories", [])

    content, issue_url, hero_url = email_ready((src / "newsletter.html").read_text(encoding="utf-8"), date, title)
    lead = top[0]["title"] if top else issue.get("dek", "")
    subject = f"{name}: {lead}" if lead else title
    preview = f"{issue.get('dek', '')}. " + "; ".join(s["title"] for s in top[1:3])

    slot = next_slot()
    if slot is None:
        print("Past this week's send time: sending now (after the issue page is live).")
        if kit_api.env_flag("KIT_SEND") and not wait_until_live(hero_url):
            sys.exit(f"{hero_url} is not live; not sending an email with a broken image. Re-run later.")
    else:
        print(f"Scheduling for {slot.strftime('%a %d %b %Y %H:%M IST')}.")
    kit_api.create_broadcast(subject=subject[:150], content=content, preview_text=preview[:150],
                             description=f"{title} ({issue_url})", send_at=slot)


if __name__ == "__main__":
    main()
