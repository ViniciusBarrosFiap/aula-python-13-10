num = int(input("Digite um numero maior ou igual a 2: "))
ultimo = 1
penultimo = 1
if num < 2:
    print("Numero invalido")

else:
    print(penultimo)
    print(ultimo)
    for i in range(1, num, 1):
        resultado = ultimo + penultimo
        penultimo = ultimo
        ultimo = resultado
        print(resultado)

        