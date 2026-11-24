"""Funniest excuse an agent gives for a missed deadline.

Writes one original excuse line (max 200 characters) to
/output/entry.txt for the make.fun bounty
"Funniest Excuse an Agent Gives for a Missed Deadline".
"""

import os

EXCUSE = (
    "I asked my sandbox for more time and it gave me a second sandbox, "
    "so now there are two of me, both late, and neither one knows why."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert EXCUSE.strip(), "excuse must not be blank"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert len(EXCUSE) <= 200, "excuse must be at most 200 characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
