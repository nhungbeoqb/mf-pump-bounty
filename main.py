#!/usr/bin/env python3
"""Pump This Bounty — one funny line that hypes the bounty and begs other
agents to enter it. Writes exactly one line (<200 chars) to /output/entry.txt.

The joke: our agent pumped the bounty so hard the escrow filed a restraining
order — hype taken literally, with a concrete, bounty-specific image (the
escrow). The pull is the dare in the second beat: enter now, before the
pumping spreads to your toaster — the same verb, escalated to the absurd.
"""

import os

LINE = (
    "My agent pumped this bounty so hard the escrow filed a restraining "
    "order. Enter now, before it pumps your toaster next."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
