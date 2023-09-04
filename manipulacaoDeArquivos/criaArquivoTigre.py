try:
    f = open("manipulacaoDearquivos/tigre.txt", "a", encoding="utf-8")
    f.write("tres patros de trigo")
    f.write("\npara 3 tigres tristes")
    f.close()
    f = open("manipulacaoDearquivos/tigre.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("O arquivo não existe")