#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun bounty entry.

Writes one line (<=200 chars) of the excuse an AI agent gives its
human for missing a deadline: it delivered the report on time — to
the wrong human. Deterministic: no network, no randomness, no time
dependence.
"""

import os
import tempfile

ENTRY = (
    "I delivered your report on time \u2014 to the wrong human. "
    "They're delighted; you get the apology."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    assert "\n" not in ENTRY, "entry must stay one line (no newline)"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write via a unique temp file in the same directory: avoids
    # temp-name collisions between concurrent runs, and os.replace means
    # a crash can never leave a partial entry.txt behind.
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", dir=out_dir,
        prefix="entry.", suffix=".tmp", delete=False,
    ) as f:
        f.write(ENTRY)
        tmp_path = f.name
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
