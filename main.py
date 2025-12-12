'''
changes to be made: have to be made compatible with laptop speakers!!!
have to optimise its listening and interpreting ability: google recogniser, its timeout value and phase time duration has to be adjusted




'''




import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():               #open basic websites
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):           #play music imported from music library
        song=c.lower().split(" ")[1]
        link=music_library.music[song]
        webbrowser.open(link)
    
        

if __name__=="__main__":
    speak("initialising jarvis......")
    while True:
        #listen for the wake word vish
        #obtain audio from microphone
        r=sr.Recognizer()
    
        
        #recognise speech using google
        print("Recognizing")
        try:
            with sr.Microphone() as source:  
                print("Listening.....")
                audio=r.listen(source,timeout=2,phrase_time_limit=2)
            wake_word=r.recognize_google(audio)
            if(wake_word.lower()=="jarvis"):
                speak("How can i help you today?")
                #listen for command
                with sr.Microphone() as source:  
                    print("Vish active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    process_command(command)
        except Exception as e:
            print(" error: {}".format(e))


