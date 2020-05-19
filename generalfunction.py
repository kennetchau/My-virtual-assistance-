import speech_recognition as sr


def sR():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Speak anything: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry could not recognize you voice")
            return ""



def getnumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please input an integer!")
            continue
        else:
            return userInput
            break



