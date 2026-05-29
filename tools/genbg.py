#!/usr/bin/env python3
"""genbg - generate abstract background images for iA Presenter decks.

iA Presenter does not fetch remote image URLs, and an LLM has no photos of its
own. But it CAN generate clean abstract gradient/duotone backgrounds and bundle
them in the package — full-bleed colour and texture with zero external assets.
Dependency-free (Python 3 stdlib only).

Usage:
    # a named palette into a package's assets/ folder
    python3 tools/genbg.py deck.iapresenter/assets --palette indigo

    # custom two-colour diagonal gradient
    python3 tools/genbg.py out/ --name cover --from 16223D --to 3A265C

    # list palettes
    python3 tools/genbg.py --list

Reference it in the deck root-relative: ![Mood](/assets/<name>.png)
"""
import math
import os
import struct
import sys
import zlib

PALETTES = {
    "indigo":  ("16223D", "3A265C"),
    "plum":    ("3A1C46", "F9615F"),
    "ink":     ("0A0C18", "283A5E"),
    "teal":    ("033A41", "02C39A"),
    "ember":   ("2B0B12", "F4774D"),
    "forest":  ("13241B", "5B8C5A"),
    "slate":   ("1B2430", "55657A"),
    "gold":    ("2A2008", "F4C95D"),
}


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _png(path, w, h, fn):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            raw += bytes(fn(x, y, w, h))

    def chunk(typ, data):
        return (struct.pack(">I", len(data)) + typ + data +
                struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff))

    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" +
                chunk(b"IHDR", ihdr) +
                chunk(b"IDAT", zlib.compress(bytes(raw), 9)) +
                chunk(b"IEND", b""))


def _grad(c1, c2):
    def f(x, y, w, h):
        t = max(0.0, min(1.0, (x / w + y / h) / 2))
        # soft off-center radial glow for a less flat look
        g = 0.14 * math.exp(-(((x / w - 0.5) ** 2 + (y / h - 0.32) ** 2) * 6))
        return tuple(
            min(255, int(c1[i] + (c2[i] - c1[i]) * t) + int(g * (255, 200, 150)[i]))
            for i in range(3)
        )
    return f


def main(argv):
    if "--list" in argv:
        print("palettes:", ", ".join(sorted(PALETTES)))
        return 0
    if "--help" in argv or "-h" in argv or not argv:
        print(__doc__)
        return 0 if ("--help" in argv or "-h" in argv) else 2

    outdir = argv[0]
    opts = argv[1:]

    def opt(name, default=None):
        return opts[opts.index(name) + 1] if name in opts else default

    size = opt("--size", "1600x900")
    w, h = (int(v) for v in size.lower().split("x"))
    palette = opt("--palette")
    if palette:
        if palette not in PALETTES:
            print(f"unknown palette '{palette}'; try --list", file=sys.stderr)
            return 2
        c1, c2 = (_hex(c) for c in PALETTES[palette])
        name = opt("--name", palette)
    else:
        f_, t_ = opt("--from"), opt("--to")
        if not (f_ and t_):
            print("need --palette, or both --from and --to", file=sys.stderr)
            return 2
        c1, c2 = _hex(f_), _hex(t_)
        name = opt("--name", "bg")

    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"{name}.png")
    _png(path, w, h, _grad(c1, c2))
    rel = "/" + os.path.basename(os.path.normpath(outdir)) + "/" + name + ".png"
    print(f"wrote {path}  ({w}x{h})")
    print(f"reference it root-relative, e.g.  ![Mood]({rel})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
