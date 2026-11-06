---
layout: post
title: "How perception shapes economic choice"
collaborators: [Miguel Barretto-García, Marius Moisa, Maike F. Renkert, Arthur Prat-Carrabin, Saurabh Bedi, Marcus Grueschow, Rafael Polanía, Michael Woodford, Franciszek Hennel, Samuel J. Gershman, Christian C. Ruff]
status: ongoing
order: 1
---

This is the core line of my work in the lab of Christian Ruff. When choosing between a safer and a riskier option, people tend to prefer the
safer one, even when the riskier option pays more on average. Classical economic
theories like
[expected utility](https://en.wikipedia.org/wiki/Expected_utility_hypothesis)
and [prospect theory](https://en.wikipedia.org/wiki/Prospect_theory) explain this
through *valuation*: people do not *like* risk.

We explore a complementary hypothesis: that risk aversion is (also) rooted in
*perception*. In many domains, such as numerosity, loudness, weight and brightness,
people tend to underestimate large magnitudes. So why would this be different for
money? This idea is formalized in a theoretical framework developed by
[Khaw, Li and Woodford](https://www.nber.org/papers/w24978).

{% capture description %}
<strong>(a)</strong> <em>Numerical receptive field models</em> show that patches of
parietal cortex prefer specific numbers, laid out as maps.
<strong>(b)</strong> These populations are tuned on a logarithmic scale.
<strong>(c)</strong> A noisy log code plus prior knowledge makes large payoffs look
smaller than they are, more so when the code is noisier.
<strong>(d)</strong> As a result, people need a larger premium before they take a gamble:
risk aversion without any dislike of risk. Panels b–d are model illustrations.
{% endcapture %}

{% include image.html url="/assets/imgs/projects/numerosity_risk/perception_choice.png"
description=description width="100" %}

We use these *numerical population receptive field models*, which build on
[seminal work](https://www.science.org/doi/full/10.1126/science.1239052) by Ben
Harvey and Serge Dumoulin, to link choices to the way parietal cortex represents
magnitude. So far, we have shown that:

 * **Noisier representations go with more risk aversion.** People with noisier numerical representations in parietal cortex are more risk-averse ([Barretto-García\*, de Hollander\* et al., 2023, *Nature Human Behaviour*](https://doi.org/10.1038/s41562-023-01643-4)).
 * **Risk attitudes change from moment to moment.** Payoffs held in working memory are noisier and pulled towards prior beliefs, which can shift people between risk aversion and risk seeking ([de Hollander et al., 2026, *Nature Communications*](https://doi.org/10.1038/s41467-026-77402-6)).
 * **The link is causal.** Combining TMS with fMRI, we found that disrupting parietal cortex weakens numerical tuning and increases risk seeking ([de Hollander\*, Moisa\* & Ruff, 2025, preprint](https://doi.org/10.1101/2025.01.13.632678)).
 * **Stress acts on perception.** Acute stress reduces risk aversion by changing how payoff magnitudes are perceived, rather than how they are valued ([Renkert\*, de Hollander\* et al., 2025, preprint](https://doi.org/10.1101/2025.11.03.685504)).
 * **Number codes adapt to context.** Numerical receptive fields shift and rescale with the range of relevant numbers, a form of efficient coding on the fly ([Prat-Carrabin\*, de Hollander\* et al., 2026, *Nature Communications*](https://doi.org/10.1038/s41467-026-78851-9)). You can explore them in our [3D brain viewers](https://ruffgroup.github.io/neural_priors_viewers/).
 * **Number codes differ in dyscalculia.** Dyscalculia reflects less precise numerical representations in parietal cortex and an altered allocation of this cortex to functional networks ([Renkert et al., 2026, preprint](https://doi.org/10.64898/2026.10.08.757623)).

We are now extending this work to new questions, such as how parietal cortex
handles several numbers at once.
