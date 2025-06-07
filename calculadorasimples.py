def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if a == 0 or b == 0:
        print("Não é possivel dividir um numero por 0")

    else:
        return a / b


def expoenciacao(a, b):
    return a ** b



def calculador():
    while True:
        print("Escolha uma Operação ")
        print("Digite 1: Se você quiser somar: ")
        print("Digite 2: Se você quiser subtrair: ")
        print("Digite 3: Se você quiser mutiplicar: ")
        print("Digite 4: Se você quiser dividir: ")
        print("Digite 5: Se você quiser realizar uma exponenciação: ")
        print("Digite 0: Se quiser sair")


        escolha = input("Digite um número para prosseguir: ")

        if escolha > "0":
            num1 = float(input("Digite o primeiro número da operação: "))
            num2 = float(input("Digite o segundo número da operação: "))

        break


    if escolha == "1":
        print("Resultado: ", soma (num1,num2))

    elif escolha == "2":
        print("Resultado: ", subtracao (num1,num2))

    elif escolha == "3":
        print("Resultado: ", multiplicacao (num1,num2))

    elif escolha == "4":
        print("Resultado: ", divisao (num1,num2))

    elif escolha == "5":
        print("Resultado: ", expoenciacao (num1,num2))

    else:
        print("Encerrando a Calculadora...")



calculador()
