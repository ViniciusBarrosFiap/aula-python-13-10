try:
    f = open("manipulacaoDearquivos/rato.txt", "a", encoding="utf-8")
    f.write("O rato roeu")
    f.write("\na roupa")
    f.write("\ndo rei de Roma")
    f.close()
    f = open("manipulacaoDearquivos/rato.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("O arquivo não existe")