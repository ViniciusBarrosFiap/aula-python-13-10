#Rm97824 - Vinicius Oliveira de Barros
import csv
print("Escolha um filtro:\n 1- Titulo\n2- Diretor\n 3- Genero\n")
opcao = int(input())
if opcao == 1:
    opcao_escolha = input("Digite o nome do titulo: ")
elif opcao == 2:
    opcao_escolha = input("Digite o nome do diretor: ")
elif opcao == 3:
    opcao_escolha = input("Digite o nome do diretor: ")

with open("D:/filmes.csv", "r", encoding="utf-8") as f:
    filmes = csv.reader(f)
    next(filmes)
    for i in filmes:
        for j in i:
            if opcao_escolha in j:
                print("LIVRO ENCONTRADO!")
                for x in i:
                    print(x)