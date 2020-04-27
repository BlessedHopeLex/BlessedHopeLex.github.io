---
sermon-title: Four Essentials
google-drive-id: 1FPPBBOn8R6bcQ99NH4Qgf8LyieSgBwN8
day-part: Morning
tags: [sunday-morning]
layout: default
---

# {{ page.sermon-title }}

### {{ page.date | date-to-string }} {{ page.day-part }} Service

{% include sermon-starts-at.md starts-at="26:50" %}

{% capture video-id %}
    {{ page.google-drive-id }}
{% endcapture %}

{% include google-drive-audio.md drive-id=video-id start-time="1610" %}