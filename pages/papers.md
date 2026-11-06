---
layout: page
permalink: /publications/
title: Publications
---

{% assign preprints = site.publications | where_exp:"pub", "pub.preprint" | sort: "date" | reverse %}
<!-- Preprints -->
<div class="row">
<div class="col-md-3 d-none d-md-block">
</div>
<div class="col-12 col-md-9 text-align-left">
<h3 class="mb-2 mt-3">Preprints</h3>
</div>
</div>
{% for paper in preprints %}
{% include paper.html paper=paper %}
{% if forloop.last == false %}
---
{% endif %}
{% endfor %}

<!-- Papers -->
{% assign grouped = site.publications | where_exp:"pub", "pub.preprint == false" | group_by_exp:"post", "post.date | date: '%Y'" %}
{% for year in grouped reversed %}
<div class="row">
  <div class="col-md-3 d-none d-md-block">
  </div>
  <div class="col-12 col-md-9 text-align-left">
  <h3 class="mb-2 mt-3">{{ year.name }}</h3>
  </div>
</div>

{% for paper in year.items %}
{% include paper.html paper=paper %}

{% if forloop.last == false %}
---
{% endif %}
{% endfor %}
{% endfor %}
