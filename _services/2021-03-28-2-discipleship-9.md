---
sermon-title: Discipleship Course 9
google-drive-id: 1lCJNd4AIcfcxHCrm8wVX7iRs6-T_cooH
start-time-seconds: 0
day-part: Evening
tags: [sunday-evening discipleship-course]
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

# Dispensations

1. Man innocent - Genesis 1:26; Genesis 3:22-24
    - Creation to expulsion from Eden
2. Man under conscience - Genesis 3:24; Genesis 6:5-13; Genesis 7:11-12, 23
    - Expulsion to the Flood
3. Man in authority over the Earth (human government) - Genesis 8; Genesis 11:1-9
    - Flood to the Dispersion (Babel)
4. Man under promise (family - Abraham) - Genesis 12; Genesis 50
    - Abraham to bondage in Egypt
5. Man under the Law - Exodus 1; Exodus 19:1-8; Exodus 20:1-26; Deuteronomy 32; Matthew 27
    - Mt. Sinai to Mt. Calvary
6. Man under grace - Matthew 27; Revelation 4
    - Crucifixion to the Rapture
7. Man under the Tribulation - Revelation 5 through Revelation 19
8. Man under the personal reign of Jesus Christ - Revelation 20:1-5
    - The Millenium
9. Man in Eternity - Revelation 21; Revelation 22:1-5
    - Final battle at Gog and Magog through Eternity