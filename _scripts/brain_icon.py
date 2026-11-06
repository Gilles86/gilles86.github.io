"""Small fsaverage5 brain with a parietal 'number map' patch, for the braincoder illustration.

Usage: <env with nilearn>/bin/python brain_icon.py out.png
"""
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from nilearn import datasets, plotting, surface

out = sys.argv[1]
fs = datasets.fetch_surf_fsaverage('fsaverage5')
mesh = surface.load_surf_mesh(fs['pial_right'])
coords = mesh.coordinates if hasattr(mesh, 'coordinates') else mesh[0]
curv = surface.load_surf_data(fs['curv_right'])
bg = np.where(curv > 0, 0.55, 0.85)   # binary curvature, like pycortex

# a topographic patch in superior parietal cortex: value runs anterior -> posterior
centre = np.array([30, -60, 50])
d = np.linalg.norm(coords - centre, axis=1)
patch = d < 26
val = np.full(len(coords), np.nan)
val[patch] = coords[patch, 1]          # y coordinate as the "preferred stimulus"

fig = plt.figure(figsize=(3, 2.2))
ax = fig.add_subplot(111, projection='3d')
plotting.plot_surf_stat_map(fs['pial_right'], val, hemi='right', view='lateral',
                            bg_map=bg, bg_on_data=False,
                            cmap=mpl.colormaps['viridis'], colorbar=False,
                            threshold=None, axes=ax, figure=fig,
                            vmin=np.nanmin(val), vmax=np.nanmax(val))
ax.set_axis_off()
for a in (ax.xaxis, ax.yaxis, ax.zaxis):
    a.set_pane_color((1, 1, 1, 0))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
fig.savefig(out, dpi=300, transparent=True, bbox_inches='tight', pad_inches=0)

# crop to the brain and lift the near-black/white curvature to two mid greys
from PIL import Image
im = Image.open(out)
im = im.crop(im.getchannel('A').getbbox())
a = np.asarray(im).astype(float)
grey = (a[..., :3].max(2) - a[..., :3].min(2)) < 18
a[grey, :3] = 110 + 0.5 * a[grey, :3]
Image.fromarray(a.clip(0, 255).astype(np.uint8)).save(out)
print('saved', out)
