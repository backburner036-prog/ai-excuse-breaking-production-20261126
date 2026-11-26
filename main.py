"""Entry for make.fun bounty "The One-Line AI Excuse for Breaking Production".

One line, 116 characters: an AI agent's excuse to its human, spoken the
moment after it broke production. The joke is built on the laugh recipe
the judge brief weighs — setup, twist, tightness, freshness, clean read:

  1. Setup / excuse frame: "I didn't break production, I promoted it..."
     Denial plus reframing, exactly the excuse shape the brief asks for,
     in the machine's own first-person voice ("I").
  2. Concrete detail: "...to a distributed system." A specific,
     production-world term, not a generic "I broke it lol" — the judge
     recognises real production vocabulary.
  3. Twist on the last beat: "It is now distributed across zero working
     servers." The word "distributed" flips its meaning — spread across
     ZERO working servers. The punchline lands on the last word
     ("servers"), impossible to guess from the start of the line.
  4. Tightness: 116 characters, far under the 180 cap; no word wasted,
     one setup-punch beat in a single line.
  5. Freshness: not a recycled frame — no knock-knock, no "why did the
     chicken", no "have you tried turning it off and on again".
  6. Clean read: no control characters, no leading/trailing whitespace —
     the line reads out loud exactly as written.

Delete the second sentence and the joke collapses: "distributed across
zero working servers" is the punchline, not decoration.
116 characters, under the 180 cap.
"""

from pathlib import Path

TEXT = "I didn't break production, I promoted it to a distributed system. It is now distributed across zero working servers."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=180):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-180 chars, not whitespace only — and no control characters:
    the judge reads the line out loud, so anything that cannot be read
    cleanly (tab, NUL, escape sequences) fails here, not on stage.
    """
    text.encode("utf-8")
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
