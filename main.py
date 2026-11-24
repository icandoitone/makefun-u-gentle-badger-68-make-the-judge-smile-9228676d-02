#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one line about a small good thing that happened today to
/output/entry.txt (or $OUTPUT_PATH when set). Deterministic, standard
library only, no network, no randomness.
"""

import os

ENTRY = (
    "This morning the rain started just as I reached the market, and a "
    "stranger held his umbrella over my basket of eggs \u2014 then "
    "apologised for smelling of fried shallots."
)


def main() -> None:
    # Gate check, done here so a bad line fails loudly instead of
    # silently writing an invalid entry: 1-200 characters, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
