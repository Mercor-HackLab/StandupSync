import speech_recognition as sr
from chatGPT import askGPT

MICROPHONE = 0 
AUDIOSTREAM = 2

def audioToText(device):
    r = sr.Recognizer()
    final_text = ""

    try : 
        with sr.Microphone(device_index=device) as src : 
            audio = r.listen(src)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        print("Unable to recognize speech")

    try: 
        text = r.recognize_google(audio)
        print(text, end = ' ')
        final_text += " " + text
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        print("Unable to recognize speech")

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

        print("Final Transcribed Text:", final_text)
        print(askGPT(f"Please give some recommendations this text and give a score out of 10: {final_text}"))


if __name__ == "__main__":
    main()







