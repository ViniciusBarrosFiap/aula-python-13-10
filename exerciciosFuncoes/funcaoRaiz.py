import math
def raiz(n1):
    resultado = math.sqrt(n1)
    return resultado

num1 = int(input("Digite um número para calcular a raiz: "))

resulRaiz = raiz(num1)
print(f"A raiz de {num1} é {resulRaiz :.2f}")