---
sermon-title: Discipleship Course 6
google-drive-id: 1rs25xKuL2ITSwMOvBmY0GA6uRW-VufIs
start-time-seconds: 0
day-part: Evening
tags: [sunday-evening discipleship-course]
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

# Why do we need the Bible? (cont.)

## The Bible reveals Satan (cont.)

### Where did Satan come from? (cont.)

Ezekiel 28:11-13

- He was created to protect God's holiness - Ezekiel 28:14-19

- He was cast out of Heaven because of rebellion - Isaiah 14:12-15

### What is Satan like?

- Natural attributes

    - Corrupted wisdom - Ezekiel 28:17

    - Second to God in power - Jude 1:9

    - Not omnipresent (not everywhere at once, only in one place at a time) - Job 1:6-7

    - The author of confusion - 1 Corinthians 14:33, Psalms 71:1

- Moral attributes

    - Sinner - 1 John 3:8

    - Liar and murderer - John 8:44

### What is Satan's plan?

- Usurp God's authority by questioning His Word - Genesis 3:1, Matthew 4:1-11, Luke 1:1-13

- Bring glory to himself

    - As god of this world - 2 Corinthians 4:4

    - By having Jesus worship him - Matthew 4:9

- Counterfeit God's plan - 2 Corinthians 11:14, Revelation 2:2

1 John 4:1-3

***

# New Bibles pervert God's Word

1 Samuel 20:30 in the Living Bible:

![Living Bible - 1 Samuel 20:30]({{ site.url }}/assets/living_bible_1_sam_20_30.jpg)

Isaiah 14:12 in an NIV gives the devil Jesus' title:

    "How you have fallen from heaven,
        morning star, son of the dawn!
    You have been cast down to the earth,
        you who once laid low the nations!"

Compare with Revelation 22:16:

    “I, Jesus, have sent my angel to give you[a] this testimony for the churches. I am the Root and the Offspring of David, and the bright Morning Star.”
