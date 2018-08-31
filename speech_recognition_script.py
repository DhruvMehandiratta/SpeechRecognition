# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


"""

import speech_recognition as sr
sr.__version__

import pyaudio as pa
pa.__version__
#pa is used for audio from microphone

r = sr.Recognizer()


harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
voice = r.recognize_google(audio)
print(voice)

