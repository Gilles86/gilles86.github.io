"""Minimal pycortex bundle for the braincoder brain icon: fsaverage, right hemisphere,
one smooth topographic patch in parietal cortex, no ROIs or labels.

Usage: pycortex2/bin/python brain_icon_bundle.py <outdir>
Then serve <outdir>, hide the left hemisphere, set mix 0.3, azimuth 270, altitude 70,
radius 260, target [30, -20, 15], screenshot, and key out the black background into
_scripts/brain_icon.png.
"""
import sys
import shutil
import numpy as np
import cortex

out = sys.argv[1]
subject = 'fsaverage'
lh, rh = cortex.db.get_surf(subject, 'fiducial')
n_l, n_r = len(lh[0]), len(rh[0])

centre = np.array([28, -62, 52])
d = np.linalg.norm(rh[0] - centre, axis=1)
patch = d < 24
vals = np.full(n_l + n_r, np.nan)
# preferred stimulus runs smoothly along the patch's posterior-anterior axis
y = rh[0][patch, 1]
vals[n_l:][patch] = (y - y.min()) / (y.max() - y.min())

alpha = np.isfinite(vals).astype(float)
v = cortex.Vertex(np.nan_to_num(vals), subject, cmap='viridis', vmin=-0.05, vmax=1.05)
v = v.blend_curvature(alpha, smooth=2, threshold=True, brightness=0.62, contrast=0.28)
shutil.rmtree(out, ignore_errors=True)
cortex.webgl.make_static(out, {'map': v}, types=('inflated',),
                         recache=False, overlays_visible=(), labels_visible=(),
                         curvature_brightness=0.62, curvature_contrast=0.28,
                         curvature_smoothness=2.0, surface_specularity=0.1)
print('bundle written to', out)
