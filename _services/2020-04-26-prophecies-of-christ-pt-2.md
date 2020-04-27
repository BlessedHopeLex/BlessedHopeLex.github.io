---
sermon-title: Prophecies of Christ Pt. 2
google-drive-id: 1oc6ttd5Kf3ajIXZwhCn9v_QpH5jmnG6u
start-time-seconds: 0
day-part: Evening
tags: [sunday-evening]
layout: default
---

# {{ page.sermon-title }}

### {{ page.date | date_to_string }} {{ page.day-part }} Service

{% if page.start-time-seconds >= 1 %}
  {% include sermon-starts-at.md starts-at="{{ page.start-time-seconds | divided_by: 60 }}:{{ page.start-time-seconds | modulo: 60 }}" %}
{% endif %}

{% include google-drive-audio.md drive-id="{{ page.google-drive-id }}" start-time-seconds="{{ page.start-time-seconds }}" %}