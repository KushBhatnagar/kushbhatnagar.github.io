#!/usr/bin/env python3
"""
One-off: rename the "ML Made Easy" series to "Concept Breakdown".

For every post in category ml-made-easy:
  - categories -> ["concept-breakdown"]
  - url        -> /concept-breakdown/<slug>/   (typo slug data-lekage -> data-leakage)
  - aliases    -> [old url]   (Hugo emits a redirect page at the old address)
  - disqus_identifier -> old url, so existing comment threads stay attached
  - images     -> [first comic image]   (social preview + listing thumbnail)
  - the write-up that lived only in `summary:` (shown on list pages, never on the
    post itself) is copied into the body when the body doesn't already contain it,
    and `summary:` is shortened to a one-line teaser
  - "ML Made Easy" wording -> "Concept Breakdown"

Idempotent: posts already in concept-breakdown are skipped.
Run from repo root:  python3 _migration/concept_breakdown.py
"""
import json, pathlib, re

import yaml

POSTS = pathlib.Path(__file__).resolve().parent.parent / "content" / "posts"
SLUG_FIXES = {"data-lekage": "data-leakage"}


def norm(s):
    return re.sub(r"\W+", " ", s).strip().lower()


def teaser(desc, summary):
    """One-line list teaser: the description if short, else its first sentence."""
    text = (desc or summary).strip()
    if len(text) <= 200:
        return text
    first = re.split(r"(?<=[.!?])\s+", text)[0]
    return first if len(first) <= 220 else text[:200].rsplit(" ", 1)[0] + "…"


def rename_series(s):
    return (s.replace("'ML Made Easy' series", "Concept Breakdown series")
             .replace("ML Made Easy", "Concept Breakdown"))


def main():
    changed = []
    for path in sorted(POSTS.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?\n)---\n(.*)$", raw, re.DOTALL)
        fm_text, body = m.group(1), m.group(2)
        fm = yaml.safe_load(fm_text)
        if fm.get("categories") != ["ml-made-easy"]:
            continue

        old_url = fm["url"]
        slug = old_url.strip("/").split("/")[-1]
        new_url = f"/concept-breakdown/{SLUG_FIXES.get(slug, slug)}/"

        summary = re.sub(r"^n\n", "", fm.get("summary", "")).strip()   # stray "n" in statistics-in-ml
        summary = rename_series(summary)
        desc = rename_series(fm.get("description", "").strip())

        first_img = re.search(r"!\[[^\]]*\]\(([^)\s]+)\)", body)

        # Copy the summary write-up into the body when it isn't there already.
        if summary and norm(summary)[:80] not in norm(body):
            paras = "\n\n".join(p.strip() for p in summary.split("\n") if p.strip())
            imgs = re.findall(r"^!\[.*$", body, re.MULTILINE)
            last_img = imgs[-1] if imgs else None
            if last_img:
                i = body.index(last_img) + len(last_img)
                body = body[:i] + "\n\n" + paras + "\n" + body[i:]
            else:
                body = paras + "\n\n" + body
        body = rename_series(body)
        body = re.sub(r"\n{3,}", "\n\n", body).rstrip() + "\n"

        # Rewrite front matter line-by-line, preserving order/formatting of untouched keys.
        out, skip = [], False
        for line in fm_text.splitlines():
            key = re.match(r"^([A-Za-z_]+)\s*:", line)
            if key:
                skip = False
                k = key.group(1)
                if k == "categories":
                    line = 'categories: ["concept-breakdown"]'
                elif k == "summary":
                    line, skip = "summary: " + json.dumps(teaser(desc, summary), ensure_ascii=False), True
                elif k == "description":
                    line, skip = "description: " + json.dumps(desc, ensure_ascii=False), True
                elif k == "url":
                    line = f"url: {new_url}"
            elif skip:
                continue            # continuation lines of a multi-line summary/description
            out.append(line)
        out.append(f"aliases: [{old_url}]")
        out.append(f"disqus_identifier: {old_url}")
        if first_img:
            out.append(f'images: ["{first_img.group(1)}"]')

        path.write_text("---\n" + "\n".join(out) + "\n---\n" + body, encoding="utf-8")
        changed.append((path.name, old_url, new_url))

    print(f"Moved {len(changed)} posts:")
    for name, old, new in changed:
        print(f"  {name:48} {old:52} -> {new}")


if __name__ == "__main__":
    main()
