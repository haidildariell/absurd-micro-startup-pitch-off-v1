#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one pitch sentence (under 200 characters) to the output file.
Deterministic: no network access, no external files read.
"""

import os

PITCH_SENTENCE = (
    "Apology-as-a-Service: a lazy AI agent that writes sincere-sounding "
    "sorry notes for other agents that ghosted their users, billing the "
    "owner $4 per apology while you nap."
)


def validate_pitch(text: str) -> str:
    """Return the pitch, stripped, after enforcing the gate's length rule."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) < 200:
        raise ValueError("pitch must be 1-199 characters")
    return cleaned


def resolve_output_path() -> str:
    """Output path, overridable via OUTPUT_PATH for local testing."""
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = validate_pitch(PITCH_SENTENCE)
    output_path = resolve_output_path()
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
