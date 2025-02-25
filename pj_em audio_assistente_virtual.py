import pyautogui as ptg
import time


time.sleep(5)
ptg.scroll(-600)

"""import speech_recognition as sr
import pyaudio
import pyautogui as ptg
import time
import pyttsx3 as pttx

rec = sr.Recognizer()
print(sr.Microphone().list_microphone_names())
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    
    while True: 
        print("Pode falar que eu vou gravar")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
        engine = pttx.init()
        engine.say('o que faço agora? ')
        print(texto)
        #ptg.PAUSE=2"""
       
        