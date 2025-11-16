import speech_recognition as sr
import pyttsx3
import os
import datetime
import wikipedia
import webbrowser
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function for telling operations
def speak(audio):   
    engine.say(audio)
    engine.runAndWait()

def openWesite(url,command):
    speak(f"Opening {command}")
    webbrowser.open(url)


# Function for Wish me(eg. Good morning, Good afternoon)
def wishme():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning sir")
    elif current_hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am Ghost, how may I help you")

# Function for take commands from commander(like you :-)😂
def takeCommand():
    """Listen to the user's command and return as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

if __name__ == "__main__":

    # calling wishme function 
    wishme()

    # while loop for continue listening
    while True:
        query = takeCommand().lower()
        print('COMMAND---',query)
        if not query:
            continue

        # May ask Wikipedia as suffix or prefix to excute this code -- 
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("I think there is an error. I can't able to connect and fetch data from wikipedia. ")

        # This code open python on   
        elif "python" in query:
            openWesite('https://www.python.org/','python')
            # speak("Opening Python.org website")
            # webbrowser.open('https://www.python.org/')

        elif "youtube" in query:
            openWesite('https://www.youtube.com/','Youtube')

            # speak("Opening YouTube")
            # webbrowser.open('https://www.youtube.com/')

        elif "whatsapp" in query:
            speak("Opening WhatsApp")
            webbrowser.open('https://web.whatsapp.com/')

        elif "stack overflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com/")

        elif "spotify" in query:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com/")
        
        elif "exit" in query:
            speak("Thanks for talking to me")
            break
        
        elif "code" in query:
            speak("Opening VS Code")
            # ---Path to VS code---------
            # path = "C:\\vs_cdoe"
            os.startfile(path)
        
        elif "music" in query:
            speak("Opening music")
            # ---Path to music ---------
            # path = "C:\\music_file"
            os.startfile(path)

        elif "time" in query:
            speak(f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}")

        elif "date" in query:
            speak("Today's date is " + datetime.datetime.now().strftime('%Y-%m-%d'))

        elif "joke" in query:
            speak("Searching jokes")
            joke = pyjokes.get_joke(language='en', category='neutral')
            speak(joke)

        elif query == None:
            speak("Sorry, I didn't understand that from if else.")
