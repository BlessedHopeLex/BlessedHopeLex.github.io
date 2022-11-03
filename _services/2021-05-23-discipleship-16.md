---
sermon-title: Discipleship Course 16
google-drive-id: 1Z5a4v-UJCCTUI9OzDSHTjMKXp21PYVVo
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

# The Seven Resurrections

1. Christ from the dead - Matthew 28:1-6
2. Old Testament saints from the dead - Ephesians 4:8-12; Matthew 27:52-53
3. New Testament saints from the dead - 1 Corinthians 15:50-56; 1 Thessalonians 4:14-16
4. Believers, spiritually - Ephesians 2:1-6; Romans 11:15
5. Nation of Israel - Ezekiel 37; Matthew 24:31
6. Post-Tribulation - Revelation 11:12
7. The unsaved dead - Revelation 20:11-15

# Sevens in the Bible
![Sevens in the Bible]({{ site.url }}assets/sevens-in-the-bible.jpg)