import csv
with open("D:/usuarios.csv", "r", encoding="utf-8") as f:
    usuarios = csv.reader(f)
    for i in usuarios:
        if i[3] == "18":
            print(i[0])