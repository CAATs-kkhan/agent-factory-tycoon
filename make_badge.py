"""Generate play_badge.png — a rounded-pill 'Play' badge for the README and concept doc.
Run:  python make_badge.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

S = 3                      # supersample factor for crisp edges
H = 34 * S                 # badge height
PAD = 16 * S               # horizontal text padding
GAP = 9 * S                # gap between play-triangle and PLAY text
GRAY = (85, 90, 100, 255)  # left segment
VIOLET = (109, 40, 217, 255)  # right segment (#6D28D9)
WHITE = (255, 255, 255, 255)
TRANSP = (0, 0, 0, 0)
RADIUS = H // 2            # full pill rounding

LEFT = "PLAY"
RIGHT = "AGENT FACTORY TYCOON"

def font(sz):
    for p in (r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\segoeuib.ttf"):
        try:
            return ImageFont.truetype(p, sz)
        except OSError:
            continue
    return ImageFont.load_default()

fnt = font(16 * S)

def tw(s):
    b = fnt.getbbox(s)
    return b[2] - b[0]

tri_w = 11 * S
left_w = PAD + tri_w + GAP + tw(LEFT) + PAD
right_w = PAD + tw(RIGHT) + PAD
W = left_w + right_w

img = Image.new("RGBA", (W, H), TRANSP)
d = ImageDraw.Draw(img)
# full violet pill (transparent corners), then gray left segment with a pill-rounded
# left end and a straight seam at left_w.
d.rounded_rectangle([0, 0, W - 1, H - 1], radius=RADIUS, fill=VIOLET)
d.rounded_rectangle([0, 0, left_w - 1, H - 1], radius=RADIUS, fill=GRAY)
d.rectangle([left_w - RADIUS, 0, left_w, H - 1], fill=GRAY)  # straighten the seam

# play triangle (vertically centred)
ty = H / 2
tx = PAD
d.polygon([(tx, ty - 7 * S), (tx, ty + 7 * S), (tx + tri_w, ty)], fill=WHITE)

def vtext(x, s):
    b = fnt.getbbox(s)
    y = (H - (b[3] - b[1])) / 2 - b[1]
    d.text((x, y), s, font=fnt, fill=WHITE)

vtext(PAD + tri_w + GAP, LEFT)
vtext(left_w + PAD, RIGHT)

img = img.resize((W // S, H // S), Image.LANCZOS)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "play_badge.png")
img.save(out)
print(f"Wrote {out}  ({img.width}x{img.height})")
