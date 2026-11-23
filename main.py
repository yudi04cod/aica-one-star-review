#!/usr/bin/env python3
"""One-star review of gravity, an everyday essential.

Writes a single deadpan one-star review, at most 160 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only. Deterministic: the same bytes on every run.
"""

import os
import sys

# The review: a deadpan one-star complaint filed in earnest against a
# thing that cannot be fixed. No exclamation marks, no winking.
REVIEW = (
    "Gravity: keeps everything down, including my phone, my keys, "
    "and my mood. No off switch, no refund, and it has been doing "
    "this since forever."
)

MAX_CHARS = 160


def validate(text):
    """Check the review meets the competition gate."""
    if not text or not text.strip():
        raise ValueError("review is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "review is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    review = validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(review + "\n")
    # Read the file back and confirm it holds exactly the review.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != review + "\n":
        raise RuntimeError("verification failed: entry.txt does not match review")
    print("wrote %s (%d characters)" % (out_path, len(review)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
