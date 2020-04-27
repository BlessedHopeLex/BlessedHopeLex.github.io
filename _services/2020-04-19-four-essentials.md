---
sermon-title: Four Essentials
google-drive-id: 1FPPBBOn8R6bcQ99NH4Qgf8LyieSgBwN8
start-time-seconds: 1610
day-part: Morning
tags: [sunday-morning]
layout: default
---

# {{ page.sermon-title }}

### {{ page.date | date_to_string }} {{ page.day-part }} Service

{% if page.start-time-seconds >= 1 %}
    {% capture starts-at-time %}
    {{ page.start-time-seconds | divided_by: 60 }}:{{ page.start-time-seconds | modulo: 60 }}
    {% endcapture %}

  {% include sermon-starts-at.md starts-at=starts-at-time %}
{% endif %}


{% capture google-drive-id %}
{{ page.google-drive-id }}
{% endcapture %}

{% capture start-time-seconds %}
{{ page.start-time-seconds }}
{% endcapture %}

{% include google-drive-audio.md drive-id=google-drive-id start-time-seconds=start-time-seconds %}