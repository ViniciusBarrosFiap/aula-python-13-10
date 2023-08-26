matriz = []
for i in range(5):
    linha = []
    for j in range(3):
        valor = int(input("Digite números inteiros: "))
        linha.append(valor)
    matriz.append(linha[:])

menorValor = matriz[0][0]
indiceLinha = 0
indiceColuna = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        elemento = matriz[linha][coluna]
        if elemento < menorValor:
            menorValor = elemento
            indiceLinha = linha
            indiceColuna = coluna

for linha in matriz:  # Corrigir o loop para exibir a matriz
    print(linha)

print(f"O menor valor é {menorValor}")
print(f"Está localizado no índice: matriz[{indiceLinha}][{indiceColuna}]")
