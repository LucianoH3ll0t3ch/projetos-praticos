import speech_recognition as sr
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
        perguntas = ['o que faço senhor deseja?','o que você quer agora ?','sabia que você é muito chato?']
        engine.say('o que faço agora mestre da computação? ')
        print(texto)
        #ptg.PAUSE=2
        if texto == "fecha cartomante":
            ptg.PAUSE=1
            ptg.click(461,751)
            ptg.click(327,210)
            time.sleep(2)
            ptg.click(1021,151)
            engine.runAndWait()
        elif texto == 'fechar novamente':
            ptg.click(327,210)
            ptg.click(1021,151)
            engine.runAndWait()
            #print('o que faço agora?')
        elif texto == 'enviar pics':
            ptg.click(578,639)
            time.sleep(1)
            ptg.write('/')
            time.sleep(1)
            ptg.write('pix')
            time.sleep(1)
            ptg.click(596,511)
            time.sleep(1)
            ptg.click(871,702)
            """ptg.click(578,639)
            ptg.press('enter')"""
            engine.runAndWait()
        elif texto == 'pics2':
            ptg.click(578,639)
            ptg.write('/')
            ptg.write('pix')
            ptg.click(595,531)
            ptg.click(578,639)
            ptg.press('enter')
            #ptg.click(871,702)
            engine.say(perguntas[1])
        elif texto == 'aguarde':
            time.sleep(120)
            engine.runAndWait()
        elif texto == 'promo 5':
            time.sleep(1)
            ptg.click(692,700)
            time.sleep(1)
            ptg.click(517,372)
            time.sleep(1)
            ptg.click(948,647)
            engine.say(perguntas[2])
            engine.runAndWait()
        elif texto == 'três perguntas':
            time.sleep(1)
            ptg.click(692,700)
            time.sleep(2)
            ptg.click(680,246)
            time.sleep(2)
            ptg.click(518,246)
            time.sleep(2)
            ptg.moveTo(320,455)
            time.sleep(2)
            ptg.scroll(-2000)
            time.sleep(2)
            ptg.click(948,647)
            time.sleep(2)
        elif texto == 'cliente':
            ptg.click(327,210)
            engine.say(perguntas[0])
            engine.runAndWait()
        elif texto == 'responda':
            ptg.click(578,639)
            ptg.write("Boa noite, meu anjo. Tudo bem? como posso melhorar seu dia? :)")
            ptg.press('enter')
            engine.say(perguntas[1])
            engine.runAndWait()
        elif texto == 'senha':
            time.sleep(1)
            ptg.click(692,700)
            ptg.click(680,246)
            time.sleep(2)
            ptg.click(518,246)
            time.sleep(2)
            ptg.moveTo(320,455)
            time.sleep(2)
        
