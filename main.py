#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is written to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when that
variable is set, and to ``./output/entry.txt`` otherwise. The output is
UTF-8 text of 1 to 280 characters (Unicode code points), never only
whitespace, and the program needs no network access.
"""

import os
import sys

JOKE = (
    "My agent's PR was 900 lines, all tests green, so I approved it in four "
    "seconds, then spent the afternoon in git blame looking for a human to "
    "blame."
)


def main() -> int:
    text = JOKE.strip()
    if not text or text.isspace():
        print("error: joke is empty", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"error: joke is {len(text)} characters, must be 1-280",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
