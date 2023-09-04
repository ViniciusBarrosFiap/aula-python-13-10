import os
try:
    if os.path.exists("manipulacaoDeArquivos/tigre.txt"):
        os.remove("manipulacaoDeArquivos/tigre.txt")
    f = open("manipulacaoDeArquivos/tigres.txt")
    print(f.read())
    f.close()
except FileNotFoundError:
    print('O arquivo não existe')