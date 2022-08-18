{% assign cur_day = 'now' | date: "%A" %}
{% if cur_day != "Wednesday" and cur_day != "Sunday" %}
{::options parse_block_html="true" /}
<div class="alert alert-primary" role="alert">
There are no live services today, but you can listen to one of our <a href="/services">recorded services</a>.
{: .m-0}
</div>
{::options parse_block_html="false" /}
{% endif %}


# Zoom Instructions


{::options parse_block_html="true" /}
<a class="btn btn-primary" href="https://us02web.zoom.us/j/7608593426?pwd=cjZJV016blVrS0k4ZWM2bVlhVVZkQT09">Join Zoom Service</a>
{: .m-0}
{::options parse_block_html="false" /}

<!-- {% include bootstrap-alert-warning.md content="If Zoom has issues, please use the backup [Google Meeting](https://meet.google.com/qrf-yiyo-ohe). Note: you will need a Google account to join." %} -->

{% include bootstrap-alert-primary.md content="If you do not already have Zoom installed, then the link above will open a website, and you will be asked to download the Zoom app.

Zoom is available on Windows, Mac, Iphone, and Android.

Once you have downloaded the Zoom app, you can click the link above again to start the meeting." %}

{% include bootstrap-alert-warning.md content="Please join the meeting muted. Many un-muted microphones can cause interference for other listeners. Feel free to unmute to give prayer requests or ask questions, but please be respectful of the service." %}
