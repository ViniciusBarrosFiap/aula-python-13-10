def parImpar():
    numUser = 1
    while numUser != 0:
        numUser = int(input("Digite números inteiros(digite 0 para parar):"))
        if numUser % 2 == 0:
            print("Esse numero é par")
        else:
            print("Esse número é impar")

parImpar()