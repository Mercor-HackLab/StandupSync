import speech_recognition as sr
from chatGPT import askGPT
import pyaudio
import wave
import keyboard
from secret_key import AZURE_KEY
from google_calendar_integration import send_calendar_notification
from languages import languages

MICROPHONE = 0 
AUDIOSTREAM = 2
FORMAT = pyaudio.paInt16  
CHANNELS = 1              
RATE = 44100             
CHUNK = 1024              
RECORD_SECONDS = 0        
WAVE_OUTPUT_FILENAME = "output.wav"
LANGUAGE_INPUT = "en-US"

def speechToText(device):
    print("Listening ...... ")
    print("Press q to stop recording ")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK,input_device_index=device)
    frames = []

    print("Recording started...")
    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        if keyboard.is_pressed("q"):
            print("done ....")
            break
        if RECORD_SECONDS and len(frames) / (RATE / CHUNK) >= RECORD_SECONDS:
            break

    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Audio saved to", WAVE_OUTPUT_FILENAME)


def audioToText():
    r = sr.Recognizer()
    try : 
        with sr.AudioFile('output.wav') as src : 
            audio = r.record(src)
    except sr.RequestError as e:
        print("Could not request results from Azure Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        print("Unable to recognize speech")

    try: 
        text = r.recognize_azure(audio,key=AZURE_KEY,language=LANGUAGE_INPUT, location='centralindia')
        return text
    except sr.RequestError as e:
        print("Could not request results from Azure Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        
    return ""


def main():
    while True: 
        print("Available Languages:")
        for index, language in enumerate(languages, start=1):
            print(f"{index}. {language}")

        selected_language = int(input("Enter the number corresponding to your preferred language: "))
        if selected_language < 1 or selected_language > len(languages):
            print("Invalid input! Please try again.")
        else:
            language_name = list(languages.keys())[selected_language - 1]
            language_code = languages[language_name]
            LANGUAGE_INPUT = language_code
            print(f"Selected language: {language_name}")
        
        final_text = ""
        print("""
            Welcome to DSM Handler : 
            Enter 1 to Record from your Microphone 
            Enter 2 to Record from Standard Audio Output 
            Enter 3 to Exit
        """)


        choice = input("Your Choice: ")

        if choice == '1' : 
            print("Taking Audio from Microphone as an Input")
            speechToText(MICROPHONE)
 
        elif choice == '2' : 
            print("Taking Audio from Input Stream")
            speechToText(AUDIOSTREAM)
            
        elif choice == '3':
            print("Exiting the program...")
            break

        else : 
            print("Invalid Choice. Please try again.")
            continue

        final_text = audioToText()

        if final_text == "" or final_text is None:
            print("No Text to process")
        else: 
            print("Final Transcribed Text:", final_text)
            final_result = askGPT(f"Extract insights, summary, and action items from the transcription of a daily standup meeting (DSM): {final_text}")
            print(final_result)
            send_calendar_notification(final_result)


if __name__ == "__main__":
    main()
