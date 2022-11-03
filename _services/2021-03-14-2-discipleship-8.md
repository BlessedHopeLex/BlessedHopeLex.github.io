---
sermon-title: Discipleship Course 8
google-drive-id: 1qr720gU5nSs7I9MUJFnosSZf9oi3Nom0
start-time-seconds: 0
day-part: Evening
tags: sunday-evening discipleship-course
preacher: James Coffman
layout: default
---

# {{ page.sermon-title }}

##### {{ page.date | date: "%A, %B %-d, %Y" }} {{ page.day-part }} Service

{% if page.start-time-seconds >= 1 %}
{% capture starts-at-time %}
{{ page.start-time-seconds | divided_by: 60 }}:{{ page.start-time-seconds | modulo: 60 }}
{% endcapture %}

{% include sermon-starts-at.md starts-at=starts-at-time %}
{% endif %}

{% capture video-id %}
{{ page.google-drive-id }}
{% endcapture %}

{% capture start-time %}
{{ page.start-time-seconds }}
{% endcapture %}

{% include google-drive-audio.md drive-id=video-id start-time=start-time %}

***

# Dispensational Chart
![Dispensational Chart]({{ site.url }}assets/dispensational-chart.jpg)

# Seven Dispensations
![Seven Dispensations]({{ site.url }}assets/seven-dispensations.jpg)

# Covenants
![Covenants]({{ site.url }}assets/covenants.jpg)