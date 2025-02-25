def calc():
    print("operações disponiveis: ")
    print('1: adição')
    print('2: subtraçaõ')
    print('3: multiplicação')
    print('4: divisão')
    print('#' *30)

    operacao = input("escolha uma operação (1/2/3/4): ")

    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    print('#' *30)
    if operacao == "1":
        resultado = num1 + num2
        print(f"O Resultado de {num1} + {num2} é: {resultado}")
    elif operacao == "2":
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {resultado}")
    elif operacao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"o resultado de {num1} / {num2} é : {resultado}")
        else: print('Divisão por zero não é permitida')
    else: 
        print("Operação invalida, por favor escolha uma operação valida")
    print('#' *30)
calc()

