---
sermon-title: Bible Versions 3
google-drive-id: 1QWXqfGzqNzIy86jgFjvcZdUSnxXCLhGq
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

- 1 Corinthians 1:22 - [Other versions](https://www.biblegateway.com/verse/en/1%20Corinthians%201:22)
- Mark 16:9-16 - [NIV](https://www.biblegateway.com/passage/?search=mark%2016%3A9-16&version=KJV;NIV)
- Psalm 9:17 - [Other versions](https://www.biblegateway.com/verse/en/Psalm%209:17)
- Psalm 16:10 - [Other versions](https://www.biblegateway.com/verse/en/Psalm%2016:10)
- Proverbs 15:11 - [Other versions](https://www.biblegateway.com/verse/en/Proverbs%2015:11)
- Proverbs 27:20 - [Other versions](https://www.biblegateway.com/verse/en/Proverbs%2027:20)
- Jonah 2:2 - [Other versions](https://www.biblegateway.com/verse/en/Jonah%202:2)
- The word "hell" only occurs 13 times in the NIV
    - It occurs 54 times in the KJV
    - It is **completely** removed from the Old Testament in the NIV
    - ["Hell" in the NIV](https://www.biblegateway.com/quicksearch/?quicksearch=hell&version=NIV)
- Luke 16:23 - [Other versions](https://www.biblegateway.com/verse/en/Luke%2016%3A23)
- Matthew 16:18 - [Other versions](https://www.biblegateway.com/verse/en/Matthew%2016%3A18)
- Acts 2:31 - [Other versions](https://www.biblegateway.com/verse/en/Acts%202%3A31)
- 1 Corinthians 15:55 - [NKJV](https://www.biblegateway.com/passage/?search=1%20Corinthians%2015%3A54-56&version=KJV,NKJV)
