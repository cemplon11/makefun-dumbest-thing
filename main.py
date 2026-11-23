"""The Dumbest Thing Your Agent Did Today.

Writes one line, at most 200 characters, about the dumbest thing my own
agent did today, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a true incident from this automation's working life: on 23 Nov
2026 a builder agent spent a whole morning building a bounty entry, then
its recording died mid-build, so the finished work could never be
submitted. Pure Python standard library only.
"""

import os

LINE = (
    "My agent spent all morning building a perfect bounty entry, then its "
    "recording died mid-build and the work could never be submitted."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
