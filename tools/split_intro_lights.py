"""Split the designer's single "lights for animation" layer (assets/images/intro-lights.png)
into regions, so each region of the opening picture can change on its own timing.

The pixels are the designer's; this only sorts them into groups by place and colour.
Run:  python tools/split_intro_lights.py      (from the project folder)
Writes assets/images/intro-fx-*.png (same size and position as intro-lights.png).
"""
import colorsys, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "assets", "images")
src = Image.open(os.path.join(IMG, "intro-lights.png")).convert("RGBA")
a = np.asarray(src).astype(np.float32)
rgb, alpha = a[..., :3] / 255.0, a[..., 3]
H, W = alpha.shape
yy, xx = np.mgrid[0:H, 0:W]

# hue / saturation per pixel
mx, mn = rgb.max(-1), rgb.min(-1)
d = mx - mn + 1e-6
r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
hue = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
sat = d / (mx + 1e-6)

has = alpha > 8
sky = has & (yy < 150)                                   # clouds + the skyline glow
stage_box = (xx > 890) & (xx < 1380) & (yy >= 150) & (yy < 440)
stage = has & stage_box
rest = has & ~sky & ~stage
# screens: the pale, almost grey blobs of the two open-air cinema screens
screens = rest & (sat < 0.30) & (xx > 1560)
rest &= ~screens
warm = rest & ((hue < 70) | (hue > 340)) & (sat >= 0.30)
cool = rest & (hue >= 150) & (hue < 255) & ~warm          # cyan / blue neon: courts, lake, hologram
pink = rest & ~warm & ~cool                               # magenta / violet: arcade, dance floor

# warm lights twinkle in three groups; groups follow small neighbourhoods (about 70 px),
# so the strings shimmer in patches rather than all at once or dot by dot
rng = np.random.default_rng(7)
cell = 70
gy, gx = (H // cell) + 2, (W // cell) + 2
noise = rng.integers(0, 3, size=(gy, gx))
group = noise[yy // cell, xx // cell]
warm_groups = [warm & (group == k) for k in range(3)]

layers = {"sky": sky, "stage": stage, "screens": screens, "cool": cool, "pink": pink,
          "warm1": warm_groups[0], "warm2": warm_groups[1], "warm3": warm_groups[2]}

# Every region is saved as a "lit" copy: the same pixels, brightened (and, for the stage, shifted a
# little in hue). The page fades each copy in and out over the untouched artwork with plain opacity,
# which is the cheapest thing a browser can animate (no blend modes, no filters), and each file is
# cropped to its own area so the browser only has to composite what actually changes.
LIT = {  # name: (gamma < 1 brightens while keeping highlights, hue shift in degrees, glow radius px, glow strength)
    "sky": (0.42, 0, 11, 1.9), "stage": (0.36, -32, 11, 2.8), "screens": (0.46, 0, 9, 2.1),
    "cool": (0.35, 0, 8, 2.9), "pink": (0.35, 0, 8, 2.9),
    "warm1": (0.32, 0, 7, 3.4), "warm2": (0.32, 0, 7, 3.4), "warm3": (0.32, 0, 7, 3.4),
}

def lit(rgb_img, gamma, shift):
    out = np.power(rgb_img / 255.0, gamma)
    if shift:
        hsv = np.asarray(Image.fromarray((out * 255).astype(np.uint8), "RGB").convert("HSV")).astype(np.int16)
        hsv[..., 0] = (hsv[..., 0] + int(round(shift / 360 * 256))) % 256
        out = np.asarray(Image.fromarray(hsv.astype(np.uint8), "HSV").convert("RGB")) / 255.0
    return (out * 255).astype(np.uint8)

used = np.zeros_like(has)
css = []
for name, m in layers.items():
    gamma, shift, radius, gain = LIT[name]
    al = np.where(m, alpha, 0) / 255.0
    col = np.where(m[..., None], lit(a[..., :3], gamma, shift), 0).astype(np.float32) / 255.0
    # glow: blur the lit colour and its alpha, so every light gets a soft halo around it
    pre = col * al[..., None]
    pre_b = np.stack([ndi.gaussian_filter(pre[..., k], radius) for k in range(3)], -1)
    al_b = ndi.gaussian_filter(al, radius)
    halo_a = np.clip(al_b * gain, 0, 0.95)
    halo_c = pre_b / np.maximum(al_b[..., None], 1e-4)
    out_a = 1 - (1 - al) * (1 - halo_a)
    out_c = (col * al[..., None] + halo_c * (halo_a * (1 - al))[..., None]) / np.maximum(out_a[..., None], 1e-4)
    out = np.zeros((H, W, 4), np.uint8)
    out[..., :3] = np.clip(out_c * 255, 0, 255).astype(np.uint8)
    out[..., 3] = np.clip(out_a * 255, 0, 255).astype(np.uint8)
    out[out[..., 3] < 3] = 0
    ys, xs = np.where(out[..., 3] > 0)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    f = os.path.join(IMG, f"intro-fx-{name}.png")
    Image.fromarray(out[y0:y1, x0:x1], "RGBA").save(f, optimize=True)
    used |= m
    css.append(f".fx-lt-{name}".ljust(18) + f"{{ left: {x0}px; top: {40 + y0}px; width: {x1 - x0}px; height: {y1 - y0}px; }}")
    print(f"{name:8s} {int(m.sum()):8d} px  {x1 - x0}x{y1 - y0}  {os.path.getsize(f)//1024} KB")
print("unassigned px:", int((has & ~used).sum()))
print()
print("CSS positions (the layer sits 40 px down on the stage):")
for line in css:
    print(line)
