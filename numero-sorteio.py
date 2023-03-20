import random

numero_aleatorio = random.randint(2, 9)
print(f"O numero sorteado foi {numero_aleatorio}")
if numero_aleatorio <= 5:
    for i in range(11):
        tabuada = numero_aleatorio * i
        print(tabuada)

elif numero_aleatorio >= 5:

    for i in range(11, 10, 9, 8, 7):
        tabuada = numero_aleatorio * i
        print(tabuada)