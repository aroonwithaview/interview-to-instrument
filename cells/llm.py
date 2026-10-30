"""One call to a language model that returns JSON.

Backends:
  anthropic  Claude through the Anthropic SDK (credentials from ANTHROPIC_API_KEY
             or an `ant auth login` profile). Default model: claude-opus-5-5.
  openai     Any OpenAI-compatible endpoint, e.g. a local vLLM or llama.cpp server
             running an open-weight model (OPENAI_BASE_URL, OPENAI_API_KEY, --model).
  manual     Writes the prompt to <run_dir>/<name>.prompt.md and reads the reply from
             <run_dir>/<name>.response.json, so any chat interface can be used.

Every prompt and reply is saved in run_dir, which keeps a record of each call.
"""
import json
import os
from pathlib import Path

DEFAULT_MODEL = "claude-opus-5-5"


class ManualResponsePending(Exception):
    pass


def _strip_fences(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]
    return text


def _anthropic(prompt, schema, model):
    import anthropic

    client = anthropic.Anthropic()
    kwargs = dict(
        model=model,
        max_tokens=16000,
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    )
    if os.environ.get("CELLS_NO_FALLBACK"):
        response = client.messages.create(**kwargs)
    else:
        # On a policy decline, the API re-runs the request on the fallback model.
        response = client.beta.messages.create(
            betas=["server-side-fallback-2026-06-01"],
            fallbacks=[{"model": "claude-opus-4-8"}],
            **kwargs,
        )
    if response.stop_reason == "refusal":
        raise RuntimeError(f"model declined the request: {response.stop_details}")
    if response.stop_reason == "max_tokens":
        raise RuntimeError("reply hit max_tokens; shorten the input or raise the limit")
    return next(b.text for b in response.content if b.type == "text")


def _openai(prompt, model):
    from openai import OpenAI

    if not model:
        raise SystemExit("--model is required with the openai backend")
    client = OpenAI()
    reply = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt + "\n\nReturn only the JSON object."}],
        response_format={"type": "json_object"},
    )
    return reply.choices[0].message.content


def complete_json(prompt, schema, *, backend, name, run_dir, model=None):
    run_dir = Path(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / f"{name}.prompt.md").write_text(prompt, encoding="utf-8")
    reply_path = run_dir / f"{name}.response.json"
    if backend == "manual":
        if not reply_path.exists():
            raise ManualResponsePending(
                f"Paste {run_dir / (name + '.prompt.md')} into a model and save its JSON reply as {reply_path}"
            )
        return json.loads(_strip_fences(reply_path.read_text(encoding="utf-8")))
    if backend == "anthropic":
        text = _anthropic(prompt, schema, model or DEFAULT_MODEL)
    elif backend == "openai":
        text = _openai(prompt, model)
    else:
        raise SystemExit(f"unknown backend: {backend}")
    data = json.loads(_strip_fences(text))
    reply_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return data


def add_backend_args(parser):
    parser.add_argument("--backend", choices=["anthropic", "openai", "manual"], default="anthropic")
    parser.add_argument("--model", default=None, help=f"default for anthropic: {DEFAULT_MODEL}")
