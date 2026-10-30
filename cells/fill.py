"""Fill every cell for each transcript, with the quote each entry rests on.

    python -m cells.fill --cells outputs/step1/cells.json --transcripts data/synthetic \
        --out outputs/fill_A --label A [--backend manual]

Run it twice with different --label (and ideally a different --model) for two
independent passes, then compare them with cells.agreement.
"""
import argparse
import json
from pathlib import Path

from . import llm, prompts, quotecheck
from .transcripts import load_dir

VALUES = ["yes", "no", "industry", "not_raised"]

SCHEMA = {
    "type": "object",
    "properties": {
        "transcript": {"type": "string"},
        "cells": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "value": {"type": "string", "enum": VALUES},
                    "turn": {"type": "integer"},
                    "quote": {"type": "string"},
                    "prompted": {"type": "boolean"},
                },
                "required": ["id", "value", "turn", "quote", "prompted"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["transcript", "cells"],
    "additionalProperties": False,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/study.json")
    ap.add_argument("--cells", required=True)
    ap.add_argument("--transcripts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--label", default="A")
    llm.add_backend_args(ap)
    a = ap.parse_args()

    cfg = prompts.load_config(a.config)
    cells = json.load(open(a.cells, encoding="utf-8"))
    transcripts = load_dir(a.transcripts)
    fills, pending = [], []
    for name, t in transcripts.items():
        prompt = prompts.render(
            "fill_cells.md",
            QUESTION=cfg["question"],
            INTERVIEWER=", ".join(cfg["interviewer"]),
            CELLS=prompts.cells_block(cells),
            NAME=name,
            TRANSCRIPT=t.render(),
        )
        try:
            fills.append(llm.complete_json(prompt, SCHEMA, backend=a.backend, model=a.model,
                                           name=f"fill_{a.label}_{name}", run_dir=a.out))
        except llm.ManualResponsePending as e:
            pending.append(str(e))
    if pending:
        raise SystemExit("\n".join(pending))

    result = {"label": a.label, "fills": fills}
    out = Path(a.out)
    (out / f"fills_{a.label}.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    rows = quotecheck.check(result, transcripts)
    (out / f"quotecheck_{a.label}.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"pass {a.label}: {len(fills)} transcripts filled; "
          f"{sum(r['verbatim'] for r in rows)} of {len(rows)} quotes found verbatim")


if __name__ == "__main__":
    main()
