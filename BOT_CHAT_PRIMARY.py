import customtkinter as ctk
import pyautogui as ptg
import time
import random

#BOT DE RESPOSTAS PARA O SISTEMA PRINCIPAL VALOR.BET/LAFA.BET
tela = ctk.CTk()
tela.geometry('400x400')
tempo = ctk.CTkEntry(tela, placeholder_text='time')
tempo.pack(pady=10)
resz = ['Hola señor. Si tiene problemas con un depósito que aún no ha sido acreditado, el plazo máximo para acreditar el depósito es de hasta 24 horas, si ya pasó la fecha límite, envíe una captura de pantalla de su recibo de pago y una captura de la pantalla del historial del deposit en la plataforma. Si su problema es un retiro que aún no ha sido acreditado, el plazo varía entre 15 minutos y 7 días. Si su retiro aún no se ha acreditado después de 7 días, envíeme una captura de pantalla de su historial de retiro. Si no puede solicitar el retiro, es posible que aún no haya completado la confirmación por correo electrónico. Para confirmar su dirección de correo electrónico, simplemente vaya a la página principal de nuestro sitio web, seleccione "Cuenta" y vaya a la sección "Mi perfil". Allí encontrarás el ícono "Enviar correo electrónico nuevamente", haz clic en él y sigue las instrucciones para verificar tu dirección de correo electrónico.',"Hola, ¿podrías darme más detalles sobre cómo puedo ayudarte? Si tu problema es un depósito, el la fecha límite es 24 horas después de la transferencia, la fecha límite de retiro es 7 días de procesamiento, se le preguntó sobre el bono, para utilizar el bono debe pasar por el rollover, si su pregunta es sobre el código promocional y envíe el código promocional por correo electrónico, si es otro problema por favor envíame una captura de pantalla del error y dime cuál es tu dirección de correo electrónico de registro, nos disculpamos por el inconveniente, estaremos revisando tu problema.",'Hola, si tienes algún problema con el depósito, ¿Podrías enviarme el recibo completo y el historial de depósitos que aparece en la plataforma, por favor?','Hola, ¿en qué podemos ayudarte? ¿Podrías enviarme más detalles?','Hola, te pedimos disculpas por el inconveniente, estaremos revisando tu problema, podrías enviarme imágenes con más detalles por favor y te ayudaré, si el problema es depósito, el plazo es el 24 horas después de la transferencia, la fecha límite para el retiro es de 7 días de procesamiento, se le preguntó sobre el bono, para usar el bono debe pasar por la transferencia, para obtener el código promocional y enviar el código promocional por correo electrónico','Hola, problemas con el retiro, ¿podría enviarme? el historial de retiros en la plataforma por favor, recordando que el período de retiro es de máximo 7 días y no puedes jugar mientras se procesa']
respostas = ['Hi sir. If you have problems with a deposit that has not yet been credited, the maximum period for the deposit to be credited is up to 24 hours, if it has already passed the deadline, please send a screenshot of your payment receipt and screenshot of history deposit in plataform please.If your problem is a withdrawal that has not yet been credited, the deadline vary between 15 minutes and 7 days.  If your withdrawal has not yet been credited after 7 days, please send me a screenshot of your withdrawal history.If you are unable to request the withdrawal, you may not have completed the email confirmation yet.  To confirm your email address, simply go to the main page of our website, select "Account" and go to the "My Profile" section.  There you will find the "Send email again" icon, click it and follow the instructions to verify your email address.',"Hello, could you give me more details on how I can help you? If your problem is a deposit, the deadline is 24 hours after the transfer, the withdrawal deadline is 7 days of processing, asked about the bonus, to use the bonus you need to go through the rollover, if your question is about the promotional code and sent the promotional code by email, if it is another problem please send me a screenshot of the error and tell me what your email address is registration, we apologize for the inconvenience, we will be checking your problem.",'Hello, if you have a problem with the deposit, could you send me the complete receipt and the deposit history that appears on the platform, please?','Hello, how can we help? Could you send me more details?','Hello, we apologize for the inconvenience, we will be checking your problem, could you send me images with more details please and I will help you, if the problem is deposit, the deadline is 24 hours after transfer, the withdrawal deadline is 7 days processing , asked about bonus, to use the bonus you need to go through the rollover, for promotional code and sent the promotional code by email','Hello problems with withdrawal, could you send me the history of withdrawals on the platform please, remembering that the withdrawal period is a maximum of 7 days and you cannot play while it is being processed']
tods = resz + respostas
print(tods)

def enviar():
    pausa = int(tempo.get())
    print('tempo de espera:', pausa)
    tempo.delete(0, "end")
    #tela.destroy()
    #ptg.PAUSE=0.5


    #respostas = ['To make a withdrawal from the ValorBet site, you need to access the "Account" section and select "Withdrawal". Note that the minimum withdrawal amount is 1000 INR and your email address must be confirmed.','To make a withdrawal from the ValorBet site, you need to access the "Account" section and select "Withdrawal". Note that the minimum withdrawal amount is 1000 INR and your email address must be confirmed.']

    respostasaleatorias = random.choice(tods)
    ptg.PAUSE=1
    ptg.click(410,744)
    ptg.click(89,704)
    time.sleep(5)
    ptg.click(288,597, clicks=3)
    time.sleep(5)
    ptg.hotkey('ctrl','c')
    ptg.click(460,750)
    ptg.click(830,284)
    ptg.press('down')
    ptg.press('up')
    ptg.hotkey('ctrl','v')
    ptg.press('right')
    ptg.press('right')
    ptg.press('right')
    ptg.click(410,744)
    ptg.click(106,20)
    ptg.click(192,67)
    ptg.hotkey('ctrl','c')
    ptg.click(460,750)
    ptg.hotkey('ctrl','v')
    ptg.press('left')
    ptg.press('left')
    ptg.press('left')
    ptg.press('down')
    ptg.click(410,744)
    ptg.click(275,694)
    ptg.write(respostasaleatorias)
    time.sleep(5)
    ptg.press('enter')
    time.sleep(5)
    while True:
        ptg.click(89,704)
        ptg.press('down')
        ptg.click(89,704)
        time.sleep(2)
        ptg.click(288,597, clicks=3)
        ptg.hotkey('ctrl','c')
        ptg.click(460,750)
        ptg.hotkey('ctrl','v')
        ptg.press('right')
        ptg.press('right')
        ptg.press('right')
        ptg.click(410,744)
        ptg.click(106,20)
        ptg.click(192,67)
        ptg.hotkey('ctrl','c')
        ptg.click(460,750)
        ptg.hotkey('ctrl','v')
        ptg.press('left')
        ptg.press('left')
        ptg.press('left')
        ptg.press('down')
        ptg.click(410,744)
        ptg.click(275,694)
        ptg.write(respostasaleatorias)
        time.sleep(5)
        ptg.press('enter') 
        time.sleep(pausa) 
btn = ctk.CTkButton(tela, text='enviar', command=enviar)
btn.pack(pady=10)




tela.mainloop()