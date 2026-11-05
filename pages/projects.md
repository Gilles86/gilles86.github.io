---
layout: page
title: Projects
permalink: /projects/
---
<div class="row">
<div class="col-md-3 d-none d-md-block">
</div>
<div class="col-12 col-md-9 text-align-left">
<p>I work in the lab of <a href="https://www.econ.uzh.ch/en/people/faculty/ruff.html">Christian Ruff</a>
at the <a href="https://www.zne.uzh.ch/en.html">Zurich Center for Neuroeconomics</a>, where most of my
current projects are based. On this page, you will find some information on ongoing and former projects:

<h5>Ongoing</h5>
<ul>
{% assign projects = site.projects | where:"status","ongoing" | sort:'order' %}
{% for project in projects %}
{% assign id = project.id | split:'/' | last %}
<li><a href="#{{ id }}">{{ project.title }}</a></li>
{% endfor %}
</ul>

<h5>Past</h5>
<ul>
{% assign projects = site.projects | where:"status","past" | sort:'order' %}
{% for project in projects %}
{% assign id = project.id | split:'/' | last %}
<li><a href="#{{ id }}">{{ project.title }}</a></li>
{% endfor %}
</ul>

</p>
</div>
</div>

{% assign projects = site.projects | sort:'order' %}
{% for project in projects %}
{% assign id = project.id | split:"/" | last %}


<div id="{{ id }}" class="row">
<div class="col-md-3 d-none d-md-block">
</div>


<div class="col-12 col-md-9 text-align-left">
<h3 class="mb-2 mt-3 text-dark"><u>{{ project.title }}</u></h3>
<p class="text-muted mb-1"><small><strong>Collaborators:</strong>
{% for collaborator_ in project.collaborators %}
{% if forloop.last %}
{% capture collaborator %}{{ collaborator_ }}{% endcapture %}
{% else %}
{% capture collaborator %}{{ collaborator_ }}, {% endcapture %}
{% endif %}
{{ collaborator  }}
{% endfor %}
</small></p>

<p class="text-justify">
{{ project.content }}
</p>

</div>
</div>
{% endfor %}
