import os
import argparse
from datetime import date, datetime

from dotenv import load_dotenv

from google_drive import (
    init_google_drive,
    init_google_sheets,
    SERVICES_SHEET_ID,
    SERVICES_SHEET_NAME,
)
from upload_services_to_sa import process_services


column_map = {
    "Date": {"columnLetter": "A", "columnIndex": 0},
    "Title": {"columnLetter": "B", "columnIndex": 1},
    "Scripture": {"columnLetter": "C", "columnIndex": 2},
    "Speaker": {"columnLetter": "D", "columnIndex": 3},
    "Series": {"columnLetter": "E", "columnIndex": 4},
    "GoogleDriveAudioID": {"columnLetter": "F", "columnIndex": 5},
    "ServiceType": {"columnLetter": "G", "columnIndex": 6},
    "UploadedDate": {"columnLetter": "H", "columnIndex": 7},
    "AudioDeleted": {"columnLetter": "I", "columnIndex": 8},
    "Notes": {"columnLetter": "J", "columnIndex": 9},
}


def run(sa_api_access_key, sa_broadcaster_id):
    date_mapping = column_map["Date"]
    title_mapping = column_map["Title"]
    scripture_mapping = column_map["Scripture"]
    speaker_mapping = column_map["Speaker"]
    series_mapping = column_map["Series"]
    gdrive_audio_id_mapping = column_map["GoogleDriveAudioID"]
    service_type_mapping = column_map["ServiceType"]
    uploaded_date_mapping = column_map["UploadedDate"]
    audio_deleted_mapping = column_map["AudioDeleted"]
    notes_mapping = column_map["Notes"]
    sheets_service = init_google_sheets()
    result = (
        sheets_service.spreadsheets()
        .values()
        .get(spreadsheetId=SERVICES_SHEET_ID, range=f"{SERVICES_SHEET_NAME}")
        .execute()
    )
    rowNum = 2
    rows = result.get("values", [])
    services = []
    for row in rows:
        if row[date_mapping["columnIndex"]] != "Date":
            if (
                not row[date_mapping["columnIndex"]]
                and not row[title_mapping["columnIndex"]]
                and not row[scripture_mapping["columnIndex"]]
                and not row[speaker_mapping["columnIndex"]]
                and not row[series_mapping["columnIndex"]]
                and not row[gdrive_audio_id_mapping["columnIndex"]]
                and not row[service_type_mapping["columnIndex"]]
                and not row[uploaded_date_mapping["columnIndex"]]
            ):
                # Entirely empty row, no more rows to process
                break
            elif row[uploaded_date_mapping["columnIndex"]]:
                # This row was already uploaded
                rowNum = rowNum + 1
                continue
            elif (
                not row[date_mapping["columnIndex"]]
                or not row[title_mapping["columnIndex"]]
                or not row[speaker_mapping["columnIndex"]]
                or not row[gdrive_audio_id_mapping["columnIndex"]]
                or not row[service_type_mapping["columnIndex"]]
            ):
                # This row does not have all required information
                update_cell(
                    sheets_service,
                    [
                        "Does not have required data. Missing Date, Title, Speaker, GoogleDriveAudioID, or ServiceType."
                    ],
                    "Notes",
                    rowNum,
                )
                rowNum = rowNum + 1
                continue

            try:
                date_object = datetime.strptime(
                    row[date_mapping["columnIndex"]], "%m/%d/%Y"
                )
            except ValueError as e:
                update_cell(
                    sheets_service,
                    [f"Invalid date. Should be like: 3/17/2024. --> {e}"],
                    "Notes",
                    rowNum,
                )
                rowNum = rowNum + 1
                continue
            sermon_title = row[title_mapping["columnIndex"]]
            scripture = row[scripture_mapping["columnIndex"]]
            preacher = row[speaker_mapping["columnIndex"]]
            series_name = row[series_mapping["columnIndex"]]
            google_drive_audio_id = row[gdrive_audio_id_mapping["columnIndex"]]
            day_part_tag = row[service_type_mapping["columnIndex"]]
            uploaded_date = row[uploaded_date_mapping["columnIndex"]]
            audio_deleted = row[audio_deleted_mapping["columnIndex"]]

            # Only process if we have all required information
            if (
                not uploaded_date
                and date_object
                and sermon_title
                and preacher
                and google_drive_audio_id
                and day_part_tag
            ):
                services.append(
                    [
                        date_object,
                        sermon_title,
                        scripture,
                        preacher,
                        series_name,
                        google_drive_audio_id,
                        day_part_tag,
                        rowNum,
                    ]
                )
                # Remove any old notes
                update_cell(sheets_service, [""], "Notes", rowNum)

            rowNum = rowNum + 1

    process_services(
        services,
        sa_api_access_key,
        sa_broadcaster_id,
        sheets_service,
        update_uploaded_date,
        None,  # Currently doesn't work: update_audio_deleted
    )


def update_cell(sheets_service, value, columnName, rowNum):
    try:
        body = {"values": [value]}
        columnLetter = column_map[columnName]["columnLetter"]
        result = (
            sheets_service.spreadsheets()
            .values()
            .update(
                spreadsheetId=SERVICES_SHEET_ID,
                range=f"{SERVICES_SHEET_NAME}!{columnLetter}{rowNum}",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
    except Exception as ex:
        print(
            f"Update services spreadsheet failed: {columnName} column. Row #: {rowNum}. --> {ex}"
        )


def update_uploaded_date(sheets_service, uploaded_date, rowNum):
    update_cell(sheets_service, [uploaded_date.__str__()], "UploadedDate", rowNum)


def update_audio_deleted(sheets_service, rowNum):
    update_cell(sheets_service, ["Yes"], "AudioDeleted", rowNum)


if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("SA_API_ACCESS_KEY"), os.getenv("SA_BROADCASTER_ID"))
    run(os.getenv("SA_API_ACCESS_KEY"), os.getenv("SA_BROADCASTER_ID"))

    # # Take API access keys for SA and Google as command line args
    # #       Later on I may change to include it as a GitHub secret and have an action run this
    # parser = argparse.ArgumentParser(
    #     prog="Blessed Hope - SermonAudio Importer",
    #     description="Imports old sermons into SermonAudio",
    # )
    # parser.add_argument("-s", "--sermonaudio", help="Your SermonAudio API key")
    # parser.add_argument("-b", "--broadcasterid", help="Your SermonAudio Broadcaster ID")

    # args = parser.parse_args()
    # print(args.sermonaudio, args.broadcasterid)
    # run(args.sermonaudio, args.broadcasterid)
