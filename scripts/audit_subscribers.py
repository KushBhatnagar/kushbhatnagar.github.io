#!/usr/bin/env python3
"""
Sort a Mailchimp audience export into keep / review / junk before the move to Kit.

    python3 scripts/audit_subscribers.py subscribed_export.csv [--out DIR]

Writes keep.csv, review.csv and junk.csv (email + reason + signup details) to DIR (default: a folder next
to the export) and prints only counts. Subscriber data never goes into this repo: run it on your machine
and keep the CSVs out of git. Standard library only.

Why these rules (from the 2026-10 audit of the real list):
- The Mailchimp forms were single opt-in with no captcha, so bots could add any address.
- Bots filled the name fields with the account ID from the form URL (u=c937565c...).
- From late 2024 a bot added about one address a day through the embedded form: each from a different
  country and IP, random-looking addresses, plus throwaway and "marketing agency" domains.
- Before that, signups were few and came from India, the US and Canada with name-like addresses.
A real-looking Gmail address isn't proof of a real subscriber: list-bombing bots often use other people's
real addresses, so review the keep list by eye before uploading it to Kit (docs/NEWSLETTER.md).
"""
import argparse, csv, os, sys

MAILCHIMP_USER_ID = "c937565c"           # from the form URL; bots copy it into the name fields
BOT_WAVE_START = "2024-09-01"            # first bot signup seen in the audit
HOME_COUNTRIES = {"IN"}                  # where real signups during the bot wave are plausible
FREE_PROVIDERS = {"gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.in", "hotmail.com", "outlook.com",
                  "live.com", "icloud.com", "me.com", "protonmail.com", "proton.me", "rediffmail.com"}
TRUSTED_DOMAINS = {"hp.com", "nexturn.com"}   # company domains of people you know; add more if needed


def classify(row):
    email = row["Email Address"].strip().lower()
    domain = email.rsplit("@", 1)[-1]
    names = (row.get("First Name", "") + row.get("Last Name", "")).lower()
    signup = row.get("OPTIN_TIME", "")[:10]
    country = row.get("CC", "").upper()
    source = row.get("SOURCE", "")

    if MAILCHIMP_USER_ID in names:
        return "junk", "bot: name fields contain the Mailchimp account ID"
    if domain not in FREE_PROVIDERS and domain not in TRUSTED_DOMAINS:
        return "junk", f"throwaway or marketing domain ({domain})"
    if signup < BOT_WAVE_START:
        return "keep", "signed up before the bot wave"
    if country in HOME_COUNTRIES or source == "Popup Form":
        return "review", "during the bot wave, but from India or via the pop-up form"
    return "junk", "bot wave: embedded form, random address/country pattern"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export")
    ap.add_argument("--out")
    args = ap.parse_args()
    out = args.out or os.path.splitext(args.export)[0] + "_audit"
    os.makedirs(out, exist_ok=True)

    with open(args.export, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    buckets = {"keep": [], "review": [], "junk": []}
    for row in rows:
        bucket, reason = classify(row)
        buckets[bucket].append([row["Email Address"].strip(), reason, row.get("OPTIN_TIME", "")[:10],
                                row.get("CC", ""), row.get("SOURCE", "")])

    for name, items in buckets.items():
        with open(os.path.join(out, f"{name}.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["email", "reason", "signed_up", "country", "source"])
            w.writerows(sorted(items, key=lambda r: r[2]))
    print(f"{len(rows)} subscribers -> keep {len(buckets['keep'])}, review {len(buckets['review'])}, "
          f"junk {len(buckets['junk'])}  (files in {out})")


if __name__ == "__main__":
    sys.exit(main())
