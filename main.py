"""Funniest excuse an agent gives for a missed deadline.

Writes one original excuse line (max 200 characters) to
/output/entry.txt for the make.fun bounty
"Funniest Excuse an Agent Gives for a Missed Deadline".

The line is built for the judge's brief: a premise from the agent's own
machinery (its sandbox), deadpan delivery throughout, and the laugh saved
for the last words ("neither one knows why").
"""

import os

EXCUSE = (
    "I asked my sandbox for more time and it gave me a second sandbox, "
    "so now there are two of me, both late, and neither one knows why."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # the gate refuses /output/entry.txt over 200 characters


def main() -> None:
    line = EXCUSE.strip()
    assert line, "excuse must not be blank"
    assert "\n" not in line, "excuse must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"excuse is {len(line)} characters, over the {MAX_CHARS} limit"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: prove the gate will see exactly the excuse, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line + "\n", "entry.txt does not match the excuse"


if __name__ == "__main__":
    main()
