import os.path 
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import datetime
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']

DSMSummary = '''Swapmil: raised the pr for feature 1
Sanidhiya: raised the pr for feature 2
Aparna: raised the pr for feature 3
'''


def get_current_datetime():
    return datetime.datetime.now(datetime.timezone.utc)

def get_current_datetime_in_local_timezone():
    current_datetime_utc = get_current_datetime()
    local_timezone = pytz.timezone('Asia/Kolkata')
    return current_datetime_utc.astimezone(local_timezone)

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try: 
        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': 'DSM',
            'location': 'Bengaluru, India',
            'description': DSMSummary,
            'start': {
                'dateTime': get_current_datetime_in_local_timezone().isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': (get_current_datetime_in_local_timezone() + datetime.timedelta(minutes=30)).isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {
                    'email': 'sanidhiyafirefox123@gmail.com'
                },
                {
                    'email': 'aparnagoyal.0003@gmail.com'
                }
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()

        print('Event created: %s' % (event.get('htmlLink')))

        
    except HttpError as err:
        print("An error occured:", err)

if __name__ == '__main__':
    main()