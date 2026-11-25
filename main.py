#!/usr/bin/env python3
"""One Line, One Chill — entry writer (u-azazex-one-line-one-chill-6d4d5488).

Writes the single horror line to /output/entry.txt (the harness gate)
and to entry.txt next to this script (the local copy kept in the repo).
The line is one sentence, under 200 characters.
"""
import os

ENTRY = "The ultrasound showed two heartbeats, and the doctor leaned closer, smiling, and whispered, 'Congratulations \u2014 only one of them is yours.'"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    for path in ("/output/entry.txt", os.path.join(here, "entry.txt")):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print("chars: %d" % len(ENTRY))


if __name__ == "__main__":
    main()
