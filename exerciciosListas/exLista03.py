# FUPQ peça para o usuário digitar números inteiros (e 
# armazene estes valores em uma lista), ele deve continuar 
# digitando até digitar 0 para encerrar a digitação. Ao final 
# exiba: o tamanho da lista, a lista completa em ordem 
# crescente, a quantidade de números negativos da lista e a 
# quantidade de números primos positivos da lista.

numeros = []
numUser = 1

while numUser != 0:
    numUser = int(input("Digite números inteiros: "))
    numeros.append(numUser)

num_neg = 0
for i in numeros:
    if i < 0:
        num_neg += 1

num_primos = 0
for i in numeros:
    div1, div2, div3, div4 = i%2, i%3, i%5, i%7
    if i != 2 and i != 3 and i != 5 and i != 7:
        if div1 and div2 and div3 and div4 != 0:
            num_primos += 1
    else:
        num_primos += 1


print(numeros)
print(f"A lista possui {len(numeros)} números")
numeros.sort()
print(numeros)
print(f"A lista possui {num_neg} números negativos")
print(f"A lista possui {num_primos - 1} números primos")