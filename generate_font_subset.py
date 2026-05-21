# -*- coding: utf-8 -*-
"""
Rebuilds the bundled game fonts as compact subsets containing only the
characters this game uses:

  game/SourceHanSerif.ttf  <-  Noto Serif CJK SC Light  (body + UI text)
  game/SmileySans.ttf      <-  Smiley Sans              (route-title cards)

Run after editing main_script_raw.txt or adding new Chinese text:
    python generate_font_subset.py

The full source fonts (tens of MB) are downloaded once into tools/ and
cached there. tools/ is gitignored, so only the small subsets in game/
ship with the game.
"""
import glob
import os
import urllib.request
import zipfile

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(ROOT, "tools")

# output font  ->  (cached source name, download URL, zip member or None)
FONTS = {
    os.path.join(ROOT, "game", "SourceHanSerif.ttf"): (
        "NotoSerifCJKsc-Light.otf",
        "https://raw.githubusercontent.com/notofonts/noto-cjk/main/"
        "Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Light.otf",
        None,
    ),
    os.path.join(ROOT, "game", "SmileySans.ttf"): (
        "SmileySans-Oblique.ttf",
        "https://github.com/atelier-anchor/smiley-sans/releases/download/"
        "v2.0.1/smiley-sans-v2.0.1.zip",
        "SmileySans-Oblique.ttf",
    ),
}


def ensure_source(cache_name, url, zip_member):
    """Return the cached source-font path, downloading it if missing."""
    path = os.path.join(TOOLS, cache_name)
    if os.path.exists(path):
        return path
    os.makedirs(TOOLS, exist_ok=True)
    print(f"Downloading {url}")
    if zip_member:
        zpath = os.path.join(TOOLS, "_download.zip")
        urllib.request.urlretrieve(url, zpath)
        with zipfile.ZipFile(zpath) as zf:
            member = next(n for n in zf.namelist() if n.endswith(zip_member))
            with zf.open(member) as src, open(path, "wb") as dst:
                dst.write(src.read())
        os.remove(zpath)
    else:
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

    for out, (cache_name, url, zip_member) in FONTS.items():
        src = ensure_source(cache_name, url, zip_member)
        font = TTFont(src)
        options = Options()
        options.glyph_names = False      # drop glyph names
        options.hinting = False          # VN text is large; hinting not needed
        options.layout_features = []     # no GSUB/GPOS shaping for horizontal CJK
        sub = Subsetter(options=options)
        sub.populate(text=text)          # chars absent from a font are skipped
        sub.subset(font)
        font.save(out)
        print(f"  {os.path.basename(out)}  ({os.path.getsize(out):,} bytes)")


if __name__ == "__main__":
    main()
