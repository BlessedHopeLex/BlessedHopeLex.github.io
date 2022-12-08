---
sermon-title: Bible Versions 9
google-drive-id: 1Tj2nBVlwzD9V7st02y0OKmQIxGAWd1SJ
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

## Westcott and Hort's Theories

- Westcott and Hort decided that all the manuscripts should be grouped into what they called "families"
	- They made up four families: the "Byzantine" (or Syrian), the "Western", the "Alexandrian", and the "Neutral" families. See https://en.wikipedia.org/wiki/Westcott_and_Hort#WH_edition
	- The trick they pulled:
		- Saying the "Byzantine" family wasn't as old as the others, then grouping manuscripts that read like the King James into that family. They said these were "less likely reliable." 
		- They grouped their two favorite manuscripts, Vaticanus and Siniaticus, into the "Neutral" family and called those the oldest.
		- They then claim that because they think are the oldest (which they aren't), they should be favored instead of the other 95% of manuscripts.

- Siniaticus - (aleph) א
	- Supposedly the only complete uncial manuscript containing the complete New Testament
		- When the scholars say that Sinaiticus contains the “complete New Testament,” they tell you a lie. 
		- What they mean is, “It contains all of the New Testament except John 5:4, 8:1–11; Matthew 16:2–3; Romans 16:24; Mark 16:9–20; 1 John 5:7; Acts 8:37 and a dozen other verses.”
		- It also throws the “Shepherd of Hermas” and the “Epistle of Barnabas” into the New Testament, and originally it contained part of the “Didache.”
		- Found in St. Catherine’s monastery on Mr. Sinai by Tischendorf in a trash pile about to be burned
		
		
- Vaticanus - B
	- Written around A.D. 350
	- It contains the Epistle to Barnabas and the Apocrypha.
	- Written by the same man as Sinaiticus (according to Tishendorf), but the Pope insists that his manuscript must be earlier than Sinaiticus (Aleph) because of the way that the divisions are placed in the Gospels.
	- Omits Genesis 1:1 through Genesis 46:28; Psalms 106 through Psalms 138; Matthew 16:2–3; Romans 16:24; the Pauline Pastoral Epistles; Revelation; and everything in Hebrews after Hebrews 9:14.
	- Its reading in John 1:18 showed every Christian exactly what it was — a Gnostic depravation.
		- Ruckman, Dr. Peter S.. The Christian's Handbook of Manuscript Evidence (p. 71). BB Bookstore. Kindle Edition. 
	- The Vatican manuscript was available at the time of the translation of the AV 1611 and was even referred to by Erasmus in 1515 and he ignored it.
	- In the book of Luke alone, B:
		- Omits 757 words
		- Substitutes 309 words
		- Has 138 readings that only occur in B (not in one single other manuscript)
	
- Vaticanus and Siniaticus
	- They disagree with each other thousands of times
	- They are two of the most corrupt manuscripts we have available. By corrupt we mean:
		- They have some of the most corrupt readings
        - They show large amounts of tampering: words scraped/scratched out and replaced, sometimes multiple times in the same place by multiple different people