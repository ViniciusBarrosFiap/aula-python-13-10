#A lista eh uma variavel capaz de armazenar varios dados (array)
#comprando listas com algo da realidade a lista eh como uma gaveta

# frutas = ["Maça", "Uva", "Morango"]
# numeros = [1,2,3,4,5]
# logicos = [True, True, False, True]
# misto = ["Lero-lero", True, 55, "Uva", 5.7]
# print(frutas, numeros, logicos, misto)

# frutas = ["Maça", "Uva", "Tomate"]
# print(frutas)
# print(frutas[2])
# print(len(frutas))
# frutas.append("cereja")
# frutas.append("acerola")
# print(frutas)
# print(len(frutas))
# print(frutas[-1])

# frutas = ["maça", "uva", "kiwi", "cereja", "pera", "manga"]
# print(frutas[2:5])
# print(frutas[:4])
# print(frutas[:])

# frutas[1] = "manga"
# print(frutas)
# frutas[1:3] = ["manga", "caqui"]
# print(frutas)
# frutas.insert(1, "banana")
# print(frutas)

# frutas.remove("manga")
# print(frutas)

# frutas.pop(5)
# print(frutas)

# frutas.sort()
# print(frutas)

numeros = [90, 1000, 50, 4,77, 143]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

frutas = ["Maça", "uva", "Pêra", "banana"]
frutas.sort(key= str.lower)
print(frutas)

copiafrutas = frutas.copy()
frutas.append("Kiwi")
print(frutas)
print(copiafrutas)
# for i in frutas:
#     print(i)

# for i in range(0, len(frutas), 1):
#     print(frutas[i])
# if "cereja" in frutas:
#     print("temos cereja")