---
sermon-title: Paul Replaces Peter
google-drive-id: 1C4ZfpQYIDngdMGCBrf_Y7v04J3HBOYaX
start-time-seconds: 0
day-part: Evening
tags: wednesday-evening
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

# Peter vs Paul

|Peter | Paul |
--- | --- |
|Acts 3:1 | Acts 14:8-10 |
|Acts 5:14-16 | Acts 19:10-12 |
|Acts 9:36-42 | Acts 20:9-12 |
|Acts 5:4 | Acts 13:8-11 |
|Acts 9:32-35 | Acts 28:8-10 |
|Acts 10:11-15 | Acts 16:9-10 |


2 Timothy 4:20

Philippians 2:25-27