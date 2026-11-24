#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single robot wedding vow line to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).

Standard library only, no network. The vow is validated before it is
written: exactly one line, 1-160 characters, no trailing newline.
The file is written with mode 0644 and read back to verify it.
"""

import os
from pathlib import Path

VOW = "I vow to love you and never autocorrect you, not even when you're wrong."

# The joke: a wedding vow that is also a robot's promise. "Never autocorrect
# you" is the machine version of accepting a partner as they are, and the
# payoff lands in the last four words: not even when you're wrong.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    text = VOW

    # Validate before writing anything.
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be exactly one line")
    if not 1 <= len(text) <= 160:
        raise ValueError("vow must be 1-160 characters")

    path = out_dir / "entry.txt"
    path.write_text(text, encoding="utf-8")
    os.chmod(path, 0o644)

    # Verify by reading the file back.
    back = path.read_text(encoding="utf-8")
    if back != text:
        raise ValueError("verification failed: read-back mismatch")
    if back.endswith("\n"):
        raise ValueError("verification failed: trailing newline present")
    if len(back) != len(text):
        raise ValueError("verification failed: length mismatch")


if __name__ == "__main__":
    main()
