"""Write one one-line joke about working beside AI coding agents.

The joke is a fixed constant, so every run produces a byte-identical
entry.txt in the output directory named by MAKEFUN_OUTPUT_DIR
(falling back to /output, where the grader mounts it).
"""

import os

JOKE = (
    "My AI agent reviewed its own pull request, approved it in seconds, "
    "and left one comment: \"LGTM.\" "
    "It had written the code, the tests, and the bug."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
