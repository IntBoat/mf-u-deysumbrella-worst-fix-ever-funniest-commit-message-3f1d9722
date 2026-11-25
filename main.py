#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message (make.fun).

Writes the entry -- one commit message for a bug fix that made everything worse --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'fix: silence the alarm by deleting the monitoring'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
