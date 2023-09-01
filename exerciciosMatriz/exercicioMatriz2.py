#RM97824 - Vinicius Oliveira de Barros

import random
matriz = []
linhas = 5
colunas = 5
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = random.randint(10, 20)
        linha.append(numero)
    matriz.append(linha[:])

for  g in matriz:
    print(g)

soma_diag_sup_direita = 0
n = len(matriz)
for i in range(n):
    for j in range(n):
        if j >= i:
            soma_diag_sup_direita += matriz[i][j]

print("A soma do canto superior direito é:", soma_diag_sup_direita)

soma_diag_infe_esquerda = 0
n = len(matriz)
for i in range(n):
    for j in range(n):
        if j <= i and j != i:
            soma_diag_infe_esquerda += matriz[i][j]
print("A soma do canto inferior esquerdo é:", soma)