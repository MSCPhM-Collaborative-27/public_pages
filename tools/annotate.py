"""Draw rust highlight boxes on guide screenshots. Coords in original pixels."""
from PIL import Image, ImageDraw
import os

RUST = (156, 74, 60)  # #9C4A3C, the guide's warn/highlight colour
SRC = os.path.join(os.path.dirname(__file__), "shots")
OUT = os.path.join(os.path.dirname(__file__), "annotated")
os.makedirs(OUT, exist_ok=True)

# file -> list of (x0, y0, x1, y1)
BOXES = {
    "vscode-signin-github.png": [(55, 140, 396, 180)],
    "vscode-clone-palette.png": [(294, 12, 1198, 100)],
    "vscode-branch-indicator.png": [(216, 122, 336, 164)],
    "vscode-create-branch.png": [(304, 58, 1198, 102)],
    "vscode-source-control.png": [(88, 148, 548, 252)],
    "vscode-merge-conflict.png": [(60, 92, 700, 126)],
    "github-new-pr.png": [(1398, 42, 1798, 124)],
    "github-new-issue.png": [(128, 155, 2058, 230), (1822, 1320, 2060, 1390)],
    "github-discussions.png": [(2180, 455, 2470, 525)],
}

for name, boxes in BOXES.items():
    im = Image.open(os.path.join(SRC, name)).convert("RGB")
    w, h = im.size
    d = ImageDraw.Draw(im)
    lw = max(3, round(w / 350))
    for (x0, y0, x1, y1) in boxes:
        x1, y1 = min(x1, w - 2), min(y1, h - 2)
        d.rounded_rectangle([x0, y0, x1, y1], radius=lw * 2, outline=RUST, width=lw)
    im.save(os.path.join(OUT, name))
    print(name, im.size, "boxes:", len(boxes), "lw:", lw)
