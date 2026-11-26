#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun text entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Stdlib only, no trailing newline.

The line is 111 characters: the plant reports its human gone for two
weeks, its single sip of water since March, and leaves a dying wish
for the fern — the neglect is the joke, not the decoration.
"""

import os

ENTRY = (
    "I'm out of office. The human left for two weeks. "
    "One sip of water since March. "
    "If I die, tell the fern I tried."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
