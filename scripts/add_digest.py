#!/usr/bin/env python3
"""
Import a Digital Dhaba (Tech Digest) issue into the blog.

    python3 scripts/add_digest.py ../Digital-Dhaba/issues/2026-09-27

Reads newsletter.html + digest.json from the issue folder and writes the page bundle
content/tech-digest/<YYYY-MM-DD>/:
    newsletter.txt   the issue HTML, byte-for-byte (.txt so Hugo treats it as a plain resource;
                     layouts/tech-digest/single.html serves it with the site bar, analytics,
                     SEO tags and fixed placeholder links added at build time)
    digest.json      structured data (top stories, sections) used for archive cards
    hero.<ext>       masthead image extracted from the HTML (social preview; hosted copy for email)
    index.md         front matter + top stories as Markdown (feeds RSS and site search)

Safe to re-run: an existing issue is overwritten. Used locally and by the Digital Dhaba
publish workflow (see docs/TECH_DIGEST.md). Standard library only.
"""
import base64, datetime, json, pathlib, re, shutil, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DEST = REPO / "content" / "tech-digest"


def yaml_str(s):
    return json.dumps(s, ensure_ascii=False)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    html_path, json_path = src / "newsletter.html", src / "digest.json"
    for p in (html_path, json_path):
        if not p.exists():
            sys.exit(f"Missing {p}")

    digest = json.loads(json_path.read_text(encoding="utf-8"))
    issue = digest["issue"]
    date = datetime.datetime.strptime(issue["date"], "%B %d, %Y").date()
    out = DEST / date.isoformat()
    out.mkdir(parents=True, exist_ok=True)

    html = html_path.read_text(encoding="utf-8")
    (out / "newsletter.txt").write_text(html, encoding="utf-8")
    shutil.copy(json_path, out / "digest.json")

    m = re.search(r'src="data:image/(jpeg|jpg|png|webp);base64,([^"]+)"', html)
    for old in out.glob("hero.*"):
        old.unlink()
    if m:
        ext = "jpg" if m.group(1) in ("jpeg", "jpg") else m.group(1)
        (out / f"hero.{ext}").write_bytes(base64.b64decode(m.group(2)))

    name = issue.get("name", "Digital Dhaba")
    top = digest.get("topStories", [])
    titles = "; ".join(s["title"] for s in top[:3])
    description = f'{issue.get("dek", "The week in tech")}. Top stories: {titles}.'
    body = "\n".join(f'- [{s["title"]}]({s["url"]}): {s.get("summary", "")}' for s in top)

    (out / "index.md").write_text(f"""---
title: {yaml_str(f"{name} — {issue['date']}")}
date: {date.isoformat()}
url: /tech-digest/{date.isoformat()}/
description: {yaml_str(description)}
summary: {yaml_str(issue.get("dek", ""))}
story_count: {yaml_str(issue.get("count", ""))}
images: ["hero.{ext if m else 'jpg'}"]
build:
  publishResources: false   # only files the page uses (hero) are published, not the raw sources
---

## Top stories

{body}
""", encoding="utf-8")

    print(f"Imported {name} {date} -> {out.relative_to(REPO)}/ ({len(top)} top stories)")


if __name__ == "__main__":
    main()
