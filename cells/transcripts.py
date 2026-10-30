"""Read interview transcripts into numbered turns.

Format (as exported by common video-call tools):

    # length: 41:20          (optional comment lines start with '#')
    Interviewer   0:03
    Text of the turn, one or more lines.

    Respondent   0:41
    ...

A speaker line is a name, two or more spaces, and a timestamp (m:ss or h:mm:ss).
"""
import re
from dataclasses import dataclass
from pathlib import Path

HEADER = re.compile(r"^(?P<speaker>[A-Za-z][\w .'-]*?)\s{2,}(?P<ts>\d{1,2}:\d{2}(?::\d{2})?)\s*$")


def to_seconds(ts):
    parts = [int(p) for p in ts.split(":")]
    secs = 0
    for p in parts:
        secs = secs * 60 + p
    return secs


def fmt_time(secs):
    h, rem = divmod(int(secs), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


@dataclass
class Turn:
    n: int
    speaker: str
    seconds: int
    text: str


@dataclass
class Transcript:
    name: str
    turns: list
    length: int  # seconds

    def text(self):
        return "\n".join(t.text for t in self.turns)

    def render(self, upto=None):
        """Numbered rendering used in prompts: [T12] Respondent (5:31): ..."""
        turns = self.turns if upto is None else [t for t in self.turns if t.n <= upto]
        return "\n".join(f"[T{t.n}] {t.speaker} ({fmt_time(t.seconds)}): {t.text}" for t in turns)


def parse(path):
    path = Path(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    turns, length, cur = [], None, None
    for line in lines:
        if line.startswith("#"):
            m = re.match(r"#\s*length:\s*([\d:]+)", line)
            if m:
                length = to_seconds(m.group(1))
            continue
        m = HEADER.match(line)
        if m:
            cur = Turn(len(turns) + 1, m.group("speaker").strip(), to_seconds(m.group("ts")), "")
            turns.append(cur)
        elif line.strip() and cur is not None:
            cur.text = (cur.text + " " + line.strip()).strip()
    if length is None:
        length = turns[-1].seconds if turns else 0
    return Transcript(path.stem, turns, length)


def load_dir(folder):
    return {t.name: t for t in (parse(p) for p in sorted(Path(folder).glob("*.txt")))}
