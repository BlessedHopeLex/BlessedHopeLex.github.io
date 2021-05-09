---
title: Past Services
---

# Past Services

<!-- <ul> -->
<table>
  {% assign sorted_date = site.services | sort: 'date' | reverse %}
  {% assign sorted = sorted_date | sort: 'day-part' | reverse %}
  {% for post in sorted %}
    {% if post.url %}
        <!-- <li> -->
        <tr>
          <td><a href="{{ post.url }}">{{ post.sermon-title }}</a></td>
          <!-- <td>{{ post.preacher }}</td> -->
          <td>{{ post.date | date: "%F" }}</td>
          <td>{{ post.date | date: "%A" }} {{ post.day-part }}</td>
        </tr>
        <!-- </li> -->
    {% endif %}
  {% endfor %}
</table>
<!-- </ul> -->