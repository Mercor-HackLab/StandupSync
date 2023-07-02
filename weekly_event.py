import os.path
import logging
import datetime as dt
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def analyze_weekly_data():
    creds = authorize_google_calendar()
    if not creds or not creds.valid:
        logging.error('Failed to obtain valid credentials for Google Calendar.')
        return

    service = build('calendar', 'v3', credentials=creds)
    start_datetime = get_current_datetime_in_local_timezone() - dt.timedelta(days=7)
    end_datetime = get_current_datetime_in_local_timezone()

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_datetime.isoformat(),
        timeMax=end_datetime.isoformat(),
        maxResults=2500,  # Adjust the number of events to retrieve
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        print('No events found for the past week.')
        return

    data = ''
    for event in events:
        print(event)
        summary = event.get('summary')
        start_date = event.get('start').get('dateTime')
        data += f"Event Summary: {summary}\n"
        data += f"Event Start Time: {start_date}\n"

    prompt = f"Extract Top Performer based on the {data}."
    gpt_result = askGPT(prompt)
    print("Top Performer: ", gpt_result)


    
