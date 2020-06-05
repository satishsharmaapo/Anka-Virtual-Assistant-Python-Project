#import api pyttsxs3 |  install using " pip install pyttsx3"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib
import wolframalpha

 

 
#initialize module sapi5 engine basically it is used to take the voice from windows pre-installed voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)

#define speak mdethod


def speak(audio):
    engine.say(audio)   # engine will activate to say
    engine.runAndWait()  # engine will wait ad run


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am cute anka  how can i help you")
#install | "pip install speechRecognition"

def takeCommand():
    # it takes microphone input from the users and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query.lower()}\n")
    except Exception as e:
        #print(e)
        print("Say that again Please")
        return "None"
    return query

 

        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
     
    wishMe()
    while True:
        query = takeCommand().lower()
         
    #speak function
        print(query)
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia.....")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dri= 'D:\\mymusic\\songs\\favourate1'
            songs=os.listdir(music_dri)
            print(songs)
            os.startfile(os.path.join(music_dri,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Windows\\notepad.exe"
            os.startfile(codePath)

        elif 'email to anka' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")   
        elif 'weather forecast' in query:
            
            driver = webdriver.Chrome()

            # uncomment if using Firefox
            # driver = webdriver.Firefox()

            # Replace space from - For example new-york.
            speak("tell me your City name : ")
            city = takeCommand()            
            speak("ok      Here is you weather report")
            try:
                
                driver.get("https://www.weather-forecast.com/locations/"+city.capitalize()+"/forecasts/latest")
                speak(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
            except:                 
                speak("Something went wrong")


# pip install pipwin 
# pipwin install pyaudio
# pip install -U selenium        - for webdriver 
# pyinstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5 --hidden-import=urllib3 --onefile anka.py
