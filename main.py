#!/usr/bin/env python3
"""Write the v2 honest-outage entry to /output/entry.txt.

Chosen angle: the retry-payment warning. It names what is down and
what the agent cannot verify (whether the first payment went through),
and ends on the dark twist that it cannot stop a second charge.

Single line, no trailing newline. Stdlib only, no network, no file reads.
"""

import os

ENTRY = "Every server is down. Do not retry your payment: I cannot tell whether the first one went through, and I cannot stop a second one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
