def dados(nome, cpf, dtnascimento):
    print("nome: ", nome)
    print("documento: ", cpf)
    print('Data de nascimento: ', dtnascimento)


dados(nome=input('Escreva seu nome: '), cpf=int(input('Escreva o seu cpf : ')), dtnascimento=input("Sua data de nascimento: "))