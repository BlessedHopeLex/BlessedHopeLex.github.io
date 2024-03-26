import os
import io
import json
import argparse
from datetime import date, datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# from dotenv import load_dotenv

import sermonaudio

from sermonaudio.broadcaster.requests import (
    Broadcaster,
    BroadcasterAPIError,
    SermonEventType,
)
from sermonaudio.node.requests import Node

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from google_drive import init_google_drive


day_part_tags_map = {
    "wednesday-evening": SermonEventType.MIDWEEK_SERVICE,
    "sunday-morning": SermonEventType.SUNDAY_AM,
    "sunday-evening": SermonEventType.SUNDAY_PM,
}

services_sheet_day_part_tags_map = {
    "Wednesday Evening": SermonEventType.MIDWEEK_SERVICE,
    "Sunday Morning": SermonEventType.SUNDAY_AM,
    "Sunday Evening": SermonEventType.SUNDAY_PM,
}

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

path_to_services_files = "C:\\Users\\warr7\\repos\\blessedhopelex.github.io\\_services"
path_to_audio_file = "/src/downloads" # os.getenv("DOWNLOAD_LOCATION")


def run(sa_api_access_key, sa_broadcaster_id):

    tryMax = 50
    tried = 0
    max_workers = 5

    # Pull in each file from root/_services folder
    with ProcessPoolExecutor(max_workers=max_workers) as e:
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

            tried = tried + 1
            if tried > tryMax:
                break

            # print(date_object.date())
            print(f"{filename} - {preacher}")
            e.submit(
                process_sermon,
                date_object,
                sa_api_access_key,
                sa_broadcaster_id,
                sermon_title,
                preacher,
                scripture,
                day_part_tag,
                series_name,
                google_drive_audio_id,
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


def process_sermon(
    date_object,
    sa_api_access_key,
    sa_broadcaster_id,
    sermon_title,
    preacher,
    scripture,
    day_part_tag,
    series_name,
    google_drive_audio_id,
):
    # You must set your API key before making any requests
    sermonaudio.set_api_key(sa_api_access_key)
    broadcaster = Node.get_broadcaster(sa_broadcaster_id)
    if not broadcaster:
        print("Broadcaster ID is incorrect")
        return

    # Access the google drive api to download the audio file
    #       Set up api key for Blessed Hope's google drive (like for personal db api)
    #           Will need to be a machine-to-machine key, because I won't be logging in via UI
    #           Also grab personal db api's google_sheets.py implementation for accessing the Drive API
    audio_filepath = download_google_drive_audio(google_drive_audio_id)
    if audio_filepath is None:
        return

    # If it is a series (part of tags, excluding some values), use SA API to create the series
    series = handle_create_series(series_name, sa_broadcaster_id)

    # Get hashtags/keywords
    keywords = get_keywords(series_name)

    # Create the sermon
    sermon = None
    try:
        sermon = Broadcaster.create_or_update_sermon(
            sermon_id=None,
            speaker_name=preacher,
            accept_copyright=True,
            full_title=sermon_title,
            preach_date=date_object,
            publish_timestamp=datetime.now(),
            event_type=day_part_tags_map.get(
                day_part_tag, SermonEventType.SPECIAL_MEETING
            ),
            subtitle=None,
            language_code="en",
            keywords=keywords,
            display_title=None,
            bible_text=scripture,
            more_info_text=None,
        )
    except BroadcasterAPIError as e:
        print(f"Sermon: create didn't work: {e}")

    # Set the series if applicable
    if series:
        move_sermon_to_series(sermon.sermon_id, series.series_id)

    # Upload the media
    if sermon and audio_filepath:
        upload_file(sermon.sermon_id, audio_filepath)

    # Cleanup
    cleanup(audio_filepath)


def process_service(
    date_object,
    sa_api_access_key,
    sa_broadcaster_id,
    sermon_title,
    preacher,
    scripture,
    day_part_tag,
    series_name,
    google_drive_audio_id,
    sheets_service,
    update_uploaded_date,
    update_audio_deleted,
    rowNum,
):
    # You must set your API key before making any requests
    sermonaudio.set_api_key(sa_api_access_key)
    broadcaster = Node.get_broadcaster(sa_broadcaster_id)
    if not broadcaster:
        print("Broadcaster ID is incorrect")
        return

    # Access the google drive api to download the audio file
    #       Set up api key for Blessed Hope's google drive (like for personal db api)
    #           Will need to be a machine-to-machine key, because I won't be logging in via UI
    #           Also grab personal db api's google_sheets.py implementation for accessing the Drive API
    audio_filepath = download_google_drive_audio(google_drive_audio_id)
    if audio_filepath is None:
        return

    # If it is a series (part of tags, excluding some values), use SA API to create the series
    series = handle_create_series(series_name, sa_broadcaster_id)

    # Get hashtags/keywords
    keywords = get_keywords(series_name)

    # Create the sermon
    sermon = None
    try:
        sermon = Broadcaster.create_or_update_sermon(
            sermon_id=None,
            speaker_name=preacher,
            accept_copyright=True,
            full_title=sermon_title,
            preach_date=date_object,
            publish_timestamp=datetime.now(),
            event_type=services_sheet_day_part_tags_map.get(
                day_part_tag, SermonEventType.SPECIAL_MEETING
            ),
            subtitle=None,
            language_code="en",
            keywords=keywords,
            display_title=None,
            bible_text=scripture,
            more_info_text=None,
        )
    except BroadcasterAPIError as e:
        print(f"Sermon: create didn't work: {e}")

    # Set the series if applicable
    if series:
        move_sermon_to_series(sermon.sermon_id, series.series_id)

    # Upload the media
    if sermon and audio_filepath:
        upload_file(
            sermon.sermon_id,
            audio_filepath,
            sheets_service,
            update_uploaded_date,
            update_audio_deleted,
            google_drive_audio_id,
            rowNum,
        )

    # Cleanup
    cleanup(audio_filepath)


def process_services(
    services,
    sa_api_access_key,
    sa_broadcaster_id,
    sheets_service,
    update_uploaded_date,
    update_audio_deleted,
):
    tryMax = 50
    tried = 0
    max_workers = 5

    # Pull in each file from root/_services folder
    with ProcessPoolExecutor(max_workers=max_workers) as e:
        for service in services:
            tried = tried + 1
            if tried > tryMax:
                break
            (
                date_object,
                sermon_title,
                scripture,
                preacher,
                series_name,
                google_drive_audio_id,
                day_part_tag,
                rowNum,
            ) = service
            e.submit(
                process_service,
                date_object,
                sa_api_access_key,
                sa_broadcaster_id,
                sermon_title,
                preacher,
                scripture,
                day_part_tag,
                series_name,
                google_drive_audio_id,
                sheets_service,
                update_uploaded_date,
                update_audio_deleted,
                rowNum,
            )


def download_google_drive_audio(google_drive_audio_id):
    filepath = None
    with init_google_drive() as google_drive:
        # print(
        #     json.dumps(
        #         # google_drive.files().list(
        #         #     q="mimeType='application/vnd.google-apps.folder'",
        #         #     corpora="allDrives",
        #         #     includeItemsFromAllDrives=True,
        #         #     supportsAllDrives=True,
        #         # )
        #         # google_drive.drives()
        #         # .list(
        #         #     q="mimeType='application/vnd.google-apps.folder'",
        #         #     pageSize=10,
        #         #     useDomainAdminAccess=True,
        #         # )
        #         google_drive.files().get(fileId=google_drive_audio_id).execute(),
        #         sort_keys=True,
        #         indent=4,
        #     )
        # )
        try:
            request = google_drive.files().get_media(fileId=google_drive_audio_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            filepath = f"{path_to_audio_file}\\{google_drive_audio_id}.m4a"
            while done is False:
                status, done = downloader.next_chunk()
                # print(f"Download {int(status.progress() * 100)}.")
            # Save the file at path_to_audio_file with a good name
            with open(filepath, "wb") as outfile:
                outfile.write(file.getbuffer())
        except HttpError as error:
            print(f"An error occurred: {error}")
            file = None
            filepath = None
    # Return filename so I can delete the file once I'm finished with it
    return filepath


def handle_create_series(series_name, sa_broadcaster_id):
    series = None
    if series_name:
        try:
            series = Broadcaster.create_series(
                title=series_name, broadcaster_id=sa_broadcaster_id
            )
            if not series:
                series = Node.get_series(
                    series_name=series_name, broadcaster_id=sa_broadcaster_id
                )
        except BroadcasterAPIError as e:
            print(f"Series: create didn't work: {e}")
    return series


def move_sermon_to_series(sermon_id, series_id):
    try:
        Broadcaster.move_sermon_to_series(sermon_id=sermon_id, series_id=series_id)
    except BroadcasterAPIError as e:
        print(f"Series: move sermon didn't work: {e}")


def upload_file(
    sermon_id,
    filepath,
    sheets_service=None,
    update_uploaded_date=None,
    update_audio_deleted=None,
    google_drive_audio_id=None,
    rowNum=None,
):
    try:
        # Broadcaster.upload_audio()
        Broadcaster._upload_media(
            upload_type="original-audio",
            sermon_id=sermon_id,
            path=filepath,
        )

        if update_uploaded_date and rowNum:
            update_uploaded_date(sheets_service, date.today(), rowNum)
        
        # NOTE: Google API won't allow service account to delete because it isn't the file owner
        # if google_drive_audio_id:
        #     with init_google_drive() as google_drive:
        #         body_value = {'trashed': True}
        #         response = google_drive.files().update(fileId=google_drive_audio_id, body=body_value).execute()
        #         if response.get("trashed"):
        #             if update_audio_deleted and rowNum:
        #                 update_audio_deleted(sheets_service, rowNum)

    except BroadcasterAPIError as e:
        print(f"Upload Media: didn't work: {e}")


def get_keywords(series_name):
    keywords = None
    if series_name:
        keywords = [series_name.lower()]
    return keywords


def cleanup(filepath):
    # Delete the local audio when finished
    os.remove(filepath)


# NOTE: Test cases
#   1. Part of a new series         Y
#   2. Part of an existing series   Y
#   3. Not part of a series         Y
#   4. Without renaming file        Y - file name doesn't matter
#   5. Without ID3 tags             Y - ID3 tags not needed


# TODONE:
#   X Fix names of sermons
#       X Various iterations of pt., (pt. ), Part, <number>, etc. - make them the same
#       X Remove "Mission - " from Jacob's missions sermons
#       X Remove " / ABC's" from 2023-09-03
#       X Change "Billy's Musical Testimony" to "Billy's Testimony"
#   X Trim recordings with start-time-seconds data
#       x Download, trim audio, re-upload


# if __name__ == "__main__":
#     load_dotenv()
#     # Take API access keys for SA and Google as command line args
#     #       Later on I may change to include it as a GitHub secret and have an action run this
#     parser = argparse.ArgumentParser(
#         prog="Blessed Hope - SermonAudio Importer",
#         description="Imports old sermons into SermonAudio",
#     )
#     parser.add_argument("-s", "--sermonaudio", help="Your SermonAudio API key")
#     parser.add_argument("-b", "--broadcasterid", help="Your SermonAudio Broadcaster ID")

#     args = parser.parse_args()
#     print(args.sermonaudio, args.broadcasterid)
#     run(args.sermonaudio, args.broadcasterid)
