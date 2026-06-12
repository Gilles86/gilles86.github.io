---
layout: page
title: Software
permalink: /software/
---

<div class="row">
<div class="col-3">
</div>
<div class="col-9 text-align-left">
<p>I build and maintain open-source Python tools for computational and cognitive
neuroscience. Two of them sit at the heart of most of my research: <strong>braincoder</strong>,
for neural encoding and decoding models, and <strong>bauer</strong>, for Bayesian
cognitive models of choice.</p>
</div>
</div>

<div class="card mt-4" style="width: 40rem;">
<div class="card-header">
<h4 class="card-title"><a class="link-dark text-decoration-none" href="https://braincoder-devs.github.io/">braincoder</a></h4>
</div>
<div class="card-body">

{% capture braincoder %}
**braincoder** fits *encoding models* to neural data (for now, fMRI) and then
*inverts* those models to decode stimulus information back out of the brain.
By inverting an encoding model, we can track — from moment to moment — exactly
which information the brain has access to, and with how much uncertainty.

It wraps stimulus handling, model definition, HRF convolution, and optimization
into a single [Keras 3](https://keras.io)-based toolkit. You can pick a ready-made
model (Gaussian population receptive field, HRF-aware, linear) or subclass your own,
and run the same code on **TensorFlow, JAX, or PyTorch**. It powers the
encoding-model work across my numerical-cognition and value projects.

- Source: [github.com/Gilles86/braincoder](https://github.com/Gilles86/braincoder)
- Documentation & tutorials: [braincoder-devs.github.io](https://braincoder-devs.github.io/)
{% endcapture %}

{{ braincoder | markdownify }}

</div>
</div>

<div class="card mt-4" style="width: 40rem;">
<div class="card-header">
<h4 class="card-title"><a class="link-dark text-decoration-none" href="https://bauer.readthedocs.io/en/latest/">bauer</a></h4>
</div>
<div class="card-body">

{% capture bauer %}
**bauer** — *Bayesian Estimation of Perceptual, Numerical and Risky choice* — is a
[PyMC](https://www.pymc.io/)-based library for fitting hierarchical Bayesian cognitive
models to behavioural decision-making data. It covers three task families —
**psychometric**, **magnitude comparison**, and **risky choice** — built on a shared
Bayesian-observer front-end, with each participant getting their own parameters,
regularised by a group-level distribution.

A central idea in my work is that the brain spends its costly representational
capacity only where it is most needed. bauer lets me formalise that idea as a
generative model and fit it directly to choices, so that quantities like
**numerical acuity** or **noise-driven risk aversion** become estimable parameters
rather than informal descriptions.

- Source: [github.com/ruffgroup/bauer](https://github.com/ruffgroup/bauer/tree/main)
- Documentation & tutorials: [bauer.readthedocs.io](https://bauer.readthedocs.io/en/latest/)
{% endcapture %}

{{ bauer | markdownify }}

</div>
</div>

<div class="card mt-4" style="width: 40rem;">
<div class="card-header">
<h4 class="card-title">Other packages I maintain</h4>
</div>
<div class="card-body">
<ul>
<li><a href="https://nideconv.readthedocs.io/en/latest/">nideconv</a> — deconvolve (neural) time series</li>
<li><a href="https://pymp2rage.readthedocs.io/en/latest/">pymp2rage</a> — compute T1 maps and T1UNI images for the MP2RAGE sequence</li>
</ul>
<p class="card-text text-muted"><small>I also contribute to
<a class="text-muted" href="https://bids.neuroimaging.io/">BIDS</a>,
<a class="text-muted" href="https://nilearn.github.io/stable/index.html">nilearn</a>,
<a class="text-muted" href="https://gallantlab.github.io/pycortex/">pycortex</a>,
<a class="text-muted" href="https://www.nipreps.org/niworkflows/master/index.html">niworkflows</a>, and
<a class="text-muted" href="https://nipype.readthedocs.io/en/latest/">nipype</a>.</small></p>
</div>
</div>
