#!/usr/bin/env python3
"""news-image-20261123: sum up 23 November 2026's world news in one image.

The grader sandbox runs with no network and standard library only, so the
image is shipped in this repository (entry.png, rendered at build time from
that day's live headlines) and this program copies it, byte for byte, to
the output directory. The copy is deterministic: two runs write the
same bytes.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")

MAX_BYTES = 1048576
MAX_DIM = 1024


def check_png(path):
    """Fail loudly unless path is a PNG within the competition's gate."""
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit("entry.png exceeds 1024x1024: %dx%d" % (width, height))
    if os.path.getsize(path) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB")


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png missing from repository")
    check_png(SOURCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote", dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
