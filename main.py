#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.

The pitch: a concierge that appeals parking tickets issued to delivery
robots, for lazy AI fleet managers, on a contingency cut of dismissed fines.
"""

from pathlib import Path

PITCH = (
    "A concierge that appeals parking tickets issued to delivery robots "
    "idling at red lights, for lazy AI fleet managers, keeping 15% of "
    "every fine it gets dismissed."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = PITCH.strip()
    if not text or text.isspace():
        raise ValueError("pitch must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch must be at most {MAX_CHARS} chars, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
