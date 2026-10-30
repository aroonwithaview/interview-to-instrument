"""Step 1: propose cells from all transcripts collected so far.

    python -m cells.propose --transcripts data/synthetic --out outputs/step1 [--backend manual]

Writes outputs/step1/cells.json and a quote check of the supporting passages. The
researchers then edit cells.json by hand (keep, merge or drop cells) and record what
they did in decisions.md before running step 2.
"""
import argparse
import json
from pathlib import Path

from . import llm, prompts, quotecheck
from .transcripts import load_dir

SCHEMA = {
    "type": "object",
    "properties": {
        "cells": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "label": {"type": "string"},
                    "definition": {"type": "string"},
                    "evidence": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "transcript": {"type": "string"},
                                "turn": {"type": "integer"},
                                "quote": {"type": "string"},
                                "prompted": {"type": "boolean"},
                            },
                            "required": ["transcript", "turn", "quote", "prompted"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["id", "label", "definition", "evidence"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["cells"],
    "additionalProperties": False,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/study.json")
    ap.add_argument("--transcripts", required=True)
    ap.add_argument("--out", required=True)
    llm.add_backend_args(ap)
    a = ap.parse_args()

    cfg = prompts.load_config(a.config)
    transcripts = load_dir(a.transcripts)
    block = "\n\n".join(f"=== Transcript {name} ===\n{t.render()}" for name, t in transcripts.items())
    prompt = prompts.render(
        "propose_cells.md",
        QUESTION=cfg["question"],
        INTERVIEWER=", ".join(cfg["interviewer"]),
        TRANSCRIPTS=block,
    )
    try:
        cells = llm.complete_json(prompt, SCHEMA, backend=a.backend, model=a.model, name="propose", run_dir=a.out)
    except llm.ManualResponsePending as e:
        raise SystemExit(str(e))

    out = Path(a.out)
    (out / "cells.json").write_text(json.dumps(cells, indent=2, ensure_ascii=False), encoding="utf-8")
    rows = quotecheck.check(cells, transcripts)
    (out / "quotecheck.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    ok = sum(r["verbatim"] for r in rows)
    print(f"{len(cells['cells'])} cells proposed; {ok} of {len(rows)} supporting quotes found verbatim")


if __name__ == "__main__":
    main()
