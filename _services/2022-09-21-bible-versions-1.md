---
sermon-title: Bible Versions 1
google-drive-id: 1PtrFPn5jDr_3mW0f-wej1iGPGTP31h8a
start-time-seconds: 0
day-part: Evening
tags: [wednesday-evening bible-versions]
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

- Proverbs 30:5 - [Other versions](https://www.biblegateway.com/verse/en/Proverbs%2030:5)
- Proverbs 30:6 - [Other versions](https://www.biblegateway.com/verse/en/Proverbs%2030:6)
- Deuteronomy 4:2 - [Other versions](https://www.biblegateway.com/verse/en/Deuteronomy%204:2)
- Deuteronomy 12:32 - [Other versions](https://www.biblegateway.com/verse/en/Deuteronomy%2012:32)
- Psalm 12:6 - [Other versions](https://www.biblegateway.com/verse/en/Psalm%2012:6)
- Psalm 12:7 - [Other versions](https://www.biblegateway.com/verse/en/Psalm%2012:7)
- 2 Timothy 3:15 - [Other versions](https://www.biblegateway.com/verse/en/2%20Timothy%203:15)
- 2 Timothy 3:16 - [Other versions](https://www.biblegateway.com/verse/en/2%20Timothy%203:16)
- Matthew 5:18 - [Other versions](https://www.biblegateway.com/verse/en/Matthew%205:18)
- 2 Corinthians 2:17 - [Other versions](https://www.biblegateway.com/verse/en/2%20Corinthians%202:17)

## Corrections

"Auto" in "autograph" means "self," not "man" or "hand."
