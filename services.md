---
title: Past Services
---

# Past Services

<ul>
  {% for post in site.services %}
    {% if post.url %}
        <li>{{ post.date | date: "%a, %b %-d, %Y" }}, {{ post.day-part }} - <a href="{{ post.url }}">{{ post.sermon-title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>