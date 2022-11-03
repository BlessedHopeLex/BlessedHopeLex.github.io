---
sermon-title: Discipleship Course 15
google-drive-id: 1RyCTcLY_lObznrjySp_xdqWAGw3Z1Voh
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

# The Rapture

Rapture means "a seizing by violence."

1 Thessalonians 4:13-18

1 Corinthians 15:51-54 - Our bodies will be changed. 1 John 3:2

Colossians 3:4

When the Bible talks about the Lord coming *for* His saints, that is the Rapture. When It talks about Him coming *with* His saints, that is the Second Coming.