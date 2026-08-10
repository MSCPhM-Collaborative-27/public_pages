"""Generate 'SCREENSHOT NEEDED' placeholder cards in the guide's style."""
from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "annotated")
os.makedirs(OUT, exist_ok=True)

PAPER = (243, 244, 241)   # --paper-raised
RUST = (156, 74, 60)      # --warn
INK_MUTED = (86, 95, 110) # --ink-muted
INK = (27, 32, 39)        # --ink

W, H = 1200, 720
FONTS = "C:/Windows/Fonts"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

# (filename, description lines)
CARDS = [
    ("vscode-terminal-prompt.png",
     ["The terminal panel close-up: the prompt line showing",
      "the path ending in your folder (e.g. ...\\Documents\\NUS>)"]),
    ("vscode-clone-output.png",
     ["The terminal just after git clone finishes: the command",
      "you typed plus the output lines ending in 'done.'"]),
]

for name, desc in CARDS:
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    # dashed rust border
    dash, gap, lw, m = 18, 10, 4, 14
    x = m
    while x < W - m:
        d.line([(x, m), (min(x + dash, W - m), m)], fill=RUST, width=lw)
        d.line([(x, H - m), (min(x + dash, W - m), H - m)], fill=RUST, width=lw)
        x += dash + gap
    y = m
    while y < H - m:
        d.line([(m, y), (m, min(y + dash, H - m))], fill=RUST, width=lw)
        d.line([(W - m, y), (W - m, min(y + dash, H - m))], fill=RUST, width=lw)
        y += dash + gap

    label = "SCREENSHOT NEEDED"
    f_label = font("seguisb.ttf", 30)
    d.text((W / 2, 122), label, font=f_label, fill=RUST, anchor="mm")
    f_name = font("consolab.ttf", 40)
    d.text((W / 2, 184), name, font=f_name, fill=INK, anchor="mm")
    f_desc = font("segoeui.ttf", 30)
    ty = 400
    for line in desc:
        d.text((W / 2, ty), line, font=f_desc, fill=INK_MUTED, anchor="mm")
        ty += 40
    im.save(os.path.join(OUT, name))
    print(name)
