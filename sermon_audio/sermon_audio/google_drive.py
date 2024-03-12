import json
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.auth.transport import requests as google_requests
import requests


SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
SERVICES_SHEET_ID = "18s-dXHcgDaquz5crSvdtnOHkMcxEFITY6IW-ocVSos4"
SERVICES_SHEET_NAME = "UploadRecord"


def get_google_creds():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, "credentials.json")

    credentials = service_account.Credentials.from_service_account_file(path, scopes=SCOPES)
    return credentials


def init_google_drive():
    credentials = get_google_creds()
    drive_service = build('drive', 'v3', credentials=credentials)

    return drive_service
    

def init_google_sheets():
    credentials = get_google_creds()
    spreadsheet_service = build('sheets', 'v4', credentials=credentials)

    return spreadsheet_service
