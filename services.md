---
title: Past Services
---

# Past Services

<!-- <ul> -->
<table>
  {% assign sorted = site.services | sort: 'date' | reverse %}
  {% for post in sorted %}
    {% if post.url %}
        <!-- <li> -->
        <tr>
          <td><a href="{{ post.url }}">{{ post.sermon-title }}</a></td>
          <td>{{ post.date | date: "%a, %F" }}</td>
          <td>{{ post.day-part }}</td>
        </tr>
        <!-- </li> -->
    {% endif %}
  {% endfor %}
</table>
<!-- </ul> -->