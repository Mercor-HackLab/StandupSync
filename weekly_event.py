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

    performance_data = {}

    for event in events:
        attendees = event.get('attendees', [])
        for attendee in attendees:
            email = attendee.get('email')
            if email not in performance_data:
                performance_data[email] = {'total_duration': 0, 'num_events': 0}
            duration = event.get('duration', EVENT_DURATION)
            performance_data[email]['total_duration'] += duration
            performance_data[email]['num_events'] += 1

    sorted_performance_data = sorted(performance_data.items(), key=lambda x: x[1]['total_duration'], reverse=True)

    top_performers = sorted_performance_data[:3]  # Select the top 3 performers

    for email, data in top_performers:
        total_duration = data['total_duration']
        num_events = data['num_events']
        print(f"Performing GPT analysis for top performer - Email: {email}, Total Duration: {total_duration} minutes, Number of Events: {num_events}")
        prompt = f"Extract insights, summary, and action items for the top performer with email: {email}"
        gpt_result = askGPT(prompt)
        print(gpt_result)


    
