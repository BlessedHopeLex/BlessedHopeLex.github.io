---
title: Past Services
---

# Past Services

{::options parse_block_html="true" /}
<a class="btn btn-primary" href="/services-speaker">Sermons by Speaker</a>
{: .m-0}
{::options parse_block_html="false" /}

<!-- <ul> -->
<table>
  {% assign sorted_day = site.services | sort: 'day-part' | reverse %}
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
<!-- </ul> -->