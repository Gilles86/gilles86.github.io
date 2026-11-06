---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Gilles de Hollander, PhD
heading: Welcome
---
I am a cognitive neuroscientist in the lab of [Christian Ruff](https://www.econ.uzh.ch/en/people/faculty/ruff.html) at the [Zurich Center for Neuroeconomics
(ZNE)](https://www.zne.uzh.ch/en.html), University of Zurich (UZH).

**I want to understand how the brain represents the world, and how the limits of those
representations shape what we perceive and decide.** Neural populations encode visual
space, numbers and value with limited precision, and much of our behaviour, including
choices that look irrational, follows from how the brain makes the most of these noisy
codes. I measure such codes in individual human brains with ultra-high-field (7T) fMRI
and encoding models, relate them to behaviour with computational models, and test their
role with causal manipulations such as brain stimulation.

{: .findings}
 * **Risk attitudes start in perception.** People whose parietal cortex encodes payoff magnitudes more precisely are less risk averse ([*Nature Human Behaviour*, 2023](https://doi.org/10.1038/s41562-023-01643-4)), disrupting these representations with TMS makes them more risk seeking ([preprint, 2025](https://doi.org/10.1101/2025.01.13.632678)), and noisier payoffs held in memory shift risk attitudes from one choice to the next ([*Nature Communications*, 2026](https://doi.org/10.1038/s41467-026-77402-6)).
 * **Neural codes adapt to context.** Number tuning in parietal cortex shifts and rescales with the range of numbers, and the change in neural precision predicts the change in behavioural precision ([*Nature Communications*, 2026](https://doi.org/10.1038/s41467-026-78851-9)).
 * **Value has a population code too.** Orbitofrontal cortex carries a probabilistic population code for value, and its decoded uncertainty predicts how stable people's preferences are ([preprint, 2026](https://doi.org/10.64898/2026.03.28.715037)).
 * **Vision at the scale of columns and layers.** At 0.7 mm resolution, fMRI separates feedforward input from attentional feedback across the layers of ocular dominance columns ([*NeuroImage*, 2021](https://doi.org/10.1016/j.neuroimage.2020.117683)), and visual cortex represents space in retinotopic coordinates ([*eLife*, 2026](https://doi.org/10.7554/eLife.110134.1)).

Next, I want to find out whether the brain uses one shared architecture for all the
scales it builds, for numbers, time, rank and value, and whether the shape of each neural
scale explains where our judgements are precise and where they are biased.

All of this runs on two open-source Python packages that I wrote and maintain:

{% include software_cards.html %}

### Selected papers

{% include selected_papers.html %}

### Updates

#### 2026

{: .news}
 * **Nov** [Out in *Nature Communications*](https://doi.org/10.1038/s41467-026-78851-9), with [Arthur Prat-Carrabin](https://arthurprat.com) and [Sam Gershman](https://gershmanlab.com): numerical receptive fields in parietal cortex shift and rescale to the range of numbers. Explore them in our [3D brain viewers](https://ruffgroup.github.io/neural_priors_viewers/).
 * **Nov** [Interactive 3D brain maps](/odc_viewer/) of ocular dominance columns from our 2021 *NeuroImage* paper, on each participant's own cortical surface.
 * **Oct** [New preprint](https://doi.org/10.64898/2026.10.08.757623) led by Maike Renkert, with Karin Kucian and Sofie Valk: dyscalculia reflects less precise numerical representations in parietal cortex and an altered allocation of this cortex to functional networks.
 * **Sep** [Out in *Nature Communications*](https://doi.org/10.1038/s41467-026-77402-6): rapid changes in risk attitudes originate from Bayesian inference on noisy parietal magnitude representations.
 * **Jun** [New preprint](https://doi.org/10.64898/2026.06.08.730978): separable efficient codes shape both perception and value along the pathway from sensation to action.
 * **Jun** Our cognitive-modelling package [bauer](https://ruffgroup.github.io/bauer/) now supports DDM and race-diffusion likelihoods.
 * **Apr** [New preprint](https://doi.org/10.64898/2026.03.28.715037): the OFC/vmPFC implements a probabilistic population code for value.

<details class="news-past" markdown="1">
<summary>2025</summary>

{: .news}
 * **Nov** [New preprint](https://www.biorxiv.org/content/10.1101/2025.11.03.685504v1) on the effect of stress on risky decision-making and numerical representations.
 * **Sep** [Material](https://github.com/Gilles86/computation-in-neuroeconomics-workshop2025/) from my workshop on Computational Methods for Neuroeconomics in Soglio, Switzerland.

</details>

### Explore in 3D

{% include demos.html %}
