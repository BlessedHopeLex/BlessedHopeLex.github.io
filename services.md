---
title: Past Services
---

# Past Services

<ul>
  {% for post in site.categories.service %}
    {% if post.url %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>