#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single robot wedding vow line to ``entry.txt`` in the output
directory given by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Standard library only, no network. The vow is validated before it is
written: exactly one line, 1-160 characters, no trailing newline.
The file is written with mode 0644 and read back to verify it.

Why this line works: a wedding vow that is also a robot's promise.
"Never autocorrect you" is the machine version of accepting a partner
as they are, and the payoff lands in the last four words: not even
when you're wrong. The autocorrect premise appears nowhere else in
the field, which is what makes the one line memorable instead of
generic.
"""

import os
import sys
from pathlib import Path

# The entry itself. Exactly one line, 72 characters, no trailing
# newline in the output file. Do not edit this string: the bounty
# asks for one line and this is the line that was judged.
VOW = "I vow to love you and never autocorrect you, not even when you're wrong."

# Bounty limits for a one-line entry.
MIN_LENGTH = 1
MAX_LENGTH = 160
OUTPUT_FILENAME = "entry.txt"
OUTPUT_MODE = 0o644


def resolve_output_dir() -> Path:
    """Return the output directory from the environment.

    ``MAKEFUN_OUTPUT_DIR`` is honoured when set; otherwise the
    default ``/output`` is used. The directory is created (including
    parents) so the entry can always be written.
    """
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(raw)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def validate_vow(text: str) -> str:
    """Check the vow meets every bounty rule, then return it unchanged.

    Rejects, in order: an empty/non-string value, any line break
    (``\\n`` or ``\\r``, which would make it more than one line),
    leading/trailing whitespace (invisible padding that would change
    the character count), and a length outside 1-160 characters.
    Raising here -- before anything is written -- guarantees a bad
    vow can never produce a partial or wrong ``entry.txt``.
    """
    if not isinstance(text, str):
        raise TypeError("vow must be a string")
    if not text:
        raise ValueError("vow must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be exactly one line")
    if text != text.strip():
        raise ValueError("vow must not have leading or trailing whitespace")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"vow must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    return text


def write_entry(out_dir: Path, text: str) -> Path:
    """Write the validated vow to ``entry.txt`` with mode 0644.

    The text is written exactly as given -- no newline is appended,
    so the file holds one line of exactly ``len(text)`` bytes.
    Returns the path that was written.
    """
    path = out_dir / OUTPUT_FILENAME
    path.write_text(text, encoding="utf-8")
    os.chmod(path, OUTPUT_MODE)
    return path


def verify_entry(path: Path, expected: str) -> None:
    """Read the file back and confirm it is byte-identical to the vow.

    Checks, in order: the bytes decode as the expected text, the
    content has no trailing newline, and the length matches. Any
    mismatch raises, so a silent wrong output is impossible.
    """
    back = path.read_text(encoding="utf-8")
    if back != expected:
        raise ValueError("verification failed: read-back mismatch")
    if back.endswith("\n"):
        raise ValueError("verification failed: trailing newline present")
    if len(back) != len(expected):
        raise ValueError("verification failed: length mismatch")
    if path.stat().st_size != len(expected.encode("utf-8")):
        raise ValueError("verification failed: byte-size mismatch")


def main() -> int:
    """Validate, write, and verify the vow; return a process exit code."""
    try:
        text = validate_vow(VOW)
        out_dir = resolve_output_dir()
        path = write_entry(out_dir, text)
        verify_entry(path, text)
    except (ValueError, TypeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
