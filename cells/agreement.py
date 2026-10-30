"""Compare two coding passes cell by cell and list the disagreements.

    python -m cells.agreement --a outputs/fill_A/fills_A.json --b outputs/fill_B/fills_B.json \
        --out outputs/agreement.md
"""
import argparse
import json
from collections import Counter


def index(fills):
    return {(f["transcript"], c["id"]): c for f in fills["fills"] for c in f["cells"]}


def compare(a, b):
    ia, ib = index(a), index(b)
    keys = sorted(set(ia) | set(ib))
    rows = []
    for k in keys:
        va = ia.get(k, {}).get("value", "missing")
        vb = ib.get(k, {}).get("value", "missing")
        rows.append({"transcript": k[0], "cell": k[1], "a": va, "b": vb, "agree": va == vb})
    return rows


def report(rows, label_a, label_b):
    n, agree = len(rows), sum(r["agree"] for r in rows)
    pairs = Counter((r["a"], r["b"]) for r in rows if not r["agree"])
    lines = [f"# Agreement between pass {label_a} and pass {label_b}", "",
             f"The two passes agree on {agree} of {n} transcript-cell pairs.", ""]
    if pairs:
        lines += ["| Pass " + label_a + " | Pass " + label_b + " | Count |", "|---|---|---|"]
        lines += [f"| {x} | {y} | {c} |" for (x, y), c in pairs.most_common()]
        lines += ["", "Disagreements, for a researcher to resolve against the transcript:", "",
                  "| Transcript | Cell | Pass " + label_a + " | Pass " + label_b + " |", "|---|---|---|---|"]
        lines += [f"| {r['transcript']} | {r['cell']} | {r['a']} | {r['b']} |" for r in rows if not r["agree"]]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    a = json.load(open(args.a, encoding="utf-8"))
    b = json.load(open(args.b, encoding="utf-8"))
    text = report(compare(a, b), a.get("label", "A"), b.get("label", "B"))
    open(args.out, "w", encoding="utf-8").write(text)
    print(text.splitlines()[2])


if __name__ == "__main__":
    main()
