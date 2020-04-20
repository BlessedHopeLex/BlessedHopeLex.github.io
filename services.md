---
title: Past Services
---

# Past Services

<ul>
  {% for post in site.services %}
    {% if post.url %}
        <li><a href="{{ post.url }}">{{ post.sermon-title }} - {{ post.date }}</a></li>
    {% endif %}
  {% endfor %}
</ul>