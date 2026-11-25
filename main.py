#!/usr/bin/env python3
"""One Line, No Deadline Met - make.fun entry.

Writes a single-line joke excusing a missed deadline to /output/entry.txt.
Python standard library only; no network, no randomness, deterministic.

The entry text is validated against the competition gate (1-200 chars,
single line, ASCII, not only white space) before anything is written, so
a bad entry fails loudly here instead of silently producing an invalid
file for the sealed scorer.
"""

import os

ENTRY = "I finished it on time in a parallel timeline, but that version of me refuses to share the file."

# The gate (see RULES.txt): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space. A single line, ASCII only,
# keeps the entry safely inside that gate.
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_entry(text):
    """Check the entry against the competition gate before writing it.

    Raises ValueError with a human-readable reason when the text would
    be rejected by the sealed scorer.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not all(ord(ch) < 128 for ch in text):
        raise ValueError("entry must be ASCII only")
    return text


def main():
    # Validate first: no file is created or touched when the entry
    # would fail the gate.
    entry = validate_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    return path


if __name__ == "__main__":
    main()
