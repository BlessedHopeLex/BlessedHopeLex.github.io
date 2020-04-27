---
sermon-title: Four Essentials
google-drive-id: 1FPPBBOn8R6bcQ99NH4Qgf8LyieSgBwN8
start-time-seconds: 1610
day-part: Morning
tags: [sunday-morning]
layout: default
---

# {{ page.sermon-title }}

### {{ page.date | date: "%A, %B %-d, %Y" }} {{ page.day-part }} Service

{% if page.start-time-seconds >= 1 %}
Needs notice
{% endif %}

{% include sermon-starts-at.md starts-at="26:50" %}

{% capture video-id %}
{{ page.google-drive-id }}
{% endcapture %}

{% capture start-time %}
{{ page.start-time-seconds }}
{% endcapture %}

{% include google-drive-audio.md drive-id=video-id start-time=start-time %}