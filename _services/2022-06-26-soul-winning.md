---
sermon-title: Soul Winning
google-drive-id: 
start-time-seconds: 0
day-part: Evening
tags: sunday-evening
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

The Gospel: 1 Corinthians 15:1-4

- Don't argue theological points with people who are lost.
- Don't argue with someone who is religious.

Ephesians 2:8-9

1. A person must know they are a sinner. Romans 3:23, Revelation 21:8, Romans 6:23
2. A person must know what Jesus Christ did for them. Romans 5:8, Romans 10:9-13, 2 Corinthians 5:21
3. A person must receive Jesus Christ as their Savior. John 1:12

"I think so" or "I hope so" isn't good enough. 1 John 5:13