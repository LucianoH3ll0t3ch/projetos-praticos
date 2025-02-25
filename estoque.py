import pandas as pd
import tkinter 
import customtkinter as ctk
import openpyxl



#Projeto calculador de gastos mensais
#Criar uma tela que receba todos os gastos semanais e somar no fim do mes
#o projeto deve usar um banco de dados nesse caso sera usado uma planilha que sera enviado todos os dados de gastos
#projeto dinamico e simples, texto retorno e funcionalidade simples 
#funcionalidade principal : armazenar valores inteiros e decimais e calcular todo mes, e ver o lucro

"""
ctk.set_appearance_mode("Dark") #theme da tela
tela = ctk.CTk()#tela de nossos dados

tela.geometry("500x500")
opcion = ctk.CTkEntry(tela, placeholder_text="Quantas contas você possui: ", width=420)
opcion.pack(pady=12)

tela.mainloop()"""
#mini sistema de estoque
class Produto:
    '''Define a classe produto'''

    #construtor da classe produto
    def __init__(self, nome, codigo, preco, quantidade):
        '''Cria uma instancia de produto'''
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade
    #retorna o nome do produto
    def obtem_nome(self):
        return self.nome
    #retorna o codigo do produto
    def obtem_codigo(self):
        return self.codigo
    #retorna o preco do produto
    def obtem_preco(self):
        return self.preco  
    #Devolve TRue se novo preco maior que o anterior
    def altera_preco(self, novo_preco):
        pp = self.preco 
        self.preco  = novo_preco
        if novo_preco > pp:
            return True
        return False
    #devolve False se a quantidade de produto requerida não esta disponivel
    def altera_quantidade(self, novo_pedido):
        if novo_pedido > self.quantidade:
            return False
        self.quantidade -= novo_pedido
        return True
    #testes da Classe
if __name__ == "__main__":
    p1  = Produto ("Camisa social", 123456,45.56, 1000)
    p2 = Produto ("Calça jeans", 423564, 98.12, 500)
    print(" oferta do dia :", p1.obtem_nome())
    print("oferta da semana", p2.obtem_nome())
    #altera o preco
    if p1.altera_preco(int(input("informe o valor de hj"))):
        print('Preço alterado hoje')
    else:
        print("Atenção - baixou  o preço")

    #verifica se pode fazr uma venda
    if p2.altera_quantidade(100):
        print("pode fazer a venda - valor total = ", p2.obtem_preco() * 100)
    else:
        print("não tem produto suficiente para esta venda")

