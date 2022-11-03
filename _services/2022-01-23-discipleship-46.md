---
sermon-title: Discipleship Course 46
google-drive-id: 15KBKCE_bk27LmSAGhWJH8Yihe1sjQuvG
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

# Baptism

The word "baptism" means "immersion". By definition sprinkling is not baptism. The slang for "baptism" would be "dunked." Getting splashed is not the same as getting dunked underwater.

- Acts 8:37-38 - baptism always occurs after salvation
- 1 Corinthians 15:1-4 - the Gospel does not include baptism
- Matthew 28:19-20 - the Great Commission, given right after the resurrection
- 1 Corinthians 1:14-17 - the Gospel does not include baptism. Baptism has **no part** in your salvation.