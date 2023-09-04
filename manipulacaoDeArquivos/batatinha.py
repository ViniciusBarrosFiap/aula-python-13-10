try:
    f = open("manipulacaoDeArquivos/batata.txt", "a", encoding="utf-8")
    f.write("\nSou pequenininha")
    f.write("\ndo tamanho de um botâo")
    f.write("\ne mamãe no coração")
    f.write("\ne papai caiu no chão")
    f.write("\nmamãe que é mais querida")
    f.write("\nficou no coração")
    f.close()
    f = open("manipulacaoDeArquivos/batata.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print('O arquivo não existe')