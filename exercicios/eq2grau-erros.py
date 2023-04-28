import math
try:
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    
    try:
        delta = (b**2) - 4 * a * c

        raiz = delta**0.5

        x_pos = (b * (-1) + raiz) / (2 * a)

        x_neg = (b * (-1) - raiz) / (2 * a)
        if delta < 0:
            print("As raizes não são reais")
        else:

            print(f"As raizes são x1: {x_pos:.2f} x2: {x_neg:.2f}")

    except ValueError:
        print("A raiz é negativa")
except ValueError:
    print("Digite apenas números inteiros")