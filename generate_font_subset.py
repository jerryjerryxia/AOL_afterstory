# -*- coding: utf-8 -*-
"""
Rebuilds game/SourceHanSansLite.ttf as a compact subset of the full
Noto Sans CJK SC / Source Han Sans (Light weight), containing only the
characters this game actually uses.

Run after editing main_script_raw.txt or adding new Chinese UI text:
    python generate_font_subset.py

The full source font (~16 MB) is downloaded once into tools/ and cached
there. tools/ is gitignored, so it is not committed; only the small
subset in game/ ships with the game.
"""
import glob
import os
import urllib.request

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_FONT = os.path.join(ROOT, "tools", "NotoSansCJKsc-Light.otf")
SRC_URL = ("https://raw.githubusercontent.com/notofonts/noto-cjk/main/"
           "Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Light.otf")
OUT_FONT = os.path.join(ROOT, "game", "SourceHanSansLite.ttf")


def ensure_source():
    """Download the full source font into tools/ if it is not cached yet."""
    if os.path.exists(SRC_FONT):
        return
    os.makedirs(os.path.dirname(SRC_FONT), exist_ok=True)
    print(f"Source font not cached - downloading:\n  {SRC_URL}")
    urllib.request.urlretrieve(SRC_URL, SRC_FONT)
    print("  done.")


def collect_chars():
    """Every character that may need rendering: the story script, all .rpy
    UI/text files, and whatever the current subset already covers (so a
    rebuild never drops coverage)."""
    chars = set()

    with open(os.path.join(ROOT, "main_script_raw.txt"), encoding="utf-8") as f:
        chars |= set(f.read())

    for path in glob.glob(os.path.join(ROOT, "game", "**", "*.rpy"), recursive=True):
        with open(path, encoding="utf-8") as f:
            chars |= set(f.read())

    if os.path.exists(OUT_FONT):
        for cp in TTFont(OUT_FONT).getBestCmap():
            chars.add(chr(cp))

    for ws in "\n\r\t":
        chars.discard(ws)
    return chars


def main():
    ensure_source()
    chars = collect_chars()
    print(f"Subsetting to {len(chars)} characters...")

    font = TTFont(SRC_FONT)
    options = Options()
    options.glyph_names = False      # drop glyph names (use glyphNNNN)
    options.hinting = False          # VN text is large; hinting not needed
    options.layout_features = []     # no GSUB/GPOS shaping for horizontal CJK
    sub = Subsetter(options=options)
    sub.populate(text="".join(sorted(chars)))
    sub.subset(font)
    font.save(OUT_FONT)

    print(f"Wrote {OUT_FONT}  ({os.path.getsize(OUT_FONT):,} bytes)")


if __name__ == "__main__":
    main()
