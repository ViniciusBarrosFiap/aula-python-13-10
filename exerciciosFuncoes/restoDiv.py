def resto(n1, n2):
    resultado = n1 % n2
    return resultado

print("Digite dois números inteiros: ")
num1 = int(input())
num2 = int(input())

resultado = resto(num1, num2)
print(f"O resto da divisão é {resultado}")