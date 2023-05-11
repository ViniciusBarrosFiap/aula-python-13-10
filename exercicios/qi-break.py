contador = qi = 1
try:
    while qi != 0:
        qi = int(input("Digite o qi dos gênios: "))
        if qi >= 140:
            contador += 1
        else:
            continue
    print(f"Foi contado {contador - 1 } gênios")
except ValueError:
    print("Digite apenas números inteiros")
    print(f"Foi contado {contador - 1 } gênios")
