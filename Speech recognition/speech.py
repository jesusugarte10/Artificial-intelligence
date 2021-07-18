import speech_recognition
from io import BytesIO
from gtts import gTTS as spk
import sys
from neuralintents import GenericAssistant

recognizer = speech_recognition.Recognizer()
mp3_fp = BytesIO()

todo_list = ['Finish Assignment 2', 'Move Out', 'Set up Meeting']

def create_note():
    global recognizer

    spk("What do you want to write onto your note?", lang='en').write_to_fp(mp3_fp)
    done = False
    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                spk("Choose filename!", lang='en').write_to_fp(mp3_fp)

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(f'{filename}.txt', 'w') as f:
                f.write(note)
                done = True
                
                spk(f"I successfully created the note {filename}", lang='en').write_to_fp(mp3_fp)

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            spk(f"I did not understand you! Please try again!", lang='en').write_to_fp(mp3_fp)

def add_todo():

    global recognizer
    done = False

    spk(f"What todo do you want to add?", lang='en').write_to_fp(mp3_fp)

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

            spk(f"I added {item} to the to do list!", lang='en').write_to_fp(mp3_fp)   

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            spk("I did not understand. Please try again!", lang='en').write_to_fp(mp3_fp)  

def show_todos():

    spk("The items on your to do list are the following", lang='en').write_to_fp(mp3_fp)  
    for item in todo_list:
        spk(item, lang='en').write_to_fp(mp3_fp) 

def hello():
    spk("Hello. What can I do for you?", lang='en').write_to_fp(mp3_fp)  

def quit():
    spk("Bye", lang='en').write_to_fp(mp3_fp)  
    sys.exit(0)

mappings = {
    "greetings": hello,
    "create_note": create_note,
    "add_todo": add_todo, 
    "show_todos": show_todos,
    "exit": quit
}

#load model?
print('test1')
assistant = GenericAssistant('intents.json', intent_methods=mappings)
print('test2')
assistant.train_model()
#Save Model here

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()
        
        assistant.request(message)

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
