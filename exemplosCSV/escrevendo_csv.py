import csv
novos_dados = [
    ["Tiburcio","tiby","Senha","25","44455566677"],
    ["Otto","otty","Password","20","11144477788"]
]

with open("D:/usuarios.csv", "a", encoding="utf-8", newline="") as aquivo:
    escreve_csv = csv.writer(aquivo)
    for i in novos_dados:
        escreve_csv.writerow(i)