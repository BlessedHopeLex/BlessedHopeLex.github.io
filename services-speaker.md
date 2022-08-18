---
title: Sermons by Speaker
---

# Sermons by Speaker

{% assign grouped_speaker = site.services | group_by:"preacher" %}
{% assign sorted_speaker = grouped_speaker | sort: 'name' %}

### Speakers
{::options parse_block_html="true" /}
<ul>
{% for group in sorted_speaker %}
    <li><a href="#{{group.name | downcase | replace: ' ', '-'}}">{{group.name}}</a></li>
{% endfor %}
</ul>
<hr>
{::options parse_block_html="false" /}


{% for group in sorted_speaker %}
##### {{ group.name }}
<table>
  {% assign sorted_day = group.items | sort: 'day-part' | reverse %}
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
<hr>
{% endfor %}
