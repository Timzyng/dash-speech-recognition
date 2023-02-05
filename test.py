# Electrical Engineering
# Igboke Timothy chekwube
# 2019234030
# Project on API Speech to Text Recognition

import speech_recognition as sr

# Initialize a recognizer object:
r = sr.Recognizer()

# Use the Microphone to record audio:
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something...\nTry Saying\nHey Dash!")
    audio = r.listen(source)

# Use the recognize_google() method to perform speech recognition
DashSpeechRecognitionSystem = r.recognize_google(audio)
print("You said: " + dashSpeechRecognitionSystem)

# Add error handling to handle cases where the speech recognition fails
try:
    SpeechRecognitionSystem = r.recognize_google(audio)
    print("You said: " + DashSpeechRecognitionSystem)
except sr.UnknownValueError:
    print("Temple Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Temple Speech Recognition service; {0}".format(e))