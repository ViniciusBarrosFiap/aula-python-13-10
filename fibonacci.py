num = int(input("Digite um numero maior ou igual a 2: "))
if num < 2:
    print("Numero invalido")

else:
    for i in range(1, num, 1):
        fibo = 1 + 1
        fibo1 = fibo - 1