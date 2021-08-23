---
sermon-title: Nine Revelations
google-drive-id: 1-05AlxDonSh9ZaUkrMMa-2ZF0D3_P0Tf
start-time-seconds: 0
day-part: Evening
tags: [wednesday-evening]
preacher: James Coffman
layout: default
---

# {{ page.sermon-title }}

### {{ page.date | date: "%A, %B %-d, %Y" }} {{ page.day-part }} Service

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


There are several types of theology:

1. Works-based

    Holds that a man gets saved by works.

2. Calvinist

    Holds what is called **TULIP** theology:

    **T**otal Depravity - man is totally depraved and **cannot** turn to God of their own will.

    **U**nconditional Election - God chose who would be saved and lost before the world began.

    **L**imited Atonement - Jesus only died for those He elected (see above), not everyone.

    **I**rresistible Grace - God comes on the elect and forces them to accept Him.

    **P**erseverance of the Saints - the elect will not fall away (if someone falls away, then they were not elect).

3. Armenian

    Holds that a man gets saved by faith but must stay saved by works (he can lose his salvation if he sins).

4. Bible-believing

    Holds that a man gets saved by faith and cannot lose it (even if he stops believing).