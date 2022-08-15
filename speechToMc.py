import speech_recognition as sr
import time
import pydirectinput
import pyautogui

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry i did not get that')
        except sr.RequestError:
            print('Service is down')
        return voice_data

def respond(voice_data):
    if 'walk forward' in voice_data:
        pydirectinput.keyDown('w')
    if 'walk backward' in voice_data:
        pydirectinput.keyDown('s')
    if 'jump' in voice_data:
        pydirectinput.press('space')
    if 'stop' in voice_data:
        pydirectinput.keyUp('w')
        pydirectinput.mouseUp(button='left')
        pydirectinput.keyUp('s')
    if 'pause' in voice_data:
        pydirectinput.press('escape')
    if 'inventory' in voice_data:
        pydirectinput.press('e')
    if 'hit' in voice_data:
        pydirectinput.click(button='left')
    if 'mine' in voice_data:
        pydirectinput.mouseDown(button='left')
    if 'place' in voice_data:
        pydirectinput.click(button='right')
    if 'left' in voice_data:   
        pydirectinput.move(-100, 0, 2)
    if 'sneak' in voice_data:
        pydirectinput.keyDown('shift')
    if 'stand' in voice_data:
        pydirectinput.keyUp('shift')

    if 'chat' in voice_data:
        message = record_audio('chat')
        pydirectinput.press('/')
        pyautogui.write(message)
        pydirectinput.press('enter')
    
    

time.sleep(0.2)
print('say something')
while 0.2:
    voice_data = record_audio()
    respond(voice_data)