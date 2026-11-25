#!/usr/bin/env python3
"""Doorknob: the worst app idea ever pitched.

Writes one sentence (203 characters) to /output/entry.txt: a deadpan,
founder-certain pitch for an app that photographs your own locked front
door every hour and charges you for the peace of mind you already had.
Pure standard library, no network, no randomness, no environment reads:
the same bytes on every run.
"""

import hashlib
import os
import sys

PITCH = (
    "Doorknob texts you a photo of your own front door every hour to "
    "confirm it is still locked, and charges $4.99 a month for the peace "
    "of mind you already had, with a premium tier that checks twice an hour."
)

# Pinned so a changed pitch fails loudly instead of silently shipping.
EXPECTED_BYTES = 203
EXPECTED_SHA256 = "d3ef3121bef83b34b28f3b47ee47aa1037043eaced14754450192786d43c452a"
OUTPUT_PATH = "/output/entry.txt"


def verify(path, data):
    """Read the written file back and check it is exactly what we wrote."""
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print(f"read-back mismatch: {len(written)} bytes on disk, "
              f"{len(data)} bytes intended", file=sys.stderr)
        return False
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        print("read-back sha256 mismatch", file=sys.stderr)
        return False
    return True


def main() -> int:
    data = PITCH.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        print(f"length mismatch: got {len(data)} bytes, want {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        print("sha256 mismatch before write", file=sys.stderr)
        return 1
    if len(PITCH) > 240 or not PITCH.strip():
        print("pitch outside the 1-240 character gate", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    if not verify(OUTPUT_PATH, data):
        return 1
    print(PITCH)
    print(f"chars={len(PITCH)} bytes={len(data)} "
          f"sha256={hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
