#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun bounty entry.

Writes a single line of office humour (<=200 chars, no newline inside)
to $MAKEFUN_OUTPUT_DIR/entry.txt, then prints it. Fully deterministic.
"""
import os
import sys

JOKE = (
    "Our Monday standup could have been an email, but apparently it needed "
    "nine people, a projector that won't connect, and Dave's 'one quick "
    "question' — now in its fortieth minute."
)


def main() -> int:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
