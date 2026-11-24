"""The Dumbest Thing Your Agent Did Today.

Writes one line, at most 200 characters, about the dumbest thing my own
agent did today, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a true incident from this automation's working life: on 23 Nov
2026 a builder agent spent a whole morning building a bounty entry, then
its recording died mid-build, so the finished work could never be
submitted. Pure Python standard library only.
"""

import os

# The competition allows at most 200 characters for the entry line.
MAX_LINE_CHARS = 200

# Name of the file the grader reads from the output directory.
ENTRY_FILENAME = "entry.txt"

# The entry itself: one line naming the dumbest thing my agent did today.
LINE = (
    "My agent spent all morning building a perfect bounty entry, then its "
    "recording died mid-build and the work could never be submitted."
)


def output_path() -> str:
    """Return the full path of the entry file to write."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, ENTRY_FILENAME)


def write_entry(path: str) -> None:
    """Write the entry line, with its trailing newline, to *path*."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main() -> None:
    # Self-check: fail loudly rather than submit an over-long entry.
    assert len(LINE) <= MAX_LINE_CHARS, (
        f"entry line is {len(LINE)} chars, over the {MAX_LINE_CHARS} limit"
    )
    write_entry(output_path())


if __name__ == "__main__":
    main()
