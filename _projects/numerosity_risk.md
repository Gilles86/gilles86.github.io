---
layout: post
title: "Parietal numerosity representations and risky decision-making"
collaborators: [Miguel Barretto Garcia, Marcus Grueschow, Rafael Polania, Michael Woodford, Franciszek Hennel, Arthur Prat-Carrabin, Saurabh Bedi, Samuel J. Gershman, Christian C Ruff]
status: ongoing
order: 1
---

In this project, we aim to better understand the *perceptual foundations*
of risky decision-making. When choosing between safer and riskier options,
human subjects tend to choose safer options –even when the expected
(average) payoff of such options is lower. Why do subjects choose like this?
Classical economic theories like
[expected utility](https://en.wikipedia.org/wiki/Expected_utility_hypothesis)
and [prospect theory](https://en.wikipedia.org/wiki/Prospect_theory) suggest
this has to do with *valuation*: subjects don't *like* the riskier options.

We explore a complementary hypothesis: that risk aversion is (also) rooted
in *perception*: subject do not completely ''grasp'' the larger payoffs magnitude of
riskier options, because their perception is *noisy* and *biased*.
In many domains such as numerosity, loudness, weight, and brightness,
people tend to underestimate large magnitudes. So why would this be different
for monetary magnitudes?
This notion is formalized in a theoretical Framework developed by
[Khaw, Li and Woodford](https://www.nber.org/papers/w24978).

{% capture description %}
<em>Numerical receptive field models</em> measure to which numbers different
patches of cortex are most responsive. It turns out that neurons in parietal
cortex are sensitive to different numbers (<em>number parietal cortex, NPC</em>).
Hence, they are a good target reason
when one is interested in the neural representations that humans are using
during economic decisions.
{% endcapture %}

{% include image.html url="/assets/imgs/projects/numerosity_risk/numberfields.png"
description=description width="75" %}

We built upon their work by using *numerical encoding models* that describe
how neural activity in parietal cortex, as measured using fMRI, represents
the numerosity of currently attended stimuli. These models are called
*numerical population receptive field models* and built upon
[seminal work](https://www.science.org/doi/full/10.1126/science.1239052)
by Ben Harvey and Serge Dumoulin at Utrecht University.

Using such numerical encoding models, we showed that *subjects that have
particularly noisy numerical representations in parietal cortex*, are also
*particularly risk-averse*. This aligns with theoretical
predictions of the model of Khaw et al.: the more noisy an individual's
perception is, the more he/she will revert to her priors/biases.

Using 7T fMRI, we then showed that risk attitudes are not a fixed trait:
they shift rapidly across contexts and repetitions of the same decision,
because people rely more on their prior beliefs about payoffs when parietal
magnitude representations are noisy
([de Hollander et al., 2026, *Nature Communications*](https://doi.org/10.1038/s41467-026-77402-6)).

Together with Arthur Prat-Carrabin and Sam Gershman, we also showed that these
numerical representations are not static either: numerical receptive fields in
parietal cortex shift and rescale when the range of relevant numbers changes,
implementing efficient coding on the fly
(Prat-Carrabin\*, de Hollander\* et al., accepted in *Nature Communications*; [preprint](https://doi.org/10.1101/2025.09.25.675916)).
