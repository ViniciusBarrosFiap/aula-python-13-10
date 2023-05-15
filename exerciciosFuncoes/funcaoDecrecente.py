def decrescente():
    numeros = []
    for i in range(4):
        numUser = float(input("Digite números reais:"))
        numeros.append(numUser)
    numeros.sort(reverse=True)
    for i in numeros:
        print(f"{i:.3f}")

decrescente()