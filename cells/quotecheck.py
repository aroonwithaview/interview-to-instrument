"""Check that every quote a model returns appears verbatim in the transcript it cites.

Comparison ignores case, curly versus straight quotes, and runs of whitespace.

    python -m cells.quotecheck --transcripts data/synthetic --file outputs/step1/cells.json
"""
import argparse
import json
import re

from .transcripts import load_dir


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("…", "...")
    return re.sub(r"\s+", " ", s).strip().lower()


def found(quote, transcript):
    """True if the quote (possibly with '...' gaps) appears in order in the transcript."""
    text = norm(transcript.text())
    pos = 0
    for piece in [p.strip() for p in norm(quote).split("...") if p.strip()]:
        i = text.find(piece, pos)
        if i < 0:
            return False
        pos = i + len(piece)
    return True


def quotes_in(data):
    """Yield (transcript, cell id, quote) from a cells file or a fills file."""
    if "cells" in data and data["cells"] and "evidence" in data["cells"][0]:
        for c in data["cells"]:
            for e in c["evidence"]:
                yield e["transcript"], c["id"], e["quote"]
    else:
        for f in data["fills"]:
            for c in f["cells"]:
                if c["quote"]:
                    yield f["transcript"], c["id"], c["quote"]


def check(data, transcripts):
    rows = []
    for name, cell, quote in quotes_in(data):
        ok = name in transcripts and found(quote, transcripts[name])
        rows.append({"transcript": name, "cell": cell, "quote": quote, "verbatim": ok})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcripts", required=True)
    ap.add_argument("--file", required=True)
    a = ap.parse_args()
    rows = check(json.load(open(a.file, encoding="utf-8")), load_dir(a.transcripts))
    bad = [r for r in rows if not r["verbatim"]]
    print(f"{len(rows) - len(bad)} of {len(rows)} quotes found verbatim")
    for r in bad:
        print(f"  NOT FOUND  {r['transcript']} / {r['cell']}: {r['quote'][:80]}")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
