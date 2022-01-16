---
sermon-title: Discipleship Course 45
google-drive-id: 14c6XentfGfZoBPsXR1WTmx-kyF8miSUH
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

# The Local Church

"The church" has two different meanings:
1. The Body of Christ - all people who have accepted Jesus Christ as their personal Savior are part of the Body of Christ (the Church). There are no lost people in the Body of Christ. The Body of Christ is sometimes called the "universal church". Ephesians 5:29-32, Colossians 1:18, Ephesians 1:20-23, Ephesians 4:4-6, Ephesians 4:11-16, 1 Corinthians 12:12-28
2. The local church - an assembly of people in a local place who come together to worship Jesus Christ. There are some lost people in local churches (religious, but lost).

