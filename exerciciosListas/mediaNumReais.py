#peça para o usuário digitar uma lista de 20
#números reais. Ao final exiba a média dos valores
#digitados contidos na lista.

numeros = []
soma = 0
for i in range(20):
    numUser = float(input(f"Digite o {i + 1}° numero real: "))
    numeros.append(numUser)
for i in numeros:
    soma += i

media = soma / 20
print(numeros)
print(soma)
print(f"A média dos números é {media}")