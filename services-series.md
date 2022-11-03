---
title: Sermons by Series
---

{% assign rawtags = "" %}
{% for post in site.services %}
  <!-- Debug -->
  {{post.tags}}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}
<!-- Debug -->
{{rawtags}}

{% assign site.tags = "" %}
{% assign tags = "" %}
{% for tag in rawtags %}
  <!-- Debug -->
  {{tag}}
  {% if tag != "" %}
    {% if tags == "" %}
      {% assign tags = tag | split:'|' %}
    {% endif %}
    {% unless tags contains tag %}
      {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
    {% endunless %}
  {% endif %}
{% endfor %}
<!-- Debug -->
{{tags}}
{% assign site.tags = tags %}
<!-- Debug -->
{{site.tags}}


# {{ page.title }}

{% assign skipped_tags = "wednesday-evening,sunday-evening,sunday-morning" | split: ','] %}

### Series
{::options parse_block_html="true" /}
<ul>
{% for tag in tags %}
    <!-- Debug -->
    {{tag}}
  {% assign t = tag | first %}

  {% unless skipped_tags contains tag %}
        {% assign array_name = ' ' | split: ',' %}
        {% assign array_tags = tag | split: '-' %}
        {% for ta in array_tags %}
            {% assign capit = ta | capitalize %}
            {% assign array_name = array_name | push: capit %}
        {% endfor %}
        {% assign name_tag = array_name | join: ' ' %}
        <li>
            <a href="#{{t | downcase | replace: ' ', '-'}}">
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
