#!/usr/bin/env python3
"""
Turn a comic PDF into a Concept Breakdown post with a LinkedIn-style carousel.

    python3 scripts/new_breakdown.py path/to/Comic.pdf --title "How LLMs Think"
    python3 scripts/new_breakdown.py Comic.pdf --title "..." --transcript convo.txt --date 2026-10-01

Creates the page bundle content/posts/<slug>/ containing:
    slide-01.webp … slide-NN.webp  one per PDF page, white print margins cropped, 1080px wide
    <slug>.pdf                     clean re-export of the slides (the "Download PDF" link)
    cover.jpg                      1200x630 social-preview image (first + last slide)
    transcript.txt                 copy of --transcript, if given (input for /breakdown-post)
    index.md                       front matter + carousel + collapsed transcript + plain-words section, draft: true

Then run the /breakdown-post skill in Claude Code to write the body, and set draft: false.
Requires: pip install pymupdf pillow
"""
import argparse, datetime, pathlib, re, shutil, sys

try:
    import pymupdf
    from PIL import Image, ImageChops
except ImportError:
    sys.exit("Missing dependencies: pip install pymupdf pillow")

REPO = pathlib.Path(__file__).resolve().parent.parent
POSTS = REPO / "content" / "posts"
SLIDE_WIDTH = 1080
RENDER_DPI = 220          # render high, then downscale: crisp lettering
CANVAS_GREY = (218, 218, 218)   # the comic's card background


def slugify(text):
    text = re.sub(r"[^a-z0-9\s-]", "", text.lower())
    return re.sub(r"[\s-]+", "-", text).strip("-")


def crop_margins(im, threshold=245):
    """Crop the white page border that 'Print to PDF' adds around the card."""
    grey = im.convert("L").point(lambda v: 255 if v > threshold else 0)
    bbox = ImageChops.invert(grey).getbbox()
    return im.crop(bbox) if bbox else im


def render_slides(pdf_path):
    doc = pymupdf.open(pdf_path)
    slides = []
    for page in doc:
        pix = page.get_pixmap(dpi=RENDER_DPI)
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        im = crop_margins(im)
        h = round(im.height * SLIDE_WIDTH / im.width)
        slides.append(im.resize((SLIDE_WIDTH, h), Image.LANCZOS))
    return slides


def make_cover(slides, out):
    """1200x630 link preview: first and last slide side by side."""
    W, H, pad = 1200, 630, 30
    canvas = Image.new("RGB", (W, H), CANVAS_GREY)
    picks = [slides[0], slides[-1]] if len(slides) > 1 else [slides[0]]
    th = H - 2 * pad
    thumbs = [s.resize((round(s.width * th / s.height), th), Image.LANCZOS) for s in picks]
    x = (W - sum(t.width for t in thumbs) - pad * (len(thumbs) - 1)) // 2
    for t in thumbs:
        canvas.paste(t, (x, pad))
        x += t.width + pad
    canvas.save(out, quality=85, optimize=True)


INDEX_TEMPLATE = """---
title: "{title}"
date: {date}
draft: true
categories: ["concept-breakdown"]
tags: []
summary: ""        # one-line teaser for list pages
description: ""    # ~150-char SEO meta description
url: /concept-breakdown/{slug}/
images: ["cover.jpg"]
ShowToc: false
slide_alt: []      # one alt text per slide, in order
---

{{{{< carousel >}}}}

{{{{< transcript >}}}}
{{{{< /transcript >}}}}

## The concept in plain words
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=pathlib.Path)
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug", help="URL slug (default: from title)")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--transcript", type=pathlib.Path, help="comic conversation as text")
    ap.add_argument("--force", action="store_true", help="overwrite slides of an existing bundle (keeps index.md)")
    args = ap.parse_args()

    slug = args.slug or slugify(args.title)
    bundle = POSTS / slug
    if bundle.exists() and not args.force:
        sys.exit(f"{bundle} already exists (use --force to regenerate slides)")
    bundle.mkdir(parents=True, exist_ok=True)
    for old in bundle.glob("slide-*.webp"):
        old.unlink()

    slides = render_slides(args.pdf)
    for i, im in enumerate(slides, 1):
        im.save(bundle / f"slide-{i:02d}.webp", quality=88, method=6)
    slides[0].save(bundle / f"{slug}.pdf", save_all=True, append_images=slides[1:],
                   resolution=150, quality=85)
    make_cover(slides, bundle / "cover.jpg")
    if args.transcript:
        shutil.copy(args.transcript, bundle / "transcript.txt")

    index = bundle / "index.md"
    if not index.exists():
        index.write_text(INDEX_TEMPLATE.format(title=args.title.replace('"', '\\"'),
                                               date=args.date, slug=slug), encoding="utf-8")

    print(f"Created {bundle.relative_to(REPO)}/ with {len(slides)} slides "
          f"({slides[0].width}x{slides[0].height}).")
    print(f"Next: in Claude Code run  /breakdown-post {bundle.relative_to(REPO)}  then set draft: false.")


if __name__ == "__main__":
    main()
