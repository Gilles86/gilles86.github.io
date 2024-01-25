---
layout: post
title: "The neural substrates of attention"
collaborators: [Marco Aqil, Martin Szinte, Tomas Knapen]
status: ongoing
order: 2
---

Humans can actively process much less information than what they have in
principle access to. Imagine crossing a busy street: you probably
sequentially observe different aspects of the traffic situation before
you commit to crossing the street. This moving ''spotlight'' is a
form of *selective attention*.

What are the neural substrates of such attentional processes? Work
in non-human primates has revealed that neural representations of the outside
world are heavily influenced by attention. For example, if you attend
a certain object, neural representations of that object are ''boosted'',
in particular when other objects are potentially also represented by
that neuron.

{% capture description %}
By inverting <em>population receptive field models</em>, we can calculate the
position of a stimulus given corresponding neural signals in the
visual system. Moreover, we can also quantify the certainty we have about this
position and thereby, possibly, the reliability of the underlying neural signals.
{% endcapture %}

{% include image.html url="/assets/imgs/projects/attention/xy.png"
description=description  width="75" %}

In this project, we first fit *population receptive field models* to see
what part of the brain is representing what part of the visual field.
Then, we *invert* those models to see ''what the brain is representing''
during a task and how these representations change as a function
of attention. Moreover, because we use a Bayesian inversion scheme,
we can also probe the fidelity with which stimuli are represented
as a function of, for example, attention or retinotopic location.

We implemented these models in the `braincoder` package. You can find more information about this package [here](https://braincoder-devs.github.io/).
