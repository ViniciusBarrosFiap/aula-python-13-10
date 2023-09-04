numeroUser = 1
numeros = set()
try:
    while numeroUser != 0:
        numeroUser = int(input("Digite números inteiros: "))
        if numeroUser != 0:
            numeros.add(numeroUser)
    numeros_pares = set()

    for i in numeros:
        if i % 2 == 0:
            numeros_pares.add(str(i))

    f = open("exercicioManipulaArquivo/numeros.txt", "a", encoding="utf-8")
    for i in numeros_pares:
        f.write(str(i) + " ")
    f.close()
    f = open("exercicioManipulaArquivo/numeros.txt", "r", encoding="utf-8")
    print("Numeros adicionados:\n"+ f.read())
except FileNotFoundError:
    print('O arquivo não existe')