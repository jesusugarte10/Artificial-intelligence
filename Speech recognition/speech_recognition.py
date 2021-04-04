import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say somehting: ")
    audio = recognizer.listen(source)

print("You said:")
print(recognizer.recognize_google(audio))