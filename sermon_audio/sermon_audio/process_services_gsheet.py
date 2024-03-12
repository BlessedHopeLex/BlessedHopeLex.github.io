import argparse
from datetime import date, datetime

from google_drive import init_google_drive, init_google_sheets, SERVICES_SHEET_ID, SERVICES_SHEET_NAME
from upload_services_to_sa import process_services


def run(sa_api_access_key, sa_broadcaster_id):
    sheets_service = init_google_sheets()
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=SERVICES_SHEET_ID,
        range=f"{SERVICES_SHEET_NAME}"
    ).execute()
    rowNum = 2
    rows = result.get('values', [])
    services = []
    for row in rows:
        if row[0] == "":
            break
        if row[0] != "Date":
            date_object = datetime.strptime(row[0], "%m/%d/%Y")
            sermon_title = row[1]
            scripture = row[2]
            preacher = row[3]
            series_name = row[4]
            google_drive_audio_id = row[5]
            day_part_tag = row[6]
            uploaded_date = row[7]
            audio_deleted = row[8]

            if not (uploaded_date and audio_deleted == "No"):
                services.append([
                    date_object,
                    sermon_title,
                    scripture,
                    preacher,
                    series_name,
                    google_drive_audio_id,
                    day_part_tag,
                    rowNum
                ])

            rowNum = rowNum + 1

    process_services(
        services,
        sa_api_access_key,
        sa_broadcaster_id,
        sheets_service,
        update_uploaded_date,
        None  # update_audio_deleted,
    )


def update_uploaded_date(sheets_service, uploaded_date, rowNum):
    try:
        values = [
            [
                uploaded_date.__str__()
            ],
        ]
        body = {"values": values}
        result = (
            sheets_service.spreadsheets()
            .values()
            .update(
                spreadsheetId=SERVICES_SHEET_ID,
                range=f"{SERVICES_SHEET_NAME}!H{rowNum}",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
    except Exception as ex:
        print(f"Update services spreadsheet failed: UploadedDate column. Row #: {rowNum}. --> {ex}")


def update_audio_deleted(sheets_service, rowNum):
    try:
        values = [
            [
                "Yes"
            ],
        ]
        body = {"values": values}
        result = (
            sheets_service.spreadsheets()
            .values()
            .update(
                spreadsheetId=SERVICES_SHEET_ID,
                range=f"{SERVICES_SHEET_NAME}!I{rowNum}",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
    except Exception as ex:
        print(f"Update services spreadsheet failed: AudioDeleted column. Row #: {rowNum}. --> {ex}")


if __name__ == "__main__":
    # Take API access keys for SA and Google as command line args
    #       Later on I may change to include it as a GitHub secret and have an action run this
    parser = argparse.ArgumentParser(
        prog="Blessed Hope - SermonAudio Importer",
        description="Imports old sermons into SermonAudio",
    )
    parser.add_argument("-s", "--sermonaudio", help="Your SermonAudio API key")
    parser.add_argument("-b", "--broadcasterid", help="Your SermonAudio Broadcaster ID")

    args = parser.parse_args()
    print(args.sermonaudio, args.broadcasterid)
    run(args.sermonaudio, args.broadcasterid)