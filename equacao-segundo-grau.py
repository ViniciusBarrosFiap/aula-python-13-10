import math
a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta = (b**2) - 4 * a * c

raiz = delta**0.5

x_pos = (b * (-1) + raiz) / (2 * a)

x_neg = (b * (-1) - raiz) / (2 * a)

if delta < 0:
    print("As raizes não são reais")
else:

    print(f"As raizes são x1: {x_pos} x2: {x_neg}")