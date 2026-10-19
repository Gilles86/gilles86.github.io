---
layout: columnar
title: Ocular dominance columns in 3D
permalink: /odc_viewer/
---
These interactive viewers show ocular dominance columns in human primary visual
cortex, measured with 7T fMRI at 0.7 mm isotropic resolution. Each viewer shows a
participant's left > right eye z-map on their own inflated cortical surface. The
V1/V2 borders were drawn by hand on population receptive field (PRF) polar-angle maps.

The data come from [de Hollander, van der Zwaag, Qian, Zhang & Knapen (2021), *NeuroImage*](https://doi.org/10.1016/j.neuroimage.2020.117683).
The full dataset is on OpenNeuro: [ds002295](https://openneuro.org/datasets/ds002295).

<div class="row my-4">
  {% assign viewers = "S1:sub-06,S2:sub-01,S3:sub-07" | split: "," %}
  {% for v in viewers %}
  {% assign parts = v | split: ":" %}
  <div class="col-sm-4 mb-3">
    <a href="/odc_viewer/{{ parts[1] }}/index.html" class="text-decoration-none link-dark">
      <div class="card h-100 text-center">
        <div class="card-body">
          <h3 class="card-title mb-1">{{ parts[0] }}</h3>
          <p class="card-text text-muted mb-0"><small>OpenNeuro {{ parts[1] }}</small></p>
        </div>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

S1–S3 are the three participants shown in Fig. 2E of the paper. Each viewer
downloads about 16–18 MB, so it can take a few seconds to load.

#### How to use the viewers

- **Surface.** The slider at the bottom morphs the surface from fiducial (folded) to
  inflated to flat.
- **Hemispheres.** In the menu (top right) you can hide one hemisphere, so you can
  see the medial surface of the other.
- **Colour scale.** z runs from −3.5 (blue, right eye) to +3.5 (orange/red, left eye).
- **Datasets.** The data buttons switch between `zmap_fig2E` (the colour map of
  Fig. 2E) and `zmap_plain`.
