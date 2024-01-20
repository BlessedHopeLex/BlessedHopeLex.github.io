import json
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.auth.transport import requests as google_requests
import requests


SCOPES = [
    'https://www.googleapis.com/auth/drive'
]


def get_google_creds():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, "credentials.json")

    credentials = service_account.Credentials.from_service_account_file(path, scopes=SCOPES)
    return credentials


def init_google_drive():
    credentials = get_google_creds()
    drive_service = build('drive', 'v3', credentials=credentials)

    return drive_service
