try:
    fraseUsuario = input("Digite um ditado popular: ")
    f = open("exercicioManipulaArquivo/exercicio1.txt", "a", encoding="utf-8")
    f.write(fraseUsuario)
    f = open("exercicioManipulaArquivo/exercicio1.txt", "r", encoding="utf-8")
    print("conteudo escrito:\n" + f.read())
    f.close()
except:
    print("Arquivo não existe")