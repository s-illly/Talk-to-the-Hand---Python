import serial
import time
import speech_recognition as sr

arduino = serial.Serial(port='COM3',   baudrate=115200, timeout=.1)

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something \n")
    audio = r.listen(source)

try:
    value = r.recognize_google(audio)
    print("You said " + value)
    # send over to arduino
    arduino.write(bytes(value, 'ASCII'))
    time.sleep(0.05)
    data = arduino.readline()

except sr.UnknownValueError:
    print("Oops! Didn't catch that")
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


except KeyboardInterrupt:
    pass






