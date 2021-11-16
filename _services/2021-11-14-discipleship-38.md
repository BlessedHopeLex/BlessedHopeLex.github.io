---
sermon-title: Discipleship Course 38
google-drive-id: 1-0HakDJhBqNKqpbPj1A2kcibUHpQB0i-
start-time-seconds: 0
day-part: Evening
tags: [sunday-evening discipleship-course]
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

Baptism does not always involve water. In fact, **most** verses in the Bible that talk about baptism do not involve water.