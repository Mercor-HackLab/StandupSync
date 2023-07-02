# StandupSync

StandupSync is a Python-based application that aims to automate the process of generating meeting transcripts and extracting important insights and tasks from daily standup meetings in offices. It utilizes speech-to-text conversion and a language model to provide an efficient and convenient solution for teams.

## Problem Statement
- Lack of comprehensive software for tracking and analyzing Daily Stand-Up Meetings (DSMs).
- Challenges in improving collaboration and individual contributions without systematic DSM insights. 
- Difficulty in identifying areas of improvement and tracking bug origins. 
- Manual analysis of DSMs leading to inefficiency in resource utilization. 
- Limited ability to generate actionable insights and performance metrics from DSM discussions.
- Difficulty in tracking meeting insights and providing timely feedback.

## Solution 
- Implemented routes and endpoints within the Flask-based API to handle audio processing, insights extraction, and summary generation. 
- Integrate the DSM transcription module to convert audio recordings into text using Azure speech-to-text API.
- Utilize the GPT API for natural language processing tasks and analysis..
- The API is fluent in US-English, Spanish and majority of our Indic-Regional languages as well.
- Seamlessly integrate with team members' Google Calendars to automatically add notes and reminders based on extracted DSM insights.

## Workflow
- User selects the preferred language.
- User chooses the audio input source (Microphone or Audio Stream).
- Audio is recorded and saved as a WAV file.
- Speech-to-text conversion is performed using the selected language and Azure Speech Recognition API.
- The transcribed text is processed using the GPT API to extract insights, summaries, and action items.
- The resulting text is sent to Google Calendar for event creation and notification.
- Enabling weekly analysis based on Google Calendar data.

## Tech Stack/ Methodology
- Python: For server-side development.
- Flask: For building the API server.
- OpenAI GPT API: For Natural Language Processing and Text Generation.
- Google Calendar API: For notes creation and notifications.
- SpeechRecognition Library: For speech-to-text conversion.
- JSON and RESTful API for data exchange. 
- Git for version control and collaborative development.

## Use Cases:
- Automated transcription and analysis of DSMs.
- Improved productivity and efficiency in meeting discussions. 
- Seamless integration with Google Calendar for event management. 
- Multilingual support for enhanced user experience.

## USPs
- Real-time Transcription 
- Multilingual Support 
- Accurate Speech-to-Text Conversion
- Intelligent Meeting Highlights 
- Google Calendar Integration
- Weekly Data Analysis
- Enhanced Efficiency

## Future Scope:
- Developing a  Interactive Dashboard
- Voice Assistant Integration
- Enhanced Scalability
- Custom Analysis Periods

## Acknowledgments
This project is inspired by the need to automate and streamline the process of daily standup meetings. We would like to express our gratitude to the developers and contributors of the libraries and APIs used in this project, which include the GPT API, speech_recognition library and Google Cloud services.