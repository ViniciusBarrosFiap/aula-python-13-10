import csv
print("Escolha um filtro:\n 1- Titulo\n2- Diretor\n 3- Genero\n")
opcao = int(input())

with open("D:/filmes.csv", "r", encoding="utf-8") as f:
    filmes = csv.reader(f)
    next(filmes)
    if opcao == 1:
        opcao_escolha = input("Digite o nome do titulo: ")
    elif opcao == 2:
        opcao_escolha = input("Digite o nome do diretor: ")
    elif opcao == 3:
        opcao_escolha = input("Digite o nome do diretor: ")
    for linha in filmes: #Ignora a primeira linha, pois é apenas os cabeçalhos das col
        if opcao_escolha in filmes:
            for i in linha:
                print (i + "\t")
    