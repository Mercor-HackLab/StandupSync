import os.path
import logging
import datetime as dt
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'credentials.json'
CALENDAR_ID = 'primary'
ATTENDEE_EMAILS = [
    'sanidhiyafirefox123@gmail.com',
    'aparnagoyal.0003@gmail.com',
    'swapnilssingh06@gmail.com'
]
TIMEZONE = 'Asia/Kolkata'
EVENT_DURATION = 30  # in minutes

logging.basicConfig(level=logging.INFO)

def get_current_datetime():
    return dt.datetime.now(pytz.utc)

def get_current_datetime_in_local_timezone():
    local_timezone = pytz.timezone(TIMEZONE)
    return get_current_datetime().astimezone(local_timezone)

def authorize_google_calendar():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return creds

def create_calendar_event(service, summary, description, start_datetime, duration, timezone, attendees):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': (start_datetime + dt.timedelta(minutes=duration)).isoformat(),
            'timeZone': timezone,
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [{'email': email} for email in attendees],
    }

    try:
        event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        logging.info('Event created: %s', event.get('htmlLink'))
    except HttpError as err:
        logging.error('An error occurred while creating the event: %s', err)

def send_calendar_notification(DSMSummary):
    creds = authorize_google_calendar()
    if not creds or not creds.valid:
        logging.error('Failed to obtain valid credentials for Google Calendar.')
        return

    service = build('calendar', 'v3', credentials=creds)
    start_datetime = get_current_datetime_in_local_timezone()
    summary = 'DSM'
    description = DSMSummary

    create_calendar_event(service, summary, description, start_datetime, EVENT_DURATION, TIMEZONE, ATTENDEE_EMAILS)

