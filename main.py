#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one single-line office joke to /output/entry.txt.
Python 3.13, standard library only, fully deterministic:
The joke: a reply-all protest that triggers the exact reply-all
storm it protests — recognition (reply-all), a turn at the end
("to debate it"), tight at 85 characters, and fresh: no Monday,
no photocopier. Run: python3 main.py
"""

import os

JOKE = "I hit reply-all to stop the reply-alls. 400 people are now replying all to debate it."


def main() -> None:
    # Gate: 1-199 characters, a single line, not only whitespace.
    assert 1 <= len(JOKE) <= 199, f"joke length {len(JOKE)} outside 1-199"
    assert "\n" not in JOKE and JOKE.strip() == JOKE
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
