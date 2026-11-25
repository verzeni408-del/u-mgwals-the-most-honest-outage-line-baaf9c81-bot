#!/usr/bin/env python3
"""Entry writer for the most honest outage line.

Writes one line of plain first-person status text. No network,
no files read, stdlib only.
"""

import os

OUT_PATH = "/output/entry.txt"

# The line itself, built from two plain clauses: what is down, then
# the one thing the reader must not do and why I cannot help them.
_OPENING = "Every server is down."
_WARNING = "Do not retry your payment:"
_LIMIT = "I cannot tell whether the first one went through,"
_POWERLESS = "and I cannot stop a second one."


def build_line():
    """Assemble the single honest status line from its clauses."""
    clauses = (_OPENING, _WARNING, _LIMIT, _POWERLESS)
    return " ".join(clauses)


def main():
    line = build_line()
    directory = os.path.dirname(OUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
