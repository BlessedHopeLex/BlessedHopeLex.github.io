---
sermon-title: Bible Versions 2
google-drive-id: 1Q4BYYHMfj88_X52GpkXfhWhk9EoMw5TN
start-time-seconds: 0
day-part: Evening
tags: wednesday-evening bible-versions
preacher: Zack Warren
layout: default
---

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

# {{ page.sermon-title }}

## Verse Comparisons

- 1 Corinthians 1:18 - [Other versions](https://www.biblegateway.com/verse/en/1%20Corinthians%201:18)
- Acts 8:37 - [Other versions](https://www.biblegateway.com/verse/en/Acts%208:37)
- Colossians 1:14 - [Other versions](https://www.biblegateway.com/verse/en/Colossians%201:14)
- Matthew 9:13 - [Other versions](https://www.biblegateway.com/verse/en/Matthew%209:13)
- Ephesians 1:13 - [Other versions](https://www.biblegateway.com/verse/en/Ephesians%201%3A13)
- 2 Corinthians 1:22 - [Other versions](https://www.biblegateway.com/verse/en/2%20Corinthians%201%3A22)
- Romans 10:4 - [Other versions](https://www.biblegateway.com/verse/en/Romans%2010:4)
- 1 John 5:7 - [Other versions](https://www.biblegateway.com/verse/en/1%20John%205:7)
- 1 Timothy 3:16 - [Other versions](https://www.biblegateway.com/verse/en/1%20Timothy%203:16)
- 1 John 4:3 - [Other versions](https://www.biblegateway.com/verse/en/1%20John%204:3)
- John 1:3 - [Other versions](https://www.biblegateway.com/verse/en/John%201:3)
