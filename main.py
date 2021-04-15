import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import webbrowser


r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            lucy_speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError():
            lucy_speak('Sorry, I did not get that.')
        except sr.RequestError():
            lucy_speak('Sorry my speech service is down')
        return voice_data

def lucy_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        lucy_speak('My name is Lucy')
    if 'what is the time' in voice_data:
        lucy_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lucy_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        lucy_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()
time.sleep(1)
lucy_speak('Hello, How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
