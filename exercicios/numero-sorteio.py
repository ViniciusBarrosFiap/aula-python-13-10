import random

numero_aleatorio = random.randint(2, 9)
print(f"O numero sorteado foi {numero_aleatorio}")

if numero_aleatorio <= 5:
    for i in range(11):
        tabuada = numero_aleatorio * i
        print(f"{numero_aleatorio} x {i} = {tabuada}")

elif numero_aleatorio >= 5:
    i = 10
    while i >= 0:
        tabuada = numero_aleatorio * i
        print(f"{numero_aleatorio} x {i} = {tabuada}")
        i -= 1
        