import csv
continuar = "sim"
novos_filmes = []
while continuar == "sim":
    print("Digite o nome do filme: ")
    titulo = input()
    print("Digite o gênero do filme: ")
    genero = input()
    print("Digite a duração do filme: ")
    duracao = input()
    print("Digite a censura do filme: ")
    sensura = input()
    print("Digite o nome do diretor do filme: ")
    diretor = input()
    novos_filmes.append([titulo, genero, duracao + "minutos", sensura + "anos", diretor])
    with open("d:/filmes.csv", "a", encoding="utf-8", newline="") as arquivo:
        adiciona_filmes = csv.writer(arquivo)
        for i in novos_filmes:
            adiciona_filmes.writerow(i)
    continuar = input("Deseja cadastrar outro filme ?\n")