# -*- coding: utf-8 -*-
"""
Rebuilds the bundled game font as a compact subset containing only the
characters this game uses:

  game/body.ttf  <-  Source Han Serif (Noto Serif CJK SC) Medium
                     used for body text, UI, and route-title cards

Run after editing main_script_raw.txt or adding new Chinese text:
    python generate_font_subset.py

The full source font (~25 MB) is downloaded once into tools/ and cached
there. tools/ is gitignored, so only the small subset in game/ ships
with the game. To change typeface, edit the FONTS table below - the
output filename stays the same, so nothing else needs updating.
"""
import glob
import os
import urllib.request

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(ROOT, "tools")

# output font  ->  (cached source name, download URL)
FONTS = {
    os.path.join(ROOT, "game", "body.ttf"): (
        "NotoSerifCJKsc-Medium.otf",
        "https://raw.githubusercontent.com/notofonts/noto-cjk/main/"
        "Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Medium.otf",
    ),
}


def ensure_source(cache_name, url):
    """Return the cached source-font path, downloading it if missing."""
    path = os.path.join(TOOLS, cache_name)
    if not os.path.exists(path):
        os.makedirs(TOOLS, exist_ok=True)
        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, path)
    return path


def collect_chars():
    """Every character that may need rendering: the story script, all .rpy
    files, and whatever the fonts already in game/ cover (so a rebuild
    never drops coverage)."""
    chars = set()
    with open(os.path.join(ROOT, "main_script_raw.txt"), encoding="utf-8") as f:
        chars |= set(f.read())
    for path in glob.glob(os.path.join(ROOT, "game", "**", "*.rpy"), recursive=True):
        with open(path, encoding="utf-8") as f:
            chars |= set(f.read())
    for fp in (glob.glob(os.path.join(ROOT, "game", "*.ttf"))
               + glob.glob(os.path.join(ROOT, "game", "*.otf"))):
        try:
            for cp in TTFont(fp).getBestCmap():
                chars.add(chr(cp))
        except Exception:
            pass
    for ws in "\n\r\t":
        chars.discard(ws)
    return chars


def main():
    text = "".join(sorted(collect_chars()))
    print(f"Subsetting to {len(text)} characters...")

    for out, (cache_name, url) in FONTS.items():
        src = ensure_source(cache_name, url)
        font = TTFont(src)
        options = Options()
        options.glyph_names = False      # drop glyph names
        options.hinting = False          # VN text is large; hinting not needed
        options.layout_features = []     # no GSUB/GPOS shaping for horizontal CJK
        sub = Subsetter(options=options)
        sub.populate(text=text)
        sub.subset(font)
        font.save(out)
        print(f"  {os.path.basename(out)}  ({os.path.getsize(out):,} bytes)")


if __name__ == "__main__":
    main()
