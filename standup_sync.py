import speech_recognition as sr
from chatGPT import askGPT
import keyboard

MICROPHONE = 0 
AUDIOSTREAM = 2

def audioToText(device):
    r = sr.Recognizer()
    final_text = ""
    stop = False 
    print("Press q button to stop recording.. ")
    while True: 
        try : 
            with sr.Microphone(device_index=device) as src : 
                audio = r.listen(src)
                if keyboard.read_key() == "q":
                    stop = True 
                    raise UserWarning
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except UserWarning as e:
            print("User has pressed stop button")
        

        try: 
            text = r.recognize_google(audio)
            print(text, end = ' ')
            final_text += " " + text
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        
        if stop: break

    return final_text


def main():
    while True: 
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
            final_text = audioToText(MICROPHONE)

        elif choice == '2' : 
            print("Taking Audio from Input Stream")
            final_text = audioToText(AUDIOSTREAM)
            
        elif choice == '3':
            print("Exiting the program...")
            break

        else : 
            print("Invalid Choice. Please try again.")
            continue

        if final_text == "":
            print("No Text to process")
        else: 
            print("Final Transcribed Text:", final_text)
            print(askGPT(f"Extract insights, summary, and action items from the transcription of a daily standup meeting (DSM): {final_text}"))


if __name__ == "__main__":
    main()







