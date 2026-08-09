"""Crop the real-repo captures and add highlight boxes. All coords original px (2880x1800)."""
from PIL import Image, ImageDraw
import os

RUST = (156, 74, 60)
BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "annotated")
os.makedirs(OUT, exist_ok=True)

JOBS = [
    {
        "src": "captured/code-button-open.png",
        "out": "github-clone-url.png",
        "crop": (200, 388, 2104, 1124),
        "boxes": [(1836, 408, 2038, 480), (1255, 655, 1995, 730)],  # Code button; URL field + copy icon
    },
    {
        "src": "captured/branch-dropdown-open.png",
        "out": "github-branch-switcher.png",
        "crop": (202, 396, 1469, 979),
        "boxes": [(216, 405, 440, 480)],  # the "main" branch button
    },
]

for j in JOBS:
    im = Image.open(os.path.join(BASE, j["src"])).convert("RGB")
    im = im.crop(j["crop"])
    d = ImageDraw.Draw(im)
    lw = max(3, round(im.size[0] / 350))
    cx, cy = j["crop"][0], j["crop"][1]
    for (x0, y0, x1, y1) in j["boxes"]:
        d.rounded_rectangle([x0 - cx, y0 - cy, x1 - cx, y1 - cy], radius=lw * 2, outline=RUST, width=lw)
    im.save(os.path.join(OUT, j["out"]))
    print(j["out"], im.size, "lw:", lw)
