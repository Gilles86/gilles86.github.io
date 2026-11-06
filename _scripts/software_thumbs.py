"""Illustrations for the braincoder and bauer cards (homepage + Software page).

Usage: python software_thumbs.py <outdir>
"""
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm

out = sys.argv[1]
mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Helvetica Neue', 'Arial'],
    'font.size': 15, 'axes.linewidth': 0.8,
    'savefig.dpi': 220, 'savefig.transparent': True,
})
INK = '0.25'
FS = 15
BLUE, RED, GREY = '#3B5BA5', '#C44E52', '0.6'


def clean(ax):
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(INK)
    ax.set_yticks([]); ax.set_xticks([])


def arrow(fig, x0, x1, y, text):
    fig.patches.append(mpl.patches.FancyArrowPatch(
        (x0, y), (x1, y), transform=fig.transFigure, arrowstyle='-|>',
        mutation_scale=20, lw=2.4, color=INK))
    fig.text((x0 + x1) / 2, y + 0.08, text, ha='center', va='bottom', color=INK, fontsize=FS)


# braincoder: tuning curves -> voxel responses -> decoded posterior
fig = plt.figure(figsize=(6.8, 2.0))
ax1 = fig.add_axes([0.02, 0.18, 0.30, 0.68])
ax2 = fig.add_axes([0.425, 0.18, 0.15, 0.30])
axb = fig.add_axes([0.40, 0.52, 0.20, 0.46])
axb.imshow(plt.imread(__file__.rsplit('/', 1)[0] + '/brain_icon.png'))
axb.set_axis_off()
ax3 = fig.add_axes([0.68, 0.18, 0.30, 0.68])

x = np.linspace(0, 1, 400)
cols = mpl.colormaps['viridis'](np.linspace(0.1, 0.9, 6))
centres = np.linspace(0.12, 0.88, 6)
for c, col in zip(centres, cols):
    ax1.fill_between(x, np.exp(-0.5 * ((x - c) / 0.09) ** 2), color=col, alpha=0.18, lw=0)
    ax1.plot(x, np.exp(-0.5 * ((x - c) / 0.09) ** 2), color=col, lw=2.6)
s_true = 0.58
ax1.axvline(s_true, color=RED, lw=1.2, ls='--')
ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.15)
ax1.set_xlabel('Stimulus', color=INK, labelpad=3)
clean(ax1)

rng = np.random.default_rng(3)
resp = np.clip(np.exp(-0.5 * ((s_true - centres) / 0.12) ** 2) + rng.normal(0, 0.05, 6), 0.1, None)
ax2.bar(np.arange(6), resp, color=cols, width=0.72)
ax2.set_ylim(0, 1.15)
ax2.set_xlabel('Voxels', color=INK, labelpad=3)
clean(ax2)

post = norm.pdf(x, 0.6, 0.06)
post /= post.max()
ax3.fill_between(x, post, color=BLUE, alpha=0.25, lw=0)
ax3.plot(x, post, color=BLUE, lw=2.6)
ax3.axvline(s_true, color=RED, lw=1.2, ls='--')
ax3.set_xlim(0, 1); ax3.set_ylim(0, 1.15)
ax3.set_xlabel('Decoded stimulus', color=INK, labelpad=3)
clean(ax3)

arrow(fig, 0.335, 0.405, 0.33, 'Encode')
arrow(fig, 0.595, 0.665, 0.33, 'Decode')
fig.savefig(f'{out}/braincoder_brain.png')
plt.close(fig)

# bauer: prior x noisy likelihood -> posterior; hierarchical fit of choices
fig = plt.figure(figsize=(6.8, 2.0))
ax1 = fig.add_axes([0.02, 0.18, 0.34, 0.66])
ax2 = fig.add_axes([0.64, 0.18, 0.34, 0.66])

x = np.linspace(0, 1, 400)
prior = norm.pdf(x, 0.4, 0.14); like = norm.pdf(x, 0.7, 0.1)
postr = prior * like
for y, col in [(prior, GREY), (like, RED), (postr, BLUE)]:
    y = y / y.max()
    ax1.fill_between(x, y, color=col, alpha=0.2, lw=0)
    ax1.plot(x, y, color=col, lw=2.6)
ax1.text(0.17, 0.75, 'Prior', color='0.45', ha='center', fontsize=FS)
ax1.text(0.86, 0.62, 'Likelihood', color=RED, ha='left', fontsize=FS)
ax1.text(0.585, 1.06, 'Posterior', color=BLUE, ha='center', fontsize=FS)
ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.25)
ax1.set_xlabel('Magnitude', color=INK, labelpad=3)
clean(ax1)

# hierarchical psychometric fit: thin per-participant curves, group curve + band, data
xs = np.linspace(-1, 1, 200)
for k in range(7):
    mu, sd = rng.normal(0, 0.12), np.exp(rng.normal(np.log(0.3), 0.25))
    ax2.plot(xs, norm.cdf((xs - mu) / sd), color=BLUE, alpha=0.18, lw=1)
g = norm.cdf(xs / 0.3)
ax2.fill_between(xs, norm.cdf(xs / 0.25), norm.cdf(xs / 0.36), color=BLUE, alpha=0.2, lw=0)
ax2.plot(xs, g, color=BLUE, lw=3)
xd = np.linspace(-0.9, 0.9, 9)
ax2.plot(xd, np.clip(norm.cdf(xd / 0.3) + rng.normal(0, 0.04, 9), 0, 1), 'o', ms=6,
         color='0.15', zorder=5)
ax2.set_xlim(-1, 1); ax2.set_ylim(-0.03, 1.05)
ax2.set_xlabel('Evidence', color=INK, labelpad=3)
clean(ax2)
ax2.spines['left'].set_visible(True); ax2.spines['left'].set_color(INK)
arrow(fig, 0.49, 0.6, 0.48, 'Fit')
fig.savefig(f'{out}/bauer_scheme.png')
print('saved')
