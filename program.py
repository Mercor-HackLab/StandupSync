import speech_recognition as sr
from chatGPT import askGPT

MICROPHONE = 0 
AUDIOSTREAM = 2


r = sr.Recognizer()
final_text = ""

def audioToText(device):
    global final_text
    try : 
        with sr.Microphone(device_index=device) as src : 
            audio = r.listen(src)
    except Exception as e:
        print("Error Occured",e) 

    try: 
        text = r.recognize_google(audio)
        print(text, end = ' ')
        final_text += " " + text
    except Exception as e:
        print("Error Occured",e) 




while True: 
    final_text = ""

    print("""
        Welcome to DSM Handler : 
        Enter 1 to Record from your Microphone 
        Enter 2 to Record from Standard Audio Output 
    """)


    choice = input("Your Choice : ")

    if choice == '1' : 
        print("Taking Audio from Mic as an Input")
        audioToText(MICROPHONE)

    elif choice == '2' : 
        print("Taking Audio from input stream")
        audioToText(AUDIOSTREAM)
           
    else : 
        print("Wrong Choice Entered , Please try again")

    print(final_text)
    print(askGPT(f"Please give some recommendations this text and give score out of 10 {final_text}"))
    








