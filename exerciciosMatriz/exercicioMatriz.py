#RM97824 - Vinicius Oliveira de Barros

import random
matriz = []
linhas = 5
colunas = 5
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = random.randint(10, 30)
        linha.append(numero)
    matriz.append(linha[:])

for  g in matriz:
    print(g)

print("--"*50)

print("Linha 4:", matriz[3])

somaLinha4 = 0
for z in matriz[3]:
    somaLinha4 += z
print("Soma da linha 4:", somaLinha4)

soma_coluna2 = 0
valores_coluna = []
for i in range(5):
    valores = []
    for j in range(5):
        if j == 1:
            num = matriz[i][1]
            soma_coluna2 += num

print("Soma da coluna 2:",soma_coluna2)

soma_diag_princi = 0
for i in range(len(matriz)):
    soma_diag_princi += matriz[i][i]
print("Soma da diagonal principal:",soma_diag_princi)

soma_diag_sec = 0
n = len(matriz)
for i in range(len(matriz)):
    soma_diag_sec += matriz[i][n - 1 - i]

print("Soma da diagonal secundaria:", soma_diag_sec)
soma_matriz_total = 0
for i in matriz:
    for j in i:
        soma_matriz_total += j
print("Soma total da matriz:", soma_matriz_total)