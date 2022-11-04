---
title: Sermons by Series
---

{% assign rawtags = "" %}
{% for post in site.services %}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% assign site.tags = "" %}
{% assign tags = "" %}
{% for tag in rawtags %}
  {% if tag != "" %}
    {% if tags == "" %}
      {% assign tags = tag | split:'|' %}
    {% endif %}
    {% unless tags contains tag %}
      {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% assign site.tags = tags %}


# {{ page.title }}

{% assign skipped_tags = "wednesday-evening,sunday-evening,sunday-morning" | split: ','] %}

### Series
{::options parse_block_html="true" /}
<ul>
{% for tag in tags %}
  {% unless skipped_tags contains tag %}
        {% assign array_name = ' ' | split: ',' %}
        {% assign array_tags = tag | split: '-' %}
        {% for ta in array_tags %}
            {% assign capit = ta | capitalize %}
            {% assign array_name = array_name | push: capit %}
        {% endfor %}
        {% assign name_tag = array_name | join: ' ' %}
        <li>
            <a href="#{{tag | downcase | replace: ' ', '-'}}">
                {{name_tag}}
            </a>
        </li>
  {% endunless %}

{% endfor %}
</ul>
<hr>
{::options parse_block_html="false" /}


{::options parse_block_html="true" /}
{% for tag in tags %}

  {% unless skipped_tags contains tag %}
    {% assign array_name = ' ' | split: ',' %}
    {% assign array_tags = tag | split: '-' %}
    {% for ta in array_tags %}
        {% assign capit = ta | capitalize %}
        {% assign array_name = array_name | push: capit %}
    {% endfor %}
    {% assign name_tag = array_name | join: ' ' %}
#### {{name_tag}}
<table>
    {% for post in site.posts %}
      {{post.tags}}
      {% assign post_tags = post.tags | split: ' ' %}
        {% if post_tags contains tag %}
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
