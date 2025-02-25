from cgitb import text
from enum import auto
from turtle import width
import customtkinter as ctk
import pyautogui as ptg
from tkinter import messagebox
import time
import random
from deep_translator import GoogleTranslator
import os
from cgitb import text


tela = ctk.CTk()
tela.geometry('300x300')
pedir = ctk.CTkLabel(tela, text=" Você esta logado no chrome ja?")
pedir.pack(pady=2)
confirma = ctk.CTkEntry(tela, placeholder_text="confirme com sim ou não", width=200)
confirma.pack(pady=2)
def executar():
    if (confirma.get() == 'sim'):
        messagebox.showinfo('waiting', 'Aguarde um momento')
        time.sleep(10)
        """   pedir1 = ctk.CTkLabel(tela, text=" ja esta no login do diretor do crm? ja coloco nas não lidas??")
        pedir1.pack(pady=2)
        confirma1 = ctk.CTkEntry(tela, placeholder_text="Veirique e confirme", width= 200)
        confirma1.pack(pady=2)"""
       
            #messagebox.showinfo("info", "more ok")
        espanish = ["Para hacer un depósito, haga clic en 'Depósito con 1 Clic', seleccione el método, ingrese el monto y haga clic en 'Pagar'. Si el depósito no se acredita en 24 horas, envíe el recibo y el historial de depósitos. Los retiros tardan entre 15 minutos y 7 días. Envíe el historial si supera 7 días. Para confirmar el correo, vaya a 'Cuenta' > 'Mi Perfil' y haga clic en 'Enviar correo nuevamente'. Para otros problemas, envíe una captura del error y su correo de registro.","Hola, ¿cómo puedo ayudarle? Para depósitos, haga clic en 'Depósito con 1 Clic' en la esquina superior derecha, elija el método, ingrese el monto y haga clic en 'Pagar'. Los depósitos pueden tardar hasta 24 horas en ser acreditados. Si tiene problemas, envíe el recibo de pago y el historial de depósitos. Los retiros pueden tardar de 15 minutos a 7 días. Envíe el historial de retiros si pasa de 7 días. Confirme su correo en 'Cuenta' > 'Mi Perfil' haciendo clic en 'Enviar correo nuevamente'. Para bonos, necesita pasar por el rollover. Para problemas adicionales, envíe una captura del error y su correo de registro. Pedimos disculpas por las molestias, estaremos verificando su problema.","¡Hola! Para hacer un depósito, haga clic en el botón 'Depósito con 1 Clic' en la esquina superior derecha de la pantalla, elija un método de pago, ingrese el monto y haga clic en 'Pagar'. Si tiene problemas con un depósito no acreditado, el plazo máximo es de 24 horas. Envíe una captura del recibo de pago y del historial de depósitos en la plataforma si pasa del plazo. Para retiros, el plazo varía entre 15 minutos y 7 días. Si su retiro no fue acreditado después de 7 días, envíe una captura del historial de retiros. Verifique si su correo está confirmado accediendo a 'Cuenta' > 'Mi Perfil' y haciendo clic en 'Enviar correo nuevamente'. Si necesita más asistencia, envíe una captura del error y su correo de registro. Disculpe las molestias, estamos aquí para ayudar." ]
        ingles2 = "Hey!  To make a deposit, click 1-Click Deposit at the top right, choose your method, enter the amount, and click <Pay.> If the amount doesn’t appear within 24 hours, please send us the receipt, deposit history, your email, and a screenshot of the start screen. Withdrawals usually take between 15 minutes and 7 days. If it takes longer, let us know with the history. Remember to complete the rollover for bonuses first. After depositing, just search for your game and start playing. "
           
        ingles = [
            "Hey! 😊 How are you doing today? To make a deposit, just click '1-Click Deposit' at the top right, pick your method, type the amount, and hit 'Pay'. If it’s not showing up in 24 hours, please send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals usually take 15 minutes to 7 days. If it’s taking longer, let us know with the history. Don't forget, you need to finish the rollover for bonuses first. Once you’ve deposited, just search for your game to start playing. Any questions? We’re here for you at support@valor.bet! 🌟",
            
            "Hello there! 😊 Hope you're having a great day! To make a deposit, click '1-Click Deposit' at the top right corner, choose your payment method, enter the amount, and click 'Pay'. If you don’t see the deposit in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it takes longer, let us know with the history. Complete the rollover to use bonuses. After depositing, just search for your game to start playing. Need help? Email us at support@valor.bet! 🌟",
            
            "Hi there! 😊 How’s everything? For deposits, click '1-Click Deposit' in the top right, select your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, please send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take anywhere from 15 minutes to 7 days. If it’s delayed, send us the history. Don’t forget to complete the rollover for bonuses. To play, just search for your game after depositing. Have questions? We’re here at support@valor.bet! 🌟",
            
            "Hey! 😊 How can I help you today? To deposit, click '1-Click Deposit' at the upper right, pick a method, enter the amount, and click 'Pay'. If it doesn’t show up in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take between 15 minutes and 7 days. If it’s delayed, send us the history. Make sure you finish the rollover for bonuses first. To start playing, search for your game after depositing. Any issues? Reach out at support@valor.bet! 🌟",
            
            "Hi! 😊 Hope all is well! To make a deposit, just click '1-Click Deposit' in the top right corner, choose your method, enter the amount, and hit 'Pay'. If the deposit isn’t credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses before using them. After depositing, search for your game to start playing. Need assistance? Email us at support@valor.bet! 🌟",
            
            "Hi there! 😊 How can we assist you today? To deposit, click '1-Click Deposit' at the upper right, choose your method, enter the amount, and press 'Pay'. If it’s not reflected in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals may take 15 minutes to 7 days. If delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Contact support@valor.bet! 🌟",
            
            "Greetings! 😊 Hope you're well! To deposit, click '1-Click Deposit' at the top right, pick your method, enter the amount, and click 'Pay'. If the deposit doesn’t appear in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Ensure you complete the rollover for bonuses first. To start playing, search for your game after deposit. Need assistance? Email us at support@valor.bet! 🌟",
            
            "Hi there! 😊 How can we help you today? To make a deposit, click '1-Click Deposit' in the upper right, choose your method, enter the amount, and click 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Remember to complete the rollover for bonuses. To start playing, search for your game after deposit. Any questions? We’re here for you at support@valor.bet! 🌟",
            
            "Hello! 😊 How’s it going? For deposits, click '1-Click Deposit' in the top right corner, pick your method, enter the amount, and hit 'Pay'. If it’s not credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Reach out at support@valor.bet! 🌟",
            
            "Hi! 😊 How are you today? To deposit, click '1-Click Deposit' at the top right corner, choose your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need assistance? Email support@valor.bet! 🌟",
            
            "Hey! 😊 How can we assist you today? To make a deposit, click '1-Click Deposit' in the top right, choose your method, enter the amount, and click 'Pay'. If it doesn’t appear in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If delayed, send us the history. Complete the rollover for bonuses first. To play, search for your game after deposit. Any questions? Contact support@valor.bet! 🌟",
            
            "Hi! 😊 Hope you're having a good day! To deposit, click '1-Click Deposit' in the upper right, pick your method, enter the amount, and press 'Pay'. If it’s not reflected in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Email us at support@valor.bet! 🌟",
            
            "Hey there! 😊 How can we help today? To make a deposit, click '1-Click Deposit' at the top right corner, choose your method, enter the amount, and click 'Pay'. If the deposit isn’t credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Finish the rollover for bonuses first. To start playing, search for your game after depositing. Need assistance? Contact us at support@valor.bet! 🌟",
            
            "Greetings! 😊 Hope everything’s going well! To deposit, click '1-Click Deposit' at the upper right, pick your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after deposit. Any questions? We’re here at support@valor.bet! 🌟",
            
            "Hey! 😊 How can we assist you today? For deposits, click '1-Click Deposit' in the top right, choose your method, enter the amount, and click 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Reach out at support@valor.bet! 🌟",
            
            "Hi there! 😊 How’s everything? To make a deposit, click '1-Click Deposit' in the upper right corner, pick your method, enter the amount, and click 'Pay'. If it’s not reflected in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need assistance? Contact support@valor.bet! 🌟",
            
            "Hello! 😊 How can we help you today? To deposit, click '1-Click Deposit' at the top right corner, choose your method, enter the amount, and hit 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To play, search for your game after deposit. Need help? Email support@valor.bet! 🌟",
            
            "Hey there! 😊 Hope you're doing great! To make a deposit, click '1-Click Deposit' in the upper right, pick your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Any questions? Contact us at support@valor.bet! 🌟",
            
            "Hello! 😊 How’s your day going? To deposit, click '1-Click Deposit' at the top right corner, choose your method, enter the amount, and click 'Pay'. If it doesn’t appear in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To play, search for your game after deposit. Need assistance? Reach out at support@valor.bet! 🌟",
            
            "Hi! 😊 How can we assist you today? For deposits, click '1-Click Deposit' in the top right corner, pick your method, enter the amount, and press 'Pay'. If it’s not reflected within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Finish the rollover for bonuses first. To play, search for your game after deposit. Need help? Contact us at support@valor.bet! 🌟"
        ]
        idioma_arab = [
                "مرحبًا! 😊 إذا كنت ترغب في الإيداع، فقط اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يظهر الإيداع خلال 24 ساعة، يرجى إرسال الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. تستغرق عمليات السحب عادةً من 15 دقيقة إلى 7 أيام. إذا استغرق الأمر وقتًا أطول، دعنا نعرف مع السجل. لا تنسَ، يجب أن تكمل متطلبات التدوير للحصول على المكافآت أولاً. بمجرد الإيداع، ابحث عن لعبتك لتبدأ اللعب. هل لديك أي أسئلة؟ نحن هنا من أجلك على support@valor.bet! 🌟",

                "مرحبًا! 😊 لإجراء إيداع، انقر على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقة الدفع الخاصة بك، أدخل المبلغ، واضغط على 'دفع'. إذا لم ترَ الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا استغرق الأمر وقتًا أطول، دعنا نعرف مع السجل. أكمل متطلبات التدوير لاستخدام المكافآت. بعد الإيداع، ابحث عن لعبتك لتبدأ اللعب. تحتاج إلى مساعدة؟ راسلنا عبر البريد الإلكتروني على support@valor.bet! 🌟",

                "مرحبًا! 😊 لإجراء الإيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يتم إضافة الإيداع خلال 24 ساعة، يرجى إرسال الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. لا تنسَ إكمال متطلبات التدوير للحصول على المكافآت. للعب، ابحث عن لعبتك بعد الإيداع. هل لديك أي أسئلة؟ نحن هنا من أجلك على support@valor.bet! 🌟",

                "مرحبًا! 😊 لإجراء الإيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يظهر الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. تأكد من إكمال متطلبات التدوير للحصول على المكافآت أولاً. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. أي مشاكل؟ تواصل معنا على support@valor.bet! 🌟",

                "مرحبًا! 😊 لإجراء إيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يتم إضافة الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. أكمل متطلبات التدوير للحصول على المكافآت قبل استخدامها. بعد الإيداع، ابحث عن لعبتك لتبدأ اللعب. تحتاج إلى مساعدة؟ راسلنا عبر البريد الإلكتروني على support@valor.bet! 🌟",

                "مرحبًا! 😊 لإجراء إيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يظهر الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. أكمل متطلبات التدوير للحصول على المكافآت أولاً. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. تحتاج إلى مساعدة؟ تواصل مع support@valor.bet! 🌟",

                "تحياتنا! 😊 لإجراء إيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يظهر الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. تأكد من إكمال متطلبات التدوير للحصول على المكافآت أولاً. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. تحتاج إلى مساعدة؟ راسلنا عبر البريد الإلكتروني على support@valor.bet! 🌟",

                "مرحبًا! 😊 لإجراء إيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يتم إضافة الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. تذكر إكمال متطلبات التدوير للحصول على المكافآت. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. أي أسئلة؟ نحن هنا من أجلك على support@valor.bet! 🌟",

                "مرحبًا! 😊 للإيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يتم إضافة الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. أكمل متطلبات التدوير للحصول على المكافآت أولاً. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. تحتاج إلى مساعدة؟ تواصل معنا على support@valor.bet! 🌟",

                "مرحبًا! 😊 للإيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يظهر الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. أكمل متطلبات التدوير للحصول على المكافآت أولاً. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. تحتاج إلى مساعدة؟ راسلنا عبر البريد الإلكتروني على support@valor.bet! 🌟",

                "مرحبًا! 😊 للإيداع، اضغط على 'الإيداع بنقرة واحدة' في الزاوية اليمنى العليا، اختر طريقتك، أدخل المبلغ، واضغط على 'دفع'. إذا لم يتم إضافة الإيداع خلال 24 ساعة، أرسل لنا الإيصال، وسجل الإيداع، وبريدك الإلكتروني، ولقطة شاشة من شاشة البدء الخاصة بك. يمكن أن تستغرق عمليات السحب من 15 دقيقة إلى 7 أيام. إذا تأخرت، أرسل لنا السجل. أكمل متطلبات التدوير للحصول على المكافآت أولاً. لبدء اللعب، ابحث عن لعبتك بعد الإيداع. هل لديك أي أسئلة؟ نحن هنا من أجلك على support@valor.bet! 🌟"
            ]

        
        reply_ingles =  [
            "Hey there! 😊 If you want to deposit, just click '1-Click Deposit' at the top right, pick your method, type the amount, and hit 'Pay'. If it’s not showing up in 24 hours, please send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals usually take 15 minutes to 7 days. If it’s taking longer, let us know with the history. Don't forget, you need to finish the rollover for bonuses first. Once you’ve deposited, just search for your game to start playing. Any questions? We’re here for you at support@valor.bet! 🌟",
            
            "Hello! 😊 To make a deposit, click '1-Click Deposit' at the top right corner, choose your payment method, enter the amount, and click 'Pay'. If you don’t see the deposit in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it takes longer, let us know with the history. Complete the rollover to use bonuses. After depositing, just search for your game to start playing. Need help? Email us at support@valor.bet! 🌟",
            
            "Hi there! 😊 For deposits, click '1-Click Deposit' in the top right, select your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, please send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take anywhere from 15 minutes to 7 days. If it’s delayed, send us the history. Don’t forget to complete the rollover for bonuses. To play, just search for your game after depositing. Have questions? We’re here at support@valor.bet! 🌟",
            
            "Hey! 😊 To deposit, click '1-Click Deposit' at the upper right, pick a method, enter the amount, and click 'Pay'. If it doesn’t show up in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take between 15 minutes and 7 days. If it’s delayed, send us the history. Make sure you finish the rollover for bonuses first. To start playing, search for your game after depositing. Any issues? Reach out at support@valor.bet! 🌟",
            
            "Hello! 😊 To make a deposit, just click '1-Click Deposit' in the top right corner, choose your method, enter the amount, and hit 'Pay'. If the deposit isn’t credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses before using them. After depositing, search for your game to start playing. Need assistance? Email us at support@valor.bet! 🌟",
            
            "Hi! 😊 To deposit, click '1-Click Deposit' at the upper right, choose your method, enter the amount, and press 'Pay'. If it’s not reflected in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals may take 15 minutes to 7 days. If delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Contact support@valor.bet! 🌟",
            
            "Greetings! 😊 To deposit, click '1-Click Deposit' at the top right, pick your method, enter the amount, and click 'Pay'. If the deposit doesn’t appear in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Ensure you complete the rollover for bonuses first. To start playing, search for your game after deposit. Need assistance? Email us at support@valor.bet! 🌟",
            
            "Hello! 😊 To make a deposit, click '1-Click Deposit' in the upper right, choose your method, enter the amount, and click 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Remember to complete the rollover for bonuses. To start playing, search for your game after deposit. Any questions? We’re here for you at support@valor.bet! 🌟",
            
            "Hi there! 😊 For deposits, click '1-Click Deposit' in the top right corner, pick your method, enter the amount, and hit 'Pay'. If it’s not credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Reach out at support@valor.bet! 🌟",
            
            "Hello! 😊 To deposit, click '1-Click Deposit' at the top right corner, choose your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need assistance? Email support@valor.bet! 🌟",
            
            "Hey! 😊 To make a deposit, click '1-Click Deposit' in the top right, choose your method, enter the amount, and click 'Pay'. If it doesn’t appear in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If delayed, send us the history. Complete the rollover for bonuses first. To play, search for your game after deposit. Any questions? Contact support@valor.bet! 🌟",
            
            "Hello! 😊 To deposit, click '1-Click Deposit' in the upper right, pick your method, enter the amount, and press 'Pay'. If it’s not reflected in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Email us at support@valor.bet! 🌟",
            
            "Hi there! 😊 To make a deposit, click '1-Click Deposit' at the top right corner, choose your method, enter the amount, and click 'Pay'. If the deposit isn’t credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Finish the rollover for bonuses first. To start playing, search for your game after depositing. Need assistance? Contact us at support@valor.bet! 🌟",
            
            "Greetings! 😊 To deposit, click '1-Click Deposit' at the upper right, pick your method, enter the amount, and press 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after deposit. Any questions? We’re here at support@valor.bet! 🌟",
            
            "Hello! 😊 For deposits, click '1-Click Deposit' in the top right, choose your method, enter the amount, and click 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Reach out at support@valor.bet! 🌟",
            
            "Hi! 😊 To make a deposit, click '1-Click Deposit' in the upper right corner, pick your method, enter the amount, and click 'Pay'. If it’s not reflected in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need assistance? Contact support@valor.bet! 🌟",
            
            "Hey there! 😊 To deposit, click '1-Click Deposit' in the top right, choose your method, enter the amount, and press 'Pay'. If the deposit doesn’t appear in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Finish the rollover for bonuses first. To play, search for your game after deposit. Have questions? We’re here at support@valor.bet! 🌟",
            
            "Hello! 😊 For deposits, click '1-Click Deposit' at the top right corner, pick your method, enter the amount, and hit 'Pay'. If it doesn’t show up in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take from 15 minutes to 7 days. If delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after deposit. Need assistance? Email support@valor.bet! 🌟",
            
            "Hi there! 😊 To deposit, click '1-Click Deposit' at the top right, choose your method, enter the amount, and click 'Pay'. If it’s not credited in 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If it’s delayed, send us the history. Complete the rollover for bonuses first. To play, search for your game after depositing. Need help? Email us at support@valor.bet! 🌟",
            
            "Hello! 😊 To make a deposit, click '1-Click Deposit' in the upper right, choose your method, enter the amount, and hit 'Pay'. If it’s not credited within 24 hours, send us the receipt, deposit history, your email, and a screenshot of your start screen. Withdrawals can take 15 minutes to 7 days. If delayed, send us the history. Complete the rollover for bonuses first. To start playing, search for your game after depositing. Need help? Reach out at support@valor.bet! 🌟"
        ]



        todosreply = reply_ingles
        #todosreply = reply_ingles + ingles#
        """tradutor = GoogleTranslator(source="auto", target="ar")
        traducao = tradutor.translate(todosreply)"""
        #print(respostasaleatorias)
        nscrol = random.randint(-777, 772)
        loc = 74,702
        reloadafter = 1095,139

        confirma2 = ctk.CTkEntry(tela, placeholder_text="Informe QTD cliente: ", width= 200)#coloca na interfa.. a quantidade de cliente a ser respondido
        confirma2.pack(pady=2)
        
        def responder():
            
            x = 0
            time.sleep(2)
            while (x < int(confirma2.get())):
                x += 1
                #tela.destroy()
                #print('deu certo')
                """#messagebox.showinfo("funcionando", confirma2.get())
                #messagebox.showinfo('funcinando', 'funcinando')"""
                nscrol = random.randint(-777, 772)
                respostasaleatorias = random.choice(todosreply)
                print(f'a resposta da vez é:  ********{respostasaleatorias}***********')
                print(f'esta no {x} cliente!!!')
            
                ptg.PAUSE=0.9#time de processo               #print(x)
                ptg.click(loc)#clica no cliente
                time.sleep(1)#espera
                ptg.click(300,694)#clica no input de msg
                ptg.write(respostasaleatorias)#escreve a resposta
                #ptg.write(traducao)
                time.sleep(2)#espera
                ptg.press('enter')#envia a resposta
                time.sleep(1)#espera

                ptg.click(loc)#clica no cliente
                time.sleep(1)#espera
                ptg.scroll(-56)#rola a scrollbar para baixo para o proximo cliente
                time.sleep(1)#espera
                #os.system('cls')

                #valida a condição de resposta ao cliente caso seja maior ou igual a certa quantidade ele faz um descanso/ porem essa condição so aplica a 70 cliente por conta do processamento da plataforma da empresa
                if x == 120:
                    time.sleep(120)
                    print('descansando!!!')
                    messagebox.showinfo('descanso','Descansando')

                    """  confirma.destroy()
                    continuar = ctk.CTkEntry(tela, placeholder_text='Deseja continuar? ')
                    continuar.pack(pady=2)
                    continuar.bind('<Return>', lambda e: continuar.configure(responder()))
                    ptg.press('f5')
                    time.sleep(35)
                    ptg.click(reloadafter)
                    ptg.click(98,249)
                    time.sleep(3)
                    ptg.click(38,293)"""
                else:
                    continue
            messagebox.showinfo('funcionando', 'Finalizou')
            
            
     
                   
        btn2 = ctk.CTkButton(tela, text='CONFIRM', command=responder)
        btn2.pack(pady=10)

        #messagebox.showinfo('funcionando')
    elif (confirma.get() == 'nao'):
        confirma.delete(0, "end")
        ptg.PAUSE=2
        ptg.hotkey('win', 'r')
        ptg.write('chrome --new https://crm.admin.valor.bet/login')
        ptg.press('enter')
        time.sleep(5)
        ptg.hotkey('ctrl', 't')
        ptg.write('https://web.telegram.org/a/')
        ptg.press("enter")
        ptg.hotkey('ctrl','shift','tab')
        ptg.press('tab')
        ptg.write('example-director@mail.ru')
        ptg.press('tab')
        ptg.write('password')
        ptg.press("enter")


    elif (confirma.get() == 'exit'):
        
        messagebox.showinfo('ok', "funcinando otario ate depois")
        tela.destroy()

confirma.bind('<Return>', lambda e: confirma.configure(executar()))        
btn = ctk.CTkButton(tela, text='confirma', width=50, command=executar)
btn.pack(pady=2)                    
tela.mainloop()




