This folder will contain scripts for dealing with the Sermon Audio API.

[Python package](https://pypi.org/project/sermonaudio/#description)

[API docs](https://api.sermonaudio.com/v2/docs#/media/create_media_v2_media_post)

[API Programming Guide](https://api.sermonaudio.com/#API_Programming_Guide)

The API access key can be found here: https://www.sermonaudio.com/secure/members_stats.asp


## Docker Instructions

```
docker build -t registry.zackwarren.dev/sermonaudio:rpi .
docker push registry.zackwarren.dev/sermonaudio:rpi
```