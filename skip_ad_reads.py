from pynput.keyboard import Key, Controller
keyboard = Controller()

# detect ad read
import speech_recognition as sr
r = sr.Recognizer()

while(True):
    with sr.Microphone() as source:
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        audio_text = r.recognize_google(audio)
        if("brought to you by" in audio_text):
            # fast-forward 16 presses * 5 sec/press
            for i in range (0, 16):
                keyboard.press(Key.right)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# TODO: lessen delay before fast-forwarding, halt the program eventually
