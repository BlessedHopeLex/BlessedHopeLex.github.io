from datetime import datetime
import os

from sermonaudio.broadcaster.requests import (
    SermonEventType,
)


day_part_tags_map = {
    "wednesday-evening": SermonEventType.MIDWEEK_SERVICE,
    "sunday-morning": SermonEventType.SUNDAY_AM,
    "sunday-evening": SermonEventType.SUNDAY_PM,
}

path_to_services_files = "C:\\Users\\warr7\\repos\\blessedhopelex.github.io\\_services"

excluded_series = []
skip_sermons = [
    # Not sure about
    "Brother Kline - Missionary to Ukraine",
    # Contains google-drive-id-2, so has two audio files that need to be combined manually
    "Acts 12",
]
skip_preachers = []
only_include_preachers = []
no_earlier_than = datetime.strptime("2024-02-27", "%Y-%m-%d")  # 2020-04-27


def run():
    for os_filename in os.listdir(path_to_services_files):
        filename = os.fsdecode(os_filename)
        date_object = get_date_from_filename(filename)

        with open(
            os.path.join(path_to_services_files, filename), "r", encoding="utf-8"
        ) as file:
            # Parse the file for sermon-title, google-drive-id, day-part, tags, preacher
            (
                sermon_title,
                preacher,
                day_part_tag,
                series_name,
                google_drive_audio_id,
                start_time_seconds,
                scripture,
            ) = get_sermon_data(file)

        if only_include_preachers and preacher not in only_include_preachers:
            continue
        
        if sermon_title in skip_sermons or preacher in skip_preachers:
            continue

        if series_name in excluded_series:
            continue

        if not google_drive_audio_id:
            print(f"{filename} does not include a google audio id")
            continue

        if date_object.date() <= no_earlier_than.date():
            print(f"{filename} is before earliest date: {date_object.date()}")
            continue

        if start_time_seconds and int(start_time_seconds) > 0:
            print(
                f"{filename} needs to be trimmed: start time = {start_time_seconds}"
            )


def get_date_from_filename(filename):
    date_string = filename[0:10]  # "2023-12-17"
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    return date_object


def get_sermon_data(file):
    google_drive_id = None
    start_time_seconds = None
    sermon_title = None  # "Emmanuel"
    tags = None  # "sunday-morning"
    preacher = None  # "James Coffman"
    day_part_tag = None
    series_tag = None
    scripture = None

    opening_metadata_hyphens_found = False
    prev_line = "Start of file"
    try:
        for line in file:
            prev_line = line
            line = line.strip()
            if line == "---":
                if not opening_metadata_hyphens_found:
                    opening_metadata_hyphens_found = True
                    continue
                else:
                    break
            metadata_tag, value = line.split(":", maxsplit=1)
            value = value.strip()
            if metadata_tag == "sermon-title":
                sermon_title = value
            elif metadata_tag == "google-drive-id":
                google_drive_id = value
            elif metadata_tag == "start-time-seconds":
                start_time_seconds = value
            elif metadata_tag == "tags":
                tags = value
            elif metadata_tag == "preacher":
                preacher = value
            elif metadata_tag == "scripture":
                scripture = value

        for tag in tags.split(" "):
            if tag in day_part_tags_map.keys():
                day_part_tag = tag
            else:
                series_tag = tag.replace("-", " ").title()
    except Exception as e:
        print(f"Error with {file.name}: {e}")
        print(f"--- Prev line: {prev_line}")
    return (
        sermon_title,
        preacher,
        day_part_tag,
        series_tag,
        google_drive_id,
        start_time_seconds,
        scripture,
    )
