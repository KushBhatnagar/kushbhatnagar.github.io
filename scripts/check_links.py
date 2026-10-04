#!/usr/bin/env python3
"""
Check every external link in a Markdown file.

    python3 scripts/check_links.py content/posts/<slug>.md

Prints one line per link: OK (2xx/3xx), BROKEN (4xx/5xx) or UNREACHABLE (network/DNS/proxy problem, so
the link is NOT checked; open it yourself). Exit code 1 if any link is BROKEN. Standard library only.
Used by the /learning-note, /build-log-entry and /breakdown-post skills.
"""
import re, sys, urllib.error, urllib.request

LINK = re.compile(r"\]\((https?://[^)\s]+)\)|^source_url:\s*(https?://\S+)", re.M)


def check(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": "Mozilla/5.0 (link check)"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return "OK", r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 429):
                continue  # some sites refuse HEAD; retry with GET
            return ("BROKEN" if e.code in (404, 410) or e.code >= 500 else "CHECK"), e.code
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            return "UNREACHABLE", getattr(e, "reason", e)
    return "CHECK", "refused"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    text = open(sys.argv[1], encoding="utf-8").read()
    urls = sorted({a or b for a, b in LINK.findall(text)})
    broken = 0
    for url in urls:
        status, detail = check(url)
        broken += status == "BROKEN"
        print(f"{status:12} {detail}  {url}")
    if not urls:
        print("No external links found.")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
