---
layout: page
permalink: /publications/
title: Publications
description: our publications
---

{% assign preprints = site.publications | where_exp:"pub", "pub.preprint" %}
<!-- {{ site.static_files | jsonify}} -->
<!-- Preprints -->
<div class="row">
<div class="col-3">
</div>
<div class="col-9 text-align-left">
<h3 class="mb-2 mt-3"><u>Preprints</u></h3>
</div>
</div>
{% for paper in preprints %}
{% include paper.html paper=paper %}
{% endfor %}

<!-- Papers -->
{% assign grouped = site.publications | where_exp:"pub", "pub.preprint == false" | group_by_exp:"post", "post.date | date: '%Y'" %}
{% for year in grouped reversed %}
<div class="row">
  <div class="col-3">
  </div>
  <div class="col-9 text-align-left">
  <h3 class="mb-2 mt-3"><u>{{ year.name }}</u></h3>
  </div>
</div>

  {% for paper in year.items %}
  {% include paper.html paper=paper %}
  {% endfor %}
  {% endfor %}
