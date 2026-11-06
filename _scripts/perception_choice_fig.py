"""Project figure: from parietal number fields to risk aversion (website, ~6.5 in wide)."""
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from scipy.stats import norm

brain_png, out = sys.argv[1], sys.argv[2]

mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Helvetica Neue', 'TeX Gyre Heros', 'Arial'],
    'font.size': 8.5, 'axes.labelsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.linewidth': 0.8, 'axes.spines.top': False, 'axes.spines.right': False,
    'xtick.direction': 'out', 'ytick.direction': 'out',
    'xtick.major.size': 3, 'ytick.major.size': 3,
    'xtick.major.width': 0.8, 'ytick.major.width': 0.8,
    'lines.linewidth': 1.6, 'savefig.dpi': 220, 'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
})

PRECISE, NOISY = '#3B5BA5', '#C44E52'
cmap = mpl.colormaps['jet']

fig = plt.figure(figsize=(6.5, 4.7))
gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1], height_ratios=[1, 1],
                      hspace=0.55, wspace=0.5)

def letter(ax, s, x=-0.13, y=1.06):
    ax.text(x, y, s, transform=ax.transAxes, fontsize=10, fontweight='bold',
            va='bottom', ha='right')

# a: number fields on the cortical surface
ax = fig.add_subplot(gs[0, 0])
im = np.asarray(Image.open(brain_png).convert('RGB'))
left, right = im[17:335, 0:465], im[17:335, 497:960]
gap = np.full((left.shape[0], 14, 3), 255, np.uint8)
ax.imshow(np.concatenate([left, gap, right], axis=1))
ax.set_axis_off()
ax.text(0.25, -0.05, 'Left', transform=ax.transAxes, ha='center', va='top')
ax.text(0.76, -0.05, 'Right', transform=ax.transAxes, ha='center', va='top')
cax = ax.inset_axes([0.22, -0.30, 0.56, 0.06])
cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=mpl.colors.Normalize(4, 12),
                               orientation='horizontal', ticks=[4, 8, 12])
cb.outline.set_visible(False)
cax.tick_params(length=2, labelsize=7.5)
cax.set_xlabel('Preferred numerosity', fontsize=8, labelpad=2)
letter(ax, 'a', x=0.0, y=1.02)

# b: tuning on a log scale
ax = fig.add_subplot(gs[0, 1])
x = np.geomspace(1, 40, 400)
prefs = np.geomspace(2.5, 20, 6)
for i, pref in enumerate(prefs):
    resp = np.exp(-0.5 * ((np.log(x) - np.log(pref)) / 0.35) ** 2)
    ax.plot(x, resp, color=cmap(0.05 + 0.9 * i / (len(prefs) - 1)), lw=1.4)
ax.set_xscale('log')
ax.set_xticks([1, 5, 10, 20, 40])
ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda v, _: f'{v:g}'))
ax.xaxis.set_minor_locator(mpl.ticker.NullLocator())
ax.set_yticks([0, 1])
ax.set_xlabel('Number of items')
ax.set_ylabel('Response')
ax.text(0.98, 1.0, 'Tuned on a log scale', transform=ax.transAxes,
        ha='right', va='bottom', fontsize=8, color='0.3')
sns.despine(ax=ax, offset=4, trim=True)
letter(ax, 'b')

# Model: log payoff + Gaussian noise, Gaussian prior on log payoff
mu, sig_p = np.log(12), 0.6
def beta(nu):
    return sig_p ** 2 / (sig_p ** 2 + nu ** 2)

# c: perceived vs true payoff
ax = fig.add_subplot(gs[1, 0])
xs = np.linspace(2, 40, 300)
ax.plot([2, 40], [2, 40], color='0.75', lw=0.8, ls='--', zorder=0)
ax.text(31, 37.5, 'Veridical', color='0.5', fontsize=8, rotation=38,
        ha='center', va='center')
for nu, col, lab in [(0.25, PRECISE, 'Precise'), (0.55, NOISY, 'Noisy')]:
    b = beta(nu)
    med = np.exp(b * np.log(xs) + (1 - b) * mu)
    ax.plot(xs, med, color=col)
    ax.text(41, med[-1], lab, color=col, fontsize=8.5, ha='left', va='center')
ax.set_xticks([2, 10, 20, 30, 40])
ax.set_yticks([2, 10, 20, 30, 40])
ax.set_xlim(2, 40); ax.set_ylim(2, 40)
ax.set_xlabel('Payoff (CHF)')
ax.set_ylabel('Perceived payoff (CHF)')
ax.annotate('Large payoffs\nlook smaller', xy=(36, np.exp(beta(.55) * np.log(36) + (1 - beta(.55)) * mu)),
            xytext=(27, 9), fontsize=8, ha='center', va='center',
            arrowprops=dict(arrowstyle='-|>', connectionstyle='angle3,angleA=0,angleB=90',
                            color='0.2', lw=1.0, mutation_scale=8, shrinkA=3, shrinkB=6,
                            relpos=(1.0, 0.5)))
sns.despine(ax=ax, offset=4, trim=True)
letter(ax, 'c', x=-0.2)

# d: choice between a sure and a risky payoff
ax = fig.add_subplot(gs[1, 1])
p = 0.55
ratio = np.geomspace(1, 6, 300)
ax.axvline(1 / p, color='0.75', lw=0.8, ls='--', zorder=0)
ax.text(1 / p * 0.97, 1.02, 'Risk neutral', color='0.5', fontsize=8, ha='right', va='bottom')
for nu, col in [(0.25, PRECISE), (0.55, NOISY)]:
    b = beta(nu)
    pr = norm.cdf((b * np.log(ratio) + np.log(p)) / (b * np.sqrt(2) * nu))
    ax.plot(ratio, pr, color=col)
ax.set_xscale('log')
ax.set_xticks([1, 2, 4, 6])
ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda v, _: f'{v:g}'))
ax.xaxis.set_minor_locator(mpl.ticker.NullLocator())
ax.set_yticks([0, 0.5, 1])
ax.set_ylim(0, 1)
ax.set_xlabel('Risky / sure payoff (55% chance)')
ax.set_ylabel('P(choose risky)')
b = beta(0.55)
xi = p ** (-1 / b)
ax.text(1.04, 0.72, 'Precise', color=PRECISE, fontsize=8.5, ha='left', va='center')
ax.text(5.0, 0.5, 'Noisy', color=NOISY, fontsize=8.5, ha='center', va='center')
ax.annotate('Risk averse:\nneeds a premium', xy=(xi, 0.5), xytext=(3.3, 0.2),
            fontsize=8, ha='left', va='center', color='0.15',
            arrowprops=dict(arrowstyle='-|>', connectionstyle='angle3,angleA=180,angleB=-60',
                            color='0.2', lw=1.0, mutation_scale=8, shrinkA=3, shrinkB=5,
                            relpos=(0.0, 0.5)))
sns.despine(ax=ax, offset=4, trim=True)
letter(ax, 'd')

fig.savefig(out)
print('saved', out)
