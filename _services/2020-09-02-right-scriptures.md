---
sermon-title: The Right Scriptures
google-drive-id: 1-mb5yB2oJtSo8E42JZr7xrIf_b3isljk
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
