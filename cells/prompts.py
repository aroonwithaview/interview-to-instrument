"""Load prompt templates from prompts/ and fill their {{PLACEHOLDERS}}."""
import json
from pathlib import Path

PROMPTS = Path(__file__).resolve().parent.parent / "prompts"


def render(name, **fields):
    text = (PROMPTS / name).read_text(encoding="utf-8")
    for key, value in fields.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def cells_block(cells):
    return "\n".join(f"- {c['id']}: {c['label']}. {c['definition']}" for c in cells["cells"])


def load_config(path):
    return json.load(open(path, encoding="utf-8"))
