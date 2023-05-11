num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
try:
    print(f"Adição: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")

    try: #O try ele tenta fazer a operação caso apresente um erro
        print(f"Divisão: {num1 // num2}")
    except ZeroDivisionError: 
    #O except faz com que o programa continue pois ele abre uma exeção para um erro específico
        print("Não é possível dividir por 0")
    
    print(f"Multiplicação: {num1 * num2}")
except ValueError:
    print("É permitido digitar apenas números inteiros")