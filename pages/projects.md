---
layout: page
title: Projects
permalink: /projects/
---
<div class="row">
<div class="col-3">
</div>
<div class="col-9 text-align-left">
<p> On this page, you will find some information on former and ongoing
projects:

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


<div id="{{ id }}" class="row">
<div class="col-3">
</div>


<div class="col-9 text-align-left">
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
