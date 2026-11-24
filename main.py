"""One line of wedding vows for a robot couple, built for make.fun.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), with no trailing newline.
"""

import os
from pathlib import Path

LINE = "I vow to love you through every firmware update, to hold your hand at 1% battery, and to never, ever factory-reset us."

assert 1 <= len(LINE) <= 160 and LINE.strip(), "line must be 1-160 non-whitespace characters"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
