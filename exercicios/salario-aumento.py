salario = float(input("Digite seu sálario: "))
tempo = int(input("Digite quanto tempo você trabalha na empresa: "))

if tempo <= 5:
    print("Menor ou igual a 5 anos")
    print(salario + (salario * 0.05))
elif tempo >= 5 and tempo <= 10:
    print("Entre 5 e 10 anos")
    print(salario + (salario * 0.1))
elif tempo >= 11 and tempo <= 15:
    print("Entre 11 e 15 anos")
    print(salario + (salario * 0.15))
elif tempo >= 16:
    print ("16 anos pra cima")
    print(salario + (salario * 0.2))