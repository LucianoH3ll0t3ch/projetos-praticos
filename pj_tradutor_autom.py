from struct import pack
import customtkinter as ctk
import deep_translator
import pyautogui  as ptg
from deep_translator import GoogleTranslator, single_detection
tela = ctk.CTk()
tela.geometry('500x500')
#entrada de teste de tradução
entrada = ctk.CTkEntry(master=tela, placeholder_text='texto', width=400)
entrada.pack(pady=12)
#retorno da tradução pro idioma selecionado
telatrad = ctk.CTkScrollableFrame(tela, orientation='vertical')
telatrad.pack(pady=12)
def traduzir():
    #definindo um tradutor e quais idioomas(identificação do idioma automatico, para o portugues)
    tradutor = GoogleTranslator(source="auto", target='ar')
    #definindo o função de tradução
    traducao = tradutor.translate(entrada.get())
    
   #tradução feita e impressa na tela
    label = ctk.CTkLabel(telatrad, text=traducao)
    label.pack(pady=12)
    
    ptg.click(94,699, duration=1)
    ptg.write(label.get())

    
    """resp = ctk.CTkLabel(telatrad, text=traducao)
    resp.pack(pady=12)"""
    #identificador de qual idioma 
    lang = single_detection(entrada.get(), api_key="8004ed31b3e275788568e01e161ae3fa")
    





    
#botão de  execução da função   
btn = ctk.CTkButton(master=tela, width=250, height=30,  command=traduzir)
btn.pack(pady=12)
tela.mainloop()

"""import deep_translator
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='pt', target='en')
x = 0
while(x < 10):
    x =+1
    texto = input('informe a frase teste: ')
    traducao = tradutor.translate(texto)
    print(traducao)"""