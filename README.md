# interview-to-instrument

Prototype for a two-step process that turns interviews with business leaders into survey-like data.

1. **Learning the cells.** Researchers hold open-ended interviews. After each one, a language model reads all the transcripts collected so far and proposes the categories of responses, with the passages behind each one and whether the respondent raised it unprompted. The researchers keep, merge or drop the proposals. These categories become the cells of the instrument.
2. **Filling the cells.** In later interviews, run by RAs, an assistant follows the transcript and shows the interviewer which cells are still empty. After the call, the model fills every cell with the passage it rests on. A script checks each quote against the transcript, and a second independent coding pass flags disagreements for a researcher.

The output is a table with one row per respondent and one column per cell.

This repository contains no real interview. `data/synthetic/` holds three synthetic transcripts written to resemble the pilot calls (see its README).

## Layout

| Path | What it does |
|---|---|
| `prompts/propose_cells.md` | Step 1 prompt: propose cells from all transcripts so far |
| `prompts/fill_cells.md` | Fill every cell for one transcript, with a quote for each entry |
| `prompts/coverage.md` | Step 2 prompt: which cells a conversation has covered so far |
| `cells/propose.py` | Runs step 1; writes `cells.json` and a quote check |
| `cells/fill.py` | Fills cells for each transcript; run twice (`--label A`, `--label B`) for two passes |
| `cells/quotecheck.py` | Checks that each quote appears verbatim in the transcript it cites |
| `cells/agreement.py` | Compares two coding passes and lists disagreements |
| `cells/replay.py` | Step 2 prototype: replays a transcript checkpoint by checkpoint and records which cells the assistant would flag as still empty |
| `cells/curate.py` | Applies the researchers' keep / merge / drop decisions and logs each one |
| `cells/llm.py` | One JSON-returning model call; three backends (below) |
| `config/study.json` | Research question, interviewer's speaker name, checkpoint spacing |
| `tests/` | Offline tests (no model calls) |
| `outputs/demo/` | A full run on the synthetic transcripts (see below) |

## Backends

Every prompt and every reply is saved next to the outputs, so each run leaves a record of what the model was asked and what it said.

- `--backend anthropic` (default): Claude through the Anthropic SDK, model `claude-opus-5-5` unless `--model` is given. Credentials come from `ANTHROPIC_API_KEY` or an `ant auth login` profile. Requests use structured outputs, so replies are valid JSON, and opt into the API's server-side refusal fallback (set `CELLS_NO_FALLBACK=1` to turn it off).
- `--backend openai --model NAME`: any OpenAI-compatible endpoint (`OPENAI_BASE_URL`, `OPENAI_API_KEY`), for instance a local vLLM or llama.cpp server running an open-weight model.
- `--backend manual`: writes each prompt to `<out>/<name>.prompt.md` and stops; paste it into any chat model, save the JSON reply as `<out>/<name>.response.json`, and run the same command again.

## Running it

```
pip install -r requirements.txt          # only for the anthropic or openai backend
python -m unittest discover tests

# step 1
python -m cells.propose --transcripts data/synthetic --out outputs/run/step1
#   decide which cells to keep, merge or drop in decisions.json (format in cells/curate.py), then
python -m cells.curate --cells outputs/run/step1/cells.json --decisions outputs/run/step1/decisions.json --out outputs/run/step1/cells_kept.json

# fill the cells, twice (ideally with two different models)
python -m cells.fill --cells outputs/run/step1/cells_kept.json --transcripts data/synthetic --out outputs/run/fill_A --label A
python -m cells.fill --cells outputs/run/step1/cells_kept.json --transcripts data/synthetic --out outputs/run/fill_B --label B --model claude-sonnet-5-5
python -m cells.agreement --a outputs/run/fill_A/fills_A.json --b outputs/run/fill_B/fills_B.json --out outputs/run/agreement.md

# step 2 replay: offline from a coding pass, or with live model calls at each checkpoint
python -m cells.replay --cells outputs/run/step1/cells_kept.json --transcripts data/synthetic --from-fills outputs/run/fill_A/fills_A.json --out outputs/run/replay
python -m cells.replay --cells outputs/run/step1/cells_kept.json --transcripts data/synthetic --out outputs/run/replay_live
```

## The demonstration run

`outputs/demo/` is a complete run on the three synthetic transcripts, using the manual backend. Each prompt was given, with nothing else, to a fresh Claude session (Opus 5.5 for step 1 and coding pass A, Sonnet 5.5 for pass B, so that the two passes come from different models), and each reply was saved unedited. The scripts did everything else.

| Stage | Files | Result |
|---|---|---|
| Step 1: propose cells | `step1/propose.prompt.md`, `step1/propose.response.json`, `step1/cells.json` | 28 cells proposed; 54 of 54 supporting quotes found verbatim (`step1/quotecheck.json`) |
| Keep, merge or drop | `step1/decisions.json`, `step1/decisions.md`, `step1/cells_kept.json` | 12 cells kept. These decisions were made only to show the format; they are not a substantive choice of cells. |
| Fill the cells, two passes | `fill_A/`, `fill_B/` | All quotes found verbatim (24 of 24 in pass A, 26 of 26 in pass B) |
| Agreement | `agreement.md` | 34 of 36 transcript-cell pairs agree; both disagreements are "not raised" in pass A against "no" in pass B |
| Step 2 replay | `replay/replay.md` | In transcript W the AI cell first comes up 86% of the way through the call, so the assistant would have flagged it at every earlier checkpoint |

The pilot analysis described in the proposal was done in interactive sessions before this code was written; it is not reproduced here, because its transcripts cannot be shared.

## Data and ethics

The pilot interviews identify respondents and their firms, so their transcripts are not shared. `.gitignore` excludes `data/real/`. Future respondents will be asked to consent to the release of de-identified excerpts.
