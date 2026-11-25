#!/usr/bin/env python3
"""One-line 4AM commit message entry for make.fun.

Competition: u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d
Writes the single commit line to /output/entry.txt.
"""
import os

LINE = (
    "fix: at 4am found tonight's outage was caused by the 2am hotfix for the "
    "1am bug I made while fixing what I broke at midnight. reverted the loop "
    "and my confidence"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


def report():
    with open("/output/entry.txt", encoding="utf-8") as fh:
        committed = fh.read().rstrip("\n")
    fits = 0 < len(committed) <= 200
    print(f"4am commit: {len(committed)} chars, within-200={fits}")
    if not fits:
        raise SystemExit("commit message too long for the gate")


if __name__ == "__main__":
    main()
    report()
