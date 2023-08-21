matriz = []
linhas = 5
colunas = 2
print("Digite seu nome e estado")
for i in range(0,linhas,1):
    linha = []
    for j in range(0, colunas, 1):
        valor = input().upper()
        linha.append(valor)
    matriz.append(linha)

escolhaDoEstado  = input("Escolha um estado brasileiro: ").upper()
for i in range(0, len(matriz), 1):
    if escolhaDoEstado == matriz[i][1]:
        print(matriz[i][0])
