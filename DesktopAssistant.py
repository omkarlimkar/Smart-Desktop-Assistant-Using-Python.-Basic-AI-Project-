import ctypes
import os
import subprocess
import pyttsx3  #pip install pyttsx3    
import datetime
import webbrowser
import pyjokes
import pywhatkit
import smtplib
import requests
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia    #pip install wikipedia
import winshell

#if any error occurs while importing any modules then refer to this video -> https://www.youtube.com/watch?v=x-BtaZDbQeo

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)  # engine will speak the audio string that we will pass
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning,Sir")
        


    elif hour >= 12 and hour <= 18:
        speak("Good afternoon,Sir")

    elif hour >= 18 and hour <= 21:
        speak("Good evening,Sir")

    else:
        speak("Have a good night,Sir")
    speak("How may I help you ?")


def takeCommand():
    """
    this function will take the command from the user and then process it accordingly to the need or
    it takes the microphone input from the user and gives a string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source, phrase_time_limit=4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        speak("didn't hear it clear, can you please say it again")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email', 'your_email_password')
    server.send('your_email', to, content)
    server.close()


if __name__ == '__main__':
    # speak("hello! how are you doing ")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("searching now")
            webbrowser.open("google.com")


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'open twitter' in query:
            webbrowser.open("twitter.com")


        elif 'open instagram' in query:
            webbrowser.open("instagram.com")


        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing..' + song)
            print(song)
            pywhatkit.playonyt(song)

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('current time is: ' + time)
            print(time)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)


        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)


        elif 'open code' in query:
            codePath = "C:\\Users\\OMKAR\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'email to abc' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "your_email"
                sendEmail(your_email , content)
                speak("Email has been sent! successfully")

            except Exception as e:
                print(e)
                speak("Sorry, Sir I couldn't send the email")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")


        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


        elif 'lock windows' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()


        elif "hibernate windows" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")


        elif 'shutdown windows' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "nova Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")


        elif 'stop' in query:
            speak("Thanks for giving me your time")
            exit()




