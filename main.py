import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import webbrowser
from datetime import datetime

class user:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            lucy_speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            lucy_speak('I did not get that')
        except sr.RequestError:
            lucy_speak('Sorry, the service is down') # error: recognizer is not connected
        print(f"You: {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def lucy_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,10000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Lucy: {audio_string}") # print what assistant said
    os.remove(audio_file) # remove audio file


def respond(voice_data):
    # 1: greetings
    if there_exists(['hey','hi','hello']):
        greetings = [f"Hey, how can I help you {user_obj.name}", f"Hey, what's up? {user_obj.name}", f"I'm listening {user_obj.name}", f"How can I help you? {user_obj.name}", f"Hello {user_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        lucy_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if user_obj.name:
            lucy_speak("My name is Lucy.")
        else:
            lucy_speak("My name is Lucy. What's your name?")
    # 3: user name
    if there_exists(["my name is"]):
        user_name = voice_data.split("is")[-1].strip()
        lucy_speak(f"Okay, i will remember that {user_name}.")
        user_obj.setName(user_name) # remember name in user object

    # 4: greeting
    if there_exists(["how are you","how are you doing"]):
        lucy_speak(f"I'm very well, thanks for asking {user_obj.name}.")

    # 5: quotes
    if there_exists(["quote of the day"]):
        quotes = [f"Work until you no longer have to introduce yourself.", f"You’re braver than you believe, and stronger than you seem, and smarter than you think.", f"Don't stop until you are proud."]
        quote = quotes[random.randint(0,len(quotes)-1)]
        lucy_speak(quote)

    # 5: time
    if there_exists(["what's the time","tell me the time","what time is it","i need the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        lucy_speak(time)
    
    # 6: search
    if there_exists(["search"]):
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lucy_speak('Here is what I found for ' + search)

    # 7: location
    if there_exists(["find location"]):
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        lucy_speak('Here is the location of ' + location)
    
    # 8: open notepad
    if there_exists(["open notepad"]):
        os.system('notepad')
        lucy_speak('Done for you!')

    # 9: google
    if there_exists(["open google"]):
            webbrowser.open("google.com")
            lucy_speak("Here is google for you!")

    # 10: youtube
    if there_exists(["open youtube"]):
            webbrowser.open("www.youtube.com")
            lucy_speak("Here is youtube for you!")

    # 11: github
    if there_exists(["open github"]):
            webbrowser.open("https://www.github.com")
            lucy_speak("Here is github for you!")
    
    # 12: exiting
    if there_exists(["thank you","exit"]):
        lucy_speak('Goodbye')
        exit()
    

time.sleep(1)
lucy_speak('Hello, how can I help you?')
user_obj = user()
while 1:
    voice_data = record_audio() # get the voice input
    respond(voice_data) #respond