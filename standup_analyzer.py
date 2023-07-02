import logging
import datetime as dt
from chatGPT import askGPT
from google_calendar_integration import *

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
        summary = event.get('summary')
        if(summary == 'DSM'):
            description = event.get('description')
            start_date = event.get('start').get('dateTime')
            data += f"Event Start Time: {start_date}\n"
            data += f"Event Description: {description}\n"

    prompt = f"Who is the top Performer based on the {data} ."
    gpt_result = askGPT(prompt)
    print("Top Performer: ", gpt_result)

# if __name__ == "__main__":
#     analyze_weekly_data()