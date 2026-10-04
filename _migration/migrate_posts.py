#!/usr/bin/env python3
"""
Jekyll -> Hugo post migration for blogsbykush.com.

For each _posts/*.md:
  - derive date + slug from filename
  - freeze the live URL (from sitemap) via explicit `url:` front matter
  - clean filename typos (data-lekage -> data-leakage) WITHOUT changing the URL
  - normalise front matter (layout/toc/seo_* -> Hugo equivalents)
  - strip Jekyll Liquid ({{ site.url }}{{ site.baseurl }}) keeping /assets/ paths
  - strip kramdown attr blocks ({: .notice--info}, {: .align-center}, ...)
  - fix visible typos (clasroom -> classroom, Lekage -> Leakage as whole words)

Run from repo root:  python3 _migration/migrate_posts.py
"""
import os, re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC = REPO / "_posts"
DST = REPO / "content" / "posts"

FNAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-\s*(.+?)\s*\.md$")

# Filename slug typo fixes (do NOT affect the frozen URL slug).
FILE_SLUG_FIXES = {"data-lekage": "data-leakage"}


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text


def split_front_matter(raw):
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", raw, re.DOTALL)
    if not m:
        raise ValueError("no front matter")
    return m.group(1), m.group(2)


def transform_front_matter(fm):
    out = []
    for line in fm.splitlines():
        s = line.rstrip("\n")
        if re.match(r"^layout\s*:", s):
            continue
        if re.match(r"^toc\s*:", s):
            continue
        if re.match(r"^seo_title\s*:", s):
            continue
        if re.match(r"^tag:", s):
            s = re.sub(r"^tag:", "tags:", s)
        if re.match(r"^seo_description\s*:", s):
            s = re.sub(r"^seo_description\s*:", "description:", s)
        if re.match(r"^excerpt\s*:", s):
            s = re.sub(r"^excerpt\s*:", "summary:", s)
        m = re.match(r"^categories:\s*(\S+)\s*$", s)
        if m:
            s = 'categories: ["%s"]' % m.group(1)
        # visible typo fixes inside front matter (tag values, titles)
        s = re.sub(r"\bclasroom\b", "classroom", s)
        s = re.sub(r"\bClasroom\b", "Classroom", s)
        s = re.sub(r"\bLekage\b", "Leakage", s)
        s = re.sub(r"\blekage\b", "leakage", s)
        out.append(s)
    return "\n".join(out).rstrip() + "\n"


def transform_body(body):
    # strip Jekyll liquid site vars, keeping the /assets/... path
    body = re.sub(r"\{\{\s*site\.[a-z_]+\s*\}\}", "", body)
    # strip kramdown attribute blocks
    body = re.sub(r"\{:\s*[^}]*\}", "", body)
    # visible typo fixes (whole word only -> never touches DataLekage.png)
    body = re.sub(r"\bclasroom\b", "classroom", body)
    body = re.sub(r"\bClasroom\b", "Classroom", body)
    body = re.sub(r"\bLekage\b", "Leakage", body)
    body = re.sub(r"\blekage\b", "leakage", body)
    return body


def main():
    DST.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(SRC.glob("*.md")):
        m = FNAME_RE.match(path.name)
        if not m:
            print("SKIP (no date match):", path.name)
            continue
        y, mo, d, raw_slug = m.groups()
        date = f"{y}-{mo}-{d}"
        url_slug = slugify(raw_slug)
        file_slug = FILE_SLUG_FIXES.get(url_slug, url_slug)

        raw = path.read_text(encoding="utf-8")
        fm, body = split_front_matter(raw)

        cat_m = re.search(r"^categories:\s*(\S+)\s*$", fm, re.MULTILINE)
        category = cat_m.group(1) if cat_m else None
        url = "/" + (category + "/" if category else "") + url_slug + "/"

        has_date = re.search(r"^date\s*:", fm, re.MULTILINE) is not None
        has_url = re.search(r"^url\s*:", fm, re.MULTILINE) is not None

        fm = transform_front_matter(fm)
        body = transform_body(body)

        fm = fm.rstrip()
        if not has_date:
            fm += f"\ndate: {date}"
        if not has_url:
            fm += f"\nurl: {url}"
        fm += "\n"
        out = "---\n" + fm + "---\n" + body
        (DST / f"{file_slug}.md").write_text(out, encoding="utf-8")
        rows.append((path.name, f"{file_slug}.md", url, category or "-"))

    print(f"\nMigrated {len(rows)} posts:\n")
    for src, dst, url, cat in rows:
        print(f"  [{cat:12}] {dst:60} -> {url}")


if __name__ == "__main__":
    main()
