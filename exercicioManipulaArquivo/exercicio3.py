try:
    numeroUser = 1
    numeros = {}
    while numeroUser != 0:
        numeroUser = int(input("Digite números inteiros: "))
        if numeroUser != 0:
            numeros.add(numeroUser)
        f = open("exercicioManipulaArquivo/numeros.txt", "a", encoding="utf-8")
        f.write(numeros)
        f.close()
        f = open("exercicioManipulaArquivo/numeros.txt", "r", encoding="utf-8")
        print("Numeros adicionados:\n"+ f.read())
except:
    print("Arquivo não existe")
    
