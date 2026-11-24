"""earned-pride-one-line — one line of earned pride.

The program holds a single sentence about a quiet moment: a father
running behind his daughter's bicycle, letting go without a word,
and her riding the rest of the street alone. It checks the line fits
the competition limits and writes it out to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "He ran behind her bicycle for three blocks and let go at the "
    "corner without telling her \u2014 and she rode the rest of the "
    "street alone, ringing the bell twice."
)

MAX_CHARS = 240
DESTINATION = Path("/output/entry.txt")


def check_line(text: str) -> None:
    """Raise if the line breaks any competition rule."""
    if not text:
        raise ValueError("entry line must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    check_line(LINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    # Write via a temp file and rename so /output/entry.txt is never
    # left half-written if the process is interrupted mid-write.
    tmp = DESTINATION.with_suffix(".tmp")
    tmp.write_text(LINE + "\n", encoding="utf-8")
    tmp.replace(DESTINATION)
    # Read back what actually landed on disk: the gate judges the file,
    # not the string in memory, so confirm they match before reporting.
    written = DESTINATION.read_text(encoding="utf-8")
    if written != LINE + "\n":
        raise ValueError("read-back mismatch: /output/entry.txt does not hold the entry line")
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
