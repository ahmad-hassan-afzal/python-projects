import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import requests

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0])

engine.setProperty('rate', 125)

def speak(audio):
    print('>>',audio)
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(">> Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4500
        audio = r.listen(source)
    try:
        print(">> Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("\t\t\t\t>>", query)
    except Exception:  
        speak("Say that again please...")  
        return "None"
    return query

def searchOnGoogle(query):
    speak('Here\'s what i found on google')
    webbrowser.open('https://www.google.com/search?q='+query)

def playOnYoutube(query):
    speak('Here\'s what i found on Youtube')
    webbrowser.open('https://www.youtube.com/results?search_query='+query.replace(' ', '+'))

def tellAJoke():
    res = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
    if res.status_code == 200:
        speak("Okay. Here's one")
        speak(str(res.json()['joke']))
    else:
        speak('Oops!I ran out of jokes')

def main():
    time = ''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        time = 'Morning'
    elif hour >=12 and hour <18:
        time = 'Afternoon'
    else:
        time = 'Evening'
    speak('Good '+time+'. This is Alex, How can i help?')
    
    while True:
        query = listen().lower()

# If you want to skip listen function Uncomment below lines one by one
        
        # query = "google pak vs eng"
        # query = "pak vs eng live on youtube"
        # query = 'Allama Iqbal wikipedia'
        # query = 'open drive'
        # query = 'open youtube'
        # query = 'open classroom'
        # query = 'open stack overflow'
        # query = 'what's the time'
        # query = 'tell me a joke'
        # query = 'goodbye'
        
        if 'open drive' in query or 'open my drive' in query:
            webbrowser.open('https://drive.google.com/drive/')
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'open stack overflow' in query:
            webbrowser.open('https://www.stackoverflow.com')
        elif 'open classroom' in query:
            webbrowser.open('https://classroom.google.com/drive/')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia.')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia: ')
            print(results)
            speak(results)

        elif 'google' in query:
            query = query.replace("google", "")
            speak('Searching Google for ' + query)
            searchOnGoogle(query)
        elif 'on youtube' in query:
            query = query.replace("on youtube", "")
            speak('Searching Youtube for ' + query)
            playOnYoutube(query)

# Some Extra Functions I added After presentation

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'tell me a joke' in query:
            tellAJoke()
        elif 'bye' in query or 'goodbye' in query:
            speak('Goodbye!')
            break        
    return
main()