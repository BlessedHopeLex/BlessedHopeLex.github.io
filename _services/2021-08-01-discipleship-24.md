---
sermon-title: Discipleship Course 24
google-drive-id: 1S0rjoWne0a3wzLF6NZxp4rHRKFkTehaN
start-time-seconds: 0
day-part: Evening
tags: [sunday-evening discipleship-course]
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

***

# God Expected His Son to be Obedient

Hebrews 5:8

1. Prophecy
    1. Circumstances of His birth
        - Place: Bethlehem (Micah 5:2, Matthew 2:6)
        - Virgin birth (Isaiah 7:14, Matthew 1:23)
        - Lineage: house of David (2 Samuel 7:12, Romans 1:3)
        - Tribe: Judah (Genesis 49:10, Hebrews 7:14)
    2. Aspects of His ministry
        - Location (Isaiah 9:1-2, Matthew 4:13-16)
        - Power (Isaiah 11:2, Luke 3:22, Luke 4:1)
        - Saving character (Isaiah 61:1, Luke 4:16-21)
        - Healing (Isaiah 53:4, Matthew 8:16-17)
        - Miracles (Isaiah 35:5-6, Matthew 11:4-5)
        - Serving character (Isaiah 42:1-4, Matthew 12:18-21)
        - Humility (Zechariah 9:9, Matthew 21:4-5)
        - Preaching (Luke 4:18-21)
        - Rejection (Isaiah 53:3, John 1:11)