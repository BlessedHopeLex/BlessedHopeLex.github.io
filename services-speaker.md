---
title: Sermons by Speaker
---

# Sermons by Speaker

{% assign grouped_speaker = site.services | group_by:"preacher" %}
{% for speaker in grouped_speaker %}
##### {% speaker.name %}
<table>
  {% assign sorted_day = grouped_speaker.items | sort: 'day-part' | reverse %}
  {% assign sorted = sorted_day | sort: 'date' | reverse %}
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
{% endfor %}
