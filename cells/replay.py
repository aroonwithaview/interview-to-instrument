"""Step 2 prototype: replay a finished interview as if it were live.

At each checkpoint (every few minutes of the recording) the assistant decides which
cells the conversation has covered so far, and flags the cells that are still empty.
The output shows when each cell first came up and what the interviewer would have
been prompted with at each checkpoint.

Two modes:
  --from-fills FILE   no model calls; a cell counts as covered from the turn of the
                      passage that fills it in a coding pass (cells.fill output)
  --backend ...       calls prompts/coverage.md on the transcript up to each checkpoint,
                      which is what a live assistant would do

    python -m cells.replay --cells outputs/step1/cells.json --transcripts data/synthetic \
        --from-fills outputs/fill_A/fills_A.json --out outputs/replay
"""
import argparse
import json
from pathlib import Path

from . import llm, prompts
from .transcripts import fmt_time, load_dir

SCHEMA = {
    "type": "object",
    "properties": {
        "covered": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"id": {"type": "string"}, "turn": {"type": "integer"}, "quote": {"type": "string"}},
                "required": ["id", "turn", "quote"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["covered"],
    "additionalProperties": False,
}


def checkpoints(t, minutes):
    """Last turn number before each checkpoint time, plus the end of the call."""
    step, marks, cut = minutes * 60, [], minutes * 60
    while cut < t.length:
        before = [x.n for x in t.turns if x.seconds <= cut]
        if before:
            marks.append((cut, before[-1]))
        cut += step
    marks.append((t.length, t.turns[-1].n))
    return marks


def first_turns_from_fills(fills, name):
    for f in fills["fills"]:
        if f["transcript"] == name:
            return {c["id"]: c["turn"] for c in f["cells"] if c["value"] != "not_raised" and c["turn"] > 0}
    return {}


def replay(t, cell_ids, marks, covered_at):
    """covered_at(cut, upto) -> {cell id: first turn}; returns timeline rows."""
    seen, rows = {}, []
    for cut, upto in marks:
        for cid, turn in covered_at(cut, upto).items():
            if turn <= upto:
                seen.setdefault(cid, turn)
        empty = [c for c in cell_ids if c not in seen]
        rows.append({"time": fmt_time(cut), "upto_turn": upto, "share_of_call": round(cut / t.length, 2),
                     "still_empty": empty})
    return seen, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/study.json")
    ap.add_argument("--cells", required=True)
    ap.add_argument("--transcripts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--from-fills", default=None)
    ap.add_argument("--minutes", type=float, default=None, help="checkpoint spacing; default from config")
    llm.add_backend_args(ap)
    a = ap.parse_args()

    cfg = prompts.load_config(a.config)
    minutes = a.minutes or cfg.get("checkpoint_minutes", 5)
    cells = json.load(open(a.cells, encoding="utf-8"))
    cell_ids = [c["id"] for c in cells["cells"]]
    transcripts = load_dir(a.transcripts)
    fills = json.load(open(a.from_fills, encoding="utf-8")) if a.from_fills else None
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    lines = ["# Replay of the step-2 assistant", "",
             f"Checkpoints every {minutes:g} minutes. At each checkpoint the assistant lists the cells still empty.", ""]
    result = {}
    for name, t in transcripts.items():
        if fills is not None:
            first = first_turns_from_fills(fills, name)
            covered_at = lambda cut, upto, first=first: first
        else:
            def covered_at(cut, upto, t=t, name=name):
                prompt = prompts.render("coverage.md", QUESTION=cfg["question"], CELLS=prompts.cells_block(cells),
                                        TRANSCRIPT=t.render(upto=upto))
                reply = llm.complete_json(prompt, SCHEMA, backend=a.backend, model=a.model,
                                          name=f"coverage_{name}_T{upto}", run_dir=out)
                return {c["id"]: c["turn"] for c in reply["covered"]}
        seen, rows = replay(t, cell_ids, checkpoints(t, minutes), covered_at)
        result[name] = {"first_turn": seen, "timeline": rows}
        turn_time = {x.n: x.seconds for x in t.turns}
        lines += [f"## {name} (recorded length {fmt_time(t.length)})", "", "| Cell | First came up | Share of call |", "|---|---|---|"]
        for c in cell_ids:
            if c in seen:
                s = turn_time[seen[c]]
                lines.append(f"| {c} | {fmt_time(s)} (turn {seen[c]}) | {s / t.length:.0%} |")
            else:
                lines.append(f"| {c} | never | |")
        lines += ["", "| Checkpoint | Cells the assistant would flag as still empty |", "|---|---|"]
        lines += [f"| {r['time']} | {', '.join(r['still_empty']) or 'none'} |" for r in rows]
        lines.append("")
    (out / "replay.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (out / "replay.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"replayed {len(transcripts)} transcripts; see {out / 'replay.md'}")


if __name__ == "__main__":
    main()
