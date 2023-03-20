salario = float(input("Digite seu sálario: "))
tempo = int(input("Digite quanto tempo você trabalha na empresa: "))

if tempo <= 5:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    print (novo_salario)