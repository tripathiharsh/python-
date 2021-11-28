import pyttsx3
import speech_recognition as sr
import microphone
import datetime
import wikipedia
import webbrowser
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def login():
    e=input("User Id:")
    
    if e=="deadpool":
        print("welcome")
    else:
        quit() 
login()
    



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        
    else:
        speak("Good Evening")
        
    speak("hey rupesh ,don't worry I am  cabel")
    
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshould = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        speak("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        
        
        query = takeCommand().lower() 
        
        
        
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open code club' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'chrome' in query:
            os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")   
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

                     
        
    
        elif 'who are you' in query:
           speak('I am your assistent')
           print('I am your assistent')
        elif 'zip it' in query:
            speak("buy rupesh ,I hope you should kill deadpool")
            
            quit()

        elif 'shutdown' in query:
            speak("ok I am going to shut whole rupeshindustris")
            os.system("shutdown /s /t 0")

        

