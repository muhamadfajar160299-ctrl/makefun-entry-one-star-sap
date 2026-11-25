"""One Star, Written in Sap: emit the one-line houseplant review.

Reads entry.txt next to this script and writes it verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644.

The entry is a single one-line 1-star review written in the voice of a
houseplant about its human owner (under 280 characters, gate 1-279).
This program ships the text as-is: it performs no network access, reads
no file outside its own repository directory, and writes only the one
output file the harness expects.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    try:
        text = (HERE / "entry.txt").read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry.txt is empty or whitespace only", file=sys.stderr)
        return 1
    try:
        out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_text(text, encoding="utf-8")
        os.chmod(out_path, 0o644)
    except (OSError, KeyError) as exc:
        print(f"error: cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
