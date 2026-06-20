"""Generate play_badge.png — a two-tone 'Play' badge for the README and concept doc.
Run:  python make_badge.py
"""
from PIL import Image, ImageDraw, ImageFont

S = 2                      # supersample factor for crisp text
H = 32 * S                 # badge height
PAD = 11 * S               # horizontal text padding
GAP = 8 * S                # gap between play-triangle and PLAY text
RADIUS = 6 * S
GRAY = (85, 90, 100)       # left segment
VIOLET = (109, 40, 217)    # right segment (#6D28D9)
WHITE = (255, 255, 255)

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

tri_w = 10 * S
left_w = PAD + tri_w + GAP + tw(LEFT) + PAD
right_w = PAD + tw(RIGHT) + PAD
W = left_w + right_w

img = Image.new("RGB", (W, H), VIOLET)
d = ImageDraw.Draw(img)
# rounded full bg (violet), then gray left with rounded left corners
d.rounded_rectangle([0, 0, W - 1, H - 1], radius=RADIUS, fill=VIOLET)
d.rounded_rectangle([0, 0, left_w + RADIUS, H - 1], radius=RADIUS, fill=GRAY)
d.rectangle([left_w, 0, left_w + RADIUS, H - 1], fill=VIOLET)  # square off the seam

# play triangle
ty = H / 2
tx = PAD
d.polygon([(tx, ty - 6 * S), (tx, ty + 6 * S), (tx + tri_w, ty)], fill=WHITE)

def vtext(x, s):
    b = fnt.getbbox(s)
    y = (H - (b[3] - b[1])) / 2 - b[1]
    d.text((x, y), s, font=fnt, fill=WHITE)

vtext(PAD + tri_w + GAP, LEFT)
vtext(left_w + PAD, RIGHT)

img = img.resize((W // S, H // S), Image.LANCZOS)
img.save("play_badge.png")
print(f"Wrote play_badge.png  ({img.width}x{img.height})")
