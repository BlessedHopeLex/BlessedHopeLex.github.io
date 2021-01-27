---
title: Past Services
---

# Past Services

<ul>
  {% assign sorted = site.services | sort: 'date' | reverse %}
  {% for post in sorted %}
    {% if post.url %}
        <li><a href="{{ post.url }}">{{ post.sermon-title }}</a> - {{ post.date | date: "%a, %F" }}, {{ post.day-part }}</li>
    {% endif %}
  {% endfor %}
</ul>