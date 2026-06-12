---
layout: page
title: Software
permalink: /software/
---

<p class="lead">I build and maintain open-source Python tools for computational and
cognitive neuroscience. Two of them sit at the heart of most of my research:
<strong>braincoder</strong>, for neural encoding and decoding models, and
<strong>bauer</strong>, for Bayesian cognitive models of choice.</p>

<div class="card mb-4 shadow-sm">
  <div class="row g-0 align-items-center">
    <div class="col-md-5">
      <img src="{{ '/assets/imgs/software/braincoder.png' | relative_url }}" class="img-fluid rounded-start p-3" alt="Two Gaussian population receptive field tuning curves over a stimulus feature axis">
    </div>
    <div class="col-md-7">
      <div class="card-body">
        <h4 class="card-title"><a class="link-dark text-decoration-none" href="https://braincoder-devs.github.io/">braincoder</a></h4>
        <p class="card-text">braincoder fits <em>encoding models</em> to neural data (for now, fMRI)
        and then <em>inverts</em> those models to decode stimulus information back out of the
        brain. By inverting an encoding model, we can track, from moment to moment, which
        information the brain has access to and with how much uncertainty.</p>
        <p class="card-text">It wraps stimulus handling, model definition, HRF convolution,
        and optimization into a single <a href="https://keras.io">Keras 3</a>-based toolkit.
        You can pick a ready-made model (Gaussian population receptive field, HRF-aware,
        linear) or write your own, and run the same code on TensorFlow, JAX, or PyTorch.
        It powers the encoding-model work across my numerical-cognition and value projects.</p>
        <p class="card-text"><small class="text-muted">
          <a class="text-muted" href="https://github.com/Gilles86/braincoder">Source</a> &middot;
          <a class="text-muted" href="https://braincoder-devs.github.io/">Documentation &amp; tutorials</a>
        </small></p>
      </div>
    </div>
  </div>
</div>

<div class="card mb-4 shadow-sm">
  <div class="row g-0 align-items-center">
    <div class="col-md-5">
      <img src="{{ '/assets/imgs/software/bauer.png' | relative_url }}" class="img-fluid rounded-start p-3" alt="Drift-diffusion model fit: psychometric choice curve and reaction times by difficulty">
    </div>
    <div class="col-md-7">
      <div class="card-body">
        <h4 class="card-title"><a class="link-dark text-decoration-none" href="https://bauer.readthedocs.io/en/latest/">bauer</a></h4>
        <p class="card-text">bauer (Bayesian Estimation of Perceptual, Numerical and Risky
        choice) is a <a href="https://www.pymc.io/">PyMC</a>-based library for fitting
        hierarchical Bayesian cognitive models to behavioural decision-making data. It covers
        three task families (psychometric, magnitude comparison, and risky choice), built on a
        shared Bayesian-observer front-end, with each participant getting their own parameters
        regularised by a group-level distribution.</p>
        <p class="card-text">bauer now reaches beyond modelling choices alone. On top of the
        same cognitive front-end it offers <em>sequential-sampling</em> likelihoods, the
        drift-diffusion model (DDM) and the race-diffusion model (RDM), so a model is informed
        by reaction times as well as the choices people make. A single model can then speak to
        both what people choose and how long they take to decide, helping to separate, for
        example, perceptual acuity from response caution.</p>
        <p class="card-text"><small class="text-muted">
          <a class="text-muted" href="https://github.com/ruffgroup/bauer/tree/main">Source</a> &middot;
          <a class="text-muted" href="https://bauer.readthedocs.io/en/latest/">Documentation &amp; tutorials</a>
        </small></p>
      </div>
    </div>
  </div>
</div>

<div class="card mb-4 shadow-sm">
  <div class="card-body">
    <h4 class="card-title">Other packages I maintain</h4>
    <ul class="mb-2">
      <li><a href="https://nideconv.readthedocs.io/en/latest/">nideconv</a>: deconvolve (neural) time series</li>
      <li><a href="https://pymp2rage.readthedocs.io/en/latest/">pymp2rage</a>: compute T1 maps and T1UNI images for the MP2RAGE sequence</li>
    </ul>
    <p class="card-text text-muted"><small>I also contribute to
    <a class="text-muted" href="https://bids.neuroimaging.io/">BIDS</a>,
    <a class="text-muted" href="https://nilearn.github.io/stable/index.html">nilearn</a>,
    <a class="text-muted" href="https://gallantlab.github.io/pycortex/">pycortex</a>,
    <a class="text-muted" href="https://www.nipreps.org/niworkflows/master/index.html">niworkflows</a>, and
    <a class="text-muted" href="https://nipype.readthedocs.io/en/latest/">nipype</a>.</small></p>
  </div>
</div>
