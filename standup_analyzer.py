import logging
import datetime as dt
from chatGPT import askGPT
from googleapiclient.errors import HttpError
from google_calendar_integration import *

def analyze_weekly_data():
    creds = authorize_google_calendar()
    if not creds or not creds.valid:
        logging.error('Failed to obtain valid credentials for Google Calendar.')
        return

    service = build('calendar', 'v3', credentials=creds)
    start_datetime = get_current_datetime_in_local_timezone() - dt.timedelta(days=8)
    end_datetime = get_current_datetime_in_local_timezone() + dt.timedelta(hours=5)

    try:
        events_result = service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start_datetime.isoformat(),
            timeMax=end_datetime.isoformat(),
            maxResults=2500,  
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

        prompt = f"What are the areas of improvement for each employee individually to perform better based on the following DSM events be gender netural:\n{data}\n"
        gpt_result = askGPT(prompt)
        print("\nAreas of Improvement for Employees:")
        print(gpt_result)
        
        # answer user question
        input_question = input("\nDo you have any questions for me?\n")
        prompt = [f"\n{input_question}\n based on  this data {data}\n"]
        gpt_result2 = askGPT(prompt)
        print("Answer:",gpt_result2)
    
    except HttpError as err:
        logging.error('An error occurred while fetching events from Google Calendar: %s', err)


# if __name__ == "__main__":
#     analyze_weekly_data()