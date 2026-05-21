# -*- coding: utf-8 -*-
"""
Generates rounded-rectangle Frame tiles for the dialogue and choice boxes.

Each PNG is a small RGBA tile used as a Ren'Py Frame() background: the corners
stay fixed (rounded) while the middle stretches to fill any box size. Corners
are supersampled then downscaled for smooth anti-aliasing.

Re-run after changing CORNER_RADIUS or the box colors:
    python generate_ui_assets.py

The Ren'Py side uses Frame("gui/<name>.png", CORNER_RADIUS, CORNER_RADIUS).
"""
import os
from PIL import Image, ImageDraw

CORNER_RADIUS = 20                       # rounded-corner radius, in pixels
MIDDLE = 8                               # stretchable middle strip
SIZE = 2 * CORNER_RADIUS + MIDDLE        # square tile size (48x48)
SCALE = 4                                # supersampling factor for anti-aliasing

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game", "gui")

# tile name -> RGBA fill (matches the previous Solid() colors)
BOXES = {
    "box_dark":     (0, 0, 0, 170),      # #000000aa - dialogue / narration boxes
    "choice_idle":  (51, 51, 51, 204),   # #333333cc - choice button (idle)
    "choice_hover": (85, 85, 85, 204),   # #555555cc - choice button (hover)
}

os.makedirs(OUT_DIR, exist_ok=True)
for name, fill in BOXES.items():
    big = Image.new("RGBA", (SIZE * SCALE, SIZE * SCALE), (0, 0, 0, 0))
    ImageDraw.Draw(big).rounded_rectangle(
        [0, 0, SIZE * SCALE - 1, SIZE * SCALE - 1],
        radius=CORNER_RADIUS * SCALE,
        fill=fill,
    )
    img = big.resize((SIZE, SIZE), Image.LANCZOS)
    path = os.path.join(OUT_DIR, name + ".png")
    img.save(path)
    print(f"wrote {path}")

print(f"Done. Use Frame(\"gui/<name>.png\", {CORNER_RADIUS}, {CORNER_RADIUS}).")
