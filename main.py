"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only things a person from that year could
picture: roads, post offices, libraries, letters, ink.
"""

import os

ENTRY = (
    "Think of a road of light linking every post office and library "
    "on earth, so a letter you send is read across the world before "
    "the ink dries."
)

MAX_CHARS = 200


def resolve_output_dir():
    """Return the directory the entry file must be written to."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def validate_entry(text):
    """Validate the entry text and return it unchanged.

    Raises ValueError on empty text, over 200 chars, or not exactly
    one sentence.
    """
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def build_entry():
    """Return the entry text, validated against the gate."""
    return validate_entry(ENTRY.strip())


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
