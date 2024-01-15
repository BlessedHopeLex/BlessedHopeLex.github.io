---
sermon-title: He Took the Lord's Side
google-drive-id: 1sISfmvTs3L2Bge_3H4l1Wkzcv6yXBkvn
start-time-seconds: 0
day-part: Morning
tags: sunday-morning
preacher: James Coffman
scripture: 1 Kings 15:9-15
layout: default
---

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

# {{ page.sermon-title }}

