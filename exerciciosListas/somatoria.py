numeros = []
soma = 0
try:
    for i in range(15):
        numUsuario = int(input(f"Digite o {i + 1}° numero inteiro: "))
        numeros.append(numUsuario)

    for i in numeros:
        soma += i

except ValueError:
    print("Digite numeros inteiros")

finally:
    print(numeros)
    print(soma)
