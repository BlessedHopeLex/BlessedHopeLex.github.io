{::options parse_block_html="true" /}
<div id="noServicesAlert" style="display: none;" class="alert alert-primary" role="alert">
There are no live services today, but you can listen to one of our <a href="/services">recorded services</a>. You can also take a look at our <a href="/">service schedule</a>.
{: .m-0}
</div>
<script>
    const current_day = new Date(new Date().toLocaleString("en-US", {timeZone: "America/New_York"})).getDay();
    if (current_day != 0 && current_day != 3) {
        $("#noServicesAlert").show();
    }
</script>
{::options parse_block_html="false" /}


# Joining the Service

Click the button below to join our service live via Zoom.

{::options parse_block_html="true" /}
<a class="btn btn-primary" href="https://us02web.zoom.us/j/7608593426?pwd=cjZJV016blVrS0k4ZWM2bVlhVVZkQT09">Join Zoom Service</a>
{: .m-0}
{::options parse_block_html="false" /}

<!-- {% include bootstrap-alert-warning.md content="If Zoom has issues, please use the backup [Google Meeting](https://meet.google.com/qrf-yiyo-ohe). Note: you will need a Google account to join." %} -->

## First time joining

If you do not already have Zoom installed, then the link above will open a website, and you will be asked to download the Zoom app.

Zoom is available on Windows, Mac, Iphone, and Android.

Once you have downloaded the Zoom app, you can click the link above again to start the meeting.

<!-- {% include bootstrap-alert-primary.md content="If you do not already have Zoom installed, then the link above will open a website, and you will be asked to download the Zoom app.

Zoom is available on Windows, Mac, Iphone, and Android.

Once you have downloaded the Zoom app, you can click the link above again to start the meeting." %} -->

{% include bootstrap-alert-warning.md content="Please join the meeting muted. Many un-muted microphones can cause interference for other listeners. Feel free to unmute to give prayer requests or ask questions, but please be respectful of the service." %}
