# StandupSync

StandupSync is a Python-based application that aims to automate the process of generating meeting transcripts and extracting important insights and tasks from daily standup meetings in offices. It utilizes speech-to-text conversion and a language model to provide an efficient and convenient solution for teams.

## Features
Record and transcribe audio from either a microphone or standard audio output.
Utilize Google's speech recognition service for accurate speech-to-text conversion.
Process the transcribed text using a language model to generate recommendations and assign a score.
Capture important insights, tasks, and reminders from the meeting and summarize them.
Integrate with Google Calendar to add the extracted tasks and reminders as events.

## Usage
1. Run the script:
`python standup_sync.py`

2. Choose the desired option from the menu:

Enter 1 to record audio from the microphone.
Enter 2 to record audio from the standard audio output.

3. Speak clearly and provide your updates or discuss topics during the meeting.

4. Once the audio recording is complete, the application will transcribe the speech to text and provide recommendations based on the input text.

5. Review the generated insights, tasks, and reminders, and if desired, the script can automatically add them as events to your Google Calendar.

## Acknowledgments
This project is inspired by the need to automate and streamline the process of daily standup meetings. We would like to express our gratitude to the developers and contributors of the libraries and APIs used in this project, which include the speech_recognition library and Google Cloud services.