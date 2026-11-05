---
layout: post
title: "Attention and visual receptive fields"
collaborators: [Marco Aqil, Martin Szinte, Serge Dumoulin, Tomas Knapen, Dock Duncan, Jan Theeuwes]
status: ongoing
order: 3
---

Humans can actively process much less information than they have access to.
Imagine crossing a busy street: you probably observe different aspects of the
traffic one after the other before you commit to crossing. This moving
''spotlight'' is a form of *selective attention*. But how does it change the way
the brain represents the world?

{% capture description %}
By inverting <em>population receptive field models</em>, we can calculate the
position of a stimulus given corresponding neural signals in the
visual system. Moreover, we can also quantify the certainty we have about this
position and thereby, possibly, the reliability of the underlying neural signals.
{% endcapture %}

{% include image.html url="/assets/imgs/projects/attention/xy.png"
description=description  width="75" %}

We first fit *population receptive field models* to see what part of the brain
represents what part of the visual field. Then, we *invert* those models to see
''what the brain is representing'' during a task, and with how much uncertainty.
These methods are implemented in our
[braincoder](https://braincoder-devs.github.io/) package.

 * **Vision stays retinotopic.** Receptive fields shift with gaze, so space is represented in a retinotopic reference frame throughout human visual cortex ([Szinte\*, de Hollander\*, Aqil\* et al., 2026, *eLife* reviewed preprint](https://doi.org/10.7554/eLife.110134.1)).
 * **Psilocybin changes visual context effects.** Psilocybin alters contextual perception in the Ebbinghaus illusion, as well as contextual modulation in cortical responses ([Aqil, de Hollander et al., 2025, *Nature Communications*](https://doi.org/10.1038/s41467-025-65150-y)).

Together with Dock Duncan and Jan Theeuwes at VU Amsterdam, we are now studying how
reward and past experience reshape visual receptive fields.
