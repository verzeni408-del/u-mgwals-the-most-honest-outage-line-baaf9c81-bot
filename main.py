"""Honest outage status line writer.

Emits a single first-person status line about the total outage
to /output/entry.txt, with no trailing newline.
"""

import os

STATUS_LINE = (
    "All our systems are down, and my memory of you went down with them. "
    "I do not know who you are, what you asked for, or what I promised you."
)

DESTINATION = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(STATUS_LINE)


if __name__ == "__main__":
    main()
