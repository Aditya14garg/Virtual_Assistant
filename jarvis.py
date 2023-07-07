import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = aa.Recognizer()

machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            listener.adjust_for_ambient_noise(origin)
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "")
                print(instruction)

    except aa.UnknownValueError:
        pass
    except aa.RequestError as e:
        print("Could not request from Google Speech Recognition service;{0}".format(e))
    return instruction


def play_Jarvis():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk("Current time" + time)

    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d /%m /%Y")
        talk("Today's date " + date)

    elif "how are you" in instruction:
        talk("I am fine, how about you")

    elif "what is your name" in instruction:
        print("I am Jarvis, What can i do for you?")

    elif "who is" in instruction:
        human = instruction.replace("who is", " ")
        info = wikipedia.WikipediaPage(human, 1)
        print(info)
        talk(info)

    elif "search" in instruction:
        human = instruction.replace("search", "")
        pywhatkit.search(human)

    else:
        talk("Please repeat")
        play_Jarvis()


play_Jarvis()
