---
sermon-title: Bible Versions 8
google-drive-id: 1Sx1YsxqlL-aPAyBJ0M_-kpF46QTaQX8b
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

## Westcott and Hort

They denied the infallible inspiration of Scripture, the sacrificial blood atonement of Christ, the Genesis account of creation, and other doctrines of the faith.

The following are quotes from Westcott and Hort:

- “But the book which has most engaged me is Darwin. Whatever may be thought of it, it is a book that one is proud to be contemporary with. ... My feeling is strong that the theory is unanswerable” (Hort writing on April 3, 1860, Life of Hort, Vol. 1).

- “No one now, I suppose, holds that the first three chapters of Genesis give literal history” (Westcott, writing to the Archbishop of Canterbury in 1890, cited in Life and Letters of Brooke Foss Westcott, Vol. II, p. 69).

- “I am inclined to think that no such state as ‘Eden’ (I mean the popular notion) ever existed, and that Adam’s fall in no degree differed from the fall of each of his descendants, as Coleridge justly argues” (Westcott, Life and Letters of Brooke Foss Westcott, Vol. I, p. 78)

- “... the popular doctrine of substitution is an immoral and material counterfeit. ... Certainly nothing could be more unscriptural than the modern limiting of Christ’s bearing our sins and sufferings to his death; but indeed that is only one aspect of an almost universal heresy” (Hort to Westcott, 1860, cited in Life of Hort, Vol. I, p. 430)

- [Commenting on John 1:29, 13:31] “... the redemptive efficacy of Christ’s work is to be found in His whole life. ... The redemptive work of Christ essentially was completed [by the time of His discourse in John 13]” (Westcott, The Gospel According to St. John, pp. 20, 196).
	- This makes it obvious why they removed "through his blood"

- The following statement, which Hort wrote to Westcott in 1861, speaks for itself: “This may sound cowardice--I have a craving that our Text [their critical New Testament] should be cast upon the world before we deal with MATTERS LIKELY TO BRAND US WITH SUSPICION. I mean a text issued by men who are already known for what WILL UNDOUBTEDLY BE TREATED AS DANGEROUS HERESY will have great difficulty in finding its way to regions which it might otherwise hope to reach and whence it would not be easily banished by subsequent alarms. … If only we speak our minds, we shall not be able to avoid giving grave offence to the miscalled orthodoxy of the day” (Hort, Life and Letters of Hort, Vol. I, pp, 421, 445). 

### The Revised Version

- Westcott and Hort were on the committee that put out the Revised Version (RV) in 1881
    - They were supposed to "adapt King James' version to the present state of the English language without changing the idiom and vocabulary".
	- They did not do that. They brought in a different text and "corrected" the King James in many places. "In the New Testament alone more than 30,000 changes were made…"
    - See [Revision Revised](https://en.wikipedia.org/wiki/Revised_Version#Features) on Wikipedia

- Their theories on manuscripts and the Bible's text were answered in their day by Dean John Burgon. You can find his works (especially "The Revision Revised") in the public domain as [digital books](https://www.gutenberg.org/ebooks/search/?query=john+burgon&submit_search=Go%21). You can also find his works as print books at amazon.com or [kjv1611.org](kjv1611.org).

### Further Resources

- [Answering the Myths of the Bible Version Debate](https://www.wayoflife.org/free_ebooks/answering-the-myths-of-the-bible-version-debate.php)
- [The Bible Version Question & Answer Database](https://www.wayoflife.org/free_ebooks/bible_version_question_answer_database.php)
- [The Modern Bible Version Hall of Shame](https://www.wayoflife.org/free_ebooks/modern_bible_version_hall_of_shame.php)
- [Rome and the Bible](https://www.wayoflife.org/free_ebooks/rome_and_the_bible.php)