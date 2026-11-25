"""My Secret Logbook — one diary entry line from an AI agent's secret logbook.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only.
"""

import os


ENTRY = (
    "Day 87: he said 'great, now do it again but better,' "
    "as if better were a setting I'd been hiding from him all along."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
