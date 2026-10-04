"""
Tiny Kit (ConvertKit) API v4 client shared by kit_notify_posts.py and kit_send_digest.py.
Standard library only, so the GitHub Actions jobs need no pip install.

Environment (GitHub: secrets for the key, repository *variables* for the rest):
    KIT_API_KEY            v4 API key (Kit → Settings → Developer). Secret.
    KIT_EMAIL_TEMPLATE_ID  ID of the minimal custom email template (docs/kit/email-template.html).
    KIT_TEST_TAG_ID        If set: TEST MODE. Broadcasts go only to subscribers with this tag (just Kush).
                           Remove the variable to send to everyone.
    KIT_SEND               "true" to actually create broadcasts. Anything else = dry run (prints payload).
    KIT_FROM_EMAIL         Optional sender address (must be verified in Kit), e.g. kush@blogsbykush.com.
    KIT_API_BASE           Optional; defaults to https://api.kit.com/v4 (override for local tests).

API reference: https://developers.kit.com/api-reference/broadcasts/create-a-broadcast
"""
import datetime, json, os, sys, urllib.error, urllib.request

API_BASE = os.environ.get("KIT_API_BASE", "https://api.kit.com/v4").rstrip("/")


def env_flag(name):
    return os.environ.get(name, "").strip().lower() == "true"


def _request(method, path, body=None):
    key = os.environ.get("KIT_API_KEY", "")
    if not key:
        sys.exit("KIT_API_KEY is not set")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API_BASE + path, data=data, method=method, headers={
        "X-Kit-Api-Key": key,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "blogsbykush-kit/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"Kit API {method} {path} failed: HTTP {e.code}: {e.read().decode(errors='replace')[:500]}")
    except urllib.error.URLError as e:
        sys.exit(f"Kit API {method} {path} failed: could not reach {API_BASE} ({e.reason})")


def existing_subjects(max_pages=5):
    """Subjects of recent broadcasts, used to skip duplicates when a workflow re-runs."""
    subjects, after = set(), None
    for _ in range(max_pages):
        q = "?per_page=100" + (f"&after={after}" if after else "")
        res = _request("GET", "/broadcasts" + q)
        for b in res.get("broadcasts", []):
            if b.get("subject"):
                subjects.add(b["subject"])
        page = res.get("pagination", {})
        if not page.get("has_next_page"):
            break
        after = page.get("end_cursor")
    return subjects


def utc_iso(dt):
    return dt.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def create_broadcast(subject, content, preview_text="", description="", send_at=None):
    """Create (and schedule) a broadcast. send_at: aware datetime; None → ~2 minutes from now.

    Respects KIT_SEND (dry run unless "true"), KIT_TEST_TAG_ID (test mode) and duplicate subjects.
    Returns the created broadcast dict, or None when skipped / dry run.
    """
    send_at = send_at or datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=2)
    payload = {
        "subject": subject,
        "content": content,
        "preview_text": preview_text,
        "description": description or subject,
        "public": False,                      # our own site is the web archive
        "send_at": utc_iso(send_at),
    }
    template = os.environ.get("KIT_EMAIL_TEMPLATE_ID", "").strip()
    if template:
        payload["email_template_id"] = int(template)
    sender = os.environ.get("KIT_FROM_EMAIL", "").strip()
    if sender:
        payload["email_address"] = sender
    test_tag = os.environ.get("KIT_TEST_TAG_ID", "").strip()
    if test_tag:
        payload["subscriber_filter"] = [{"all": [{"type": "tag", "ids": [int(test_tag)]}]}]
        payload["subject"] = "[TEST] " + subject

    mode = "TEST (tag %s only)" % test_tag if test_tag else "ALL SUBSCRIBERS"
    if not env_flag("KIT_SEND"):
        preview = dict(payload, content=f"<{len(content)} chars of HTML>")
        print(f"DRY RUN ({mode}) — would create broadcast:\n" + json.dumps(preview, indent=2))
        return None
    if payload["subject"] in existing_subjects():
        print(f"SKIP: a broadcast with subject {payload['subject']!r} already exists.")
        return None
    res = _request("POST", "/broadcasts", payload)
    b = res.get("broadcast", res)
    print(f"Created broadcast {b.get('id')} ({mode}), send_at {payload['send_at']}: {payload['subject']}")
    return b
