---
title: Sermons by Series
---

# {{ page.title }}

{% assign skipped_tags = "wednesday-evening,sunday-evening,sunday-morning" | split: ','] %}

### Series
{::options parse_block_html="true" /}
<ul>
{% for tag in site.tags %}
  {% assign t = tag | first %}
  {% assign posts = tag | last %}

  {% unless skipped_tags contains t %}
        {% assign tag_name_array = ' ' | split: ',' %}
        {% assign tag_array = t | split: '-' %}
        {% for ta in tag_array %}
            {% assign capit = ta | capitalize %}
            {% tag_name_array = tag_name_array | push: capit %}
        {% endfor %}
        {% assign tag_name = tag_name_array | join: ' ' %}
        <li>
            <a href="#{{t | downcase | replace: ' ', '-'}}">
                {{tag_name}}
            </a>
        </li>
  {% endunless %}

{% endfor %}
</ul>
<hr>
{::options parse_block_html="false" /}


{::options parse_block_html="true" /}
{% for tag in site.tags %}
  {% assign t = tag | first %}
  {% assign posts = tag | last %}

  {% unless skipped_tags contains t %}
    {% assign tag_name_array = ' ' | split: ',' %}
    {% assign tag_array = t | split: '-' %}
    {% for ta in tag_array %}
        {% assign capit = ta | capitalize %}
        {% tag_name_array = tag_name_array | push: capit %}
    {% endfor %}
    {% assign tag_name = tag_name_array | join: ' ' %}
#### {{tag_name}}
<table>
    {% for post in posts %}
        {% if post.tags contains t %}
        <tr>
          <td><a href="{{ post.url }}">{{ post.sermon-title }}</a></td>
          <td>{{ post.preacher }}</td>
          <td>{{ post.date | date: "%F" }}</td>
          <td>{{ post.date | date: "%A" }} {{ post.day-part }}</td>
        </tr>
        {% endif %}
    {% endfor %}
</table>
<hr>
  {% endunless %}

{% endfor %}
{::options parse_block_html="false" /}
