"""Apply the researchers' keep / merge / drop decisions to the proposed cells.

    python -m cells.curate --cells outputs/demo/step1/cells.json \
        --decisions outputs/demo/step1/decisions.json --out outputs/demo/step1/cells_kept.json

decisions.json:
    {"keep": [id, ...],
     "merge": [{"into": {"id": ..., "label": ..., "definition": ...}, "from": [id, ...]}],
     "drop": [id, ...],
     "notes": {id: "reason", ...}}

Every proposed cell must appear exactly once across keep, merge and drop, so no
proposal is lost without a recorded decision. A decision log is written next to --out.
"""
import argparse
import json
from pathlib import Path


def curate(cells, d):
    by_id = {c["id"]: c for c in cells["cells"]}
    named = list(d.get("keep", [])) + [i for m in d.get("merge", []) for i in m["from"]] + list(d.get("drop", []))
    missing = sorted(set(by_id) - set(named))
    unknown = sorted(set(named) - set(by_id))
    repeated = sorted({i for i in named if named.count(i) > 1})
    if missing or unknown or repeated:
        raise SystemExit(f"decisions do not cover the proposals exactly once: "
                         f"missing={missing} unknown={unknown} repeated={repeated}")
    kept = [by_id[i] for i in d.get("keep", [])]
    for m in d.get("merge", []):
        cell = dict(m["into"])
        cell["evidence"] = [e for i in m["from"] for e in by_id[i]["evidence"]]
        cell["merged_from"] = m["from"]
        kept.append(cell)
    return {"cells": kept}


def log(cells, d, kept):
    notes = d.get("notes", {})
    lines = ["# Decisions on the proposed cells", "",
             f"{len(cells['cells'])} cells proposed; {len(kept['cells'])} kept after merging.", "",
             "| Proposed cell | Decision | Note |", "|---|---|---|"]
    for c in cells["cells"]:
        i = c["id"]
        if i in d.get("keep", []):
            dec = "keep"
        elif i in d.get("drop", []):
            dec = "drop"
        else:
            dec = "merge into " + next(m["into"]["id"] for m in d["merge"] if i in m["from"])
        lines.append(f"| {i} | {dec} | {notes.get(i, '')} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cells", required=True)
    ap.add_argument("--decisions", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    cells = json.load(open(a.cells, encoding="utf-8"))
    d = json.load(open(a.decisions, encoding="utf-8"))
    kept = curate(cells, d)
    out = Path(a.out)
    out.write_text(json.dumps(kept, indent=2, ensure_ascii=False), encoding="utf-8")
    (out.parent / "decisions.md").write_text(log(cells, d, kept), encoding="utf-8")
    print(f"{len(kept['cells'])} cells kept; log in {out.parent / 'decisions.md'}")


if __name__ == "__main__":
    main()
