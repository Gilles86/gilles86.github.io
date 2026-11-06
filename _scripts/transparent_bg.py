"""Make the white background of figure thumbnails transparent (house style, see CLAUDE.md).

Background = near-white pixels connected to the image border (after padding with white),
morphologically opened so it cannot leak into the figure through narrow gaps, with a
2 px colour-to-alpha fringe for anti-aliasing. Also trims a thin white frame around an
otherwise dark image.

Usage: python transparent_bg.py in.png [out.png]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else src
rgb = np.asarray(Image.open(src).convert('RGB')).astype(float)
pad = 6
p = np.pad(rgb, ((pad, pad), (pad, pad), (0, 0)), constant_values=255)
white = p.min(axis=2) > 235
lab, _ = ndi.label(white)
border_labels = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
bg = np.isin(lab, border_labels[border_labels > 0])
disk = np.hypot(*np.mgrid[-4:5, -4:5]) <= 4
bg = ndi.binary_opening(bg, structure=disk)
bg = bg[pad:-pad, pad:-pad]

alpha = np.where(bg, 0.0, 1.0)
fringe = ndi.binary_dilation(bg, iterations=2) & ~bg
whiteness = rgb.min(axis=2) / 255
alpha[fringe] = np.clip((1 - whiteness[fringe]) / (1 - 235 / 255), 0, 1)
out = np.dstack([rgb, alpha * 255]).astype(np.uint8)

ys, xs = np.nonzero(alpha > 0)
out = out[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
Image.fromarray(out, 'RGBA').save(dst)
print(dst, out.shape, f'{(alpha == 0).mean():.0%} transparent')
