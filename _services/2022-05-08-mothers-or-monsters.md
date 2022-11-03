---
sermon-title: Mothers or Monsters
google-drive-id: 1F1IIZwgq3YiTGaDIQOOrT_WL5AQXzqqK
start-time-seconds: 0
day-part: Morning
tags: sunday-morning
preacher: James Coffman
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

1 Kings 3:16-28

2 Timothy 1:6,11

Psalm 97:10, Proverbs 8:13, Amos 5:15, Micah 3:2

2 Timothy 2:2