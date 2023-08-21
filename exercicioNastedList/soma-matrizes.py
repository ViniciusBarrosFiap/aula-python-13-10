matriz1 = []
matriz2 = []
matrizFinal = [[0, 0],
               [0, 0],
               [0, 0]]
for i in range(0, 3, 1):
    linha = []
    for j in range(0, 2, 1):
        valor = float(input(f"Digite o valor [{i}][{j}] da primeira matriz: "))
        linha.append(valor)
    matriz1.append(linha[:])

for a in range(0, 3,1):
    linhaMatriz2 = []
    for b in range(0, 2, 1):
        valor2 = float(input(f"Digite o valor [{a}][{b}] da segunda matriz: "))
        linhaMatriz2.append(valor2)
    matriz2.append(linhaMatriz2[:])

print("Matriz 1:")
for i in matriz1:
    print(i)

print("Matriz 2: ")
for c in matriz2:
    print(c)

for y in range(3):
    for z in range(2):
        matrizFinal[y][z] = matriz1[y][z] + matriz2[y][z]

print(matrizFinal)