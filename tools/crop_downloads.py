"""Crop the download-page captures and add highlight boxes. All coords original px (2880x1800)."""
from PIL import Image, ImageDraw
import os

RUST = (156, 74, 60)
BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "annotated")
os.makedirs(OUT, exist_ok=True)

JOBS = [
    {
        "src": "captured/vscode-download-page.png",
        "out": "vscode-download-page.png",
        "crop": (432, 240, 2448, 1400),
        "boxes": [(634, 880, 962, 1046), (1893, 880, 2147, 1046)],  # Windows button; Mac button
    },
    {
        "src": "captured/git-download-page.png",
        "out": "git-download-page.png",
        "crop": (980, 144, 2390, 1310),
        "boxes": [(1043, 464, 1398, 522)],  # "Click here to download" link
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
