
import customtkinter as ctk
import pyautogui as ptg
import time
import random
tela = ctk.CTk()
tela.geometry('400x400')
tempo = ctk.CTkEntry(tela, placeholder_text='time')
tempo.pack(pady=10)

#jorginho para idiomas em espanhol ADC BD SQL
"""res = ctk.CTkEntry(tela, placeholder_text='time')
res.pack(pady=10)"""
espanish = ["Para hacer un depósito, haga clic en 'Depósito con 1 Clic', seleccione el método, ingrese el monto y haga clic en 'Pagar'. Si el depósito no se acredita en 24 horas, envíe el recibo y el historial de depósitos. Los retiros tardan entre 15 minutos y 7 días. Envíe el historial si supera 7 días. Para confirmar el correo, vaya a 'Cuenta' > 'Mi Perfil' y haga clic en 'Enviar correo nuevamente'. Para otros problemas, envíe una captura del error y su correo de registro.","Hola, ¿cómo puedo ayudarle? Para depósitos, haga clic en 'Depósito con 1 Clic' en la esquina superior derecha, elija el método, ingrese el monto y haga clic en 'Pagar'. Los depósitos pueden tardar hasta 24 horas en ser acreditados. Si tiene problemas, envíe el recibo de pago y el historial de depósitos. Los retiros pueden tardar de 15 minutos a 7 días. Envíe el historial de retiros si pasa de 7 días. Confirme su correo en 'Cuenta' > 'Mi Perfil' haciendo clic en 'Enviar correo nuevamente'. Para bonos, necesita pasar por el rollover. Para problemas adicionales, envíe una captura del error y su correo de registro. Pedimos disculpas por las molestias, estaremos verificando su problema.","¡Hola! Para hacer un depósito, haga clic en el botón 'Depósito con 1 Clic' en la esquina superior derecha de la pantalla, elija un método de pago, ingrese el monto y haga clic en 'Pagar'. Si tiene problemas con un depósito no acreditado, el plazo máximo es de 24 horas. Envíe una captura del recibo de pago y del historial de depósitos en la plataforma si pasa del plazo. Para retiros, el plazo varía entre 15 minutos y 7 días. Si su retiro no fue acreditado después de 7 días, envíe una captura del historial de retiros. Verifique si su correo está confirmado accediendo a 'Cuenta' > 'Mi Perfil' y haciendo clic en 'Enviar correo nuevamente'. Si necesita más asistencia, envíe una captura del error y su correo de registro. Disculpe las molestias, estamos aquí para ayudar." ]

ingles = ["To make a deposit, click '1-Click Deposit', select the method, enter the amount, and click 'Pay'. If the deposit isn't credited in 24 hours, send the receipt and deposit history. Withdrawals take 15 minutes to 7 days. Send history if over 7 days. To confirm your email, go to 'Account' > 'My Profile' and click 'Send email again'. For other issues, send a screenshot of the error and your registration email.","Hello sir. To make a deposit, click the '1-Click Deposit' button in the upper right corner of the screen, select a convenient replenishment method, enter the amount and click the 'Pay' button. If you have problems with a deposit that has not yet been credited, the maximum period for the deposit to be credited is up to 24 hours. If it has already passed the deadline, please send a screenshot of your payment receipt and a screenshot of the deposit history on the platform. If the problem is a withdrawal that has not yet been credited, the deadline varies between 15 minutes and 7 days. If your withdrawal has not yet been credited after 7 days, please send me a screenshot of your withdrawal history. If you are unable to request the withdrawal, you may not have completed the email confirmation yet. To confirm your email address, go to the main page of our website, select 'Account' and go to the 'My Profile' section. There you will find the 'Send email again' icon, click it and follow the instructions to verify your email address. If you have other questions, please send me a screenshot of the error and provide your registration email address. We apologize for the inconvenience, we will be checking your problem.","Hello! To make a deposit, click the '1-Click Deposit' button in the upper right corner of the screen, choose a payment method, enter the amount and click 'Pay'. If you have problems with a deposit not credited, the maximum period is 24 hours. Send a screenshot of your payment receipt and the deposit history on the platform if it exceeds the deadline. For withdrawals, the period varies between 15 minutes and 7 days. If your withdrawal hasn't been credited after 7 days, send a screenshot of your withdrawal history. Check if your email is confirmed by accessing 'Account' > 'My Profile' and clicking 'Send email again'. If you need further assistance, send a screenshot of the error and your registration email. We apologize for the inconvenience, we are here to help.","Hello, how can I help? For deposits, click the '1-Click Deposit" "button in the upper right corner, choose the method, enter the amount and click 'PAY'. Deposits can take up to 24 hours to be credited. If you have issues, send the payment receipt and deposit history. Withdrawals can take from 15 minutes to 7 days. Send the withdrawal history if it exceeds 7 days. Confirm your email in 'Account' > 'My Profile' by clicking 'Send email again'. For bonuses, you need to go through the rollover. For additional issues, send a screenshot of the error and your registration email. We apologize for the inconvenience, we will be checking your problem."]
todosreply = ingles + espanish
print(todosreply)

def enviar():

    pausa = int(tempo.get())
    print('tempo de espera:', pausa)
    tempo.delete(0, "end")
    #tela.destroy()
    #ptg.PAUSE=0.5


    #respostas = ['To make a withdrawal from the ValorBet site, you need to access the "Account" section and select "Withdrawal". Note that the minimum withdrawal amount is 1000 INR and your email address must be confirmed.','To make a withdrawal from the ValorBet site, you need to access the "Account" section and select "Withdrawal". Note that the minimum withdrawal amount is 1000 INR and your email address must be confirmed.']

    respostasaleatorias = random.choice(todosreply)
    ptg.PAUSE=1
    ptg.click(409,755)
    ptg.click(120,681)
    time.sleep(5)
    ptg.write(respostasaleatorias)
    time.sleep(5)
    ptg.press('enter')
    time.sleep(5)
    x = 0
    while (x < 1000):
        #ptg.click(409,755)
        ptg.click(120,681)
        ptg.write(respostasaleatorias)
        time.sleep(5)
        ptg.press('enter') 
        time.sleep(pausa) 
        if x == 50:
            ptg.press('f5')
            time.sleep(20)
            ptg.click(1007,168, duration=2)

btn = ctk.CTkButton(tela, text='enviar', command=enviar)
btn.pack(pady=10)




tela.mainloop()