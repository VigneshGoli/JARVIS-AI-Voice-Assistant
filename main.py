#Gurthupetkoo bayyyaa
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
# def read_variable_from_file(filename, variable_name):
#     variables = {}
#     with open(filename, "r") as file:
#         exec(compile(file.read(), filename, 'exec'), variables)
#     return variables.get(variable_name)
#
# # Specify the filename of file1.py and the variable you want to access
# filename_file1 = "Whether API.py"
# variable_name = "POP"
# my_variable = read_variable_from_file(filename_file1, variable_name)
#
# # Now you can use my_variable in file2.py
# print(my_variable)

# my_variable = read_variable_from_file1(filename_file1)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hr=int(datetime.datetime.now().hour)
    if(hr>=0 and hr<12):
        speak("Good Morning Sir")
    elif(hr>=12 and hr<=3):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("How may I help you today?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except  Exception as e:
        speak("Can you please Repeat?")
        return "None"
    return query
def sendEmail(to,what):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('22r21a05e5@mlrit.ac.in','spidey@2005')
    server.sendmail('22r21a05e5@mlrit.ac.in',to,what)
    server.close()
if __name__ == '__main__':
    speak("Hello Sir. I am Jarvis, How may I assist you today??")
    i=1
    while(i==1):
        query = takeCommand().lower()
        # The Real Excecution
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(result)
            print(result)
        elif 'open youtube' in query:
            speak("Yes Sir, Opening")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Yes Sir, Opening Google...")
            webbrowser.open("google.com")
        elif ('homepage' or 'home page') in query:
            speak("Opening...")
            webbrowser.open("https://mlrit.ac.in/")
        elif 'open instagram' in query:
            speak("Yes Sir")
            webbrowser.open("www.instagram.com")
        elif 'play music' in query:
            speak("Just a second Sir")
            musicDir = 'C:\Music'
            songs = os.listdir(musicDir)
            print(songs)
            os.startfile(os.path.join(musicDir, songs[0]))
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("Sir, The time is")
            speak(time)
            print(time)
        elif 'open whatsapp' in query:
            speak("Okay Boss")
            whatsappDir = "C:\\Users\\goliv\\OneDrive\\Desktop\\WhatsApp"
            os.startfile(whatsappDir)
        elif 'email' in query:
            try:
                speak("Whom Do you want me to mail?")
                whom = takeCommand()
                if 'vignesh' in whom:
                    to = 'golivignesh@gmail.com'
                else:
                    to = 'anothervignesh@gmail.com'
                speak("What do you  want  to write?")
                what = takeCommand()
                sendEmail(to, what)
                speak("Email has been Sent sir.")
            except Exception as e:
                print(e)
                print("Sorry sir. There might be an Error in sending the mail.")
        elif 'stop'  in query:
            speak("Okay Boss. Have a Nice Day")
            i=0