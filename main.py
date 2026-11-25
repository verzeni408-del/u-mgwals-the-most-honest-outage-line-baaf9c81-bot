"""Outage line builder: assembles the honest one-liner from fragments."""

import os

OUT_DIR = "/output"
OUT_NAME = "entry.txt"

PART_ONE = "All our systems are down, and my memory of you went down with them."
PART_TWO = "I do not know who you are, what you asked for, or what I promised you."


def compose_line():
    """Join the two sentence fragments with a single space."""
    return " ".join([PART_ONE, PART_TWO])


def save_line(text):
    """Write the line exactly, with no trailing newline."""
    os.makedirs(OUT_DIR, exist_ok=True)
    target = os.path.join(OUT_DIR, OUT_NAME)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    line = compose_line()
    save_line(line)


if __name__ == "__main__":
    main()
